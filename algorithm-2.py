
'''
Group 23: StaySteady
February 25 2018
IBEHS 1P10B
'''
# import modules for sensor code
import smbus
import math
import time

# import modules for RPI Code
import RPi.GPIO as GPIO
from time import sleep
import json

## Code Required to get Data From Gyro Sensor ##

# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
address = 0x68       # This is the address value read via the i2cdetect command

# Now wake the 6050 up as it starts in sleep mode
bus.write_byte_data(address, power_mgmt_1, 0)


## Code for the RPI Output Sensor ##
# Initialize the pin variables
Green = 22 # Output to inidcate a good balance outcome 
Blue = 6 # Output to indicate a Mild imbalance outcome
Red = 19 # Output to indicate a Wild imbalance outcome

# Setup pins on the RPI Board
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(Green, GPIO.OUT) #Pin number 22 is responsible for GREEN light displaying baseline change in movement
GPIO.setup(Blue, GPIO.OUT) #Pin number 6 is responsible for BLUE light displaying mild change in movement
GPIO.setup(Red, GPIO.OUT) #Pin number 19 is responsible for RED light displaying wild change in movement

# Color Display Function
def colorGenerator(light): # input of function is the output of the algorithm defined later in the code ## takes value 0 1 or 2
    global Green,Blue,Red # Call the 3 predefined pins for the GPIO output
    if light == 0:
        GPIO.output(Green,1) # Turn on Green light from this outcome of the algorithm ## Indicating a balanced event (Baseline)
    elif light == 1:
        GPIO.output (Blue,1) # Turn on Blue light from this outcome of the algorithm ## Indicating a slight imbalanced event (Mild)
    elif light == 2:
        GPIO.output (Red,1) # Turn on Red light from this outcome of the algorithm ## Indicating a severe imbalanced event (Wild)
    else:
        pass 
    

def turnOff(): # Turns off all lights instead of turning off specific light 
    global Green,Blue,Red # Call the 3 predefined pins for the GPIO output
    GPIO.output(Green,0) # Turn off the green light
    GPIO.output(Blue,0) # Turn off the blue light
    GPIO.output(Red,0) # Turn off the red light

# Initalize List Variables
yRotationList = [] # List for the Y axis rotation degree values
zRotationList = [] # List for the Z axis rotation degree values
algorithmValues = [] # List for the outputs of the algorithm 

# light @0 = green, @1 = blue, @2 = red
light = 0 # initialize light variable (so that i can be updated)
counter = 0 # initialize a counter variable so that algoirthim only runs for a specifc number of times 
# This global counter aspect of the alogorthm mimics a realive scenario as the diagnostic tests for patients do not take long 
# periods of time. Additionally, if the patient would like to perform their own data collection, they can specify the length
# of time the algorithm would run.
Max = 60 # This variable indicates the total number of time the function runs as each iteration of the for loop sleeps for 1 second
# and the rest of the code required elapses very quickly; thus 'Max' is the time specified in seconds for the function to run

while counter < Max: #  while loop that iterates over a predetermined amount of time
    sleep(1) # sleep for 1 second allows us to properly identify significant changes in the patient's movements in relation to one another
    # additionally, the use of the sleep function suppresses the total amount of outputs we would receive in a given time interval
    turnOff() # predefined function that ensures all the lights of the sensor are turned off ## this is done before main part of 
    # algorithm runs so only 1 light is seen at a time

    # Using Sensor Data - Scaling Values
    # The Data from the X Axis was suppressed as this varied a lot in a patients walking movement so changes in these data values would not be indicative of an imbalance event
    # Instead we noticed that the validity of an imbalance event can be determined from significant changes in the Y and Z axis data so this was used in data processing
    # only using y and z data
    gyro_yout = (read_word_2c(0x45))/131 # code from the starter sensor collection file ## dividing by 131 scales the data ### Y axis rotation degree data
    gyro_zout = (read_word_2c(0x47))/131 # Z axis rotation degree data

    yRotationList.append(gyro_yout) # Appends this data to the predefined Y data list
    zRotationList.append(gyro_zout) # Appends this data to the predefined Z data list
    # The above line is important as the raw data from the sensor is used in the graphical representation of the data

    ## Main Algorithim Data Processing Begins Here ##
    # The premise for this algorithm is the tendency of an indication of an imbalance event (and the magnitude of said event) if we compare
    # Two degree values from the gyro sensor. If the change in a value ( in Y or Z axis) is large, this tends to be an imbalance event from our testing. 
    # We used this concept to create the algorithm. Additionally, since the gyro sensor readjusts its 'origin point' (i.e. when gyro is moved, the initial movement
    # might register 50 degrees perhaps, but if kept in that position, a second later the gyro would display 0 degrees of motion), we decided to compare
    # the current data value of the gyro sensor and the one before it, for both Y and Z axes, and if either axis registered a significant difference that 
    # output would be appropriately labelled as an imbalance event based on the magnitude of this difference.
    if counter == 0: # If the algorithm is on its first iteration it will not have any data to compare to the it is skipped
        pass
    else:
        # Green Light (Good) This condition is for small degrees of rotation or big degrees of motion that occur slowly 
        # (i.e. bending over to pick up an item occurs at a slow pace and wouldnt be registed as Balance event)
        if (abs(yRotationList[-2] - yRotationList[-1]) < 50) and (abs(zRotationList[-2] - zRotationList[-1]) < 50):
            # Using negative indicies, the algorithim checks the last and the second last values of both Y and Z data lists and 
            # determines if their difference is less than 50, if they are both less than 50 it is registed as a balance event and 
            # assigned a light value of 0

            light = 0
            print("Green")
        # Blue Light (Medium)
        elif (abs(yRotationList[-2] - yRotationList[-1]) < 130) and (abs(zRotationList[-2] - zRotationList[-1]) < 130):
            # If the first condition is passed then both values are atleast greater than 50 so a lowerbound need not be specified. 
            # This clause works the same way as the previous if statement, and if the values are both less than 130 light is assigned value 1
            light = 1
            print("Blue")
        # Red Light (Bad)
        else: # If a Y or Z value difference is greater than 130, light is assigned a value of 2
            light = 2
            print("Red")
        
        colorGenerator(light) # This predefined function displays the appropriate color (@0 = green, @1 = blue, @2 = red) based on the outcome of the algorithm above
        algorithmValues.append(light) # the value of the light is also appended to the algorithm values list as it is manipulated and graphically depicted 
    counter+= 1 # Add 1 to global counter to keep track of iterations through the algorithim

# Create a python dictionary to be used for the depiction of calculated data onto website
# Dictionary is created in this manner so that it can be easily converted to json and can thus be easily manipulated in javascript
# As all data processing has been completed with algorithim, the outputting of data into json file is strictly for presentation process 
# and the code is inclded for completeness and to demonstrate understanding of the concepts required to accomplish this 
data = {
    "patientID":"AE175B7",
    "patientData": {
        "yData":yRotationList,
        "zData":zRotationList,
        "resultData":algorithmValues
        }
    }
# Open json file and place the processed data into the file so that it can be manipulated in javascript for website component
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
outfile.close()
# N.B. Json is file format that is easy to use and manipulate.
# Link to website: staySteay.ga or https://staysteady.000webhostapp.com or staysteady.ga (ga for group assignment)
# Code on hosted websites uses previously generated data and not current data from sensor as their would be no easy way to update this given the resources we have
# ^^ The above code works well if the website code is to be run on a local server in which the json file could be readily opened and analyzed.

var ctx = $(".firstChart");

function section1(){
    var scatterChart = new Chart(ctx[1], {
        type: 'line',
        xAxisID: 'Degree of Rotation',
        // scaleOverride: true,
        // scaleSteps: 10,
        // scaleStepWidth: 20,
        // scaleStartValue:-20,
        data: {
            labels: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
            datasets: [{
                label: "Y Data",
                backgroundColor: 'rgba(255, 99, 132,0.3)',
                borderColor: 'rgb(255, 99, 132)',
                data: [9, 25, -4, -31, 35, -24, -37, 27, 24, -51, 11, 73, -38, -39, 30, 49, -44, -31, 49, -37, -3, 17, 88, -49, -17, 51, 9, -20, -5, 32, -12, -32, 51, -8, -27, 14, -5, -5, -4, 23],
            },{
               label: "Z Data",
                backgroundColor: 'rgba(0, 99, 132,0.3)',
                borderColor: 'rgb(0, 99, 132)',
                data: [-3, -3, -1, -12, -3, 0, -14, 2, -13, 2, -6, 8, -6, 11, -11, -1, 1, -5, -6, 0, 10, -6, 10, -10, -2, 1, -5, -3, -3, -1, -3, -14, -1, -3, -6, 49, -32, -62, 10, 91], 
            }]
        },
        options: {}
    });

    var scatterChart2 = new Chart(ctx[0], {
        type: 'line',
        responsize: true,
        //scaleOverride: true,
        // scaleSteps: 9,
        // scaleStepWidth: 20,
        // scaleStartValue:-80,
        data: {
            labels: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
            datasets: [{
                label: "Y Data",
                backgroundColor: 'rgba(255, 99, 132,0.3)',
                borderColor: 'rgb(255, 99, 132)',
                data: [1, -11, -8, -1, -7, -7, -5, -2, -16, -14, 1, 3, -1, 2, 5, -3, -4, 2, 3, -1, 7, -4, -3, -5, 10, -5, 8, 10, -6, 1, 3, 7, 9, 7, 5, 10, 3, -6, 1, 6],
            },{
               label: "Z Data",
                backgroundColor: 'rgba(0, 99, 132,0.3)',
                borderColor: 'rgb(0, 99, 132)',
                data: [-3, 0, -3, -9, -7, -3, -5, -6, -2, -6, -6, -2, -3, 0, -6, 0, -1, -6, -12, -23, -16, 1, -10, -6, -5, -8, 3, 0, 0, -6, -10, -3, -8, 0, -1, -6, -7, -3, -15, -5], 
            }]
        },
        options: {
            scales: {
                yAxes : [{
                    ticks: {
                        beginAtZero: false,
                        stepSize: 20,
                        min: -80,
                        max: 100
                    }
                }]
            }
        }
    });
}


var ctx2 = $(".secondChart");

function section2(){
    var myDoughnutChart = new Chart(ctx2[0], {
            type: 'doughnut',
            data: {
                datasets: [{
                    data: [34,5,0],
                    backgroundColor:[
                        'rgba(109, 255, 111,0.2)', // red -> green
                        'rgba(173, 204, 255,0.2)', // yellow -> blue
                        'rgba(255, 109, 109,0.2)', // blue - > red
                        ],
                    borderColor:[
                        'rgba(109, 255, 111,1)', // red -> green
                        'rgba(173, 204, 255,1)', // yellow -> blue
                        'rgba(255, 109, 109,1)', // blue - > red
                        ]
                }],

                // These labels appear in the legend and in the tooltips when hovering different arcs
                labels: [
                    'Baseline (34)',
                    'Mild (5)',
                    'Wild (0)'
                ]
                
                //borderWidth:['rgb(255, 109, 109)','rgb(255, 252, 109)','rgb(173, 204, 255)'],
                //hoverBackgroundColor:['rgb(255, 109, 109)','rgb(255, 252, 109)','rgb(173, 204, 255)'],
                //hoverBorderColor:['rgb(255, 109, 109)','rgb(255, 252, 109)','rgb(173, 204, 255)']
                //hoverBorderWidth:['rgb(255, 109, 109)','rgb(255, 252, 109)','rgb(173, 204, 255)']
            }
        });
    var myDoughnutChart = new Chart(ctx2[1], {
                type: 'doughnut',
                data: {
                    datasets: [{
                        data: [10,22,7],
                        backgroundColor:[
                            'rgba(109, 255, 111,0.2)', // red -> green
                            'rgba(173, 204, 255,0.2)', // yellow -> blue
                            'rgba(255, 109, 109,0.2)', // blue - > red
                            ],
                        borderColor:[
                            'rgba(109, 255, 111,1)', // red -> green
                            'rgba(173, 204, 255,1)', // yellow -> blue
                            'rgba(255, 109, 109,1)', // blue - > red
                            ]
                    }],

                    // These labels appear in the legend and in the tooltips when hovering different arcs
                    labels: [
                        'Baseline (10)',
                        'Mild (22)',
                        'Wild (7)'
                    ]
                    
                    //borderWidth:['rgb(255, 109, 109)','rgb(255, 252, 109)','rgb(173, 204, 255)'],
                    //hoverBackgroundColor:['rgb(255, 109, 109)','rgb(255, 252, 109)','rgb(173, 204, 255)'],
                    //hoverBorderColor:['rgb(255, 109, 109)','rgb(255, 252, 109)','rgb(173, 204, 255)']
                    //hoverBorderWidth:['rgb(255, 109, 109)','rgb(255, 252, 109)','rgb(173, 204, 255)']
                }
            });
}

var ctx3 = $(".thirdChart");

function section3(){
    var scatterChart = new Chart(ctx3, {
        type: 'line',
        // scaleOverride: true,
        // scaleSteps: 10,
        // scaleStepWidth: 20,
        // scaleStartValue:-20,
        data: {
            labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
            datasets: [{
                label: "Average Data",
                backgroundColor: 'rgba(255, 99, 132,0.3)',
                borderColor: 'rgb(255, 99, 132)',
                data: [7, 7, 8, 7, 4, 2, 3, 6, 2, 2, 3, 7, 8, 6, 3, 6, 6, 4, 8, 4, 6, 2, 6, 3, 8, 2, 2, 3, 4, 2],
            },{
               label: "Your Data",
                backgroundColor: 'rgba(0, 99, 132,0.3)',
                borderColor: 'rgb(0, 99, 132)',
                data: [31, 30, 31, 32, 26, 26, 25, 31, 25, 25, 25, 33, 27, 31, 31, 26, 26, 31, 30, 26, 32, 27, 25, 32, 31, 30, 32, 28, 33, 30], 
            }]
        },
        options: {}
    });
}
section1();section2();section3();

var first = $(".firstChart")
var second = $(".secondChart")
var third = $(".thirdChart")

first[0].addEventListener("mouseover",section1)
second[0].addEventListener("mouseover",section2)
third[0].addEventListener("mouseover",section3)
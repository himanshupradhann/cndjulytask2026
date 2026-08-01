const temperatureData = [];
const pressureData = [];
const altitudeData = [];

let tempChart;
let pressureChart;

function createCharts() {

    tempChart = new Chart(

        document.getElementById("tempChart"),

        {

            type: "line",

            data: {

                labels: altitudeData,

                datasets: [{

                    label: "Temperature",

                    data: temperatureData,

                    borderColor: "red",

                    borderWidth: 1,

                    pointRadius: 0,

                    borderWidth: 1,
                    
                    pointRadius: 0,       
                    
                    pointHoverRadius: 4,  
                    
                    tension: 0.1,

                    fill: false

                }]

            },

            options: {

                responsive: true,

                animation: false

            }

        }

    );


    pressureChart = new Chart(

        document.getElementById("pressureChart"),

        {

            type: "line",

            data: {

                labels: altitudeData,

                datasets: [{

                    label: "Pressure",

                    data: pressureData,

                    borderColor: "green",

                    borderWidth: 1,

                    pointRadius: 0,

                    borderWidth: 1,
                    
                    pointRadius: 0,       
                    
                    pointHoverRadius: 4,  
                    
                    tension: 0.1,

                    fill: false

                }]

            },

            options: {

                responsive: true,

                animation: false

            }

        }

    );

}
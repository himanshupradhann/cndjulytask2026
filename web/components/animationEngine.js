function animateCharts(rows) {

    let index = 0;

    const timer = setInterval(() => {

        if (index >= rows.length) {

            clearInterval(timer);

            return;

        }

        altitudeData.push(rows[index].altitude);

        temperatureData.push(rows[index].temperature);

        pressureData.push(rows[index].pressure);

        tempChart.update();

        pressureChart.update();

        index++;

    }, 30);

}

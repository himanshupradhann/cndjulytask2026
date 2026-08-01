function loadCSV() {

    Papa.parse("data/clean_data.csv", {

        download: true,

        header: true,

        dynamicTyping: true,

        complete: function(results) {

            createCharts();

            animateCharts(results.data);

        }

    });

}

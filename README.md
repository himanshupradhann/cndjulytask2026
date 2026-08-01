# cndjulytask2026

file structure

Data
  testdata.txt
  
output
  graph.png

src
  analyser.py
  cleaner.py
  export.py
  parser.py
  server.py
  visua;isation.py

web
  index.html
  style.css
  script.js
  data
    cleandata.csv
  components
    chart.js
    animationEngine.js
    csv_extractor.js

app.py


pipeline

  raw data -> parser.py -> cleaner.py -> analyser.py -> expoter.py -> CSV data saved in web/data -> visualisation.py -> graphs saved in /output 
  server.js -> starts the server at http://localhost:8000 -> web/data/clean_data.csv -> csv_extractor.js -> (chart.js , animationEngine.js)


  how to use :

  commands:

  git clone https://github.com/himanshupradhann/cndjulytask2026
  python app.py

  Dependency:
  python
  telemetry data

  Note:
  -Make sure add the telemetry data in the \data directory
  -Change the file path inside app.py

  

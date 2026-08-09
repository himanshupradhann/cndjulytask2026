# cndjulytask2026

## File Structure

```text
                 ┌──────────────────┐
                 │ Raw Telemetry TXT│
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │    parser.py     │
                 │ Parse TXT fields │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │   cleaner.py     │
                 │ Missing values   │
                 │ Unit conversion  │
                 │ Sort by altitude │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │   analyser.py    │
                 │ Statistics       │
                 └────────┬─────────┘
                          │
              ┌───────────┴───────────┐
              ▼                       ▼
     ┌────────────────┐      ┌────────────────┐
     │   export.py    │      │visualisation.py│
     │   CSV output   │      │ Static graphs  │
     └───────┬────────┘      └────────────────┘
             │
             ▼
     ┌────────────────┐
     │ clean_data.csv │
     └───────┬────────┘
             │
             ▼
     ┌────────────────────┐
     │   Web Dashboard    │
     │ HTML/CSS/JavaScript │
     └─────────┬──────────┘
               │
        ┌──────┴───────┐
        ▼              ▼
   Chart.js       Animation
```

## Pipeline

```text
                 ┌──────────────────┐
                 │ Raw Telemetry TXT│
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │    parser.py     │
                 │ Parse TXT fields │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │   cleaner.py     │
                 │ Missing values   │
                 │ Unit conversion  │
                 │ Sort by altitude │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │   analyser.py    │
                 │ Statistics       │
                 └────────┬─────────┘
                          │
              ┌───────────┴───────────┐
              ▼                       ▼
     ┌────────────────┐      ┌────────────────┐
     │   export.py    │      │visualisation.py│
     │   CSV output   │      │ Static graphs  │
     └───────┬────────┘      └────────────────┘
             │
             ▼
     ┌────────────────┐
     │ clean_data.csv │
     └───────┬────────┘
             │
             ▼
     ┌────────────────────┐
     │   Web Dashboard    │
     │ HTML/CSS/JavaScript │
     └─────────┬──────────┘
               │
        ┌──────┴───────┐
        ▼              ▼
   Chart.js       Animation
```

## How to Use

Download the DataSet
~~~
https://www.ncei.noaa.gov/pub/data/igra/data/data-por/
~~~

Clone the repository

```bash
git clone https://github.com/himanshupradhann/cndjulytask2026.git
```
```bash
cd cndjulytask2026
```
IMP:
place the dataset in the data folder and change the file path in app.py

Run the project

```bash
python app.py
```

## Dependencies

* Python
* Telemetry Data

## Note

* Add the telemetry data file inside the `data/` directory.
* Change the telemetry data file path inside `app.py` if required.
* Generated CSV will be saved in `web/data/`.
* Generated graphs will be saved in `output/`.

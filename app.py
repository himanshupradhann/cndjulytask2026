from src.parser import parse_data
from src.cleaner import clean_data
from src.analyser import calculate_statistics
from src.visualisation import (plot_tempvsalt , plot_altvspress)
from src.export import export_csv
from src.server import start_server

try :
 filepath="data/INM00042971-data.txt"

 df = parse_data(filepath)

 df = clean_data(df)

 print(df.head())
 print()
 stats = calculate_statistics(df)


 for key, value in stats.items():

    print(f"{key}: {value} \n")

 export_csv(df)
 plot_altvspress(df)
 plot_tempvsalt(df)

 start_server()

except FileNotFoundError:
  print("File not found \npotentially File Name not correct \nFile is not present in data \n[HARDCODED FILE PATH WITH NAME - data/INM00042971-data.txt]")

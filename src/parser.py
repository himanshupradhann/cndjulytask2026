import pandas as pd 

def parse_data(file_path):
    records =[]
    with open(file_path,"r") as file:

        for line in file:
            if line.startswith("#"):
                continue

            parts=line.split()

            if len(parts)<8:
                continue

            try:
                pressure=parts[2]
                altitude=parts[3]
                temprature=parts[4]
                humidity=parts[5]

                pressure =pressure.replace("B","")
                altitude=altitude.replace("B","")
                temprature=temprature.replace("B","")
                humidity=humidity.replace("B","")

                pressure=int(pressure)
                temprature=int(temprature)
                altitude=int(altitude)
                humidity=int(humidity)

                records.append([pressure,altitude,temprature,humidity])

            except:
                continue

    df=pd.DataFrame(records,columns=["pressure","altitude", "temperature","humidity"])
    return df






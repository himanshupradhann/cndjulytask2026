def calculate_statistics(df):

    max_altitude = df["altitude"].max()

    temperature_variance = df["temperature"].var()

    ground_pressure = df.iloc[0]["pressure"]
    top_pressure = df.iloc[-1]["pressure"]

    pressure_difference = ground_pressure - top_pressure

    return {
        "Maximum Altitude": max_altitude,
        "Temperature Variance": temperature_variance,
        "Pressure Difference": pressure_difference
    }

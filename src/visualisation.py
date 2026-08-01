import matplotlib.pyplot as plt

def plot_tempvsalt(df):

    plt.figure(figsize=(8,6))

    plt.plot(
        df["temperature"],
        df["altitude"],
        color="red",
        linewidth=1.5
    )

    plt.title("Altitude vs Temperature")

    plt.xlabel("Temperature (°C)")
    plt.ylabel("Altitude (m)")

    plt.grid(True)

    plt.savefig("output/temp_vs_altitude.png")

def plot_altvspress(df):

    plt.figure(figsize=(8,6))

    plt.plot(
        df["altitude"],
        df["pressure"],
        color="blue",
        linewidth=1.5
    )

    plt.title("Altitude vs Pressure")

    plt.xlabel("Altitude (m)")
    plt.ylabel("Pressure")

    plt.grid(True)

    plt.savefig("output/altitude_vs_pressure.png")

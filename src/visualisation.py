import matplotlib.pyplot as plt

def plot_tempvsalt(df):

    plt.figure(figsize=(8,6))

    plt.plot(
        df["altitude"],
        df["temperature"],
        color="red",
        linewidth=1.5
    )

    plt.title("Altitude vs Temperature")

    plt.xlabel("Altitude (m)")
    plt.ylabel("Temperature (°C)")

    plt.grid(True)

    plt.savefig("output/altitude_vs_temp.png")

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
    plt.ylabel("Pressure ")

    plt.grid(True)

    plt.savefig("output/altitude_vs_pressure.png")

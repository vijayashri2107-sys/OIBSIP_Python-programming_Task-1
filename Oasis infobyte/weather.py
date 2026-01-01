import tkinter as tk
from tkinter import messagebox

# --------- SAMPLE OFFLINE WEATHER DATA ---------
weather_data = {
    "chennai": {"temp": 32, "humidity": 65, "condition": "Sunny"},
    "madurai": {"temp": 34, "humidity": 60, "condition": "Hot"},
    "coimbatore": {"temp": 28, "humidity": 70, "condition": "Cloudy"},
    "bangalore": {"temp": 26, "humidity": 68, "condition": "Cool"},
    "delhi": {"temp": 30, "humidity": 55, "condition": "Clear"}
}

# --------- FUNCTION ---------
def get_weather():
    city = city_entry.get().lower()

    if city == "":
        messagebox.showwarning("Warning", "Please enter city name")
        return

    if city in weather_data:
        data = weather_data[city]
        result_label.config(
            text=f" Temperature : {data['temp']} °C\n"
                 f" Humidity : {data['humidity']} %\n"
                 f" Condition : {data['condition']}"
        )
    else:
        messagebox.showerror("Error", "City not found in offline data")

# --------- APP WINDOW ---------
app = tk.Tk()
app.title("Weather App")
app.geometry("400x350")
app.resizable(False, False)

# --------- UI DESIGN ---------
title = tk.Label(app, text=" Weather Application", font=("Arial", 18, "bold"))
title.pack(pady=15)

city_frame = tk.Frame(app)
city_frame.pack(pady=10)

tk.Label(city_frame, text="Enter City Name:", font=("Arial", 12)).pack(side=tk.LEFT)
city_entry = tk.Entry(city_frame, width=15)
city_entry.pack(side=tk.LEFT, padx=5)

get_btn = tk.Button(
    app,
    text="Get Weather",
    command=get_weather,
    bg="blue",
    fg="white",
    width=18
)
get_btn.pack(pady=15)

result_label = tk.Label(
    app,
    text="Weather details will appear here",
    font=("Arial", 12),
    justify="center"
)
result_label.pack(pady=20)

footer = tk.Label(app, text="Python Mini Project - Tkinter App", font=("Arial", 10))
footer.pack(side=tk.BOTTOM, pady=10)

app.mainloop()


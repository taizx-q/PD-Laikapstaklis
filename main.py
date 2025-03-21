import requests
import tkinter as tk

#api key from openweathermap
API_KEY = '79d1ca96933b0328e1c7e3e7a26cb347'

#atrast laikapstakļus
def get_weather():
    city = weather_request.get()
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={API_KEY}'
    try:
        weather_data = requests.get(url).json()
        if weather_data['cod'] == 200:
            temperature = round(weather_data['main']['temp'])
            temperature_feels = round(weather_data['main']['feels_like'])
            result["text"] = f'Temperatūra: {temperature}°C\nJūtas ka: {temperature_feels}°C'
        else:
            result["text"] = f"Pilsēta {city} nav atrasta."
    except Exception as e:
        result["text"] = "Error in request by API: " + str(e)

#main gui
root = tk.Tk()
root.title("Laikapstaklis")

Font_tuple = ("Noto Sans", 13, "bold")

main_label = tk.Label(root, text="Laikapstaklis")
main_label.pack(pady=15)
main_label.configure(font=Font_tuple)

weather_request = tk.Entry(root, width=50)
weather_request.pack(pady=5)
weather_request.configure(font=Font_tuple)

send_request = tk.Button(root, text="Atrast temperatūru", command=get_weather)
send_request.pack(pady=15)
send_request.configure(font=Font_tuple)

result = tk.Label()
result.pack(pady=10)
result.configure(font=Font_tuple)

#cikls
root.mainloop()

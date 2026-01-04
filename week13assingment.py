import requests


def get_weather(city_name):
    api_key = "ffe4799006f843c7a0785253253012"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}&aqi=no"
    response = requests.get(url)
    return response

def get_motivation():
    quote_url = "https://zenquotes.io/api/random"
    response = requests.get(quote_url)
    return response

print("--- Uzbekistan Weather & Motivation Program ---")
city = input("Enter city name (e.g., Urgench, Tashkent): ")


try:
    weather = get_weather(city)

    if weather.status_code == 200:
        data = weather.json()
        temp = data['current']['temp_c']
        condition = data['current']['condition']['text']

        if temp < 5:
            advice = "Very cold! Wear a heavy coat."
        elif 5 <= temp < 20:
            advice = "Chilly weather. Wear a jacket."
        else:
            advice = "Warm weather. Light clothes are fine."

        m_res = get_motivation()
        if m_res.status_code == 200:
            quote = m_res.json()[0]['q']
        else:
            quote = "Have a nice day!"

        print("\n" + "="*30)
        print("City:", city.capitalize())
        print("Temperature:", temp, "C")
        print("Condition:", condition)
        print("Advice:", advice)
        print("Quote:", quote)
        print("="*30)

        with open("weather_report.txt", "a") as f:
            f.write(f"City: {city}, Temp: {temp}\n")

    else:
        print("Error: City not found!")

except:
    print("An error occurred with the network or API.")
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    weather_info = None
    if request.method == "POST":
        city = request.form.get("city")
        api_key = "c3f73979360d4fa7bc4102452253110"  # 🔑 Replace with your WeatherAPI key
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temp_c = data["current"]["temp_c"]
            advice = ""
            if temp_c > 35:
                advice = "🔥 It's a hot day! Stay hydrated."
            elif temp_c < 15:
                advice = "❄️ It's quite cold! Wear warm clothes."
            else:
                advice = "😊 The weather feels moderate and pleasant."

            weather_info = {
                "city": data["location"]["name"],
                "temp_c": temp_c,
                "condition": data["current"]["condition"]["text"],
                "humidity": data["current"]["humidity"],
                "wind_speed": data["current"]["wind_kph"],
                "advice": advice
            }

    return render_template("weather.html", weather=weather_info)

if __name__ == "__main__":
    app.run(debug=True)

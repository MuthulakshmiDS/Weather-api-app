# Weather-api-app
# Weather App
### Project Title

## Real-Time Weather App using WeatherAPI

### Overview

This project implements a web-based weather application using **Python**, **Flask**, and **WeatherAPI**.  
Users can enter a city name and get current weather details, including temperature, humidity, wind speed, and weather conditions. The app also provides advice based on the weather.

### Key Features

• Fetches real-time weather data for any city.  

• Displays temperature (°C), humidity (%), wind speed (km/h), and condition.  

• Gives advice based on temperature (hot, cold, moderate).  

• Simple and user-friendly interface using HTML, CSS, and Bootstrap.  

• Responsive design with background images for better UX.  

### When to Use

Use this app when you need:

• Quick weather updates for planning daily activities.  

• A simple and interactive interface for checking weather.  

• Integration of weather information into other Python or Flask projects.  

## Algorithm — High-level Steps

• User inputs a city name in the web form.  

• Flask backend receives the request and calls the WeatherAPI with the city and API key.  

• JSON data is returned and parsed to extract temperature, condition, humidity, and wind speed.  

• Optional advice is generated based on temperature ranges.  

• The processed data is displayed in the HTML template with proper styling.  

## Input

• City name (string).  

• WeatherAPI key (replace the placeholder in `weather.py`).  

• Optional: adjust backend logic to handle multiple parameters or additional API features.  

## Output

• Weather information for the city:  

  - Temperature (°C)  
  - Condition (e.g., Sunny, Rainy)  
  - Humidity (%)  
  - Wind speed (km/h)  
  - Advice for weather conditions  

• Displayed on a styled web page using Flask templates.  

## Expected Results

• Accurate and real-time weather data from WeatherAPI.  

• User-friendly display with proper color contrast and background images.  

• Advice and alerts based on temperature for better planning.  

## Common Applications

• Daily weather updates for personal use.  

• Integration into dashboards or smart home apps.  

• Learning Flask, API integration, and web development.  

• Teaching or demonstrating real-time data fetching in Python projects.  

## File structure
```weather-app/
│
├── weather.py # Flask backend script; handles API calls and logic
├── templates/ # HTML templates for rendering pages
│ └── weather.html # Main HTML template for the weather app interface
├── static/ # Folder for static assets (images, CSS, JS)
│ └── weather.png # Background image for the web page
└── README.md # Project documentation and instructions
```


## License

Use and adapt this README freely. Include proper attribution if you reuse substantial parts in published work.  

### References

• WeatherAPI Documentation: [https://www.weatherapi.com/](https://www.weatherapi.com/)  

• Flask Official Documentation: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)  

• Python Requests Library Documentation: [https://docs.python-requests.org/](https://docs.python-requests.org/)

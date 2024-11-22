from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# API configuration
API_KEY = '99ff24c012144fb4582bdbb87e7f6612'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric' # Fetch temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        return render_template('index.html', weather=weather)
    else:
        error_message = data.get('message', 'Error fetching data')
        return render_template('index.html', error=error_message)
    
if __name__ == '__main__':
    app.run(debug=True)
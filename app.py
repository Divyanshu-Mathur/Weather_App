from flask import Flask,request,render_template
from datetime import datetime
import requests
app=Flask(__name__)
api_key="api"
url=f"https://api.openweathermap.org/data/2.5/weather/"
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather",methods=['GET','POST'])
def get_weather():
    if request.method == 'POST':
        city = request.form.get('city')
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data=response.json()
        if data['cod']==404:
            return render_template('error.html',msg="City Not Found")
        elif data['cod']==200:
            weather={
                'city':data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
                'humidity':data['main']['humidity'],
                'wind_speed':data['wind']['speed'],
                'sunrise':datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S'),
                'sunset':datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S'),
                'formatted_date_time' : current_date_time.strftime("%Y-%m-%d %H:%M:%S")
            }
            print(weather)
            return render_template('weather.html',weather=weather)
        else:
            return render_template('error.html',msg="City Not Found")
    return render_template('error.html',msg="Please enter the City Name")

if __name__=="__main__":
    app.run(debug=True)

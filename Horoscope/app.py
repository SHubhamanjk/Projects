from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_horoscope(zodiac_sign, month, day, year):
    url = f"https://www.vogue.in/horoscope/collection/horoscope-today-{month}-{day}-{year}/"
    response = requests.get(url)
    
    if response.status_code != 200:
        return "Failed to retrieve the horoscope. Please try again later."

    soup = BeautifulSoup(response.content, 'html.parser')
    horoscopes = soup.find_all('h2')
    
    for horoscope in horoscopes:
        title = horoscope.get_text(strip=True).lower()
        if zodiac_sign.lower() in title:
            content = horoscope.find_next('span').get_text(strip=True)
            return content
    
    return "Horoscope for the given zodiac sign not found."

@app.route('/', methods=['GET', 'POST'])
def horoscope():
    horoscope_text = ""
    if request.method == 'POST':
        user_month = request.form['month'].lower()
        user_day = request.form['day'].lower()
        user_year = request.form['year'].lower()
        user_horoscope = request.form['horoscope'].lower()
        horoscope_text = get_horoscope(user_horoscope, user_month, user_day, user_year)
    return render_template('index.html', horoscope_text=horoscope_text)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
from generator import *
app = Flask(__name__)

plans = []

@app.route('/', methods =["GET", "POST"])
def home():
    if request.method == "POST":
        email = request.form.get('email')
        start_date = request.form.get('trip-start')
        end_date = request.form.get('trip-end')
        country = request.form.get('country')
        area = request.form.get('area')
        interests = request.form.get('interests')
        accommodations = request.form.get('accommodations')
        requirements = request.form.get('requirements')
        business = request.form.get('business')

        global plans
        plans = [["Email:", email], ["Start Date:",start_date], ["End Date:",end_date], ["Country:",country], ["Area within country:",area], ["Interests:",interests], ["Accomodations:",accommodations], ["Wants to see:",requirements], ["How busy:",business]]
        return redirect(url_for('itinerary'))

    return render_template('home.html')

@app.route('/itinerary', methods =["GET", "POST"])
def itinerary():
    query = ''
    for i in plans:
        query += i[0] + i[1] + ". "

    itinerary_html = convo(query)

    return render_template('itinerary.html', itinerary_html=itinerary_html)


if __name__ == '__main__':
    app.run()
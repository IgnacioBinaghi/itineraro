from flask import Flask, render_template, request, redirect, url_for
import csv
import write
from generator import *
from mail_to_users import *
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
        budget = request.form.get('budget')

        global plans
        plans = [["Email:", email], ["Start Date:",start_date], ["End Date:",end_date], ["Country:",country], ["Area within country:",area], ["Interests:",interests], ["Accomodations:",accommodations], ["Wants to see:",requirements], ["How busy:",business], ["Budget:",budget]]

        if 'share' in request.form:
            return redirect(url_for('share'))
        elif 'create' in request.form:
            return redirect(url_for('itinerary'))

    return render_template('home.html')

@app.route('/itinerary', methods =["GET", "POST"])
def itinerary():
    query = ''
    for i in plans:
        query += i[0] + i[1] + ". "

    itinerary_html = convo(query)
    #itinerary_html = convoBard(query)
    #itinerary_html = " <h1>Itinerary for May 18, 2023 &#x1F4C5;</h1> <p>In the morning, you can start your day with a relaxing run through the Greenwich Point Park. After the run, grab some breakfast at the Elm Street Oyster House where you can enjoy some delicious pancakes and an omelette.</p>   <p>After breakfast, you can head over to the Beardsley Zoo to see some animals. Note that the zoo has a strict policy on food and does not allow outside food to be brought in, but fortunately, they have options for individuals with dietary restrictions, so be sure to let them know about your allergy to fish.</p>  <p>For lunch, you can head over to Back 40 Kitchen where you can enjoy some delicious farm-to-table cuisine. They have a great selection of vegetarian and gluten-free options as well.</p>  <p>In the afternoon, you can take a stroll around Greenwich Avenue and visit some of the unique shops and boutiques in the area. In the evening, you can have dinner at Mediterraneo where you can enjoy some fantastic Mediterranean-inspired cuisine.</p>  <h1>Itinerary for May 19, 2023 &#x1F43B;</h1> <p>In the morning, you can grab some breakfast at the Harvest Bakery where you can enjoy delicious pastries and coffee. If you have a bit more time, you can even take a baking class at the bakery.</p>  <p>After breakfast, you can head over to the Audubon Greenwich where you can take a leisurely walk through the sanctuary and enjoy some beautiful wildlife. The sanctuary is dedicated to conservation and wildlife education, so it is an excellent place to learn about local animals.</p>  <p>For lunch, you can head over to Meli-Melo where you can enjoy some delicious crepes and salads. They have vegetarian and gluten-free options as well, so there is something for everyone.</p>  <p>In the afternoon, you can take a stroll through the Bruce Museum where you can enjoy some fantastic art and exhibits. The museum has pieces that range from photography to sculpture, which makes it a diverse and exciting place to visit.</p>  <p>In the evening, you can have dinner at the Little Pub where you can enjoy some fantastic pub food. There are plenty of vegetarian options as well. </p>  <p>Note that all travel arrangements to and from these destinations will be done by you, and it is recommended that you stay at Greenwich Hotel, which is conveniently located near most destinations. </p>"

    #sendEmail(plans[0][1], itinerary_html)

    return render_template('itinerary.html', itinerary_html=itinerary_html)

@app.route('/share', methods =["GET", "POST"])
def share():
    with open("users.csv", 'a') as file:
        csv_writer = csv.writer(file, delimiter=',',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(plans)
    return render_template('share.html')



if __name__ == '__main__':
    app.run()
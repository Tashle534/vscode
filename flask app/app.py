from flask import Flask, render_template, request, redirect, url_for, session

import os
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about-us')
def about_us():
    return render_template('about-us.html')


@app.route('/contact-us')
def contact_us():
    return render_template('contact-us.html')   

@app.route('/booking-exhibition')
def booking_exhibition():
    session['booking'] = 'exhibition'
    session['first_name'] = request.form.get('firstname')
    session['last_name'] = request.form.get('lastname')
    session['email'] = request.form.get('email')    
    session['date'] = request.form.get('date')
    session['time'] = request.form.get('time')
    
    
    return render_template('booking-exhibition.html')

@app.route('/boooking-guided-tour')
def booking_guided_tour():
    session['booking'] = 'guided tour'
    session['first_name'] = request.form.get('firstname')
    session['last_name'] = request.form.get('lastname')
    session['email'] = request.form.get('email')    
    session['date'] = request.form.get('date')
    session['time'] = request.form.get('time')
    
    
    return render_template('booking-guided-tour.html')

if __name__ == '__main__':
    
    
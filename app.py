from flask import Flask, render_template, redirect, url_for, request
from .forms import HealthDataForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'virginia'

app.config['SQLALCHEMY_DATABSE_URI'] = 'sqlite://health_tracker.db' 
app.config['SQLALCHEMY_TRACKBACK_MODIFICATIONS'] = False

#Home Route
@app.route('/')
def home():
    return render_template('index.html')

#Form Route
@app.route('/form')
def form(request, methods = ['POST', 'GET']):
    form = HealthDataForm
    if form.request.method == 'POST' and form.save_on_validate():
        date = form.date.data
        execise = form.exercise.data
        sleep = form.sleep.data
        meditate = form.meditate.data
        return redirect(url_for('/dashboard'))
    return render_template('form.html', form= form)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
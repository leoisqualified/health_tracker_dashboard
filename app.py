from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

#Home Route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form')
def form(request, methods = ['POST', 'GET']):
    if request.method == 'POST':
        # TODO:
        return redirect(url_for('/dashboard'))
    return render_template('form.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
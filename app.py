from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/certifications')
def certifications():
    return render_template('certifications.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

app.run(debug=True , port= 5000)
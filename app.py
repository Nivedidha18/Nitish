from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')  # This will load the contact page

@app.route('/project')
def project():
    return render_template('project.html')  # This will load the project page

if __name__ == "__main__":
    app.run(debug=True)

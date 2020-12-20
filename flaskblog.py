from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author' : 'Chaitanya Kale',
        'title' : 'Practising Sucess',
        'People viewed this' : '68 Million'
    },

    {
        'author' : 'Kanchan Kale',
        'title' : 'Rules for Life',
        'People viewed this' : '88 Million'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', dictionary=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)   
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def about_me()->'html':
    return render_template("resume.html",
                           location = 'Ekaterinburg, Russia',
                           telephone = '+7(922)5682830', 
                           email = 'dimkkov99@gmail.com',
                           site = 'https://github.com/KowalskiVevo')

@app.route("/shop")
def resume()->'html':
    return render_template("index.html")

app.run(debug = True)
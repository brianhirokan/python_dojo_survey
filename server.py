from flask import Flask, render_template, request, redirect 
app = Flask(__name__)

@app.route('/')
def survey():
    return render_template('survey.html')

@app.route("/result", methods = ["POST"])
def result():
    name_from_survey = request.form['usernames']
    location_from_survey = request.form['locations']
    language_from_survey = request.form['languages']
    comment_from_survey = request.form['comments']
    return render_template('submitted.html', name_on_template = name_from_survey, location_on_template = location_from_survey,
                            language_on_template = language_from_survey, comment_on_template = comment_from_survey)

if __name__ == "__main__":
    app.run( debug = True )
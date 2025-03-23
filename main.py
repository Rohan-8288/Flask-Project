from flask import Flask,render_template,jsonify

app=Flask(__name__)

jobs=[
    {
        'id':1,
        'title':'Data Analyst',
        'location':'Bengaluru, India',
        'salary':'RS. 1,00,000'
    },
    {
        'id':2,
        'title':'Data Scientist',
        'location':'Delhi, India',
        'salary':'RS. 15,00,000'
    },
    {
        'id':3,
        'title':'Front-End Engineer',
        'location':'Remote',
        'salary':'RS. 12,00,000'
    },
    {
        'id':4,
        'title':'Back-End Engineer',
        'location':'San Francisco, USA',
        'salary':'$ 120,000'
    },
]
@app.route("/")
def home():
    return render_template("home.html",jobs=jobs)

@app.route("/api/jobs")
def listJobs():
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(debug=True)
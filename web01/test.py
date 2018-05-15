from flask import Flask, render_template
app=Flask(__name__) #tao ra 1 server/app

@app.route('/')
def index():
    posts=[
    {
    'title':"Thơ con ex",
    'content':"Ahihi",
    'author':"QD",
    'gender':1
    },
    {
    'title':"Thơ củ lạc",
    'content':"Lạy chúa trên cao, turndown for what",
    'author':"Minh",
    'gender':1
    },
    {
    'title':"GG Navi",
    'content':"Lạy chúa Dendi, trị vì muôn cõi",
    'author':"Miracle",
    'gender':0
    }
    ]
    return render_template("index.html",posts=posts)

@app.route("/c4e")
def sayhi():
    return "Hi C4E 17"

@app.route("/nb/<name>/<age>") #request parameter voi <> la ki hieu cua parameter
def nb(name,age):
    return "Hi {0}, you are {1} years old".format(name,age)

@app.route("/sum/<int:a>/<int:b>")
def sum(a,b):
    return "Sum is: " + str(a+b)

if __name__ == '__main__':
  app.run(debug=True)

from flask import Flask, render_template, request


# WSGI

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to Microinformatics, it's the home page. Haseeb Raza is a DS." 

@app.route('/about')
def about():
    return "<html><h1>Biotech and Data Science Education Start-Up</h1><html>"

@app.route('/index',methods=['GET','POST'])
def index():
    if request.method=='POST':
        pass
    return render_template('index.html')

### HTTP verbs, ## GET, POST

@app.route('/form', methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name=request.form['name']
        return f'Ya Salam {name}! '
    return render_template('form.html')
    




if __name__=="__main__":
    app.run(debug=True)
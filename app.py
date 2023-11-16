from flask import Flask, request, render_template 

app = Flask(__name__)
@app.route("/")
def home():
    if(request.method=='GET'):
        return render_template('main.html')
    else:
        username = request.form["bleh"]
        return username





if __name__ == "__main__":
    app.run(debug=True)
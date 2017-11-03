from flask import Flask, render_template, request #from --> model of something, library  of code which is Flask this time
import requests #request is like flask, library

app = Flask("MyApp") #import  Setting up the internal of the web server, app is the variable (a flask)

@app.route("/") 
def hello():   
	return "Hello World"


@app.route("/request_api")

def exchange_code(code):
	API_ENDPOINT = 'https://api.instagram.com/oauth/access_token'
	CLIENT_ID = '58afe6a207db45a0a4c709a6ce8fff0a'
	CLIENT_SECRET = '1d846b34d9b743b5b68d303e41eeeb57'
	REDIRECT_URI = 'https://food-print.herokuapp.com'
	data = {
    	'client_id': CLIENT_ID,
    	'client_secret': CLIENT_SECRET,
    	'grant_type': 'authorization_code',
    	'code': 'eccd0dee29284a7892de22ff9d98d81b',
    	'redirect_uri': REDIRECT_URI
 	}
  	print response.headers["content-type":'application/x-www-form-urlencoded']  
  	r = requests.post('%s/oauth2/token' %API_ENDPOINT, data, headers)
  	print r.url
	print r.raise_for_status()
	return r.json()
	 
@app.route("/index/<NumberOfIndex>/<hello>")  
def index(NumberOfIndex, hello):
	return int(NumberOfIndex)*hello 


@app.route("/foodprint/<name>", strict_slashes=False) 
def foodprint_website(name):
	return render_template("index.html", name=name)


@app.route("/foodprint", strict_slashes=False)
def foodprint_website2():
	return render_template("index.html")
	
@app.route("/signup", methods=["POST"])
def sign_up():
	form_data = request.form 
	print form_data["email"]  
	print requests.post(
       "https://api.mailgun.net/v3/sandbox628a63d1ccd742dd9ac51128b8c2ca53.mailgun.org/messages",
       auth=("api", "key-53a2b49ec0cae16153f7343713ebfc8d"),
       data={"from": "Excited User <mailgun@sandbox628a63d1ccd742dd9ac51128b8c2ca53.mailgun.org>",
             "to": [form_data["email"],"YOU@sandbox628a63d1ccd742dd9ac51128b8c2ca53.mailgun.org"], 
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"}
              ) 
	return "Thanks for submitting!" 

app.run(debug=True) 
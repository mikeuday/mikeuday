from flask import flask
app=Flask(__name__)


@app.route('/')
def home():
	return 'welcome to my creations'



if(__name__)==__main__:
	app.run(debug=True)



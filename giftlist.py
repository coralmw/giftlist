from flask import Flask, abort, redirect, url_for
app = Flask(__name__)

from Cheetah.Template import Template
import pickle
from simpledb import Client
from datetime import date

client = Client() # get db access.

# data model: keys are giftnames.
# key gifts has a list of known gifts.
# gifts have links, claimed status, and date claimed.
# need to schedule dumps.

# get page templates and static data.
with open("list.templ", "r") as f:
	listtempl = f.read()


@app.route("/")
def list():
	gifts = [client.get(name) for name in client.get("gifts")]
	nameSpace = {"giftdb":gifts, "url_for":url_for}
	body = Template(listtempl, searchList=[nameSpace])
	return str(body)

@app.route("/claim/<giftname>", methods=["POST"])
def claim(giftname):
	try:
		gift = client.get(giftname)
	except KeyError:
		abort(400) # gift does not exist.

	# should check if claimed allready and error??
	gift["claimed"] = True
	gift["claimdate"] = str(date.today())
	client.set(giftname, gift)
	return redirect(url_for("list")) 

@app.route("/release/<giftname>", methods=["POST"])
def release(giftname):
	try:
		gift = client.get(giftname)
	except KeyError:
		abort(400) # gift does not exist.

	# should check if claimed allready and error??
	gift["claimed"] = False
	gift["claimdate"] = None
	client.set(giftname, gift)
	return redirect(url_for("list")) 

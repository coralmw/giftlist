from flask import Flask, abort, redirect, url_for
app = Flask(__name__)

from Cheetah.Template import Template

# need some kind of DB.
# have a list of gifts, links to buy, and claimed status.
# captcha?
# keep backups so can revert list 10min/1h/1day of changes.

class Gift(object):

	def __init__(self, name, link, claimed=False):
		self.name = name
		self.link = link
		self.claimed = claimed
		self.claimdate = None

class GiftDB(object):

	def __init__(self):
		self.gifts = []

	def __getitem__(self, key):
		for gift in self.gifts:
			if gift.name == key:
				return gift
		raise KeyError

	def add(self, gift):
		self.gifts.append(gift)

# list as the prnt order should be consistent.
DB = GiftDB()
DB.add(Gift("spoons", "http://the.best.spoons.com"))
DB.add(Gift("fast car", "http://bmw.co.uk"))


with open("list.templ", "r") as f:
	listtempl = f.read()

print(listtempl)

@app.route("/")
def list():
	nameSpace = {"giftdb":DB.gifts}
	body = Template(listtempl, searchList=[nameSpace])
	return str(body)

@app.route("/claim/<giftname>", methods=["POST"])
def claim(giftname):
	try:
		gift = DB[giftname]
	except KeyError:
		abort(400) # gift does not exist.

	# should check if claimed allready and error??
	DB[giftname].claimed = True
	return redirect(url_for("list")) 

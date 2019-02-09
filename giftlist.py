from flask import Flask
app = Flask(__name__)

from Cheetah.Template import Template

# need some kind of DB.
# have a list of gifts, links to buy, and claimed status.
# captcha?
# keep backups so can revert list 10min/1h/1day of changes.

DB = {
  "spoons":("http://the.best.spoons.com/", False),
  "fast cars":("bmw.co.uk", False)
}

with open("list.templ", "r") as f:
	listtempl = f.read()

print(listtempl)

@app.route("/")
def list():
	nameSpace = {"giftdb":DB}
	body = Template(listtempl, searchList=[nameSpace])
	return str(body)

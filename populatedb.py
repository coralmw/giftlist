from simpledb import Client
client = Client() # get db access.

from datetime import date
today = date.today()


client.set('gifts', ["spoons", "fast car", "olive oil"])
client.set("spoons", {"name":"spoons", "link":"http://the.best.spoons.com", "claimed":False, "claimdate":None})
client.set("fast car", {"name":"fast car", "link":"http://bmw.co.uk", "claimed":False, "claimdate":None})
client.set("olive oil", {"name":"olive oil", "link":"http://oil.co.uk", "claimed":True, "claimdate":str(today)})

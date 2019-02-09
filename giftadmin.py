# /usr/bin/env python3
# list gifts, add gists, remove gifts.
from simpledb import Client
client = Client() # get db access.

import argparse
parser = argparse.ArgumentParser(description='Manage the giftlist.')
parser.add_argument("--list", "-l", action='store_true',
                    help='List gifts currently in the database.')

parser.add_argument("--add", "-a", nargs=2,
                    help='Adds a gift. --add NAME LINK.')

parser.add_argument("--delete", help='Removes a gift. --delete NAME.', default=None)

args = parser.parse_args()

if args.list:
    giftnames = client.get("gifts")
    print("List of gifts:{}".format(giftnames))
    
    if giftnames:
        for gift in [client.get(name) for name in giftnames]:
            print("{}: link - {}, claimed - {} on the {}".format(gift['name'], gift['link'], gift['claimed'], gift['claimdate']))

if args.add:
    name, link = args.add[0], args.add[1]
    newgifts = client.get("gifts")
    newgifts = newgifts+[name] if newgifts else [name]
    client.set("gifts", newgifts)
    client.set(name, {"name":name, "link":link, "claimed":False, "claimdate":None})

if args.delete:
    print("not impl!!")
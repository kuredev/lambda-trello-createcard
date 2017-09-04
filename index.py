# coding:utf-8
import requests
import yaml
import json
import sys
import urllib
import os
from datetime import date,timedelta

members = ""
key = ""
token = ""
idlist = ""
cardname = ""
idmembers = []
dayafter = 0
duedate = ""

########
def init():
	global members
	global key
	global token
	global idlist
	global cardname
	global dayafter
	global duedate

	# dataload
	f = open("data.yaml", "r")
	data = yaml.load(f)
	env = os.environ['ENV']
	if env == "PROD":
		members = data['membersprod']
		key = data['keyprod']
		token = data['tokenprod']
		idlist = data['idlistprod']
	elif env == "DEV":
		members = data['membersdev']
		key = data['keydev']
		token = data['tokendev']
		idlist = data['idlistdev']
	else:
		print "error!! No Environment Variable[ENV]"
		sys.exit()

	cardname = data['cardname']
	dayafter = data['dayafter']
	duedate = date.today() + timedelta(dayafter)
	f.close()

def get_memberid(username):
	payload = {'key':key,'token':token}
	r = requests.get("https://trello.com/1/members/" + username,params=payload)
	return json.loads(r.text)["id"]

def create_card(name, idmembers, due):
	payload = {'key':key,'token':token,'name':name,'idList':idlist,'idMembers':idmembers,'due':due}
	r = requests.post("https://trello.com/1/cards/", params=payload)
	return json.loads(r.text)["id"]

def create_checklist_to_card(card_id):
	payload = {'key':key,'token':token}
	r = requests.post("https://trello.com/1/cards/"+card_id+"/checklists", params=payload)
	return json.loads(r.text)["id"]

def create_checkitem(card_id, checklist_id, members):
	for member in members:
		print member
		print card_id
		print checklist_id
		payload = {'key':key,'token':token,'name':member}
		r = requests.post("https://trello.com/1/cards/"+card_id+"/checklist/"+checklist_id+"/checkitem", params=payload)

def lambda_handler(event, context):
	init()
	global idmembers
	for member in members:
		idmembers.append(get_memberid(member))

	card_id = create_card(cardname, ",".join(idmembers), duedate)
	checklist_id = create_checklist_to_card(card_id)
	create_checkitem(card_id,checklist_id,members)




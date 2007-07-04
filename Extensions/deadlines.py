#import MySQLdb
from time import *
from DateTime import DateTime

host   = "localhost"
user   = "dippdemo"
passwd = "dippdemo"
db     = "dippdemo"
"""
def getComments(instance_id, workitem_id):
    database = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
    cursor = database.cursor()
    query  = "SELECT activity_id, message FROM dipp_demo"
    query += " WHERE instance_id='" + instance_id + "'"
    query += "   AND workitem_id='" + workitem_id + "'"
    cursor.execute(query)
    result = cursor.fetchall()
    database.close()
    print query
    return  result
"""
def deadline_date(max,self):
	'''max: deadline des Atikels'''
	liste = []
	now = DateTime()
	if max == self.portal_properties.deadline_no:
		delta = self.portal_properties.deadline_max
	else:
		delta = max - now 
	for i in range(0, delta ):
		date = now + i
		if date.dow() == 0:
			klasse='sonntag'
		elif date.dow() == 6:
			klasse='samstag'
		else:
			klasse='wochentag'
		liste.append({'value':date,'class':klasse})
	return liste

def deadline_time(selected):
	liste = []
	for i in range(24):
		if i == selected:
			select = "selected"
		else:
			select = ""
		liste.append({'H':i,'M':'00','selected':select})
	return liste

def deadline_delay(date,self):
	red    = self.portal_properties.deadline_red
	yellow = self.portal_properties.deadline_yellow
	days   = date - DateTime()
	delay  = {}

	delay['days'] = str(int(days))
	hours = DateTime((days - int(days)) * 24 * 60 * 60)
	delay['hours'] = hours
	if days <= red:
		alert = "red"
	elif red < days < yellow:
		alert = "yellow"
	else:
		alert = "green"
	delay['class'] = alert
	return delay

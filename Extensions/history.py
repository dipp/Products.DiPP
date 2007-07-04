import MySQLdb
from time import *
from DateTime import DateTime

host   = "localhost"
user   = "rtejournal"
passwd = "rtejournal"
db     = "dipp"

table  = "rtejournal"

def getComments(instance_id, workitem_id):
    database = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
    cursor = database.cursor()
    query  = "SELECT activity_id, message FROM " + table
    query += " WHERE instance_id='" + instance_id + "'"
    query += "   AND workitem_id='" + workitem_id + "'"
    cursor.execute(query)
    result = cursor.fetchall()
    database.close()
    print query
    return  result



def insert(instance_id,workitem_id,process_id,activity_id,actor,formalOK,autorOK,gastHrsgOK,message,deadline,deadline_next,autor,titel):
    connection = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
    cursor = connection.cursor()
    query  = "INSERT INTO " + table + " SET "
    query += "instance_id='" + instance_id + "', "
    query += "workitem_id='" + workitem_id + "', "
    query += "process_id='"  + process_id + "', "
    query += "activity_id='" + activity_id + "', "
    query += "message='" + message + "', "
    query += "autor='" + autor + "', "
    query += "titel='" + titel + "', "
    query += "formalOK='" + formalOK + "', "
    query += "autorOK='" + autorOK + "', "
    query += "gastHrsgOK='" + gastHrsgOK + "', "
    query += "deadline='" + deadline + "', "
    query += "deadline_next='" + deadline_next + "', "
    query += "actor='"       + actor + "'"
    cursor.execute(query)
    connection.close()

"""
def get(instance_id):
    connection = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
    cursor = connection.cursor()
    #query  = "SELECT * FROM instances"
    query  = "SELECT * FROM instances WHERE "
    query += "instInstance_id='" +instance_id + "'"
    cursor.execute(query)
    connection.close()    
    result = cursor.fetchall()
    return  result

print get('hrsg1088586400.37')


def insert2(instId,processId,instAutor,instTitel,instJahr,instAusgabe,instArtikel,instFormalOk,instAutorOk,instNachrichten):
    connection = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
    cursor = connection.cursor()
    query  = "INSERT INTO instance SET "
    query += "instId='" + instId + "', "
    query += "processId='" + processId + "', "
    query += "instAutor='" + instAutor + "', "
    query += "instTitel='" + instTitel + "',  "
    query += "instJahr='" + instJahr + "',  "
    query += "instAusgabe='" + instAusgabe + "',  "
    query += "instArtikel='" + instArtikel + "',  "
    query += "instFormalOk='" + instFormalOk + "',  "
    query += "instAutorOk='" + instAutorOk + "',  "
    query += "instNachrichten='" + instNachrichten + "' "
    connection.close()    
    cursor.execute(query)

	# get the resultset as a tuple
	#result = cursor.fetchall()
"""

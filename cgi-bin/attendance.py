import cgi,cgitb,sqlite3,time,calendar,datetime
cgitb.enable()

print('Content-Type: text/html')
print()


#Getting timestamp
ts = calendar.timegm(time.gmtime())

#Connecting to data base.
conn=sqlite3.connect('ams.db')
tcon=sqlite3.connect('attendance.db')

#Getting data from takeattandance.py
form=cgi.FieldStorage()
classname=(str(form["classname"].value)).strip()
subject=(str(form["subject"].value)).strip()
id=str((form["id"].value)).strip()
noofhours=int(form["noofhours"].value)
att=form.getlist("att")
porab=str(form["porab"].value)
hours=str(form["hours"].value)
datetime=form["date"].value

#Query for inserting data into staffattendancelog table.
query="insert into staffattendancelog ('id','datetime','classname','subject','timestamp','noofhours','hours') values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(str(id),str(datetime),str(classname),str(subject),int(ts),int(noofhours),hours)
temp=conn.execute(query)
conn.commit()


#Query for getting sno from staffattendancelog table.
squery="select sno from staffattendancelog where id='{0}' and subject='{1}' and classname='{2}' and timestamp='{3}'".format(id,subject,classname,str(ts))
sno=conn.cursor()
sno.execute(squery)
sno=sno.fetchall()

#Query for inserting data into studentattandancelog
iquery="insert into studentattandancelog values(?,?,?)"


#Query for updating the total no.of hours taken by a staff in particular class and particular subject.
tnhquery="update staffclass set tnhours=tnhours + {0} where id='{1}' and subject='{2}' and batch='{3}' and section='{4}' and classname='{5}'".format(noofhours,id,subject,classname[0:9],classname[-1],classname[10:len(classname)-2])
tncursor=conn.cursor()
tncursor.execute(tnhquery)
conn.commit()

#converting att in str to att in int
att=[int(x) for x in att]

#Adding attandance in studentattandancelog table.
sno=int(sno[0][0])
if porab=='present':
    for rno in att:
        a,b=conn.execute(iquery,(rno,noofhours,sno)),conn.commit()
if porab=='absent':
    for rno in att:
        a,b=conn.execute(iquery,(rno,0,sno)),conn.commit()

#Query for updating the main attandance table.
subatt="update '{0}' set {2}={2} + {1} where rno".format(classname,noofhours,subject)
subatt=subatt+'= {0}'

#Query for getting rno from required table.
query="select rno from '{0}'".format(classname)
cur = tcon.cursor()
cur.execute(query)
data = cur.fetchall()


#Finally entering attandance
if porab=='absent':
    att=list(set([x[0] for x in data])-set(att))

att.append(0)
for rno in att:
	a,b=tcon.execute(subatt.format(rno)),tcon.commit()


#Redirecting to stafftakeattendance.py
if temp:
    print('''
	<!DOCTYPE html>
    <html>
    <head>
    <title></title>
	<script>window.alert("Successful");</script>
	<script>window.location.href="stafftakeattendance.py";</script>
    </head>
    <body>
    </body>
    </html>
	''')

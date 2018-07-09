import cgi,cgitb,sqlite3
cgitb.enable()

print('Content-Type: text/html')
print()

#Getting form data
form=cgi.FieldStorage()
batch=str(form["batch"].value).strip()
year=str(form["year"].value).strip()
sem=str(form['sem'].value).strip()
nsubs=int(form["nsubs"].value)
nsecs=int(form["nsecs"].value)
subjects=[x.strip() for x in form.getlist("subjects")]
sections=[x.strip() for x in form.getlist("sections")]
snos=[int(x) for x in form.getlist("sno")]
enos=[int(x) for x in form.getlist("eno")]
facids=[int(x) for x in form.getlist("facid")]
facids=iter(facids)
subjectsset,sectionsset=list(set(subjects)),list(set(sections))

#Query for inserting into staffclass table.
insertstaffclass="insert into staffclass values(?,?,?,?,?,?,?)"


if len(subjectsset)!=nsubs or len(sectionsset)!=nsecs:
    print('''
	<!DOCTYPE html>
    <html>
    <head>
    <title></title>
	<script>window.alert("please enter proper data(don't enter duplicate data)");window.location.href='admincreatebatch.py'</script>
    </head>
    <body>
    </body>
    </html>
	''')
for i in range(0,len(snos)):
    if not snos[i]<enos[i]:
	    print('''
	<!DOCTYPE html>
    <html>
    <head>
    <title></title>
	<script>window.alert("please enter proper data(enter correct range of numbers)");window.location.href='admincreatebatch.py'</script>
    </head>
    <body>
    </body>
    </html>
	''')

#Getting tables	
conn=sqlite3.connect("attendance.db")
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables=cursor.fetchall()

amsconn=sqlite3.connect("ams.db")

#Converting lower to upper.
year=year.lower()
sections=[x.upper() for x in sections]
subjects=[x.upper() for x in subjects]
subjectall=list(subjects)
#Replacing - with _.
branch=batch+'_'+year+sem
branch=branch.replace('-','_')
newtables=[]

subjects=''.join([(", "+x+" INTEGER") for x in subjects])

#creating sections adn attendance list
for i in sections:
    newtables.append("create table {0} (rno INTEGER {1})".format("'"+branch+i+"'",subjects))
	
questionmarks=['?']*(nsubs+1)
initiating=[0]*nsubs
sattendance=[]

for i in range(nsecs):
    sattendance.append([[i]+initiating for i in range(snos[i],enos[i]+1)])

#subjectsall=iter(list(subjects)*nsecs)
for i in sections:
    for j in range(nsubs):
        amsconn.execute(insertstaffclass,(str(next(facids)), year.replace('-', '_'), subjectall[j], 0, batch.replace('-', '_'), sem, i))
        amsconn.commit()

for i in range(nsecs):
    try:
	    t1,t2,t3,t4=conn.execute(newtables[i]),conn.executemany('INSERT INTO {0} VALUES ({1})'.format("'"+branch+sections[i]+"'",','.join(questionmarks)),sattendance[i]),conn.execute('INSERT INTO {0} VALUES ({1})'.format("'"+branch+sections[i]+"'",','.join(questionmarks)),initiating+[0]),conn.commit()

    except:
	    print('''
	<!DOCTYPE html>
    <html>
    <head>
    <title></title>
	<script>window.alert("Creating the same table another time.");window.location.href='admincreatebatch.py'</script>
    </head>
    <body>
    </body>
    </html>
	''')
    
print('''
	<!DOCTYPE html>
    <html>
    <head>
    <title></title>
	<script>window.alert("Successfull.......!!");window.location.href='admincreatebatch.py'</script>
    </head>
    <body>
    </body>
    </html>
	''')
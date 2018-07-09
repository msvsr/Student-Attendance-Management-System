import cgi,cgitb,sqlite3,variable
cgitb.enable()

print('Content-Type: text/html')
print()

#Connecting to data base.
conn=sqlite3.connect('ams.db')

#Getting form data.
form=cgi.FieldStorage()

#Form for getting cookie data using java script.
if not form:
    print(variable.cookiedata1, "staffclasses.py", variable.cookiedata2)

#Splitting Cookie data into userid and usertype
uname,utype=(form["cookiedata"].value).split()

#Query for getting data from staffclass table.
query="select * from staffclass where id='{0}'".format(str(uname))
cur = conn.cursor()
cur.execute(query)
data = cur.fetchall()

table=''
if data:
    table="<h4>You have the following classes:</h4><table border='3px' cellspacing='5px' cellpadding='5px'><tr align='center'><th>ClassName</th><th>Batch</th><th>Semister</th><th>Subject</th><th>Section</th><th>Total no.of Hours</th></tr>"
if data:
    for noofrows in range(0,len(data)):
        table=table+"<tr align='center'><td>"+data[noofrows][1]+"</td><td>"+str(data[noofrows][4])+"</td><td>"+str(data[noofrows][5])+"</td><td>"+data[noofrows][2]+"</td><td>"+str(data[noofrows][6])+"</td><td>"+str(data[noofrows][3])+"</td></tr>"
if data:
    table+="</table>"
	

#Query for getting data from staffclass table.
query="select * from staffclass where id={0}".format(str(uname))
cur = conn.cursor()
cur.execute(query)
data = cur.fetchall()

formfields=""
if data:
    for row in range(0,len(data)):
        formfields+="<input type='checkbox' name='classname' value='"+str(data[row][1])+" "+str(data[row][6])+" "+str(data[row][4])+" "+str(data[row][5])+" "+str(data[row][2])+"'>"+str(data[row][1])+" "+str(data[row][6])+" "+str(data[row][4])+" "+str(data[row][5])+" "+str(data[row][2])+'''&nbsp&nbsp&nbsp&nbsp'''
else:
    formfields="You don't have any class."

if formfields!="You don't have any class.":
    formfields+='''<br><input type="submit" value="remove">'''	

#Splitting Cookie data into userid and usertype
uname,utype=(form["cookiedata"].value).split()

#Printing staffaddclass page.
print('''
<!doctype html>
<html>
<head>
<title>staffaddorremoveclass</title>
<link rel="stylesheet" href="/staffstyles.css" >
''',variable.loginornot,variable.changepassword,'''
</head>

<body onload="shows_form_part(0)">
	<div class="width">
		''',variable.logout,'''
		<header>
			
				<h2>Welcome to Attandance Management System</h2>
				<div class="tagline">
					<p>Your classes.</p>
				</div>
			
		</header>
		<section id="body" class="clear">
			''',variable.stafflinks,'''
		<section id="content" class="column-right">		
	    <article>''',table,'''<br>
		  </div>
		</article>
		<article>

		</article>
		</section>
	</section>
	</div>
</body>
</html>
     ''') 
import cgi,cgitb,sqlite3,variable
cgitb.enable()

print('Content-Type: text/html')
print()

#Connecting to data base.
conn=sqlite3.connect('ams.db')
cur=conn.cursor()

#Getting form data.
form=cgi.FieldStorage()

#Form for getting cookie data using java script.
if not form:
    print(variable.cookiedata1, "staffgenrep.py", variable.cookiedata2)

#Getting user name
uname,usertype=(form["cookiedata"].value).split()
uname=int(uname)
#Query for getting data from the staffclass table.
query="select * from staffclass where id={0}".format(uname)
cur.execute(query)
data=cur.fetchall()

formfields=""
if data:
    for row in range(0,len(data)):
        formfields+="<input type='radio' name='classname' value='"+str(data[row][4])+"_"+str(data[row][1])+str(data[row][5])+str(data[row][6])+" "+str(data[row][2])+"' checked>"+str(data[row][1])+" "+str(data[row][6])+" "+str(data[row][4])+" "+str(data[row][2])+'''<br>'''
else:
    formfields="Please add a class."

if formfields!="Please add a class.":
    formfields+='''<br><input type="submit" value="submit">'''
	
#Printing staffgenrep home page.
print('''
<!doctype html>
<html>
<head>
<title>staffhome</title>
<link rel="stylesheet" href="/staffstyles.css" >
''',variable.loginornot,'''
<script>function changepassword(){window.location.href='/changepassword.html'}</script>
</head>

<body>
	<div class="width">
		''',variable.logout,'''
		<header>
			
				<h2>Welcome to Attandance Management System</h2>
				<div class="tagline">
					<p>It's your profile.</p>
				</div>
			
		</header>
		<section id="body" class="clear">
		''',variable.stafflinks,'''
		<section id="content" class="column-right">		
	    <article>
		<h5>Choose a class</h5><br>
		<form method="post" action="genrepbystaff.py">
		Attendance less than or equal to:
		<input type="number" name="percentage" value='100' min='0' max='100' required><br>
		<input type="hidden" name="id" value="''',uname,'''"><br>
		Select a class.<br>
		''',formfields,'''<br>
		</article>
		<article>
		</article>
		</section>
	</section>
	</div>
</body>
</html>
     ''') 
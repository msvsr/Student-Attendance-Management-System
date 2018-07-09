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
    print(variable.cookiedata1, "stafftakeattendance.py", variable.cookiedata2)

#Splitting Cookie data into userid and usertype
uname,utype=(form["cookiedata"].value).split()

#Query for getting data from staffclass table.
query="select * from staffclass where id={0}".format(str(uname))
cur = conn.cursor()
cur.execute(query)
data = cur.fetchall()

formfields=""
if data:
    for row in range(0,len(data)):
        formfields+="<input type='radio' name='classname' value='"+str(data[row][4])+"_"+str(data[row][1])+str(data[row][5])+str(data[row][6])+" "+str(data[row][2])+"' checked>"+str(data[row][1])+" "+str(data[row][6])+" "+str(data[row][4])+" "+str(data[row][2])+'''<br>'''
else:
    formfields="Please add a class."

if formfields!="Please add a class.":
    formfields+='''<br><input type="submit" value="submit">'''
#Printing stafftakeattendance page.
print('''
<!doctype html>
<html>
<head>
<title>stafftakeattendance</title>
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
					<p>Take attendance.</p>
				</div>
			
		</header>
		<section id="body" class="clear">
		''',variable.stafflinks,'''	
		<section id="content" class="column-right">		
	    <article>
		<h5>Choose a class</h5><br>
		<form method="post" action="takeattendance.py">
		<input type="hidden" name="id" value="''',uname,'''"><br>
		''',formfields,'''
		</form>
		</article>
		<article>
		</article>
		</section>
	</section>
	</div>
</body>
</html>
     ''') 
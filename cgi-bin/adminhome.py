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
    print(variable.cookiedata1,"adminhome.py",variable.cookiedata2)

#Splitting Cookie data into userid and usertype
uname,utype=(form["cookiedata"].value).split()

#Query for getting data of a admin from admin table.
squery="select * from admin where id=(?)"
cur = conn.cursor()
cur.execute(squery,(uname,))
data = cur.fetchall()

#Printing admin page.
print('''
<!doctype html>
<html>
<head>
<title>adminhome</title>''',variable.loginornot,'''<link rel="stylesheet" href="/adminstyles.css" >
''',variable.changepassword,'''
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
		''',variable.adminlinks,'''
		<section id="content" class="column-right">		
	    <article>
		<h1>Your Profile</h1>
		</article>
		<article>
        <table>
		<tr><td>User Id</td><td><B>''',data[0][0],'''<B></td></tr>
		<tr><td>Name</td><td>''',data[0][2],'''</td></tr>
		<tr><td>Mail Id</td><td>''',data[0][4],'''</td></tr>
		<tr><td>PhoneNo</td><td>''',data[0][3],'''</td></tr>
		</table>
		</article>
		</section>
	</section>
	</div>
</body>
</html>
     ''')
import cgi, cgitb, sqlite3, variable

cgitb.enable()

print('Content-Type: text/html')
print()

# Connecting to data base.
conn = sqlite3.connect('ams.db')

# Getting form data.
form = cgi.FieldStorage()

# Form for getting cookie data using java script.
if not form:
    print(variable.cookiedata1, "adminupdateprofile.py", variable.cookiedata2)

# Splitting Cookie data into userid and usertype
uname, utype = (form["cookiedata"].value).split()

# Query for getting data of a admin from admin table.
squery = "select * from admin where id=(?)"
cur = conn.cursor()
cur.execute(squery, (uname,))
data = cur.fetchall()

# Printing admin page.
print('''
<!doctype html>
<html>
<head>
<title>adminupdateprofile</title>''', variable.loginornot, '''<link rel="stylesheet" href="/adminstyles.css" >
''', variable.changepassword, '''
</head>
<body>
	<div class="width">
		''', variable.logout, '''
		<header>

				<h2>Welcome to Attandance Management System</h2>
				<div class="tagline">
					<p>update your profile here.</p>
				</div>

		</header>
		<section id="body" class="clear">
		''', variable.adminlinks, '''
		<section id="content" class="column-right">		
	    <article>
		<h1>Your Profile</h1>
		</article>
		<article>

		<form action="homechanges.py" method="post">
		<table>
		<tr><td>User Id</td><td><B>''', data[0][0], '''<B></td></tr>
		<tr><td>Name</td><td><input type="text" name="username" value=''', data[0][2], ''' placeholder=''', data[0][2], ''' required></td></tr>
		<tr><td>Mail Id</td><td><input type="email" name="gmail" value=''', data[0][4], ''' placeholder=''', data[0][4], ''' required></td></tr>
		<tr><td>PhoneNo</td><td><input type="number" name="phoneno" size="4" value=''', data[0][3], ''' placeholder=''',
      data[0][3], '''required></td></tr>
		</table>
		<input type="hidden" name="userid" value=''', uname, ''' >
		<input type="hidden" name="usertype" value=''', utype, ''' >
		<input type="submit" value="Save changes">
		</form>
		<input type="button" onclick="changepassword()" value="Change password">
		</article>
		</section>
	</section>
	</div>
</body>
</html>
     ''')
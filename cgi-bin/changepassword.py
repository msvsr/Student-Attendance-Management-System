import cgi,cgitb,sqlite3
cgitb.enable()

#Connecting to database. 
conn = sqlite3.connect('ams.db')

#Getting form data.
form=cgi.FieldStorage()
usertype=form["usertype"].value
username=form["username"].value
oldpassword=form["oldpassword"].value
newpassword=form["newpassword"].value
cnewpassword=form["cnewpassword"].value

#Getting data from table of usertype.
query="select id,password from "+usertype


print('Content-Type: text/html')
print()

#Checking userid and old password in database and evaluating newpassword,confirm new password.
#Returning to changepassword.html page if failed.	
if not (form["username"].value,form["oldpassword"].value) in conn.execute(query) and newpassword!=cnewpassword:
    print('''
	<!DOCTYPE html>
    <html>
    <head>
    <title></title>
    <script>window.alert("Username or oldpassword is incorrect and newpassword and confirmed new password are not same")</script>
	<script>window.location.href='/changepassword.html'</script>
    </head>
    <body>
    </body>
    </html>
	''')
	
#Checking userid and old password in database.
#Returning to changepassword.html page if failed.	
if not (form["username"].value,form["oldpassword"].value) in conn.execute(query):
    print('''
	<!DOCTYPE html>
    <html>
    <head>
    <title></title>
    <script>window.alert("Username or oldpassword is incorrect")</script>
	<script>window.location.href='/changepassword.html'</script>
    </head>
    <body>
    </body>
    </html>
	''')
	
	
#Evaluating newpassword,confirm new password.
#Returning to changepassword.html page if failed.
if newpassword!=cnewpassword:
    print('''
	<!DOCTYPE html>
    <html>
    <head>
    <title></title>
    <script>window.alert("Newpassword and confirmed new password are not same")</script>
	<script>window.location.href='/changepassword.html'</script>
    </head>
    <body>
    </body>
    </html>
	''')
	
#Query for updating password.
query=("update {0} set password = '{1}' where id = '{2}'").format(str(usertype),str(newpassword),str(username))
conn.execute(query)
conn.commit()

#If user is admin type redirecting to adminhome page.
if usertype=='admin':  
    print('''
	<!DOCTYPE html>
    <html>
    <head>
    <title></title>
	<script>document.cookie = "username=''',username,''' ''',usertype,'''";</script>
	<script>window.alert("Successfully changed the password");window.location.href='adminhome.py'</script></head>
    <body>
    </body>
    </html>
	''')

#If user is staff redirecting to staffhome page.	
elif usertype=='staff':
    print('''
	<!DOCTYPE html>
    <html>
    <head>
    <title></title>
	<script>document.cookie = "username=''',username,''' ''',usertype,'''";</script>
	<script>window.alert("Successfully changed the password");window.location.href='staffhome.py'</script></head>
    <body>
    </body>
    </html>
	''')
    
#If user is student redirecting to studenthome page.	
else:
    print('''
	<!DOCTYPE html>
    <html>
    <head>
    <title></title>
	<script>document.cookie = "username=''',username,''' ''',usertype,'''";</script>
	<script>window.alert("Successfully changed the password");window.location.href='studenthome.py'</script></head>
    <body>
    </body>
    </html>
	''')
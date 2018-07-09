import cgi,cgitb,sqlite3
cgitb.enable()

#Connecting to database.
conn = sqlite3.connect('ams.db')
cur=conn.cursor()

#Getting data from form(index.html)
form=cgi.FieldStorage()
usertype=(form["usertype"].value).strip()
username=(form["username"].value).strip()

#Query for getting data from admin or staff or student table.
query="select id from {0}"
query=query.format(usertype)


print('Content-Type: text/html')
print()

if usertype in ['admin','staff']:
    t1,data=cur.execute(query),cur.fetchall()

#For admin and staff.
	
if usertype in ['admin','staff'] and (username,) in data:
    print('''
	<!DOCTYPE html>
<html>
<head>
<title>preAMSindex</title>
 <link rel="stylesheet" href="/styles.css">
</head>
<body align="center">
<form align ="center" action="main.py" method="post" autocomplete="on">
  <input type="password" name="password" placeholder="P A S S W O R D" required><br><br>
  <input type="hidden" name="usertype" value="''',usertype,'''" >
  <input type="hidden" name="username" value="''',username,'''" >
  <input type="submit" value="LOGIN">
  <input type="reset" value="RESET"><br>
  <a href="#">Forgot your password?</a>
</form> 
</body>
</html>
	''')

#If user is student
if usertype=='student':  
    print('''
	<!DOCTYPE html>
    <html>
    <head>
    <title></title>
	<script>window.location.href='studenthome.py'</script></head>
    <body>
    </body>
    </html>
	''')

if usertype in ['admin','staff'] and (username,) not in data:
    print('''
	<!DOCTYPE html>
    <html>
    <head>
    <title></title>
	<script>window.alert("user does not exists.....")</script>
	<script>window.location.href='/index.html'</script>
	</head>
    <body>
    </body>
    </html>
	''')

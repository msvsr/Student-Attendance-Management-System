import cgi,cgitb,sqlite3
cgitb.enable()

#Connecting to database.
conn = sqlite3.connect('ams.db')
cur=conn.cursor()


#Getting data from form(index.html)
form=cgi.FieldStorage()
usertype=(form["usertype"].value).strip()
username=(form["username"].value).strip()
password=(form["password"].value).strip()

#Query for getting data from admin or staff or student table.
query="select id,password from {0}"
query=query.format(usertype)
cur.execute(query)
data=cur.fetchall()

#sessions here.
'''  '''

#If not logged in checks for validity of user.	
if (username,password) not in data:
    print('''
	<!DOCTYPE html>
    <html>
    <head>
    <title></title>
    <script>window.alert("Password is incorrect")</script>
	<script>window.location.href='/'</script>
    </head>
    <body>
    </body>
    </html>
	''')

#If user is admin it will redirect to admin home page.
if usertype=='admin':  
    print('''
	<!DOCTYPE html>
    <html>
    <head>
    <title></title>
	<script>document.cookie = "username=''',username,''' ''',usertype,'''";</script>
	<script>window.location.href='adminhome.py'</script></head>
    <body>
    </body>
    </html>
	''')

#If user is staff it will redirect to staff home page.
elif usertype=='staff':
    print('''
	<!DOCTYPE html>
    <html>
    <head>
    <title></title>
	<script>document.cookie = "username=''',username,''' ''',usertype,'''";</script>
	<script>window.location.href='staffhome.py'</script></head>
    <body>
    </body>
    </html>
	''')
    

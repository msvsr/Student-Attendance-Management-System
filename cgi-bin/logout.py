import cgi,cgitb,sqlite3,variable
cgitb.enable()

#Getting data from form.
form=cgi.FieldStorage()
conn=sqlite3.connect("ams.db")

print('Content-Type: text/html')
print()

#Form for getting cookie data using java Script.
if not form:
    print(variable.cookiedata1, "logout.py", variable.cookiedata2)

#Getting Cookiedata from form.(hidden form)	
uname,utype=(form["cookiedata"].value).split()


#Logging out of a user(deleting cookies)
print('''
	<!DOCTYPE html>
    <html>
    <head>
    <title></title>
	<script>var s=document.cookie;window.alert("Loggin Out: "+s.substr(9));</script>
	<script>document.cookie = "username=;"</script>
	<script>window.location.href='/'</script>
    </head>
    <body>
    </body>
    </html>
	''')

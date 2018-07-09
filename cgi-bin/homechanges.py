import cgi,cgitb,sqlite3
cgitb.enable()

#Connecting to database  
conn = sqlite3.connect('ams.db')

#Getting form data.
form=cgi.FieldStorage()
userid=form["userid"].value
usertype=form["usertype"].value
username=form["username"].value
email=form["gmail"].value
phoneno=str(form["phoneno"].value)

#Updating the data.
query=("update {0} set mailid = '{1}' , phoneno = '{2}', name= '{3}' where id = '{4}'").format(str(usertype),str(email),str(phoneno),str(username),str(userid))
conn.execute(query)
conn.commit()

page=usertype+"home.py"

print('Content-Type: text/html')
print()
	
#Redirecting to usertype home on success.
print('''
	<!DOCTYPE html>
    <html>
    <head>
    <title></title>
    <script>window.alert("Updated Successfully")</script>
	<script>window.location.href="''',page,'''"</script>
    </head>
    <body>
    </body>
    </html>
	''')
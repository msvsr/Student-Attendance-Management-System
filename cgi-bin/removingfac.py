import cgi,cgitb,sqlite3
cgitb.enable()

#Connecting to data base.
conn = sqlite3.connect('ams.db')

#Getting data from form.
form=cgi.FieldStorage()
names=list(set(form.getlist("names")))

print('Content-Type: text/html')
print()

#If no values are entered in form it will raise an alert box and redirect to adminremfac.py 
if not names:
    print('''
	<!DOCTYPE html>
    <html>
    <head>
    <title></title>
	<script>window.alert("please enter Staff Id's");window.location.href='adminremfac.py'</script>
    </head>
    <body>
	</script>
    </body>
    </html>
	''')

#Query for removing faculty.	
query="delete from staff where id = '{0}'"

#Query for selecting data from staff table.
rquery="select id from staff"

#for loop for adding data into staff table after checking the table for avoiding constraint failures.
for faculty in names:
    if (str(faculty),) in conn.execute(rquery):
	    TEMP=conn.execute(query.format(str(faculty))),conn.commit()

#After successfull creation redirecting to adminremfac.py
print('''
	<!DOCTYPE html>
    <html>
    <head>
    <title></title>
	<script>window.alert("Successfully removed.");window.location.href='adminremfac.py'</script>
    </head>
    <body>
	</script>
    </body>
    </html>
	''') 	
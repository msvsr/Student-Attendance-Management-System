import cgi,cgitb,sqlite3
cgitb.enable()

#Connecting to data base.
conn = sqlite3.connect('ams.db')

#Getting data from form adminremstu.py
form=cgi.FieldStorage()
starting,ending=(str(form["starting"].value).strip()),(str(form["ending"].value).strip())

print('Content-Type: text/html')
print()

#Checking starting and ending have entered correctly or not.
if not starting<ending:
    print('''
	<!DOCTYPE html>
    <html>
    <head>
    <title></title>
	<script>window.alert("please enter a proper range");window.location.href='adminremstu.py'</script>
    </head>
    <body>
	</script>
    </body>
    </html>
	''')

#Query for inserting data in to staff.
query="insert into staff (id,password) values(?,?)"

#Query for getting data from staff table.
rquery="select id from staff"
c=conn.cursor()
c.execute(rquery)
data=c.fetchall()

#Declaring empty list.
l=list()

#for loop for checking if faculty already in the staff table or not and adding it to list l 
# if the faculty id present in staff table.
for faculty in range(int(starting),int(ending)+1):
    if (str(faculty),) in conn.execute(rquery):
        l.append(faculty)

#for loop for adding data into the table if the staff id is not present in the staff table.
for faculty in range(int(starting),int(ending)+1):
    if (str(faculty),) not in data:
        a, b = conn.execute(query, (str(faculty), str(faculty))), conn.commit()

#If l is not empty it will raise an alert box showing duplicate values of data.
# After that it will redirect to adminaddfac.py
if l:   
    print('''
	<!DOCTYPE html>
    <html>
    <head>
    <title></title>
	<script>window.alert("These staff ids are already created.''',l,''' and successfully created for others");window.location.href='adminaddfac.py'</script>
    </head>
    <body>
	</script>
    </body>
    </html>
	''') 

#Redirecting to adminaddfac.py
else:
    print('''
	<!DOCTYPE html>
    <html>
    <head>
    <title></title>
	<script>window.alert("Successfully created.");window.location.href='adminaddfac.py'</script>
    </head>
    <body>
	</script>
    </body>
    </html>
	''') 	
		
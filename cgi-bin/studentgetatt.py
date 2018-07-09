import cgi,cgitb,sqlite3
cgitb.enable()

print('Content-Type: text/html')
print()

#Connecting to data base.
conn=sqlite3.connect('attendance.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables=cursor.fetchall()
tables=[t[0] for t in tables]

#Getting form data
form=cgi.FieldStorage()
rno=int(str(form["rno"].value).strip())
batch=str(form["batch"].value).strip().lower()
year=str(form["year"].value).strip().lower()
sem=str(form['sem'].value).strip()
section=str(form['section'].value).strip().upper()

classname=(batch+'_'+year+sem+section).replace('-','_')

#query for getting student attandance:

if classname not in tables:
    print('''
	<!DOCTYPE html>
    <html>
    <head>
    <title></title>
    <script>window.alert("Please enter correct information");</script>
	<script>window.location.href="studenthome.py"</script>
    </head>
    <body>
    </body>
    </html>
	''')

cursor.execute("PRAGMA table_info('{0}')".format(classname))
subs=cursor.fetchall()
subs=[i[1] for i in subs]

attendancequery="select * from '{0}' where rno='{1}'".format(classname,rno)
cursor.execute(attendancequery)
attendance=cursor.fetchall()

thoursqy="select * from '{0}' where rno='{1}'".format(classname,0)
cursor.execute(thoursqy)
thours=cursor.fetchall()

attsum,tsum=0,0
atable="<table border='3px' cellspacing='2px' cellpadding='2px'>"
atable+="<tr><th>Subject</th><th>Attendance/Total no.of hours</th></tr>"
for i in range(1,len(subs)):
    atable,attsum,tsum=atable+"<tr><td>"+subs[i]+"</td><td>"+str(attendance[0][i])+'/'+str(thours[0][i])+"</td></tr>",(attsum+attendance[0][i]),(tsum+thours[0][i])
atable+="<tr><th>TOTAL</th><td>"+str(attsum)+'/'+str(tsum)+"</td></tr>"
atable+="</table>"

print('''
<!doctype html>
<html>
<head>
<title>studentatt</title>
<link rel="stylesheet" href="/adminstyles.css" >
<meta name="viewport" content="width=device-width, minimum-scale=1.0, maximum-scale=1.0" />
</head>

<body>
	<div class="width">
		<header>
				<h2>Welcome to Attandance Management System</h2>
				<div class="tagline">
					<p>Your attandance.</p>
				</div>	
		</header>
		
		<section id="body" class="clear">
			<aside id="sidebar" class="column-left">
			<ul>
                	<li>
                        <ul class="blocklist">
						     <br>
							<li class="selected-item"><a href="/index.html">Home</a></li>
                            <li class="selected-item"><a href="studenthome.py">Go Back</a></li>
                            <li class="selected-item">Reg No:''',rno,'''</li>
                            <li class="selected-item">Batch:''',batch,'''</li>
                            <li class="selected-item">Year:''',year,'''</li>
                            <li class="selected-item">Sem:''',sem,'''</li>
                            <li class="selected-item">Section:''',section,'''</li>							
                        </ul>
					</li>	
				</ul>
			</aside>
			<section id="content" class="column-right">		
	    <article>
		''',atable,'''
		</article>
		</section>
	</section>
	</div>
</body>
</html>
     ''')

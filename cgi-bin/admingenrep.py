import cgi,cgitb,sqlite3,variable
cgitb.enable()
print('Content-Type: text/html')
print()

#Getting table names.
conn=sqlite3.connect('attendance.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables=cursor.fetchall()
tables=[t[0] for t in tables]

batches=list(set([x[0:9] for x in tables]))

print('''
<!doctype html>
<html>
<head>
<title>admingenrep</title>
''',variable.loginornot,'''<link rel="stylesheet" href="/adminstyles.css" >
</head>

<body>
	<div class="width">
		''',variable.logout,'''
		<header>
			    <h2>Welcome to Attandance Management System</h2>
				<div class="tagline">
					<p>You can generate reports here.</p>
				</div>
			
		</header>
		<section id="body" class="clear">
		''',variable.adminlinks,'''	
		<section id="content" class="column-right">		
	    <article>
        <form method="post" action="genrepbyadmin.py">
		''',variable.form,'''
		</form>		
		</article>
		<article class="expanded">
		</article>
		</section>
	</section>
	</div>
</body>
</html>
     ''')
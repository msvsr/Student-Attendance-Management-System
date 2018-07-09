import cgi,cgitb,sqlite3
cgitb.enable()

print('Content-Type: text/html')
print()

#Connecting to data base.
conn=sqlite3.connect('attendance.db')

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
					<p>Get your attandance here.</p>
				</div>	
		</header>
		
		<section id="body" class="clear">
			<aside id="sidebar" class="column-left">
			</aside>
			<section id="content" class="column-right">		
	    <article>
		<h4>Fill this form to know your attendance:</h4>
		  <p>*Don't use / and spaces in any case.</p>
		  <p>Example: <br>Registerno:_ _ _ _ _ _ _ _ _ _ _<br>Batch:2015-2019 <br>Year:3-4cse <br>sem:2<br>Section:A<br></p>
          <form method="post" action="studentgetatt.py">
		  <input type="number" name="rno" placeholder="Reg no" required><br>
		  <input type="text" name="batch" placeholder="Batch" required><br>
		  <input type="text" name="year" placeholder="Year" required><br>
		  <input type="number" name="sem" placeholder="Sem" min='1' max='2' required><br>
		  <input type="text" name="section" placeholder="Section" required><br>  
          <input type="submit" value="Get Attendance">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<input type="reset" value="Reset">		
		  </table>		 
          </form>
		</article>
		</section>
	</section>
	</div>
</body>
</html>
     ''')


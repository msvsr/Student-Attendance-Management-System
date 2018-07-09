import cgi,cgitb,variable
cgitb.enable()

print('Content-Type: text/html')
print()

#Printing 2forms for getting data of faculty to add and sending it to addingfacindividual.py
# and addingfacseries.py 
print('''
<!doctype html>
<html>
<head>
<title>adminaddfac</title>''',variable.loginornot,'''
<link rel="stylesheet" href="/adminstyles.css" >
<script>
function shows_form_part(n){
    p = document.getElementById("form_part1");
	q = document.getElementById("form_part2");
	
	if(n===0){p.style.display = "none";q.style.display = "none";}
	else if(n===1){p.style.display = "";q.style.display = "none";}
	else{p.style.display = "none";q.style.display = "";}
}
function addrows(){
var row='<input type="number" placeholder="Enter FacultyId" name="names" required><br>';
var rows=document.getElementById("rows").value;
for(var i=0;i<rows;i++)
document.getElementById("input_rows").innerHTML+=row;
}
</script>
</head>

<body onload="shows_form_part(0)">
	<div class="width">
    ''',variable.logout,'''
		<header>
			
				<h2>Welcome to Attandance Management System</h2>
				<div class="tagline">
					<p>Add Faculty here.</p>
				</div>
			
		</header>
		<section id="body" class="clear">
''',variable.adminlinks,'''
		<section id="content" class="column-right">		
	    <article>
        	
			<input type="button" onclick="shows_form_part(1)" value="Add Individual Members">
            <input type="button" onclick="shows_form_part(2)" value="Add Series of Members"><br><br><br><br><br><br>
        
        <div id="form_part1">
		  <input id="rows" type="number" name="noofrows" placeholder="Enter no of entries">
          <input type="button" onclick="addrows()" value="Go">
          <form method="post" action="addingfacindividual.py">
          <div id="input_rows">
          </div>
          <input type="submit" value="submit">
          </form> 
        </div>
	
	
        <div id="form_part2">
          <form method="post" action="addingfacseries.py">
          <input type="number" name="starting" placeholder="starting number" required>
	      <input type="number" name="ending" placeholder="Ending number" required>
          <input type="submit" value="submit">
          </form> 
        </div>
		</article>
		<article>
		</article>
		</section>
	</section>
	</div>
</body>
</html>
     ''')
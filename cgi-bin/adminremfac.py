import cgi,cgitb,variable
cgitb.enable()

print('Content-Type: text/html')
print()


print('''
<!doctype html>
<html>
<head>
<title>adminremfac</title>
''',variable.loginornot,'''<link rel="stylesheet" href="/adminstyles.css" >
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

<body>
	<div class="width">
		''',variable.logout,'''
		<header>
			
				<h2>Welcome to Attandance Management System</h2>
				<div class="tagline">
					<p>You can remove faculty here</p>
				</div>
			
		</header>
		<section id="body" class="clear">
		''',variable.adminlinks,'''
		<section id="content" class="column-right">		
	    <article><br><br><br><br><br>
          <div id="form_part1">
		  <input id="rows" type="number" name="noofrows" placeholder="Enter no of entries">
          <input type="button" onclick="addrows()" value="Go">
          <form method="post" action="removingfac.py">
          <div id="input_rows">
          </div>
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
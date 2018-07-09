import cgi,cgitb,variable
cgitb.enable()
print('Content-Type: text/html')
print()
print('''
<!doctype html>
<html>
<head>
<title>adminviewstu</title>
''',variable.loginornot,'''<link rel="stylesheet" href="/adminstyles.css" >
<script>
function addsubs(){
var n=document.getElementById("subs").value;
var newsub='<input type="text" name="subjects" placeholder=" subject" required><br><br>';
var subs='';
for(var i=0;i<n;i++){
subs+=newsub;
}
document.getElementById("subjects").innerHTML=subs;
}
function addfacs(){
var n=document.getElementById("subs").value;
var newfac='<input type="number" name="facid" placeholder="Fac ID" required><br><br>';
var fac='';
for(var i=0;i<n;i++){
fac+=newfac;
}
return String(fac);  
}
function addsections(){
var n=document.getElementById("secs").value;
var newsec='<input type="text" name="sections" placeholder="section" required><br><input type="number" name="sno" placeholder="Starting no" required><br><input type="number" name="eno" placeholder="Ending no" required><br><br>';
var sec='';
for(var i=0;i<n;i++){
sec+=newsec+addfacs();
}
document.getElementById("sections").innerHTML=sec;
}
</script>

</head>

<body>
	<div class="width">
		''',variable.logout,'''
		<header>
			
				<h2>Welcome to Attandance Management System</h2>
				<div class="tagline">
					<p>Get student/s details here.</p>
				</div>
			
		</header>
		<section id="body" class="clear">
		''',variable.adminlinks,'''	
		<section id="content" class="column-right">		
	    <article>
		<h4>Fill this form to add a class:</h4>
		  <p>*Don't use / and spaces in any case.</p>
		  <p>Example: <br>Batch: 2015-2019 <br>Year: 3-4cse <br>Enter no. of subjects:6 (and then enter the subjects)<br>Enter no. of sections: 4(and then enter sectionname,startingno,endingno)<br></p>
          <form method="post" action="createbatch.py">
		  <input type="text" name="batch" placeholder="Batch" required>&nbsp&nbsp&nbsp
		  <input type="text" name="year" placeholder="Year" required><br>
		  <input type="number" name="sem" placeholder="Sem" min='1' max='2' required><br>
			  <input type="number" name="nsubs" id="subs" placeholder="No. of subjects" required>&nbsp&nbsp&nbsp
		      <input type="button" onclick="addsubs()" value="Go">
		  <div id="subjects"></div><br>	  
			  <input type="number" name="nsecs" id="secs" placeholder="No. of sections" required>&nbsp&nbsp&nbsp
			  <input type="button" onclick="addsections()" value="Go">
		  <div id="sections"></div><br>
          <input type="submit" value="create">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<input type="reset" value="Reset">		
		  </table>		 
          </form>
		</article>
		</section>
	</section>
	</div>
</body>
</html>
     ''')
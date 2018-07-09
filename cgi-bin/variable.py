all=['adminlinks']
adminlinks='''
			<aside id="sidebar" class="column-left">
				<ul>
                	<li>
                        <ul class="blocklist">
                            <li class="selected-item"><a href="adminhome.py">Home</a></li>
                            <li class="selected-item"><a href="adminaddfac.py">Add Faculty</a></li>
                            <li class="selected-item"><a href="adminremfac.py">Remove Faculty</a></li>
                            <li class="selected-item"><a href="admincreatebatch.py">Create Batches</a></li>
							<li class="selected-item"><a href="admingenrep.py">Generate Reports</a></li>
                            <li class="selected-item"><a href="adminupdateprofile.py">View/Update Profile</a></li>							
                        </ul>
					</li>	
				</ul>
			</aside>
			'''
stafflinks='''
<aside id="sidebar" class="column-left">
				<ul>
                	<li>
                        <ul class="blocklist">
                            <li class="selected-item"><a href="staffhome.py">Home</a></li>
                            <li class="selected-item"><a href="staffclasses.py">Your classes</a></li>
                            <li class="selected-item"><a href="stafftakeattendance.py">Take Attendance</a></li>
							<li class="selected-item"><a href="staffgenrep.py">Generate Reports</a></li>
                            <li class="selected-item"><a href="staffupdateprofile.py">View/Update Profile</a></li>							
                        </ul>
					</li>	
				</ul>
			</aside>
'''

logout='''<div id="sitename">
				<nav>
					<ul>
          	 			<li class="end"><a href="logout.py">Logout</a></li>
        			</ul>
				</nav>
				<div class="clear"></div>
		</div>'''

form='''<table>
        <tr>
		<td>Branch:</td>
		<td><input type='checkbox' name='branch' value='cse'>CSE</td>
		<td><input type='checkbox' name='branch' value='civil'>CIVIL</td>
		<td><input type='checkbox' name='branch' value='ece'>ECE</td>
		<td><input type='checkbox' name='branch' value='mech'>MECH</td>
		<td><input type='checkbox' name='branch' value='it'>IT</td>
		<td><input type='checkbox' name='branch' value='eee'>EEE</td>
		</tr>
		<tr>
		<td>Year:</td>
		<td><input type='checkbox' name='year' value='1_4'>1/4</td>
		<td><input type='checkbox' name='year' value='2_4'>2/4</td>
		<td><input type='checkbox' name='year' value='3_4'>3/4</td>
		<td><input type='checkbox' name='year' value='4_4'>4/4</td>
		</tr>
		<tr>
		<td>sem:</td>
		<td><input type='radio' name='sem' value=1 checked>1</td>
		<td><input type='radio' name='sem' value=2>2</td>
		</tr>
		</table>
		<input type='submit' value="submit">
		<input type='reset' value="reset">
		'''

loginornot='''<script>var s=document.cookie;var st=s.substr(9);
if(st.length==0){window.alert("please login...!");window.location.href='/';}</script>
<meta name="viewport" content="width=device-width, minimum-scale=1.0, maximum-scale=1.0" />
'''

cookiedata1='''<!DOCTYPE html>
    <html>
    <head>
    <title></title>
    </head>
    <body>
	<form id="autosubmit" method="post" action="'''

cookiedata2='''">
	<input type="hidden" id="cookiedata" name="cookiedata" value="">
	</form>
	<script>var s=document.cookie;document.getElementById("cookiedata").value = s.substr(9);
	var st=s.substr(9);
    if(st.length==0){window.alert("please login...!");window.location.href='/';}
	else{document.forms["autosubmit"].submit();}
	</script>
    </body>
    </html>'''
changepassword='''<script>function changepassword(){window.location.href='/changepassword.html'}</script>'''
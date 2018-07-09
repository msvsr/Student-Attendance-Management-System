import cgi,cgitb,sqlite3,datetime
cgitb.enable()

print('Content-Type: text/html')
print()

#Getting present time.
now = datetime.datetime.now()
yesterday=now - datetime.timedelta(days=1)
#Connecting to data base.
conn=sqlite3.connect('attendance.db')

#Getting form data.
form=cgi.FieldStorage()
id=str(form["id"].value).strip()
classname,subject=(str(form["classname"].value).strip()).split()

#Query for getting data from attendance tables.
query="select rno from '{0}'".format(classname)
cur = conn.cursor()
cur.execute(query)
data = cur.fetchall()
data.pop()
attendance=[]
if data:
    for rno in data:
        attendance.append("<input type='checkbox' name='att' value="+str(rno[0])+">"+str(rno[0])[-3:]+'''&nbsp&nbsp''')
attstring="<tr>"
mainattstring=""
for i in range(len(attendance)):
    attstring+="<td>"+attendance[i]+"</td>"
    if (i+1)%8==0:
        mainattstring+=attstring+"</tr>"
        attstring="<tr>"
if len(attendance)%8!=0:
    mainattstring += attstring + "</tr>"
print('''<html>
      <head><title>attendance</title>
<style>

body
{
    background: linear-gradient(#1e90ff,#F8f8ff );
    font-family:TradeGothic, sans-serif;
    margin-left:-450px;
    margin-top:-240px;
    position:absolute;
    height:9px;
    width:900px;
    left:50%;
    top:50%;
	right:10%;
	bottom:10%;
    font-size:120%;

}


input[type=submit],input[type=reset],input[type=button] {
    background-color: #33E6FF  ;
    border: none;
    color: #FF4233;
    padding: 5px 48px;
    text-decoration: none;
    margin: 4px 2px;
    cursor: pointer;
}
input[type=button] {
    background-color: #FF00FF  ;
    border: none;
    color: white;
    padding: 5px 48px;
    text-decoration: none;
    margin: 4px 2px;
    cursor: pointer;
}

input[type=submit]:hover,input[type=reset]:hover,input[type=button]:hover {
    background-color: #336BFF;
    border: none;
    color: white;
    padding: 10px 48px;
    text-decoration: none;
    margin: 4px 2px;
    cursor: pointer;
}

input[type=button]:hover {
    background-color: blue;   
}
input[type=radio]:hover {
    width:25px;
    height:25px;	
}
</style>
<script>function goback(){window.location.href='stafftakeattendance.py';}</script>
</head>
	  <body><h2 align="center">Attendance sheet</h2><br><p align="center"><B>Class:</B>
	  ''',classname,'''&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<b>Subject:</b>''',subject,'''</p>
	  <form method="post" action="attendance.py" align="center">
	  <div align="center">
	  <table>
	  <tr>
	  <td>
	  <b>Date and time:</b>
	  <select name="date">
      <option value="''',now.strftime("%d-%m-%Y"),'''">''',now.strftime("%d-%m-%Y"),'''</option>
      <option value="''',yesterday.strftime("%d-%m-%Y"),'''">''',yesterday.strftime("%d-%m-%Y"),'''</option>
      </select></td>

	  <td><b>No of Hours</b>:<input type="number" name="noofhours" min="1" max="4" required></td>
	  <td>
	  <b>Hours</b>
	  <select name="hours">
      <option value="0">0</option>
      <option value="1">1</option>
      <option value="2">2</option>
      <option  value="3">3</option>
      <option  value="4">4</option>
      <option  value="5">5</option>
      <option  value="6">6</option>
      <option  value="7">7</option>
      <option  value="8">8</option>
      <option  value="12">1,2</option>
      <option  value="34">3,4</option>
      <option  value="56">5,6</option>
      <option  value="78">7,8</option>
      <option  value="1234">1,2,3,4</option>
      <option  value="5678">5,6,7,8</option>
      </select>
      </td></tr>
      </table>
	  </div><br><br>
	  <div align="center" >
	  <input type="radio" value="present" name="porab" checked>Present&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
	  <input type="radio" value="absent" name="porab">Absent
	  </div><br><br><table align="center" cellpadding='4px' cellspacing='4px'>
	  ''',mainattstring,'''</table><br><br>
	  <input type="hidden" name="id" value="''',id,'''">
	  <input type="hidden" name="classname" value="''',classname,'''">
	  <input type="hidden" name="subject" value="''',subject,'''">
	  <div align="center">
	  <input type="submit" value="submit">
	  <input type="button" onclick="goback()" value="cancel">
	  </div>
	  </form></body>
      </html>''')






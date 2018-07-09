import cgi,cgitb,sqlite3,datetime
cgitb.enable()

conn=sqlite3.connect('attendance.db')

print('Content-Type: text/html')
print()

form=cgi.FieldStorage()
id=str(form["id"].value).strip()
classname,subject=(str(form["classname"].value).strip()).split()
percentage=int(form["percentage"].value)
#Query for getting data from specified table.
query="select rno,{0} from '{1}'".format(subject,classname)
cur=conn.cursor()
cur.execute(query)
data=cur.fetchall()
thours=data.pop()

table="<table border='3px' cellpadding='2px' cellspacing='2px' align='center'><tr><th>R.No</th><th>"+subject+"</th></tr>"
if thours[1]!=0:
    for i in data:
        if ((i[1]/thours[1])*100)<=percentage:
            table+="<tr><td>"+str(i[0])+"</td><td>"+str((i[1]/thours[1])*100)+"</td></tr>"
table+="</table>"

print('''<html>
      <head><title>attendance</title>
<style>html
{
    background: linear-gradient(#ccffff, #ccffff);
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
	  <body align='center'>''',table,'''<br><br>
	  <a href="staffgenrep.py"><button>GO BACK</button></a>
	  </body>
      </html>''')
import cgi,cgitb,sqlite3
cgitb.enable()

print('Content-Type: text/html')
print()

#Getting form data.
form=cgi.FieldStorage()
branch=form.getlist("branch")
year=form.getlist("year")
sem=form["sem"].value
#option=form["opt"].value

#Getting all combinations
combinations=[y+b+sem for y in year for b in branch]

#Getting table names.
conn=sqlite3.connect('attendance.db')
cur1 = conn.cursor()
cur1.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables=cur1.fetchall()
tables=[t[0] for t in tables]

cur2=conn.cursor()
cur3=conn.cursor()

batches=list(set([x[0:9] for x in tables]))
ybs=[x[9:-1] for x in tables]


#Queries
tabledata="select * from '{0}'"
tableattributes="PRAGMA table_info('{0}')"
subs=''

total=''
data=''

def func(data,total):
    table=""
    try:
        table +="<tr>" + ''.join(["<td>" + str(int(sum(data[j])*100 / (len(data[j]) * total[j]))) + "</td>" for j in range(1, len(data))]) + "</tr>"
    except:
        table+="</table>"
    return table

def gentable(info):
    table="<table border=1px cellspacing='5' cellpadding='5' align='center'>"+"<caption>"+info+"</caption>"
    cur3.execute(tableattributes.format(info))
    subs=[i[1] for i in cur3.fetchall()]
    table+=("<tr>"+(''.join(["<th>"+subs[j]+"</th>" for j in range(1,len(subs))]))+"</tr>")
    cur2.execute(tabledata.format(info))
    data = cur2.fetchall()
    total,data = data.pop(),list(zip(*data))
    return table+func(data,total)



tablesmain=list(gentable(t) for t in tables if t[9:-1] in ybs)
print('''
<!doctype html>
<html>
<head>
<style>
button { 
    background-color: #EB6800;
    border-radius: 5px 5px 5px 5px;
    color: #FFFFFF;
    display: inline-block;
    font-weight: bold;
    padding: 8px 15px;
    text-decoration: none;
    text-transform: uppercase;
}
body
{
   background: linear-gradient(#1effff,#1effff );
}

button:hover {
	background-color: #E54300;
}

button-reversed { 
    background-color: #549EE8;
}

button-reversed:hover {
	background-color: #2885E2;
}
</style>
<title>reportsbyadmin</title>

<meta name="viewport" content="width=device-width, minimum-scale=1.0, maximum-scale=1.0" />
</head>
<body><a href="admingenrep.py"><button>GO BACK</button></a><br>''',"<br>".join(tablesmain),'''
</body>
</html>
     ''')
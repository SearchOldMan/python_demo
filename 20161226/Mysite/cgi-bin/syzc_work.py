#coding=utf-8

#!/usr/bin/env python

import cgi

#获取操作数据的对象
form = cgi.FieldStorage()
f = open('work.xls','w')
startTime = form.getvalue('startTime',open('work.xls').read())
programName = form.getvalue('programName')
working = form.getvalue('working')
endTime = form.getvalue('endTime')
worker = form.getvalue('worker')
f.write(startTime)
f.close()

print '''Content-Type=text/html\n
<html>
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>
	<h1>上海商羊资产项目跟进登记表</h1>
	<form action="syzc_work.py" method="post">
		<p>开始时间：
			<input type="text" name="startTime" id="">
		</p>
		<p>项目名称：
			<input type="text" name="programName" id="">
		</p>
		<p>进行到哪里：
		    <textarea name="working" id="" cols="30" rows="10"></textarea><br>
		</p>
		<p>打算完成的时间：
			<input type="text" name="endTime">
		</p>
		<p>成员：
			<input type="text" name="worker">
		</p>
		<input type="submit" value="提交">
	</form>
</body>
</html>
'''



#!/usr/bin/python
# -*- coding: UTF-8 -*-

print( "Content-type:text/html")
print()                               # 空行，告诉服务器结束头部
print('''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>hello,world</title>
</head>
<body>
<h1>Hello world</h1>
<p>hello world</p>
<img src="http://www.runoob.com/images/logo.png/" width="258" height="39" />
</body>
</html>
''')

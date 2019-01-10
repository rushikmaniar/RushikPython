'''
    write html file in python
'''
import webbrowser
f = open("hello.html","w")
code = """
<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
	<table border="5" align="center">
		<tr>
			<th>Name</th>
			<th>Class</th>
		</tr>

		<tr>
			<td>
				Rushik
			</td>
			<td>BCA</td>
		</tr>

		<tr>
			<td>
				Nakul
			</td>
			<td>BCA</td>
		</tr>
	</table>
</body>
</html>
"""
f.write(code)
f.close()

webbrowser.open_new_tab("hello.html")
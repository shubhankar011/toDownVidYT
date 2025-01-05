import cgi
import cgitb

cgitb.enable()
print("Content-type: text/html\n")  # Required HTTP header
form = cgi.FieldStorage()  # Parse form data

# Retrieve data
name = form.getvalue('name')
dir = form.getvalue('folderName')
url = form.getvalue('URL')
# Generate HTML response
print(f"<html><body>")
print(f"<h1>Hello, {name}!</h1>")
print(f"<p>You are {name} years old.</p>")
print(f"</body></html>")

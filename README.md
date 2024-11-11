# EX01 Developing a Simple Webserver
## Date:27/10/2024

## AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
'''from http.server import HTTPServer,BaseHTTPRequestHandler

content='''

<html>
    <boby>
    <form>
        <label>Work Application Form</label><br><br>
        <label>Designation*</label>
        <select>
            <option>Manager</option><option>Developer</option><option>Tester</option>
        </select><br><br>

        <label>Applicant Name*</label>
        <input type="Applicant Name"><br><br>

        <label>Date of Birth*</label>
        <input type="date"><br><br><br>

        <label>Education Details</label><br><br>
        <input type="checkbox">PG<br>
        <input type="checkbox">UG<br>
        <input type="checkbox">HSC<br><br><br>
        
        <label>Resume Upload*</label>
        <input type="file">
        <br>
            About yourself:
            <textarea rows="4 cols=50"></textarea>
        </form>
    </boby>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()'''
## OUTPUT:
![Screenshot 2024-10-27 132332](https://github.com/user-attachments/assets/3eee7c9b-9d0a-4480-9720-7dd24d47d1fc)
![Screenshot 2024-10-27 132356](https://github.com/user-attachments/assets/a1728308-30b4-4efc-a599-32a0ff7772eb)


## RESULT:
The program for implementing simple webserver is executed successfully.

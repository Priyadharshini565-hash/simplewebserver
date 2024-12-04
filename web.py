from http.server import HTTPServer,BaseHTTPRequestHandler

content='''

<html>
    <head>
        <center>
        <tittle>
           <b>LAPTOP CONFIGURATION</b>
            </tittle>
        </head>
        <boby>
            <table border="2" cellpadding="10">
            <tr> 
                <td>Brand</td>       
                <td>Lenovo</td>
                </tr>
                <tr>
                <td>Series</td>
                <td>ThinkPad E16 Gen1</td>
                </tr>
                <tr>
                    <td>Processor Brand</td>
                    <td>INTEL</td>
                    </tr>
                    <tr>
                        <td>Processor Type</td>
                        <td>Core 15</td>
                        </tr> 
                        <tr>
                            <td>Graphics Card Interface</td>
                            <td>Integrated</td>
                            </tr>
                            <tr>
                                <td>Operating System</td>
                                <td>Windows 11 Home</td>
                                </tr> 
        </table>
   

</html>
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
httpd.serve_forever()
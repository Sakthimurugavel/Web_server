from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<html>
<head>
</head>
<body>
<h1>Name: m.sakthivel </h1>
<h1>reference no: 22007765 </h1>
</body>
</html>
"""
  
class myserver1(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())


Server_address =('',80)
httpd= HTTPServer(Server_address,myserver1)
httpd.serve_forever()
"""
	webserver.py

"""

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

STAT_SUCCESS	= 200
STAT_FILE_NOT_FOUND = 404

FORM_TAG = "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name='message' type='text' ><input type='submit' value='Submit'> </form>"


class WebserverHandler(BaseHTTPRequestHandler):
	"""
		WebserverHandler class
		Handles all client requests.
	"""
	def do_GET(self):
		try:
			if self.path.endswith("/hello"):
				self.send_response(STAT_SUCCESS)
				self.send_header("Content-type", "text/html")
				self.end_headers()

				output = ""
				output += "<html><body>Hello!"
				output += FORM_TAG
				output += "</body></html>"

				self.wfile.write(output)
				print(output)
				return
			if self.path.endswith("/hola"):
				self.send_response(STAT_SUCCESS)
				self.send_header("Content-type", "text/html")
				self.end_headers()

				output = ""
				output += "<html><body>Hola!"
				output += FORM_TAG
				output += "<a href = '/hello'>Back to Hello</a></body></html>"
				self.wfile.write(output)
				print(output)
				return
		except IOError:
			self.send_error(STAT_FILE_NOT_FOUND, "File Not Found: {}".format(self.path))

	def do_POST(self):
		try:
			self.send_response(301)
			self.send_header('Content-type', 'text/html')
			self.end_headers()

			ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
			if ctype == 'multipart/form-data':
				fields = cgi.parse_multipart(self.rfile, pdict)
				messagecontent = fields.get('message')

			output = ""
			output += "<html><body>"
			output += " <h2> Okay, how about this: </h2>"
			output += "<h1> {} </h1>".format(messagecontent[0])
			output += FORM_TAG
			output += "</body></html>"
			self.wfile.write(output)
			print output
		except:
			pass


def main():
	try:
		port = 8080
		server = HTTPServer(('',port), WebserverHandler)
		print("Web server running on port {}".format(port))
		server.serve_forever()

	except KeyboardInterrupt:		# built in axception in python that is called whenever the user presses Ctrl-C (to close the program)
		print("Ctrl-C was pressed - stopping web server...")
		server.socket.close()


if __name__=='__main__':
	main()

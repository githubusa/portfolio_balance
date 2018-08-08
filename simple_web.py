from http.server import BaseHTTPRequestHandler, HTTPServer
import basic_stats
import csv_reader
 
# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

  def get_stats(self):
    data = csv_reader.csv_array("")
    # daily price array
    dp = data.get_dp()
    dp_s = basic_stats.dp_stats(dp)
    return dp_s
 
# GET
  def do_GET(self):
    # Send response status code
    self.send_response(200)

    # Send headers
    self.send_header('Content-type','text/html')
    self.end_headers()

    # Send message back to client
    message = "STOCK INFO" + "\n"

    dp_s = self.get_stats()
    mean = "mean: " + str(dp_s.get_mean())

    # Write content as utf-8 data
    self.wfile.write(bytes(message, "utf8"))
    self.wfile.write(bytes(mean, "utf8"))
    return

def run():
  print('starting server...')
 
  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('127.0.0.1', 8081)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()
 
 
run()
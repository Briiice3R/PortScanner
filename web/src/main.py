from PortScanner.scan import PortScanner
from PortScanner.strategies import TCPScannerStrategy
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/helo")
def hello():
    return render_template("hello.html")

@app.route("/b")
def b():
    return render_template("hello.html")

# port_scanner = PortScanner("127.0.0.1", TCPScannerStrategy())
# port_scanner.running_scan()
# print(port_scanner.result)
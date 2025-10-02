# from PortScanner import PortScanner
# from PortScanner.strategies import TCPScannerStrategy
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")


# port_scanner = PortScanner("127.0.0.1", TCPScannerStrategy())
# port_scanner.running_scan()
# print(port_scanner.result)

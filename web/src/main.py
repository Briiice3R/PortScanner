# from PortScanner import PortScanner
# from PortScanner.strategies import TCPScannerStrategy
from flask import Flask, render_template, request
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from PortScanner.scan import PortScanner
from PortScanner.strategies import TCPScannerStrategy, UDPScannerStrategy
app = Flask(__name__)

@app.route("/", methods=["GET"])
def launch_scan():
    protocol = request.args.get("protocol") or "TCP"
    host = request.args.get("host") or None
    if protocol is None or host is None:
        return render_template("index.html")
    else:
        print("Ici")
        scanner = PortScanner(host, TCPScannerStrategy() if protocol=="TCP" else UDPScannerStrategy())
        scanner.running_scan()
        return render_template("index.html", res=scanner.result)



# port_scanner = PortScanner("127.0.0.1", TCPScannerStrategy())
# port_scanner.running_scan()
# print(port_scanner.result)

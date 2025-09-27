import socket
import threading
from PortScanner.strategies import ScannerStrategy, TCPScannerStrategy, UDPScannerStrategy

class PortScanner:
    def __init__(self, host, strategy):
        self.strategy: ScannerStrategy = strategy
        self.host = host
        self.result = list()
    
    def store_ports(self, port):
        if self.strategy.scan(self.host, port) == True:
            self.result.append(port)

    def running_scan(self):
        threads = []
        for i in range(0, 65535+1):
            thread = threading.Thread(target=self.store_ports, args=(i,))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()

if __name__ == "__main__":
    port_scanner = PortScanner("127.0.0.1", TCPScannerStrategy())
    port_scanner.running_scan()
    print(port_scanner.result)
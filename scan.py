import socket
import threading
import concurrent.futures
from PortScanner.strategies import ScannerStrategy, TCPScannerStrategy, UDPScannerStrategy

class PortScanner:
    def __init__(self, host, strategy):
        self.strategy: ScannerStrategy = strategy
        self.host = host
        self.result = list()
        self.lock = threading.Lock()
    
    def store_ports(self, port):
        if self.strategy.scan(self.host, port) == True:
            with self.lock:
                print(port)
                self.result.append(port)

    def running_scan(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=600) as pool:
            futures = [pool.submit(self.store_ports, i) for i in range(0, 65535+1)]
            for future in concurrent.futures.as_completed(futures):
                pass


if __name__ == "__main__":
    port_scanner = PortScanner("127.0.0.1", TCPScannerStrategy())
    port_scanner.running_scan()
    print(port_scanner.result)
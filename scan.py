import socket
import threading

class PortScanner:
    def __init__(self, host):
        self.host = host

    def scan(self, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex((self.host, port)) == 0:
                print("Port ouvert : "+str(port))

    def get_standard_ports_range(self):
        return range(0, 1023)
    
    def get_most_used_ports_range(self):
        return range(1024, 49151)
    
    def get_dynamic_private_ports_range(self):
        return range(49152, 65535)
    
    def running_scan(self, range_ports):
        threads = []
        for i in range_ports:
            thread = threading.Thread(target=self.scan, args=(i,))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()

if __name__ == "__main__":
    port_scanner = PortScanner("127.0.0.1")
    port_scanner.running_scan(port_scanner.get_dynamic_private_ports_range())
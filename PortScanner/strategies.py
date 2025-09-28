import socket

class ScannerStrategy:
        def scan(self, host, port):
            try:
                return self._scan(host, port)
            except socket.gaierror:
                print("Adresse incorrecte.")
                return False
            except TimeoutError:
                print("Le scan a pris trop de temps.")
                return False
            except Exception as e:
                print("Problème : " + e)
        
        def scan(self, host, port):
            raise NotImplementedError()
        
class TCPScannerStrategy(ScannerStrategy):
      def scan(self, host, port) ->bool:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.2)
                return s.connect_ex((host, port)) == 0

class UDPScannerStrategy(ScannerStrategy):
      def scan(self, host, port) ->bool:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                return s.connect_ex((host, port)) == 0
            
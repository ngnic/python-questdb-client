import socket
from enum import Enum


class ConnectionType(Enum):
    TCP = socket.SOCK_STREAM
    UDP = socket.SOCK_DGRAM


class Client:
    def __init__(self, host, port, connection_type=ConnectionType.TCP):
        self.host = host
        self.port = port
        self._buffer = []
        self.sock = socket.socket(socket.AF_INET, connection_type.value)

    def current_buffer(self):
        return self._buffer

    def buffer_row(self, row):
        return self.buffer_rows([row])

    def buffer_rows(self, rows):
        self._buffer.extend(rows)
        return self

    def flush(self):
        # No op if no points buffered
        if len(self._buffer) == 0:
            return
        try:
            self.sock.connect((self.host, self.port))
        except socket.error as e:
            print("Got error: %s" % (e))
            return

        try:
            while True:
                point = self._buffer.pop(0)
                self.sock.sendall((str(point) + "\n").encode())
        except IndexError:
            pass
        self.sock.close()

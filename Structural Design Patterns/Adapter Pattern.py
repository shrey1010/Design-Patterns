class RoundSocket:
    def connect(self):
        print("Connected to Round Socket. Charging...")


class FlatSocket:
    def plug_in(self):
        print("Connected to Flat Socket.")


class SocketAdapter(RoundSocket):
    def __init__(self, flat_socket):
        self.flat_socket = flat_socket

    def connect(self):
        # Adapting flat_socket's plug_in() method to match connect()
        print("Using adapter...")
        self.flat_socket.plug_in()
        print("Adapter converted it to round socket. Charging...")


old_socket = FlatSocket()
adapter = SocketAdapter(old_socket)
adapter.connect()

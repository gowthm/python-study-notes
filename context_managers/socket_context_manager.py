# without context manager

socket = create_socket()

try:
    socket.send(data)
finally:
    socket.close()


# with context manager

with SocketConnection() as socket:
    socket.send(data)
    # Automatically closes the socket.

    
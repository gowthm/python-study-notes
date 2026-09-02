"""
Illustrative pseudocode (not runnable as-is: create_socket(), SocketConnection,
and data are undefined) contrasting manual try/finally cleanup with a context
manager that does the same cleanup automatically via __exit__.
"""

# --- Without a context manager: cleanup must be written by hand ---
socket = create_socket()

try:
    socket.send(data)
finally:
    socket.close()


# --- With a context manager: __exit__ closes the socket automatically ---
with SocketConnection() as socket:
    socket.send(data)
    # Automatically closes the socket, even if send() raises.

from pyModbusTCP.server import ModbusServer

# Define the Modbus TCP server address and port
SERVER_HOST = "127.0.0.1"  # Listen on all network interfaces
SERVER_PORT = 502  # Choose a port for the Modbus TCP server

# Create and start the Modbus TCP server
server = ModbusServer(host=SERVER_HOST, port=SERVER_PORT, no_block=True)
server.start()

# Check if the server is running
if server.is_run:
    print(f"Modbus TCP server is running on {SERVER_HOST}:{SERVER_PORT}")
else:
    print("Failed to start Modbus TCP server")
##if the Modbus client is run by itself, which isn't the case with this project.

from pyModbusTCP.client import ModbusClient
from .models import Fan

# Define the Modbus server address and port
server_address = "127.0.0.1"
server_port = 502

# Create a Modbus TCP client instance
client = ModbusClient(host=server_address, port=server_port)

# Connect to the Modbus server
client.open()

try:
    # Retrieve data from your Django database
    queryset = Fan.objects.all()  # Fetch all objects from your model

    # Map the data to the registers
    register_values = [obj.id for obj in queryset]  # Example mapping, adjust as needed

    # Define the starting address for writing
    start_address = 0

    # Write the mapped data to the registers
    result = client.write_multiple_registers(start_address, register_values)

    if result:
        print("Registers updated successfully")
    else:
        print("Failed to update registers")

finally:
    # Close the connection to the Modbus server
    client.close()

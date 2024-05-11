from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
from random import uniform

num_registers = 15000

DataBank.set_words(0, [0] * num_registers)

server = ModbusServer('127.0.0.1',502,no_block=True)

try:
    # Start the server
    server.start()

    # Print server information
    print("Modbus server started...")

    # Keep the server running until interrupted
    while True:
        pass

except KeyboardInterrupt:
    # Stop the server on KeyboardInterrupt
    server.stop()
    print("Modbus server stopped.")
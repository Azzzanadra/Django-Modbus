from django.http import Http404, JsonResponse
from pyModbusTCP.client import ModbusClient
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Album, Fan
from django.db.models import F
import random, time, threading
from pyModbusTCP.server import ModbusServer
import threading
# Create your views here.

#Modbus server address
server_address = "127.0.0.1"
server_port = 502
client = ModbusClient(host=server_address, port=server_port)

#ignore
def index(request):
    all_albums = Album.objects.all()
    return render(request,'index.html',{'all_albums':all_albums})

#ignore
def detail(request, album_id):
    try:
        album = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        raise Http404("Album doesn't exist")
    return render(request,'detail.html',{'album_id':album_id})

#Fan object views
def fans(request):
    all_fans = Fan.objects.all()
    #dictates which button executes which function
    if request.method == 'POST':
        if 'reset' in request.POST:
           reset()
        if 'increase' in request.POST:
            threading.Thread(target=increase_speed).start()
        if 'restart' in request.POST:
            restart()
        if 'modbusWrite' in request.POST:
            write_thread = threading.Thread(target=write_client)
            write_thread.start()
        if 'modbusRead' in request.POST:
            read_client()
    return render(request, 'fans.html', {'all_fans':all_fans})

#write the modbus client
def write_client():
    client.open()
    try:
        queryset = Fan.objects.all()  # Fetch all objects from your model
        start_address = 0

        chunk_size = 100  # Adjust as needed
        while True:
            for i in range(0, len(queryset), chunk_size):
                # Extract a chunk of objects
                chunk = queryset[i:i + chunk_size]
                register_values = [obj.id for obj in chunk] 
                result = client.write_multiple_registers(start_address, register_values)
                if result:
                    print("Registers updated successfully")
                else:
                    print("Failed to update registers")
                for obj in chunk:
                    # Read the register corresponding to the object's ID
                    register_id = obj.id
                    register_value = client.read_holding_registers(register_id, 1)
                    if register_value:
                        # Update the actual_speed property based on the register value
                        obj.actual_speed = 500  # Assuming actual_speed is a field of the Fan model
                Fan.objects.bulk_update(chunk, ['actual_speed'])
                print("Bulk update completed")
                    #     print(f"Updated actual_speed for Fan {obj.id} to {obj.actual_speed}")
                    # else:
                    #     print(f"Failed to read register for Fan {obj.id}")

    finally:
        client.close()

#read the modbus client
def read_client():
    client.open()

    try:
        start_address = 0
        num_registers = 30
        registers = client.read_holding_registers(start_address, num_registers)

        if registers:
            # Print the values of the registers
            print("Values of registers:", registers)
        else:
            print("Failed to read registers")  
    finally:
        # Close the connection to the Modbus server
        client.close()          

#reset Fan object properties of actual speed and status to 0
def reset():
    Fan.objects.all().update(actual_speed=0)
    Fan.objects.all().update(status=0)

#old code for pressing a button that makes any Fan with status = 3 becomes 0
def restart():
    for fan in Fan.objects.all():
        if fan.status == 3:
            fan.status = 0
        fan.save()

#code that starts the infinite loop simulation of actual speed
def increase_speed():
        while True:
            fans_to_update = []
            for fan in Fan.objects.all():
                if fan.actual_speed < min(fan.set_speed,fan.max_speed) - 50:
                    new_speed = fan.actual_speed + 50
                elif fan.actual_speed > min(fan.set_speed,fan.max_speed):
                    new_speed = fan.actual_speed - 20
                else:
                    new_speed = fan.actual_speed + 10
                if fan.status != 7:
                    fan.status = random.randint(0,7)

                fans_to_update.append((fan.id, new_speed, fan.status))        
            Fan.objects.bulk_update(
                [Fan(id=fan_id, actual_speed=new_speed, status=new_status) for fan_id, new_speed, new_status in fans_to_update],
                fields=['actual_speed', 'status']  
            )
            time.sleep(1)
    # if all(fan.actual_speed >= fan.set_speed for fan in Fan.objects.all()):
    #     return
    # for x in range(1,50):
    #     fan = Fan.objects.get(id=x)
    #     fan.actual_speed += 1
    #     fan.save()
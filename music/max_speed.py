import os
import sys
import random

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
import django
django.setup()

from music.models import Fan
import random

#adds maximum speed to the fan objects
def maximum():
    speeds = [500,1000,1500,2000]
    for i in range(1, 15001):
        fan = Fan.objects.get(id=i)
        fan.max_speed = random.choice(speeds)
        fan.set_speed = fan.max_speed/2
        fan.status = 0
        fan.save()
        print(f'Fan {i} set max speed to: {fan.max_speed} and the set speed is: {fan.set_speed}')

if __name__ == '__main__':
    maximum()
#ignore

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
import django
django.setup()

from music.models import Fan
import random

def update_speed():
    fan = Fan.objects.get(id=14999)
    fan.actual_speed = 50
    fan.status = 0
    fan.save()
    print(f'Real speed of Fan {fan.id} updated to {fan.actual_speed}')

if __name__ == '__main__':
    update_speed()
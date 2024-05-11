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
#creates 15000 fan objects with random status
def populate_fans():
    for i in range(1, 15001):
        status = random.randint(1, 7)
        fan = Fan.objects.create(status=status)
        print(f'Fan {i} created with status: {status}')

if __name__ == '__main__':
    populate_fans()
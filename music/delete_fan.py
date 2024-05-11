#ignore
import os
import sys

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
import django
django.setup()

from music.models import Fan

# Retrieve all Fan objects
fans = Fan.objects.all()

# Loop through each fan and update the status property
for fan in fans:
    fan.status = ''  # Set status to an empty string
    fan.save()  # Save the changes to the database

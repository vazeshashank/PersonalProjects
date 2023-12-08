import random
from faker import Faker
from django.core.management.base import BaseCommand
from caller.models import Contacts

class Command(BaseCommand):
    help = 'Populate Contacts table with random data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(10):  # Adjust the number as needed
            name = fake.name()
            phone = 8490827898
            email = fake.email()
            
            contact = Contacts.objects.create(
                name=name,
                phone=phone,
                registered_user=False,
                email=email,
                spam_count=0
            )

            print(f"Created contact: {contact}")
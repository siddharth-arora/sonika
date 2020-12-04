# import os
import os
# refer the settings.py file of the project
os.environ.setdefault('DJANGO_SETTINGS_MODULE' , 'sonika.settings')

# import django
import django
django.setup()      #  ???

# import the model
from app1.models import school
# # import faker
from faker import Faker

# declare Faker class object
faker = Faker()

# define a function to generate fake data
# for model - school
def populate(n):
    # loop
    for i in range(1,n+1,1):
        # generate fake data for model
        # generate fake school name
        fake_school_name = faker.company()
        # generate fake principal name
        fake_principal_name = faker.prefix() + " " + faker.name()
        # generate fake location
        fake_location = faker.address()
        # declare Model class object with the fake data
        schoolobj = school(name=fake_school_name, principal=fake_principal_name, location=fake_location)
        # save the data
        schoolobj.save()

#####################################
print("Fake record generation starts")
populate(100)
print("Fake record generation ends")

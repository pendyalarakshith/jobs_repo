import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sunnyjobs.settings')
import django
django.setup()

from testapp.models import HydJobs
from faker import Faker
from random import *
fake = Faker()
def phonenumbergen():
	d1 = randint(6,9)
	num = '' + str(d1)
	for i in range(9):
		num += str(randint(0,9))
	return int(num)
def populate(n):
    #['date','company','title','eligibility','address','email','phonenumber']
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('Project Manager','Team Lead','Software Engineer','Associate Engineer'))
        feligibility = fake.random_element(elements = ('B.Tech','MCA','M.Tech','Mahesh Sir Student','Phd'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()
        hyd_jobs_records = HydJobs.objects.get_or_create(
            date = fdate,
            company = fcompany,
            title = ftitle,
            eligibility = feligibility,
            address = faddress,
            email = femail,
            phonenumber = fphonenumber,
        )
n = int(input('Enter number of records:'))
populate(n)
print(f'{n} Records inserted successfully..........')

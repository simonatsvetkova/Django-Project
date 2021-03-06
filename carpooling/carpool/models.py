import csv

from django.contrib.auth.models import User
from django.db import models
from multiselectfield import MultiSelectField

from accounts.models import ProfileUser

# Create your models here.

CSV_PATH = 'carpool/Sofia_districts.csv'  # Csv file path


with open(CSV_PATH, newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=',', quotechar=';')
    districts = list(rows)
    flat_list = [item for sublist in districts[1:] for item in sublist]
    print(flat_list)


class Offer(models.Model):
    DISTRICTS = [(dist, dist) for dist in flat_list]

    # get list of days' names from the default python calendar as tuple --> import calendar first
    # REGULARITY = [(str(i), str(calendar.day_name[i])) for i in range(0,7)]
    REGULARITY = (
        ('*', 'All'),
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday')
    )
    TYPE_OF_CONTACT = (
        ('E', 'email'),
        ('PH', 'phone')
    )
    NUMBER_OF_SEATS = [(i, i) for i in range(1, 7)]

    user = models.ForeignKey(ProfileUser, on_delete=models.CASCADE, default=1)
    start_location = models.CharField(max_length=50, default='choose start location', choices=DISTRICTS)
    destination = models.CharField(max_length=50, default='KBC')
    departure_time = models.TimeField(default='7:00')
    return_time = models.TimeField(default='18:00')
    route = models.TextField(max_length=400, blank=True)
    regularity = MultiSelectField(choices=REGULARITY, default='*')
    type_of_contact = models.CharField(max_length=2, choices=TYPE_OF_CONTACT, default='PH')
    number_of_seats = models.IntegerField(choices=NUMBER_OF_SEATS, default=1)
    car_picture = models.ImageField(upload_to='images/', default='images/default_car.png', null=True, blank=True)
    passengers = models.CharField(max_length=70, null=True, default='full_name')
    terms_and_conditions = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return f"Offer ID {self.id} with driver {self.user}"



class SeatRequest(models.Model):
    user = models.ForeignKey(ProfileUser, on_delete=models.CASCADE, unique=False)
    passenger = models.CharField(max_length=70, blank=False, null=False, default='full_name')
    ride_id = models.CharField(max_length=700, blank=False, default='null')
    drivers_name = models.CharField(max_length=70, default='full_name', blank=False, null=False)
    comments = models.TextField(max_length=400, blank=True)
    terms_and_conditions = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return f"Request from {self.user}"


class SeatApprovalRejection(models.Model):
    DECISION = [
        ('1', 'Approve'),
        ('0', 'Reject')
    ]

    user = models.ForeignKey(SeatRequest, on_delete=models.CASCADE)
    passenger = models.CharField(max_length=70, blank=False, null=False, default='full_name')
    approve_reject = models.CharField(max_length=10, choices=DECISION, default=1)
    comments = models.TextField(max_length=400, blank=True)

    def __str__(self):
        return f"{self.approve_reject}"

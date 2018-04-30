from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    emp = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    dob = models.DateField()
    sex = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    marital_status = models.CharField(max_length=30)
    contact = models.IntegerField()
    joining_date = models.DateField()
    position = models.CharField(max_length=100)
    emp_status = models.CharField(max_length=70)
    salary = models.CharField(max_length=30)
    bank_name = models.CharField(max_length=100)
    bank_account = models.IntegerField()
    skill_set = models.TextField()
    image = models.ImageField(upload_to='HR/static/HR')

    def __str__(self):
        return self.name


class Complaints(models.Model):
    complaint = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.TextField()
    date_time = models.DateTimeField()
    complaint_text = models.TextField()
    complainant = models.CharField(max_length=50)
    choice = (('0', 'Pending'), ('1', 'Resolved'))
    status = models.CharField(max_length=10, choices=choice)

    def __str__(self):
        return self.subject


class Feedback(models.Model):
    feed = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    respondent = models.CharField(max_length=50)
    date_time = models.DateTimeField()
    polarity = models.CharField(max_length=10)

    def __str__(self):
        return self.respondent

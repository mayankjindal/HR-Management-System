from django.contrib import admin
from .models import User, Employee, Complaints, Feedback


admin.site.register(Employee)
admin.site.register(Complaints)
admin.site.register(Feedback)
from django.contrib import admin
from .models import *
# Register your models here.
class deptadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Deparment,deptadmin)

class docadmin(admin.ModelAdmin):
    list_display = ['name','img','desig']
    list_editable = ['img','desig']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Doctor,docadmin)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'doctor', 'date')
admin.site.register(Appointments, AppointmentAdmin)
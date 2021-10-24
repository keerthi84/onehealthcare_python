from django.contrib import admin
from django.urls import path
from . import views
from .views import dc_list,dept_list,appoint

urlpatterns = [
    path('',views.home,name='h'),
    path('<slug:dp_slug>/',views.dept_details,name='dp_dc'),
    path('<slug:dp_slug>/<slug:dc_slug>',views.doc_details,name='dcdetails'),
    path('dclist',dc_list.as_view(),name='dctlist'),
    path('deplist',dept_list.as_view(),name='deptlist'),
    path('appointment', appoint.as_view(), name='appt')
    # path('appointment',AppointmentForm.as_view,name='appoint'),

    # path('<slug:dp_slug>/',views.dept,name='deptdetails')
]
from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from django.views import generic
from .forms import appoinment_form
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.

def home(request):
    doc=Doctor.objects.all()
    dept=Deparment.objects.all()
    paginator=Paginator(dept,3)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        dp=paginator.page(page)
    except(EmptyPage,InvalidPage):
        dp=paginator.page(paginator.num_pages)

    return render(request,'index.html',{'dt':doc,'dep':dept,'pg':dp})

class dc_list(generic.ListView):
    model =Doctor
    template_name = 'doctors.html'
    context_object_name = 'dt'

class dept_list(generic.ListView):
    model =Deparment
    template_name = 'departments.html'
    context_object_name = 'dep'

def dept_details(request,dp_slug=None):
    dp_page=None
    drt=None
    if dp_slug!=None:
        dp_page=get_object_or_404(Deparment,slug=dp_slug)
        drt=Doctor.objects.filter(dept=dp_page)
    else:
        # dep=Deparment.objects.all()
        drt=Doctor.objects.all()
    depart=Deparment.objects.all()
    return render(request,'dept_details.html',{'dt':drt,'dep':depart})

def doc_details(request,dp_slug,dc_slug):
    try:
        doc=Doctor.objects.get(dept__slug=dp_slug,slug=dc_slug)
    except Exception as e:
        raise e
    return render(request,'doc-details.html',{'dt':doc})

class appoint(generic.CreateView):
   model = Appointments
   form_class =  appoinment_form
   template_name='appointment.html'
   # fields = '__all__'

# def new_appointment(request):
#     if request.method == 'POST':
#         form = AppointmentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form = AppointmentForm()
#     return render(request, 'appointment.html', {'form': form})
# def dept(request,dp_slug):
#     try:
#         dept=Doctor.objects.get(slug=dp_slug)
#     except Exception as e:
#         raise e
#     return render(request,'dept_details.html',{'dep':dept})
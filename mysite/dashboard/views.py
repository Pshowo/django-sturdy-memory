from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Client, Project, Software
from django.views import View
from .form  import NameForm
from django.conf import settings

SOFT = "-"
COMP = {
    "clients": [
        {"id": 1, "CPU": SOFT, "RAM":SOFT, "RAM_USE": SOFT, "RAM_PER":SOFT, "is_active": False, "last": 0}, 
        {"id": 2, "CPU": SOFT, "RAM":SOFT, "RAM_USE": SOFT, "RAM_PER":SOFT, "is_active": False, "last": 0}, 
        {"id": 3, "CPU": SOFT, "RAM":SOFT, "RAM_USE": SOFT, "RAM_PER":SOFT, "is_active": False, "last": 0},
        {"id": 4, "CPU": SOFT, "RAM":SOFT, "RAM_USE": SOFT, "RAM_PER":SOFT, "is_active": False, "last": 0},
        {"id": 5, "CPU": SOFT, "RAM":SOFT, "RAM_USE": SOFT, "RAM_PER":SOFT, "is_active": False, "last": 0},
        {"id": 6, "CPU": SOFT, "RAM":SOFT, "RAM_USE": SOFT, "RAM_PER":SOFT, "is_active": False, "last": 0},
        {"id": 7, "CPU": SOFT, "RAM":SOFT, "RAM_USE": SOFT, "RAM_PER":SOFT, "is_active": False, "last": 0},
        {"id": 8, "CPU": SOFT, "RAM":SOFT, "RAM_USE": SOFT, "RAM_PER":SOFT, "is_active": False, "last": 0},
        ],
}

@login_required
def dashboard(request):
    return render(request, "dashboard/main.html", {'section':"dashboard"})


def clients(request):
    clients = Client.objects.all()
    print("\t ** Len clients", len(clients))
    context = {'clients': clients, "soft": SOFT}
    print(settings.MY_HOST)
    return render(request, 'dashboard/clients.html', context)

def client_detail(request, num):
    client = Client.objects.filter(id=num).first()
    context = {"client": client, 'soft': SOFT}
    return render(request, 'dashboard/client_details.html', context)

def errorslog(request):
    return render(request, 'dashboard/errorslog.html')

def structures(request):
    return render(request, 'dashboard/structure.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'dashboard/projects.html', {'projects':projects, 'active_menu': 'projects'})

class NewClient(View):

    def get(self, request, *args, **kwargs):
       form = NameForm()
       return render(request, 'versions/clients/new_client.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = NameForm(request.POST)
        if form.is_valid():
            client_name = form.cleaned_data['clinet_name']
            country = form.cleaned_data['country']
            city = form.cleaned_data['city']
            longitude = form.cleaned_data['longitude']
            latitude = form.cleaned_data['latitude']
            new_client = Client(name=client_name, country=country, city=city, longitude=longitude, latitude=latitude)
            new_client.save()
        return redirect(clients)
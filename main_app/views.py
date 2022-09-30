from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Brewery
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import SpecialbrewForm

# # Create your views here.
# class Brewery:
#     def __init__(self, name, address, description, toptap, established):
#         self.name = name
#         self.address = address
#         self.description = description
#         self.toptap = toptap
#         self.established = established

# breweries = [
#     Brewery('Gipsy Hill', 'Unit 5, 160 Hamilton Rd, Norwood, London SE27 9SF', 'Delicious London Brewery in an off-road setting - great atmosphere', 'Gipsy Hill IPA', 2004),
#     Brewery('Ignition', 'Ground Floor, The Sydenham Centre, 44A Sydenham Rd, London SE26 5QX', 'New Brewery set up by the local counsel to provide jobs for people with learning difficulties', 'Ignition Pale', 2019),
#     Brewery('Southey', '21 Southey St, London SE20 7JD', 'Small Brewery tucked away in a corner of Penge surrounded by quality street art', '666', 2016),
#     Brewery('Br3wery', '253 Beckenham Rd, Beckenham BR3 4RP', 'Delicious beers found between the towns of ever growing Penge and well-established Beckenham', 'Gipsy Hill IPA', 2016),
# ]
class BreweryCreate(CreateView):
    model = Brewery
    fields = ['name', 'address', 'description', 'toptap', 'established']

class BreweryUpdate(UpdateView):
    model = Brewery
    fields = ['address', 'description', 'toptap', 'established']

class BreweryDelete(DeleteView):
    model = Brewery
    success_url = '/breweries/'

# def home(request):
#     return HttpResponse('<h1> Hello London Drinker </h1>')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def breweries_index(request):
    breweries = Brewery.objects.all()
    return render(request, 'breweries/index.html', { 'breweries': breweries})

def breweries_detail(request, brewery_id):
    brewery = Brewery.objects.get(id = brewery_id)

    specialbrew_form = SpecialbrewForm()
    return render(request, 'breweries/detail.html', {'brewery': brewery, 'specialbrew_form': specialbrew_form})

def add_specialbrew(request, brewery_id):
    form = SpecialbrewForm(request.POST)

    if form.is_valid():
        new_specialbrew = form.save(commit=False)
        new_specialbrew.brewery_id = brewery_id
        new_specialbrew.save()
    return redirect('detail', brewery_id = brewery_id)


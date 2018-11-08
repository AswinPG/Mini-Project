from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView


def home(request):
    return render(request,'home.html')

def dnr_reg(request):
    return render(request,'dnr_reg.html')

def search(request):
    return render(request,'search.html')

def about(request):
    return render(request,'about.html')

#class DonorCreate(CreateView):
    #model = DonorCreate
    fields = ['name','age','blood_grp','location','ph_no','bld_pre','sugar_lvl','cholestrol','other']
#

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

# Create your views here.
class IndexView(generic.View):
    """ This class is responsible for displaying the homepage """
    
    def dispatch(self,request,*args,**kwargs):
        return render(request,'app/base.html')
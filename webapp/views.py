#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
def index(request):
    #now returning HttpResponse()
    #return render(request, "personal/home.html")
    temp=loader.get_template("personal/home.html")
    return HttpResponse(temp.render({},request))

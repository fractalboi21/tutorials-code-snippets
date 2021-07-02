from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Person

#/<app>/views.py
# function based viewa using HttpResponse
def geeks_view(request):
    count = Person.objects.count()
    html = f"Total number of entries: {count}"
    return HttpResponse(html)
#fuction
def name_list(request):
    return render(request,"index.html",context = {"info":"world"})
#dont forget to include the to urld.py


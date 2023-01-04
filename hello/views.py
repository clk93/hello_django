import re
from django.shortcuts import render
from django.utils.timezone import datetime
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    print("start print request")
    print(request)
    print("Finished print request")
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
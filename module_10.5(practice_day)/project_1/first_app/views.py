from django.shortcuts import render
import datetime 

# Create your views here.
def home(request):
    d = {'author' : "gulnaj is a student", 'age' : 24,
         'value' : datetime.datetime.now(),
         'num' : 22,
         'name': "I'm Gulnaj",
         'empty': '',
         'lst': [
                    {'name': 'zed', 'age': 19},
                    {'name': 'amy', 'age': 22},
                    {'name': 'joe', 'age': 31},
                ],
        }
    return render(request, 'first_app/home.html', context=d)

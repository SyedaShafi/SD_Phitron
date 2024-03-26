from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d = {'author':'Mr. M', 'age': 35, 'lst': ['Python', 'Is', 'Best'], 
         'value': '',
         'birthday': datetime.datetime.now() , 'courses':[
        {
            'id' : 1,
            'name': 'Python',
            'fee' : 1000
        },
        {
            'id' : 2,
            'name' : 'Django',
            'fee' : 5000
        },
        {
            'id' : 2,
            'name' : 'C',
            'fee' : 1500
        }
    ]}
    return render(request, 'first_app/home.html', context=d)
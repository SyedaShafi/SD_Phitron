from django.shortcuts import render
from datetime import datetime, timedelta, timezone
from django.http import HttpResponse
# Create your views here.
def home(request):
    response = render(request, 'home.html')
    response.set_cookie('name', 'rahim')
    # response.set_cookie('name', 'rahim', max_age = 10)
    response.set_cookie('name', 'rahim', expires=datetime.now(timezone.utc) + timedelta(days=7))
    return response

def get_cookie(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request, 'home.html', {'name': name})

def delete_cookie(request):
    response = render(request, 'delete_cookie.html')
    response.delete_cookie('name')
    return response


def set_session(request):
    data = {
        'name' : 'rahim',
        'age' : 23,
        'language' : 'Bangla',
    }
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_date())
    # session name er table already ase django te, session update korte hole makemigrations lagbe to active these tables
    request.session.update(data) 

    return render(request, 'home.html')


def get_session(request):
    if 'name' in request.session:
        data = request.session
        request.session.modified = True
        return render(request, 'home.html', {'data': data})
    else:
        return HttpResponse("Your session has been expired log in again!")

def delete_session(request):
    # del request.session['name']
    request.session.flush()
    return render(request, 'home.html')
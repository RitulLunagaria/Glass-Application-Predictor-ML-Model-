from operator import imod
from weakref import finalize
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import joblib
from requests import request

# Create your views here.


def home(request):
    return render(request, 'home.html')


def result(request):
    cls = joblib.load('finalized_model.sav')

    lis = []
    lis.append(request.GET['RI'])
    lis.append(request.GET['Na'])
    lis.append(request.GET['Mg'])
    lis.append(request.GET['Al'])
    lis.append(request.GET['Si'])
    lis.append(request.GET['K'])
    lis.append(request.GET['Ca'])
    lis.append(request.GET['Ba'])
    lis.append(request.GET['Fe'])

    ans = cls.predict([lis])

    return render(request, 'result.html', {'ans': ans})

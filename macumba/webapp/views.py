from django.shortcuts import render


# Create your views here.
from .forms import *


def index(request):
    return render(request, "index.html")

def uploads(request):
    if request.method == 'POST':
        pass
    else:
        victimeForm = VictimeForm()
    return render(request, "Upload.html",{'victimeForm':victimeForm})

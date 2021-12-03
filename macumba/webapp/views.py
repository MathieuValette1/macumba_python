from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")

def uploads(request):
    return render(request, "Upload.html")

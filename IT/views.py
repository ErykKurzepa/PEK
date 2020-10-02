from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'IT/index.html',)


def scraping(request):
    return render(request, 'IT/scraping.html',)


def management(request):
    return render(request, 'IT/management.html',)

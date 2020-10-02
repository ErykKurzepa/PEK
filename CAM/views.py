from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'CAM/index.html',)


def probe(request):
    return render(request, 'CAM/probe.html',)

def measure(request):
    return render(request, 'CAM/measure.html',)

def cnc(request):
    return render(request, 'CAM/cnc.html',)
from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.

def irnss_index(request):
    return render(request,"irnss/irnss-index.html")
def about(request):
    return render(request,"irnss/about.html")
def about_classifications(request):
    return render(request,"irnss/about-classifications.html")
def about_applications(request):
    return render(request,"irnss/about-applications.html")
def irnss_applications(request):
    return render(request,"irnss/irnss-applications.html")
def irnss_gagan(request):
    return render(request,"irnss/irnss-gagan.html")
def qzss(request):
    return render(request,"irnss/qzss.html")
def qzss_qzo(request):
    return render(request,"irnss/qzss-qzo.html")
def qzss_applications(request):
    return render(request,"irnss/qzss-applications.html")
def gps(request):
    return render(request,"irnss/gps.html")
def gps_applications(request):
    return render(request,"irnss/gps-applications.html")
def gps_future(request):
    return render(request,"irnss/gps-future.html")
def galileo(request):
    return render(request,"irnss/galileo.html")
def galileo_os(request):
    return render(request,"irnss/galileo-os.html")
def galileo_applications(request):
    return render(request,"irnss/galileo-applications.html")
def glonass(request):
    return render(request,"irnss/glonass.html")
def glonass_characteristics(request):
    return render(request,"irnss/glonass-characteristics.html")
def glonass_applications(request):
    return render(request,"irnss/glonass-applications.html")

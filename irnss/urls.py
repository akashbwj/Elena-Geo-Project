from django.urls import path
from irnss import views

urlpatterns=[
    path('',views.irnss_index,name='index'),
    path('about/',views.about,name='about'),
    path('about/classifications/',views.about_classifications,name='about_classifications'),
    path('about/applications/',views.about_applications,name="about-applications"),
    path('irnss/applications/',views.irnss_applications,name="irnss_applications"),
    path('irnss/gagan/',views.irnss_gagan,name="irnss_gagan"),
    path('qzss/',views.qzss,name="qzss"),
    path('qzss/qzo/',views.qzss_qzo,name="qzss_qzo"),
    path('qzss/applications/',views.qzss_applications,name="qzss_applications"),
    path('gps/',views.gps,name="gps"),
    path('gps/applications/',views.gps_applications,name="gps_applications"),
    path('gps/future/',views.gps_future,name="gps_future"),
    path('galileo/',views.galileo,name="galileo"),
    path('galileo/os/',views.galileo_os,name="galileo_operational_satellite"),
    path('galileo/applications/',views.galileo_applications,name="galileo_applications"),
    path('glonass/',views.glonass,name="glonass"),
    path('glonass/characteristics/',views.glonass_characteristics,name="glonass_characteristics"),
    path('glonass/applications/',views.glonass_applications,name="glonass_applications"),
]

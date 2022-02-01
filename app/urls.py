from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('asia/', asia, name='asia'),
    path('africa/', africa, name='africa'),
    path('europe/', europe, name='europe'),
    path('north_america/', north_america, name='north_america'),
    path('south_america/', south_america, name='south_america'),
    path('australia_ocenia/', australia_ocenia, name='australia_ocenia'),
    path('about/', about, name='about'),
    path('covid_news/', covid_news, name='covid_news'),
    path('health_news/', health_news, name='health_news'),
    path('vaccine_news/', vaccine_news, name='vaccine_news'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
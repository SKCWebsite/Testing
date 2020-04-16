from django.urls import include, path

from .views import HomePageView

from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),

    path('SKC_contactus/', csrf_exempt(contactus.contactus), name='contactus'),
    
]

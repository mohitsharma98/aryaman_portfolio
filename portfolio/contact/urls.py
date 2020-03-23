from django.urls import path
from contact.views import ContactView

app_name = 'contact'

urlpatterns = [
    path('', ContactView, name='contact'),
]
from django.urls import path

from core.views import user

app_name = 'core'

urlpatterns = [
    path('', user.index, name='index'),
]
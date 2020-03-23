from django.urls import path
from .views import ListAggressionsView

from .import views

app_name = 'alertas'
urlpatterns = [
    path('', views.index, name='index'),
    path('aggressions/', ListAggressionsView.as_view(), name="aggressions-all")
]

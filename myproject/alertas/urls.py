from django.urls import path, re_path
from .views import ListAggressionsView, AggressionsStatsView

from .import views

app_name = 'alertas'
urlpatterns = [
    path('', views.index, name='index'),
    path('aggressions/<int:id>/', views.detail),
    re_path(r'^stats', views.stats, name='stats'),       
    path('aggressions/', ListAggressionsView.as_view(), name="aggressions-all")
]

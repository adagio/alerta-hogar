from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from .models import Aggression

def index(request):
    latest_aggression_list = Aggression.objects.all()
    misoginia_aggression_list = Aggression.objects.filter(tags__name__in=["misoginia"])
    context = {
        'latest_aggression_list': latest_aggression_list,
        'misoginia_aggression_list': misoginia_aggression_list
    }
    return render(request, 'alertas/index.html', context)

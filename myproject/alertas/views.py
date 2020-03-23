from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from .models import Aggression

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import AggressionSerializer

def index(request):
    latest_aggression_list = Aggression.objects.all()
    misoginia_aggression_list = Aggression.objects.filter(tags__name__in=["misoginia"])
    homofobia_aggression_list = Aggression.objects.filter(tags__name__in=["homofobia"])
    context = {
        'latest_aggression_list': latest_aggression_list,
        'misoginia_aggression_list': misoginia_aggression_list,
        'homofobia_aggression_list': homofobia_aggression_list
    }
    return render(request, 'alertas/index.html', context)


def stats(request):
    latest_aggression_list = Aggression.objects.all()
    context = {
        'latest_aggression_list': latest_aggression_list
    }
    return render(request, 'alertas/stats.html', context)


class ListAggressionsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Aggression.objects.all()
    serializer_class = AggressionSerializer


class AggressionsStatsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Aggression.objects.all()
    serializer_class = AggressionSerializer


@api_view(['GET'])
def aggression_collection(request):
    if request.method == 'GET':
        aggressions = Aggressions.objects.all()
        serializer = AggressionSerializer(aggressions, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def aggression_element(request, pk):
    try:
        aggression = Aggression.objects.get(pk=pk)
    except Aggression.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AggressionSerializer(aggression)
        return Response(serializer.data)

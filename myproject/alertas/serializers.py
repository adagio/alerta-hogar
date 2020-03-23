from rest_framework import serializers
from .models import Aggression


class AggressionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aggression
        fields = ('id', 'aggression_text', 'place', 'time', 'pub_date')


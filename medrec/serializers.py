from rest_framework import serializers 
from . models import *

class ICDSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ICDSearch
        fields = '__all__'
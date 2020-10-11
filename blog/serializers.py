

from rest_framework import serializers
from .models import Category,Vlog



class Categoryserializers(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields ='__all__'

class Vlogserializers(serializers.ModelSerializer):
    class Meta:
        model= Vlog
        fields ='__all__'

# hello git
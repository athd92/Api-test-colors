from rest_framework import serializers
from .models import Colors

class ColorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = ('id', 'name','color', 'year','pantone_value' )


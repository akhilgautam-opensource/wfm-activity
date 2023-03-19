from rest_framework import serializers
from .models import WfmActivity

class WfmActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = WfmActivity
        fields = '__all__'

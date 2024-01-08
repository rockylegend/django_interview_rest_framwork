from rest_framework import serializers
from .models import *


class UserInformationSerilizer(serializers.ModelSerializer):
    class Meta:
        model=UserInformationModal
        fields='__all__'
    
    
    
class ContentSerilizers(serializers.ModelSerializer):
    class Meta:
        model=ContentModal
        exclude=("primaryKey",)
    
    
class UserLoginSerilizer(serializers.ModelSerializer):
    class Meta:
        model=UserLogin
        fields='__all__'
        
        
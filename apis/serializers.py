from rest_framework import serializers
from .models import Regisration,Contacts,Charts

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        models = Regisration
        fields = ['username','phonenumber','userimage','password','is_active','is_loggedin']
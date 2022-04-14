from django.shortcuts import render
from django.contrib.auth.hashers import make_password,check_password
from .serializers import RegistrationSerializer,ContactsSerializer,ChartsSerializer
from .models import Regisration,Contacts,Charts
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['POST'])
def registration_view(request):
    details = request.data
    username = details['username']
    phonenumber = details['phonenumber']
    userimage = details['userimage']
    password = details['password']
    password = make_password(password)

    checkuser = Regisration.objects.filter(phonenumber=phonenumber)
    if checkuser.exists():
        return Response("user with this email already exist")
    else:
        new_user = Regisration(username=username,phonenumber=phonenumber,userimage=userimage,password=password)
        new_user.save()
        data = {
            'username': username,
            'phonenumber':phonenumber,
            'userimage':userimage,
            'password':password
        }
        response = RegistrationSerializer(data, many = True)
        return Response(response.data)


@api_view(['POST'])
def addcontact_view(request):
    details = request.data
    user = details['user']
    username = details['username']
    phonenumber = details['phonenumber']

    checkcontact = Contacts(user=user, phonenumber=phonenumber)
    if checkcontact.exists():
        return Response("This contact already added")
    else:
        new_contact = Contacts(user=user, username=username, phonenumber=phonenumber)
        new_contact.save()
        data = {
            'user':user,
            'username':username,
            'phonenumber':phonenumber
        }
        serialize = ContactsSerializer(data, many =True)
        return Response(serialize.data)
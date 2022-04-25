from django.shortcuts import render
from django.contrib.auth.models import User
from starterupperupp.models import Company, Transaction
from starterupperupp.serializers import CompanySerializer, TransactionSerializer, UserSerializer
from rest_framework import viewsets
from django.db import IntegrityError
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
import django_filters
# Views handle the HTTP requests for our models


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)  # data is a dictionary
            user = User.objects.create_user(
                username=data['username'],
                password=data['password'],
                email=data['email'],
                first_name=data['first_name'],
                last_name=data['last_name'])

            user.save()

            token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=201)
        except IntegrityError:
            return JsonResponse(
                {'error': 'username and/or email taken. choose another username and/or email'},
                status=400)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(
            request,
            username=data['username'],
            password=data['password'])
        if user is None:
            return JsonResponse(
                {'error': 'unable to login. check username and password'},
                status=400)
        else:  # return user token
            try:
                token = Token.objects.get(user=user)
            except:  # if token not in db, create a new one
                token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=201)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    authentication_classes = [ TokenAuthentication ]
    permission_classes = [permissions.IsAuthenticated]
    

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    authentication_classes = [ TokenAuthentication ]
    permission_classes = [permissions.IsAuthenticated]
    name = 'transaction-list'

    filter_fields = (
        'associated_company_id',
        'associated_user_id',
    )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [ TokenAuthentication ]
    permission_classes = [permissions.IsAuthenticated]

from .serlizers import *
from rest_framework import generics
from .models import UserInformationModal,ContentModal
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.views import APIView


class UserRegisteration(generics.CreateAPIView):
    serializer_class=UserInformationSerilizer
    queryset=UserInformationModal.objects.all()

    def post(self,request):
        serilizerData=self.get_serializer(data=request.data)
        print(request.data)
        if serilizerData.is_valid():            
            serilizerData.save()
            createUser=User.objects.create_user(username=serilizerData.data['email'],password=serilizerData.data['password'])
            createUser.save()
            return Response("Successfully created !!")
        
        return Response(serilizerData.errors)
        
    
        
class UserSignIn(generics.CreateAPIView):
    serializer_class=UserLoginSerilizer
    queryset=UserLogin.objects.all()
    
    def post(self,request):
        serializersData=self.get_serializer(data=request.data)
        if serializersData.is_valid():
            authenticatUser=authenticate(username=serializersData.data['email'],password=serializersData.data['password'])
            if authenticatUser is not None:
                login(request,authenticatUser)
                return redirect('UserInformationSectionForRoute')
            else:
                return Response(serializersData.errors)    
        
        
class userInformationSection(generics.CreateAPIView):
    serializer_class=ContentSerilizers
    permission_classes=[IsAuthenticated]
    
    def post(self,request):
        serializersData=self.get_serializer(data=request.data)
        if serializersData.is_valid():
            ContentModal.objects.create(primaryKey=str(request.user),**serializersData.validated_data)
            return Response(serializersData.data,status=status.HTTP_201_CREATED)
        return Response(serializersData.errors,status=status.HTTP_103_EARLY_HINTS)

class ContextCreation(APIView):
    permission_classes=[IsAuthenticated]
    
    def get(self,request):
        data=ContentModal.objects.filter(primaryKey=request.user)
        print(data)
        serilizedData=ContentSerilizers(data,many=True)
        return Response(serilizedData.data)
        
        
        
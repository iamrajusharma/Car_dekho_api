from django.shortcuts import render
from rest_framework.response import Response
from .models import Carlist,Showeroom_model,Review
from .api_file.serialization import CarSerializer,ShowroomSerializer,ReviewSerializers,UserRegistrationSerializer
from rest_framework.decorators import api_view,authentication_classes
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions
from  rest_framework import generics
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from .api_file.permission import AdminOrReadyOnlyPermission,ReviewANdReda
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()
# def car_list(request):
#     cars=Carlist.objects.all()
#     data={
#         'cars':list(cars.values()),

#     }
#     return JsonResponse(data)

class Showroom_views(generics.ListCreateAPIView):
      queryset=Showeroom_model.objects.all()
      serializer_class=ShowroomSerializer
     #  authentication_classes=[SessionAuthentication,TokenAuthentication]
     #  permission_classes=[DjangoModelPermissions]

class Review_list(viewsets.ModelViewSet):
     queryset=Review.objects.all()
     # serializer_class=ReviewSerializers
     # permission_classes=[ReviewANdReda]




# @api_view(['GET','POST'])

class car_list(generics.ListCreateAPIView):
      queryset=Carlist.objects.all()
      serializer_class=CarSerializer
     #  authentication_classes=[JWTAuthentication]
     #  permission_classes=[IsAuthenticated]



class car_detail(generics.RetrieveAPIView):
     queryset=Carlist.objects.all()
     serializer_class=CarSerializer
     # authentication_classes=[SessionAuthentication,TokenAuthentication]
     # permission_classes=[DjangoModelPermissions]



        # if request.method=='GET':
        #   try:
        #       car=Carlist.objects.get(pk=pk)
        #   except:
        #        return Response({'error':'car not found'},status=status.HTTP_404_NOT_FOUND)
        #   serializer=CarSerializer(car)
        #   return Response(serializer.data)
      
        # if request.method=="PUT":
        #   car=Carlist.objects.get(pk=pk)
        #   serializer=CarSerializer(car,data=request.data)
        #   if serializer.is_valid():
        #       serializer.save()
        #       return Response(serializer.data)
        #   else:
        #       return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
          
        # if request.method=="DELETE":
        #       car=Carlist.objects.get(pk=pk)
        #       car.delete()
        #       return Response(status=status.HTTP_204_NO_CONTENT)
      
   


    # if request.method=='GET':
        
    #        car=Carlist.objects.all()
    #        serializer=CarSerializer(car,many=True)
    #        return Response(serializer.data)
    
    # if request.method=="POST":
    #     serializer=CarSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors)














# class Showroom_views(APIView):
#         authentication_classes=[BasicAuthentication]
#         permission_classes=[IsAuthenticated]
#         def get(self,request):
#             showroom=Showeroom_model.objects.all()
#             serializer=ShowroomSerializer(showroom,many=True)
#             return Response (serializer.data)
        
#         def post(self,request):
#             serializer=ShowroomSerializer(data=request.data)
#             if serializer.is_valid():
#                   serializer.save()
#                   return Response(serializer.data)
#             else:
#                 return Response(serializer.errors)

class showroom_detail(APIView):
        def get(self,request,pk):
           shworoom=get_object_or_404(Showeroom_model, pk=pk)  
           ser=ShowroomSerializer(shworoom)
           return Response(ser.data)
        def put(self,request,pk):
              showroom=get_object_or_404(Showeroom_model,pk=pk)
              ser=ShowroomSerializer(showroom,data=request.data)
              if ser.is_valid():
                   ser.save()
                   return Response(ser.data)
              else:
                   return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
                       
        def delete(self,request,pk):
            showroom=get_object_or_404(Showeroom_model,pk=pk)
            showroom.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)  
        

        def patch(self,request,pk):
              showroom=get_object_or_404(Showeroom_model,pk=pk)
              ser=ShowroomSerializer(showroom,data=request.data,partial=True)
              if ser.is_valid():
                   ser.save()
                   return Response(ser.data,status=status.HTTP_200_OK)
              return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
             
 
     
      

# @api_view(['GET','POST'])

# def car_list(request):
#     if request.method=='GET':
        
#            car=Carlist.objects.all()
#            serializer=CarSerializer(car,many=True)
#            return Response(serializer.data)
    
#     if request.method=="POST":
#         serializer=CarSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# @api_view(['GET','PUT','DELETE'])
@csrf_exempt  # Disable CSRF for API logout
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout_view(request):
     if request.method=='POST':
          request.user.auth_token.delete()
          return Response(status=status.HTTP_200_OK)
          
# class UserRegistrion(APIView):
#      def post(self,request,*args,**kwargs):
#           serializer=UserRegistrationSerializer(data=request.data)
          

#           if serializer.is_valid():
#                 user =serializer.save()
              

#           refresh = RefreshToken.for_user(User)
#           access_token = str(refresh.access_token)

#           return Response({
#                 "username": user.username,
#                 "access_token": access_token,
#                 "refresh_token": str(refresh)  # Convert to string
#             }, status=status.HTTP_201_CREATED)

          
         
         
class UserRegistrion(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()  # Save and get the user instance

            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)  # Pass the user instance
            access_token = str(refresh.access_token)

            return Response({
                "username": user.username,
                "access_token": access_token,
                "refresh_token": str(refresh)  # Convert to string
            }, status=status.HTTP_201_CREATED)

        # If serializer is not valid, return the errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
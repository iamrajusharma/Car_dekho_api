from rest_framework import serializers
from ..models import Carlist,Showeroom_model,Review,User


class ReviewSerializers(serializers.ModelSerializer):
     user_name=serializers.StringRelatedField(read_only=True)
     class Meta:
          model=Review
          fields="__all__"
class ShowroomSerializer(serializers.ModelSerializer):
     class Meta:
          model=Showeroom_model
          fields="__all__"


class CarSerializer(serializers.ModelSerializer):
     discounted_price=serializers.SerializerMethodField()
     reviews=ReviewSerializers(many=True,read_only=True)
     class Meta:
          model=Carlist
          fields="__all__"
         
     def get_discounted_price(self,objest):
          discountprice=objest.price-5000
          return discountprice   
     
     def validate_price(self,value):
          if value <=2000.00:
                raise serializers.ValidationError("price muse be greter than 20000.00")
          return value
         
     def validate(self, data):
          if data['name']==data['descriptions']:
               raise serializers.ValidationError("name and descriptions must be different")  
          return data
     

class UserRegistrationSerializer(serializers.ModelSerializer):
     password2=serializers.CharField(style={'input_type':'password'},write_only=True)     
     
     class Meta:
          model=User
          fields=['username','email','password','password2']
          extra_kwargs={
               'password':{'write_only':True}
          }

     def validate(self, data):
           if data['password']!=data['password2']:
                raise serializers.ValidationError({"password":"password field did`n match"})  
           return data
     def create(self, validated_data):
         validated_data.pop('password2',None) 


         user=User.objects.create_user(
              username=validated_data['username'],
              email=validated_data['email'],
              password=validated_data['password']
         )

         return user
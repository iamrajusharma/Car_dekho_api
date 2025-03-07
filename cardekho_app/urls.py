from django.urls import path,include
from rest_framework.routers import DefaultRouter
from cardekho_app import views
from rest_framework.authtoken.views import obtain_auth_token
# router = DefaultRouter()
# router.register('Review_list',views.Review_list, basename='Review_list')


# from . import views

# urlpatterns = [
#     path('', include(router.urls)),
#     path('list',views.car_list.as_view(),name='car_list'),
#     path('list/<int:pk>/', views.car_detail.as_view(), name='car_detail'), 
#     path('showroom',views.Showroom_views.as_view(),name="Showroom_views"),
#     path('showroom_detail/<int:pk>',views. showroom_detail.as_view(),name='showroom_detail'),
#     # path('showroom/<int:pk>/review-create',views.ReviewCreate.as_view(),name='review_create'),
#     # path('showroom/<int:pk>/',views.Review_list.as_view(),name='Review_list'),
#     # path('showroom/int:pk>/',views.ReviewDetails.as_view(),name='review_detail'),


# ]
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register('Review_list', views.Review_list, basename='Review_list'),

urlpatterns = [
    path('logout',views.logout_view,name='logout_view'),
    path('api',obtain_auth_token, name='api_token_auth'),
  
    path('register',views.UserRegistrion.as_view(), name='register'),
    path('', include(router.urls)),  # This will handle all ViewSets
    path('list', views.car_list.as_view(), name='car_list'),
    path('list/<int:pk>/', views.car_detail.as_view(), name='car_detail'),
    path('showroom', views.Showroom_views.as_view(), name="Showroom_views"),
    path('showroom_detail/<int:pk>', views.showroom_detail.as_view(), name='showroom_detail'),
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]







 
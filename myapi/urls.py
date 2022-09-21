from django.urls import path
from . import views
from .views import *

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('', ItemAPIList.as_view(), name='list'),
#     path('<int:pk>/', ItemAPIView.as_view(), name='product'),
#     path('<int:pk>/', ItemAPIUpdate.as_view(), name='update'),
#     path('<int:pk>/', ItemAPIDetailView.as_view(), name='detail'),
# ]

"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myapi.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'product', ItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('api/product/', ItemViewSet.as_view({'get': 'list'})),
    # path('api/product/<int:pk>/', ItemViewSet.as_view({'put': 'update'})),
    # path('api/product/', ItemAPIList.as_view(), name='list'),
    # path('api/product/<int:pk>/', ItemAPIView.as_view(), name='product'),
    # path('api/product/<int:pk>/update/', ItemAPIUpdate.as_view(), name='update'),
    # path('api/product/<int:pk>/detail/', ItemAPIDetailView.as_view(), name='detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

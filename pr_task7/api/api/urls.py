from django.contrib import admin
from django.urls import path, include
from freelancer.views import FreelancerViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'freelancers', FreelancerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
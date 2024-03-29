
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from bills import views


router = DefaultRouter()
router.register('enduser', views.EndUser, base_name='enduser-viewset')
router.register('interuser', views.InternalUser, base_name='interuser-viewset')

urlpatterns = [
    # path('enduser/', views.EndUser.as_view({'get': 'list'})),
    path('', include(router.urls)),
]


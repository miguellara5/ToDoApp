
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from tasks.api import TaskViewSet
from tasks.customToken import CustomAuthToken
from profiles.api import ProfileCreationView

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', views.obtain_auth_token),
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('api/register/', ProfileCreationView.as_view()),
]

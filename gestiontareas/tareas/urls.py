from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tareas', views.TareaViewSet, basename='tareas')
urlpatterns = [
    path('', include(router.urls))
]
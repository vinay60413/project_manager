from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChatMessageViewSet, chatroom

router = DefaultRouter()
router.register(r'', ChatMessageViewSet)

urlpatterns = [
    path('chat/', include(router.urls), name='chat'),
    path('', views.project_list, name='project_list'),
    path('<int:project_id>/', views.project_detail, name='project_detail'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/<int:task_id>/complete/', views.delete_task, name='complete'),
    path('add_project/', views.add_project, name='add_project'),
    path('project/<int:project_id>/add_task/', views.add_task, name='add_task'),
]

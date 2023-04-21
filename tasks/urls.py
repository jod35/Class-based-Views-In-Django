from django.urls import path
from . import views


urlpatterns = [
    path('',views.HomePageView.as_view(),name='homepage'),
    path('add/',views.TaskCreateView.as_view(),name='add_task'),
    path('task/<int:pk>/',views.TaskDetailView.as_view(),name='view_task'),
    path('task/<int:pk>/update/',views.TaskUpdateView.as_view(),name='update_task'),
    path('task/<int:pk>/delete/',views.TaskDeleteView.as_view(),name='delete_task'),
    path('settings/',views.SettingsViews.as_view(),name='settings')
]
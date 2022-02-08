from django.urls import path
from . import views

app_name = 'sjvideo'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('notes/', views.AllNote.as_view(), name='note-list'),
    path('add-lesson/', views.AddLesson.as_view(), name='add-lesson'),
    path('view-lesson/<int:pk>',views.ViewLesson.as_view(), name='view-lesson'),
    path('update-lesson/<int:pk>', views.UpdateLesson.as_view(), name='update-lesson'),
    path('update-notes/<int:pk>', views.update_notes, name='update-notes'),
    path('update-download-url/<int:pk>', views.update_download_url, name='update-download-url'),
]

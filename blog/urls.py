from django.urls import path 
from . import views 

app_name = 'blog'

urlpatterns = [
    path('', views.AllPost.as_view(), name='home'),
    path('view/<int:pk>', views.ViewPost.as_view(), name="view-post"),
    path('new/', views.CreatePost.as_view(), name="create-post"),
    path('update/<int:pk>', views.UpdatePost.as_view(), name="update-post"),
]

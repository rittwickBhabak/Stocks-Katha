from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='home'),
    path('sjvideo/', include('sjvideo.urls')),
    path('blog/', include('blog.urls')),
]

from django.urls import path, include
from django.contrib import admin

urlpatterns = [
	path('admin/',admin.site.urls),
	path('', include('data_app.urls')) # Note: all your app urls will start with this path
]

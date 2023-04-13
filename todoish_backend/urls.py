from django.urls import path, include
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todoish.urls')),
]

# Format url pattern so that we can receive diff content types
urlpatterns = format_suffix_patterns(urlpatterns)

from django.contrib import admin
from django.urls import path, include

from exam.urls import urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('exam/', include((urlpatterns, 'exam'))),
]

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^chat/', include('message.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^docs/', include_docs_urls(title='API Documentation')),
]

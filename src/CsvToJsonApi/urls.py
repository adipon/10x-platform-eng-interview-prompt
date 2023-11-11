from django.contrib import admin
from django.urls import path
from .views import DataView, UploadCSVView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/query/', DataView.as_view(), name='query'),
    path('api/upload/', UploadCSVView.as_view(), name='upload-csv'),
]

from django.urls import path
from files.views import FileViewSet

urlpatterns = [
    path('', FileViewSet.as_view({'get': 'list'}), name="file-list"),
    path('upload/', FileViewSet.as_view({'post': 'upload'}), name="file-upload")
]

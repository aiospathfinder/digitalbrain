from django.urls import path
from .views import fnBuildSecondBrain, fnQA, download_text

urlpatterns = [
    path('buildbrain', fnBuildSecondBrain, name="buildBrain"),
    path('ask', fnQA, name="QA"),
    path('download-text', download_text, name='download_text'),
]

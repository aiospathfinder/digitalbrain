from django.urls import path
from .views import fnBuildSecondBrain, fnQA

urlpatterns = [
    path('buildbrain', fnBuildSecondBrain, name="buildBrain"),
    path('ask', fnQA, name="QA"),
]

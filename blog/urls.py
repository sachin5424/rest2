from django.contrib import admin
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns

from blog import views
urlpatterns = [
    path('home/',views.vlog_list),
    path('home/<int:pk>/',views.snippet_detail)
]
urlpatterns = format_suffix_patterns(urlpatterns)
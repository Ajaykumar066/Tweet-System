
# from django.urls import path
# from . import views

# ulrpatterns = [
#     path('',views.index,name = 'index'),
# ] 

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Add other URL patterns here
]

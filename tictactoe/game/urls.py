from django.urls import path
from .views import BoardView 

app_name = 'game'

urlpatterns = [
    path('', BoardView.as_view()), 
]


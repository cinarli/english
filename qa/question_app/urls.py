from django.urls import path
from .views import index
app_name='question_app'
urlpatterns = [
    path('', index,name='empty'),
]


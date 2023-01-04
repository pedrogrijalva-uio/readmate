from django.urls import path, include
from readlist_app.views import book_list

urlpatterns = [
    path('list/', book_list, name='movie_list'),
]

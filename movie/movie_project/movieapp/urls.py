from django.urls import path
from . import views
app_name='movieapp'
urlpatterns=[
    path('',views.home,name='homepage'),
    path('details/<int:id_movie>/',views.movie_details,name='moviedetails'),
    path('add/',views.add,name='add'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]   
# from django.urls import path
# from.import views
#
# urlpatterns = [
#     path("",views.index,name="BlogHome"),
#     path("blogpost/",views.blogpost,name="BlogPost")
# ]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blogHome"),
    path("blogpost/<int:id>", views.blogpost, name="blogHome")
]


from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("add-item",views.add_item,name="add-item"),
    path("", views.index, name="index"),
]
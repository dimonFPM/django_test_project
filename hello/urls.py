from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="hello_index"),
    path("1", views.index_1, name="hello_mother_fucker")
]

from django.urls import path
from api.views import MyModelListCreate, MyModelRetrieveUpdateDestroy
# from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path('mymodel/', MyModelListCreate.as_view()),
    path('mymodel/<int:pk>/', MyModelRetrieveUpdateDestroy.as_view()),
]

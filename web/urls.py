from django.urls import path
from .views import ToDoViewGet, ToDoViewPost, ToDoViewPut, ToDoViewDelete
from script import GetData
# from .views import ToDoView


app_name = "organizer"

# urlpatterns = [
#     path('todos', ToDoView.as_view()),
#     path('todos/<int:pk>', ToDoView.as_view())
# ]

urlpatterns = [
    path('todos/get/<int:chatID>', ToDoViewGet.as_view()),
    path('todos/post', ToDoViewPost.as_view()),
    path('todos/put/<int:pk>', ToDoViewPut.as_view()),
    path('todos/delete/<int:pk>', ToDoViewDelete.as_view()),
    # path('todos/<int:pk>', ToDoView.as_view())
]

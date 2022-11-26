from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ToDo
from .serializers import ToDoSerializer


# class ToDoView(ListCreateAPIView):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer
#
#     def perform_create(self, serializer):
#         name = get_object_or_404(ToDo, id=self.request.data.get('id'))
#         return serializer.save(name=name)
#
#
# class SingleToDoView(RetrieveUpdateDestroyAPIView):
#     queryset = ToDo.objects
#     serializer_class = ToDoSerializer

# class ToDoView(ListModelMixin, GenericAPIView):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def perform_create(self, serializer):
#         name = get_object_or_404(ToDo, id=self.request.data.get('todo_id'))
#         return serializer.save(name=name)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class ToDoView(APIView):
#     def get(self, request):
#         todo = ToDo.objects.all()
#         serializer = ToDoSerializer(todo, many=True)
#         return Response({"todos": serializer.data})
#
#     def post(self, request):
#         todo = request.data.get('todos')
#         # Create an article from the above data
#         serializer = ToDoSerializer(data=todo)
#         if serializer.is_valid(raise_exception=True):
#             todos_saved = serializer.save()
#         return Response({"Успешно": "Задача '{}' успешно создана".format(todos_saved.name)})
#
#     def put(self, request, pk):
#         saved_article = get_object_or_404(ToDo.objects.all(), pk=pk)
#         data = request.data.get('todos')
#         serializer = ToDoSerializer(instance=saved_article, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             todos_saved = serializer.save()
#         return Response({
#             "Успешно": "Задача '{}' успешно изменена".format(todos_saved.name)
#         })
#
#     def delete(self, request, pk):
#         # Get object with this pk
#         article = get_object_or_404(ToDo.objects.all(), pk=pk)
#         article.delete()
#         return Response({
#             "Успешно": "Задача '{}' успешно удалена".format(pk)
#         }, status=204)


class ToDoViewGet(APIView):
    def get(self, request):
        todo = ToDo.objects.all()
        serializer = ToDoSerializer(todo, many=True)
        return Response({"todos": serializer.data})


class ToDoViewPost(APIView):
    def post(self, request):
        todo = request.data.get('todos')
        # Create an article from the above data
        serializer = ToDoSerializer(data=todo)
        if serializer.is_valid(raise_exception=True):
            todos_saved = serializer.save()
        return Response({"Успешно": "Задача '{}' успешно создана".format(todos_saved.name)})


class ToDoViewPut(APIView):
    def put(self, request, pk):
        saved_article = get_object_or_404(ToDo.objects.all(), pk=pk)
        data = request.data.get('todos')
        serializer = ToDoSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            todos_saved = serializer.save()
        return Response({
            "Успешно": "Задача '{}' успешно изменена".format(todos_saved.name)
        })


class ToDoViewDelete(APIView):
    def delete(self, request, pk):
        # Get object with this pk
        article = get_object_or_404(ToDo.objects.all(), pk=pk)
        article.delete()
        return Response({
            "Успешно": "Задача '{}' успешно удалена".format(pk)
        }, status=204)
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework import mixins

class BooksAPIMixins(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
'''
    def get(self, request, *args, **kwargs): #get메소드 처리 - 전체목록
        return self.list(request, *args, **kwargs) #mixins.ListModelMixin과 연결
    def post(self, request, *args, **kwargs): #post 메소드 처리 - 1권 등록
        return self.create(request, *args, **kwargs) #mixins.CreateModelMixin과 연결
'''

class BookAPIMixins(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'bid' #django 기본모델 pk가 아닌 bid로 사용하고 있어서 이렇게 설정해야 함. 
'''
    def get(self, request, *args, **kwargs): #get메소드 처리 - 1권
        return self.retrieve(request, *args, **kwargs) #mixins.RetrieveModelMixin과 연결
    def put(self, request, *args, **kwargs): #put메소드 처리 - 1권 수정
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs): #delete메소드 처리 - 1권 삭제
        return self.destroy(request, *args, **kwargs)
'''


'''
class BooksAPI(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookAPI(APIView):
    def get(self, request, bid):
        book = get_object_or_404(Book, bid=bid)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

'''

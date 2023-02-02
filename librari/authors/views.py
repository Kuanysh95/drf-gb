from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Author, Book, Article, Biography
from .serializers import AuthorModelSerializer, BookModelSerializer, BiographyModelSerializer, ArticleModelSerializer
from rest_framework.views import APIView


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
    filterset_fields = ['first_name', 'last_name', 'birthday_year']


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer


class MyAPIView(ViewSet):
    def list(self, request):
        authors = Author.objects.all()
        serializer = AuthorModelSerializer(authors, many=True)
        return Response(serializer.data)









from re import A
from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE_HASH_VALUE
from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.models import Article
from articles.serializers import ArticleSerializer
from rest_framework import status


@api_view(['GET', 'POST'])
def index(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import render
from .models import Article
from .serializers import ArticleSerializer
from django.http import HttpResponse, JsonResponse
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, generics
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
# Create your views here.

#============Function Base API Start=============

# @api_view(['GET', 'POST'])
# def FunctionBase_Article_list(request):
#     if request.method == 'GET':
#         article = Article.objects.all()
#         serializer = ArticleSerializer(article, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



# @api_view(['GET', 'PUT', 'DELETE'])
# def FunctionBase_Article_detail(request, pk):

#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         article.delete()

#============Function Base API End=============



#============Class Base API Start=============
# class ClassView_Article_list(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'article.html'

#     def get(self, request, format=None):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response({'article': articles})

#     def post(self, request, format=None):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class ClassView_Article_detail(APIView):
#     def get_object(self, pk):
#         try:
#             return Article.objects.get(pk=pk)
#         except Article.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         articles = self.get_object(pk)
#         serializer = ArticleSerializer(articles)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         articles = self.get_object(pk)
#         serializer = ArticleSerializer(articles, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         articles= self.get_object(pk)
#         articles.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

    #============Class Base API End=============




    #============Mixin Base API Start=============
# class MixinsArticle_list(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

#     def get(self, request):
#         return self.list(request)
 
#     def post(self, request):
#         return self.create(request)
    
#     def put(self, request, id=None):
#         return self.update(request)
    


# class MixinsArticle_detail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

    #============Class Base API End=============
    





    #============Generic API Start=============
# class GenericArticle_list(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
#     permission_classes = [IsAuthenticated]


# class GenericArticle_detail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer



    #============Generic API End=============




        #============Viewsets API Start=============
# class GenericArticleView(viewsets.GenericViewSet, 
#                         mixins.ListModelMixin,
#                         mixins.CreateModelMixin,
#                         mixins.RetrieveModelMixin,
#                         mixins.UpdateModelMixin,
#                         mixins.DestroyModelMixin):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
#     permission_classes = [IsAuthenticated]

    #============Viewsets API End=============
    
    
    
    
    #============ModelViewsets API Start=============
class GenericArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    
    #============Viewsets API End=============
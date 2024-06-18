
from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('article', views.GenericArticleView)

urlpatterns = [
    #============function Base API===========
    # path('article-list/', views.FunctionBase_Article_list, name='article-list'),
    # path('article-detail/<int:pk>/', views.FunctionBase_Article_detail,name='article-detail'),

    #============Class Base API===========
    # path('article-list/', views.ClassView_Article_list.as_view(), name='article-list'),
    # path('article-detail/<int:pk>/', views.ClassView_Article_detail.as_view(),name='article-detail'),

    #============Mixin API===========
    # path('article-list/', views.MixinsArticle_list.as_view(), name='article-list'),
    # path('article-detail/<int:pk>/', views.MixinsArticle_detail.as_view(),name='article-detail'),

     #============Generic API===========
    # path('article-list/', views.GenericArticle_list.as_view(), name='article-list'),
    # path('article-detail/<int:pk>/', views.GenericArticle_detail.as_view(),name='article-detail'),

    #============ViewSet API===========
    # path('viewsets/', include(router.urls)),
    # path('viewsets/<int:pk>/', include(router.urls)),
    
    #============ModelViewSet API===========
    path('viewsets/', include(router.urls)),
    path('viewsets/<int:pk>/', include(router.urls)),
    
 ]
from django.urls import path,include
from Blog.views import ArticleListView,ArticleDetailView,ArticleCreateView,ArticleUpdateView,ArticleDeleteView

app_name='Blog';
urlpatterns = [
    path('',ArticleListView.as_view(),name='Listview'),
    path('<int:my_id>/',ArticleDetailView.as_view(),name='Detail_view'),
    path('create/',ArticleCreateView.as_view(),name='Create'),
    path('<int:my_id>/update/',ArticleUpdateView.as_view(),name='Update'),
    path('<int:selected_id>/delete',ArticleDeleteView.as_view(),name='delete'),
]
from django.urls import path,include
from .views import CourseView,CourseListView,CourseCreateView,CourseUpdateView,CourseDeleteView

urlpatterns = [
    path('',CourseView.as_view(),name='About'),
    path('<int:id>/',CourseView.as_view(template_name='Course/Contact.html'),name='Course_detail'),
    path('list/',CourseListView.as_view(),name='course_list'),
    path('create/',CourseCreateView.as_view(),name='course_create'),
    path('<int:id>/update/',CourseUpdateView.as_view(),name='course_update'),
    path('<int:id>/delete/',CourseDeleteView.as_view(),name='Course_delete'),
]
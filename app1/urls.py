from django.urls import path
from . import views

urlpatterns = [
    #path('',views.index.as_view())
    path('', views.SchoolListView.as_view(),name='list'),
    #path('<int:pk>',views.SchoolDetailView.as_view(),name='detail'),
    #path('school<int:pk>',views.SchoolDetailView.as_view(),name='detail'),
    #path('school/<int:pk>',views.SchoolDetailView.as_view(),name='detail'),
    path('school=<int:pk>',views.SchoolDetailView.as_view(),name='detail'),
    path('create_school',views.SchoolCreateView.as_view(), name='create'),
    path('delete=<int:pk>',views.SchoolDeleteView.as_view(),name='delete'),
    path('school_updation_success', views.school_updation_success, name='school_updation_success'),
    path('update=<int:pk>',views.SchoolUpdateView.as_view(),name='update'),
]
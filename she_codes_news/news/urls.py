from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(),name='newStory'),
    path('<int:pk>/deleteStory', views.DeleteStoryView.as_view(), name='deleteStory'),
    path('<int:pk>/editStory', views.EditStoryView.as_view(), name='editStory'),
    path('category/<str:category>', views.CategoryView.as_view(), name='category'),
    path('<int:pk>/comments', views.AddCommentView.as_view(), name='newComment'),
    
]
#  pensar en el autor

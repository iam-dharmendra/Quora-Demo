
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('create_post', views.CreatePost.as_view(), name='create_post'),
    path('get_post_answer/<int:id>', views.GetPostAnswerView.as_view(), name='get_post_answer'),
    path('add_answer/<int:post_id>', views.AddPostAnswerView.as_view(), name='add_answer'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

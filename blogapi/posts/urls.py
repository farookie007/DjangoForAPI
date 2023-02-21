from django.urls import path
# Local imports
from .views import PostList, PostDetail


app_name = "posts"

urlpatterns = [
    path("<int:pk>/", PostDetail.as_view(), name = "post_detail"),
    path("", PostList.as_view(), name="post_list"),
]
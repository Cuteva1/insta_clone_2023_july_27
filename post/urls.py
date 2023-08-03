from django .urls import path
from post.views import home_feed
from post.views import add_post, edit_post
app_name ="post"

urlpatterns = [
    path("feed/", home_feed, name = "home"),
    path("create_post/", add_post, name = "add_post"),
    path("change-post/<int:post_id>/", edit_post, name = "edit_post"),
]
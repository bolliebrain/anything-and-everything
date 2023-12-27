from django.urls import path, include
from myaande.views import (AandeView, AandeDetail, 
    PostAande, EditAande, DeleteAande, EditComment, DeleteComment, AllMyPosts)
from myaande import views



urlpatterns = [
    path('', AandeView.as_view(), name='seeposts'),
    path('<slug:slug>/', AandeDetail.as_view(), name='post_detail'),
    path('addapost', PostAande.as_view(), name='addpost'),
    path('<slug:slug>/edit', EditAande.as_view(), name='edit_post'),
    path('<slug:slug>/delete', DeleteAande.as_view(), name='delete_post'),
    path('<pk>/editcomment', EditComment.as_view(), name='edit_comment'),
    path('<pk>/deletecomment', DeleteComment.as_view(), name='delete_comment'),
    path('<slug:slug>/myposts', AllMyPosts.as_view(), name='allmyposts')
]
from django.urls import path, include
from myaande.views import (AandeView, AandeDetail, 
    PostAande, EditAande, DeleteAande, EditComment, DeleteComment)
from myaande import views



urlpatterns = [
    path('', AandeView.as_view(), name='seeposts'),
    path('<slug:slug>/', AandeDetail.as_view(), name='post_detail'),
    path('addapost', PostAande.as_view(), name='addpost'),
    path('<slug:slug>/edit', EditAande.as_view(), name='edit_post'),
    path('<slug:slug>/delete', DeleteAande.as_view(), name='delete_post'),
    path('editcomment', EditComment.as_view(), name='edit_comment'),
    path('<slug:slug>/deletecomment', DeleteComment.as_view(), name='delete_comment')
]
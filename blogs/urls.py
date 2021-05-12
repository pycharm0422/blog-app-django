from django.urls import path
from . import views

urlpatterns=[
    path('', views.PostListView.as_view(), name='home-page'),
    # path('', views.home, name='home-page'),
    path('about/', views.about, name='about-page'),
    path('register/', views.registerForm, name='register-page'),
    path('account/', views.account, name='account-page'),
    path('detail/<int:pk>/', views.detail, name='detail-page'),
    path('update/<int:pk>/', views.updateBlog, name='update-page'),
    path('create/', views.createBlog, name='create-page'),
    path('delete/<int:pk>/', views.deleteBlog, name='delete-page'),
    path('individual/<str:username>/', views.individualPost, name='individual-page'),
    path('createAccount/', views.setAccount, name='account_set-page'),
    path('likePost/', views.likePost, name='liked-post'),
    path('serialized/', views.post_serialized_view, name='serialized-view'),
]
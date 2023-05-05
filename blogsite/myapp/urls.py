from django.urls import path
from django.contrib import admin
from django.conf import settings
from . import views
from django.conf.urls.static import static
app_name='myapp'

urlpatterns=[
  path('',views.index,name='index_page'),
  path('login_page',views.loginview,name='login_page'),
  path('register_page',views.registerview,name='register_page'),
  path('user_page',views.writestory,name='user_page'),
  path('user_blogs',views.user_blogs,name='user_blogs'),
  path('logout',views.logoutview,name='logout'),
  path('edit/<int:pk>', views.EditBlogs, name='edit_blog'),
  path('del/<int:pk>', views.DeleteBlogs, name='delete_blog'),
  path('author_page/<int:pk>',views.authorBlogs,name='author_page')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
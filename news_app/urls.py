from django.urls import path

from news_app.views import CreateNews, HomeNews, user_login, user_logout, NewsByCategory, register, contact_us, ViewNews

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('news/add_news/', CreateNews.as_view(), name='add_news'),
    path('contact/', contact_us, name='contact'),

    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

    path('admin/', HomeNews.as_view(), name='admin'),
]

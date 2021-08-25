
from django.urls import path, include
from . import views
urlpatterns = [
    # path('register/', views.RegisterView),
    path('login/', views.LoginApiView.as_view(), name='login'),
    path('register/', views.RegisterApiView.as_view(), name='register'),
    # path('', include('auth.urls'))
    path('logout/', views.logoutUser, name='logout')
]

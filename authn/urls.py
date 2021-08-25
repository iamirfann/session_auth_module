
from django.urls import path, include
from . import views
urlpatterns = [
    path('register/', views.RegisterView),
    path('login/', views.LoginView),
    path('registerview/', views.RegisterApiView.as_view())
    # path('', include('auth.urls'))

]

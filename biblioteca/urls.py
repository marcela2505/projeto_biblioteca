from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('livros/', views.lista_livros, name='lista_livros'),
    path('emprestimos/', views.emprestimos, name='emprestimos'),
    path('adicionar_livro/', views.adicionar_livro, name='adicionar_livro'),
    
    # Login e Logout
    path('login/', auth_views.LoginView.as_view(template_name='biblioteca/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    
    # Registro de usuários
    path('registro/', views.registro, name='registro'),
    path('devolver/<int:emprestimo_id>/', views.devolver, name='devolver'),
]

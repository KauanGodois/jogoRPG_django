from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('escolha_classe/', views.escolha_classe, name='escolha_classe'),
    path('login/', auth_views.LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('personagem/<int:classe_id>', views.personagem, name='personagem'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # path('admin/', admin.site.urls),
    # path('', views.home, name='home'),
    # path('categorias/', views.categorias, name='categorias'),
    # path('produto/<int:id>/', views.produto, name='produto'),
    # path('excluir/<int:id>/', views.excluir, name='excluir'),
    

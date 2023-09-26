from django.urls import path
from recipes import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="recipes-home"),
    path('recipes/<int:id>/', views.recipe, name="recipes-recipe"),
    path('recipes/category/<int:category_id>/', views.category, name="recipes-category"),
        ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

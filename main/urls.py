from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from main import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),  # Используйте views.product_detail
    path('', views.home, name='home_page'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('aps.product.urls')),
    path('user/',include('aps.user.urls')),
    path('order/',include('aps.order.urls')),
    path('test/',include('aps.userValidator.urls')),
    path('orderplaced/',include('aps.ordersplaced.urls')),
    path('dashboard/',include('aps.dashboard.urls'))

] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
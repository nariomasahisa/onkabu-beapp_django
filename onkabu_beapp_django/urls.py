from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('portfolio/', include('portfolio.urls')),
    path('onkabu/', include('onkabu.urls')),
    path('calc-value/', include('calc_value.urls'))
]

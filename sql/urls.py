
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Records Administrator'
admin.site.site_title = 'Records Administrator'
admin.site.index_title = 'Records'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('records.urls')),
    path('api/', include('records.api.urls'))
]

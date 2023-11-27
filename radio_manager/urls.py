from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from radio_manager.views import Login, Logout

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path("admin/", admin.site.urls),
    path('logout/', Logout.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
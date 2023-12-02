from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from programa.views import ListarProgramas


from radio_manager.views import Login, Logout

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path("admin/", admin.site.urls),
    path('logout/', Logout.as_view(), name='logout'),
    path('programa/', include('programa.urls'), name='programa'),
    path("__reload__/", include("django_browser_reload.urls")),
]
from django.contrib import admin
from django.urls import include, path
from msmg.views import Login, Logout

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', Login.as_view(), name="index"),
    path('logout/', Logout.as_view(), name='logout'),
    path("eventos/", include('eventos.urls'), name='eventos'),
    path('bandas/', include('banda.urls'), name="banda"),
    path('musicas/', include('musicas.urls'), name="musicas"),
]
from django.contrib import admin
from django.urls import path, include
from MainApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='home'),
    path('notebooks/list', views.NotebooksList.as_view(), name='notebooks-list'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout', views.logout, name="logout"),
    path('auth/registration', views.RegistrationUser.as_view(), name='registration'),
    path('statistics', views.get_statistics, name='statistics')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

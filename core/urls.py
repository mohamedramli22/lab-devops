from django.contrib import admin

from django.urls import path

from portal.views import home

 

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', home, name='home'), # La racine du site

]

from portal.views import home , trigger_error

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('sentry-debug/', trigger_error, name='sentry_debug'),

]

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('sentry-debug/', trigger_error),
    # ...
]
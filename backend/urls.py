from django.conf.urls import url
from django.contrib import admin

from . import views


urlpatterns = [
    # Admin UI
    url(r'^admin/', admin.site.urls),

    # Home (landing page)
    url(r'^$', views.Home.as_view(), name='home'),
]

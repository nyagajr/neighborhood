from django.conf.urls import url
from . import views

urlpatterns = [
    url('home', views.welcome, name = 'welcome'),
    url(r'^$',views.signup, name='sign')
]
# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

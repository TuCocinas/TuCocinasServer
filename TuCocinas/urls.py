from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin

api_patterns = [
	url(r'^receta/', include('TuCocinas.apps.receta.urls')),
	url(r'^usuario/', include('TuCocinas.apps.users.urls')),
	url(r'^base/', include('TuCocinas.apps.base.urls')),
]

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	url(r'^api/', include(api_patterns)),
]

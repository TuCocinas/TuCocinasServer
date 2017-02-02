from django.conf.urls import url, include
from django.contrib import admin

api_patterns = [
	url(r'^receta/', include('TuCocinas.apps.receta.urls')),
]

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	url(r'^api/', include(api_patterns)),
]

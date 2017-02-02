from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.shortcuts import render

class JSONResponse(HttpResponse):

	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)
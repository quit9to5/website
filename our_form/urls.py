from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
	# similarly another pages for form can be created
]

from django.conf.urls import url

from . import views

urlpatterns = [	
	# ex: /polls/
	url(r'^$',views.home, name='home'),
]

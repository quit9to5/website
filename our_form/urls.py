from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
    url(r'^about-us/', views.aboutus,name='aboutus'),
    url(r'^contact/', views.contact, name='contact'),
	# similarly another pages for form can be created
]

from django.conf.urls import urls

from.views import HeroesView


urlpatterns = [
	url(r'^/heroes', HeroesView.as_view(), name='heroes_list')
]
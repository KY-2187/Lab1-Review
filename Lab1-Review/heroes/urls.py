from django.conf.urls import url

from.views import HeroesView, JesterView


urlpatterns = [
	url(r'^/heroes', HeroesView.as_view(), name='heroes_list')
	url(r'^/hero/jester', JesterView.as_view(), name='jester_detail')
]


from django.contrib.auth.decorators import permitions_requered
from news.views import NewsListView, NewsDetailVie, NewsCreate, NewsUpdate, NewsDelete

urlpatterns = [
	url(r'^$', NewsListView.as_view(), name = "news_index"),
	url(r'^(?P<pk>\d+)/detail/$', NewsDetailView.as_view(), name = "news_detail"),
	url(r'^add/$', permission_required ('news.add_news'), NewsCreate.as_view(), name = "news_add"),
	url(r'^(?P<pk>\d+)/edit/$', permission_required ('news.change_news'), 
		NewsUpdate.as_view(), name = "news_edit"),
	url(r'^(?P<pk>\d+)/delete/$', permission_required ('news.delete_news'), 
		NewsDelete.as_view(), name = "news_delete"),
	]
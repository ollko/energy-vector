# coding=utf-8
from django.conf.urls import url
from . import views 


app_name = 'company'
urlpatterns = [

    url(r'^sro/$', views.SroView.as_view(), name='sro',),

    url(r'^certificates/$', views.CertificateList.as_view(), name='certificates'),

    url(r'^certificates_new/$', views.certificates_new, name='certificates_new'),
    url(r'^certificate_list_del/$', views.certificate_list_del, name='certificate_list_del'),


    url(r'^otzivi/$', views.OtzivList.as_view(), name='otzivi'),
    url(r'^otzivi_new/$', views.otziv_new, name='otziv_new'),
    url(r'^otziv_corr/$', views.OtzivCorr.as_view(), name='otziv_corr'),
    url(r'^otziv_corr/(?P<otziv_id>\d+)/$', views.otziv_corr_detail, name='otziv_corr_detail'),
    url(r'^otziv_del/$', views.otziv_list_del, name='otziv_del'),

    url(r'^documents/$', views.DocumentsView.as_view(),),

    url(r'^contacts/$', views.ContactsView.as_view(),),

]
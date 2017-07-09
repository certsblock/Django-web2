#coding=utf-8
from django.conf.urls import url
from django.views.generic import TemplateView
from app import views

urlpatterns = [
   # url(r'^index/$',views.index, name="index"),
    url(r'^(index.html){0,1}$', TemplateView.as_view(template_name="app/index.html")),
    url(r'^about.html/$', TemplateView.as_view(template_name='app/about.html')),
    url(r'^guide/index.html$', TemplateView.as_view(template_name='guide/index.html')),
    url(r'^guide/faq.html$', TemplateView.as_view(template_name='guide/faq.html')),
    url(r'^guide/quick-start.html$', TemplateView.as_view(template_name='guide/quick-start.html')),
    url(r'^guide/recipient_experience.html$', TemplateView.as_view(template_name='guide/recipient_experience.html')),
    url(r'^guide/standard.html$', TemplateView.as_view(template_name='guide/standard.html')),
    url(r'^guide/roadmap.html$', TemplateView.as_view(template_name='guide/roadmap.html')),
    url(r'^guide/verification-process.html$', TemplateView.as_view(template_name='guide/verification-process.html')),
    url(r'^indexw.html$', TemplateView.as_view(template_name='app/indexw.html'))

]


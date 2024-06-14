from django.urls import path
from portfolio.views import *

app_name = 'portfolio'


urlpatterns = [
    path('', portfolio_view, name='index'),
    path('project-image', projectimage_view, name='image'),
    path('project-slideshow', projectslideshow_view, name='slideshow'),

]
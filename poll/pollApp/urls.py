from django.urls import path
from . import views

#app_name = 'pollApp'

urlpatterns = [
    # ex: /pollApp/
    path('', views.index, name='index'),
    # ex: /pollApp/results/
    path('results/', views.results, name='results'),
    # ex: /pollApp/vote/
    path('vote/', views.vote, name='vote'),

]

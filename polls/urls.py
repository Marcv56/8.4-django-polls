from django.urls import path

from . import views

app_name ='polls'

urlpatterns = [
    # these are the urls for each "view" to be displayed
    path('', views.IndexView.as_view(), name='index'),
    # index is the main view that shows the questions
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # Detail view shows the questions and the bouttons for voting
	path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # this will show the results for what the user selected
	path('<int:question_id>/vote/', views.vote, name='vote'),
    # this gives the ability to vote
]

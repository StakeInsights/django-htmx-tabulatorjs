from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    
    # ex: /polls/crud/
    path("crud/",views.crud, name="crud"),

    path('get_question_list/', views.get_question_list, name='get_question_list'), #new

    path('add_question/', views.add_question, name='add_question'), #new
    path('cancel_add_question/', views.cancel_add_question, name='cancel_add_question'), #new
    path('<int:question_id>/delete_question', views.delete_question, name='delete_question'),
    path('<int:question_id>/edit_question', views.edit_question, name='edit_question'), #new 
    path('<int:question_id>/edit_question_submit', views.edit_question_submit, name='edit_question_submit'), #new
]

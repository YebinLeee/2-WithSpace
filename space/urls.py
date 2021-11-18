from django.urls import path
from . import views

urlpatterns = [
   path('', views.main, name='main'),
   path('main', views.main, name='main'),
   path('register', views.register, name='register'),
   path('space/<str:id>', views.space, name='space'),
   path('space/book/<str:id>', views.book, name='book'),
   path('host_booking_list', views.host_booking_list, name='host_booking_list'),
   path('booking_list', views.booker_booking_list, name='booker_booking_list'),
   path('header', views.header, name='header'),
   
   # review
   path('create_review/<str:id>', views.create_review, name="create_review"),
   
   # question
   path('create_question/<str:id>', views.create_question, name="create_question"),
   path('create_question/<str:space_id>/<str:question_id>', views.create_answer, name="create_answer"),
]

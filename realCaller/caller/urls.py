from django.urls import path
from . import views



urlpatterns = [
     path('user-registration/', views.user_registration, name='user-registration'),
     path('report/',views.report_spam,name='report_spam'),
     path('search-person-by-name/', views.search_person_by_name, name='search_person_by_name'),
     path('search-person-by-number/',views.search_person_by_phone,name='search-person-by-number')
]
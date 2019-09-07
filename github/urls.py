from . import views
from django.urls import path
app_name='github'

urlpatterns=[path('user',views.get,name='user'),
path('submit',views.submit,name='submit')
]
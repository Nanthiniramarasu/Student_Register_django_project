from django.contrib import admin
from django.urls import path
from Myapplication import views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Authentication
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # CRUD / Dashboard
    path('', views.home, name='Home'),  # Dashboard with table + form
    path('add-data/', views.addData, name='addData'),
    path('update-data/<int:id>/', views.updateData, name='updateData'),
    path('delete-data/<int:id>/', views.deleteData, name='deleteData'),
]



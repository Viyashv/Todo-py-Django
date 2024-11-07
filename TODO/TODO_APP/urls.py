from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('login/', login_user, name="login"),
    path('signup/', signup_user, name="signup"),
    path('logout/', logout_user, name="logout"),
    path('edit/<int:id>', edit, name="edit"),
    path('delete/<int:id>', delete_task, name="delete"),
    # path('update/<int:id>', update_name, name="update"),
    path('cancel/<int:id>', cancel, name="cancel"),
    # path('taskName' , taskName , name='taskname')
]

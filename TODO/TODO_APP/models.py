from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TODO(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    todo_name = models.CharField(max_length= 200)
    status = models.BooleanField(default=False)

    def __str__(self):
        return "Id :-"+str(self.id)+ " "+"user :-" + str(self.user)+" "+"Task Name:-"+" "+str(self.todo_name)

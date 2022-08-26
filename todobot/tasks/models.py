from django.db import models

# Create your models here.

class task(models.Models):
    task_name = models.CharField(max_field=200, blank=True )
    description = models.TextField()
    completed = models.BoolenField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(on_delete=models.CASCADE)

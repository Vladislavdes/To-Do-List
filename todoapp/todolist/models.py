from django.db import models


class ToDo(models.Model):
    title = models.CharField('The name of task', max_length=255)
    is_complete = models.BooleanField('Completed')
    
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        
    def __str__(self):
        return self.title
# Create your models here.

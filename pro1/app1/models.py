from django.db import models

# Create your models here.
class Food(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return f'{self.id}--{self.title}--{self.description}--{self.completed}--{self.created_at}--{self.updated_at}'
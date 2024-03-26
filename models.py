from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('added', 'Добавлено'),
        ('in_progress', 'В работе'),
        ('done', 'Выполнено'),
    ])

    def __str__(self):
        return self.name

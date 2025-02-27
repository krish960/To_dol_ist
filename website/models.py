from django.db import models

# Create your models here.

CHOICES = [
    ('HIGH', 'HIGH'),
    ('LOW', 'LOW'),
    ('MEDIUM', 'MEDIUM')
]


class Task(models.Model):

    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    expiry_date = models.DateField()
    priority = models.CharField(choices=CHOICES, default='HIGH', max_length=20)

    def  __repr__(self):
        return self.name
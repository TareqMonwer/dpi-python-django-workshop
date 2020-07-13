from django.db import models
from django.urls import reverse


class Plan(models.Model):
    LABELS = (
        ('t', 'Top'),
        ('m', 'Medium'),
        ('l', 'Low')
    )

    plan_name = models.CharField(max_length=255)
    time_starts = models.DateTimeField()
    time_ends = models.DateTimeField()
    label = models.CharField(choices=LABELS, 
                             default='m',
                             max_length=1)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.plan_name

    def get_absolute_url(self):
        return reverse('details', args=[str(self.id)])
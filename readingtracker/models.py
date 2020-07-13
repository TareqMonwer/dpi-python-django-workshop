from django.db import models


class Plan(models.Model):
    LABELS = (
        ('t', 'Top'),
        ('m', 'Medium'),
        ('l', 'Low')
    )

    plan_name = models.CharField(max_length=255)
    time_starts = models.DateField()
    time_ends = models.DateField()
    label = models.CharField(choices=LABELS, 
                             default='m',
                             max_length=1)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.plan_name

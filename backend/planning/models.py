from django.db import models
from dishes.models import Dish

class DayPlan(models.Model):
    DAY_CHOICES = [
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday'),
    ]

    day = models.CharField(
        max_length=3,
        choices=DAY_CHOICES,
        unique=True
    )

    def __str__(self):
        return self.get_day_display()


class DayPlanDish(models.Model):
    day_plan = models.ForeignKey(
        DayPlan,
        on_delete=models.CASCADE,
        related_name='dishes'
    )
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('day_plan', 'dish')

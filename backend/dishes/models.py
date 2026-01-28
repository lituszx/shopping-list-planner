from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    unit = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DishIngredient(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

    class Meta:
        unique_together = ('dish', 'ingredient')

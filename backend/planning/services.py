from collections import defaultdict
from dishes.models import DishIngredient
from .models import DayPlan

def generate_shopping_list():
    result = defaultdict(float)

    # Traemos todos los días con sus platos
    day_plans = DayPlan.objects.prefetch_related('dishes__dish')

    for day_plan in day_plans:
        for day_dish in day_plan.dishes.all():
            ingredients = DishIngredient.objects.filter(dish=day_dish.dish)

            for item in ingredients:
                key = f"{item.ingredient.name} ({item.ingredient.unit})"
                result[key] += item.quantity

    return dict(result)

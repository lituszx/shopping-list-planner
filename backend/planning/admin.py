from django.contrib import admin
from .models import DayPlan, DayPlanDish

class DayPlanDishInline(admin.TabularInline):
    model = DayPlanDish
    extra = 1

@admin.register(DayPlan)
class DayPlanAdmin(admin.ModelAdmin):
    inlines = [DayPlanDishInline]

from django.contrib import admin

# Register your models here.
from .models import Product,Ingredient
class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 2


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['pname','pdesc']}),
        # (None,               {'fields': ['pdesc']}),
        ('Date information', {'fields': ['pdate'], 'classes': ['collapse']}),
    ]
    inlines = [IngredientInline]
    list_display = ('pname', 'pdesc', 'pdate', 'was_published_recently')
    list_filter = ['pdate']
    search_fields = ['pname']

admin.site.register(Product,ProductAdmin)
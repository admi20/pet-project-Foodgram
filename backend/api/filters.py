import django_filters
from rest_framework.filters import SearchFilter

from recipes.models import Recipe, Tag


class IngredientFilter(SearchFilter):
    search_parameter = 'name'


class RecipeFilter(django_filters.FilterSet):
    author = django_filters.CharFilter()
    tags = django_filters.ModelMultipleChoiceFilter(
        field_name='tags__slug',
        queryset=Tag.objects.all(),
        label='Tags',
    )
    is_favorite = django_filters.BooleanFilter(method='get_favorite')
    is_in_cart = django_filters.BooleanFilter(method='get_is_in_cart')

    class Meta:
        model = Recipe
        fields = [
            'tags',
            'author',
            'is_favorite',
            'is_in_cart'
        ]

    def get_favorite(self, queryset, name, value):
        if value:
            return queryset.filter(favorites__user=self.request.user)
        return queryset

    def get_is_in_cart(self, queryset, name, value):
        if value:
            return queryset.filter(cart__user=self.request.user)
        return queryset

from django.core.validators import MinValueValidator
from django.db import models
from users.models import User
from django.db.models import UniqueConstraint


class Tag(models.Model):
    """Базовая модель тег"""

    name = models.CharField('Название цвета',
                            unique=True,
                            max_length=200,)
    color = models.CharField('Цветовой HEX-код',
                             unique=True,
                             max_length=7)
    slug = models.SlugField('Slug',
                            max_length=200,
                            unique=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Базовая модель ингридиент"""
    name = models.CharField(max_length=200,
                            verbose_name='Название ингридиента',
                            )
    quantity = models.CharField('Количество',
                                max_length=200)
    measurement_unit = models.CharField('Единицы измерения',
                                        max_length=200)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Базовая модель рецепт"""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipy',
        verbose_name='Автор публикации'
    )

    name = models.CharField(max_length=256,
                            verbose_name='Категория',)

    image = models.ImageField(
        'Изображение',
        upload_to='recipes/images/'
    )

    text = models.TextField(
        'Описание рецепта',
        help_text='Введите описание рецепта'
    )

    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        verbose_name='Ингредиенты'
    )

    tags = models.ManyToManyField(
        Tag,
        through='RecipeTag',
        verbose_name='Теги',
        related_name='tags'
    )

    cooking_time = models.PositiveIntegerField(
        verbose_name='Время приготовления',
        validators=[MinValueValidator(
            1, message='Время приготовления должно быть не менее 1 минуты!'
        )]
    )

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    """ Модель ингредиентов в рецепте """

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Ингредиент'
    )
    amount = models.IntegerField(
        'Количество',
        validators=[MinValueValidator(1)]
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='recipe_ingredient_unique'
            )
        ]


class RecipeTag(models.Model):
    """ Модель связи тега и рецепта. """

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт'
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        verbose_name='Тег'
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['recipe', 'tag'],
                name='recipe_tag_unique'
            )
        ]


class ShoppingCart(models.Model):
    """ Модель корзиныlsls """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='shopping_cart',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name='shopping_cart',
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['user', 'recipe'],
                name='user_shoppingcart_unique'
            )
        ]


class Favorite(models.Model):
    """ Модель избранного. """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='favorites',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name='favorites',
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['user', 'recipe'],
                name='user_favorite_unique'
            )
        ]

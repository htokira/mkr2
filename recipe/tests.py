from django.test import TestCase
from django.urls import reverse
from .models import Category, Recipe

class RecipeViewsTestCase(TestCase):
    def setUp(self):
        self.category_soups = Category.objects.create(name="Супи")
        self.category_desserts = Category.objects.create(name="Десерти")

        self.recipes = []
        for i in range(12):
            recipe = Recipe.objects.create(
                title=f"Рецепт {i}",
                description=f"Опис {i}",
                instructions=f"Інструкції {i}",
                ingredients=f"Інгредієнти {i}",
                category=self.category_soups if i < 6 else self.category_desserts
            )
            self.recipes.append(recipe)

    def test_main_view_status_and_template(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertIn('recipes', response.context)

    def test_main_view_returns_max_ten_recipes(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(len(response.context['recipes']), 10)


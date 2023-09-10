from django.test import TestCase
from restaurant.models import MenuItem


class MenuItemTest(TestCase):
    def test_menu_item_creation(self):
        # Create a new MenuItem instance
        menu_item = MenuItem.objects.create(
            title="Beef Pasta",
            price=0.21,
            inventory=4
        )

        # Query the database to retrieve the created instance
        saved_menu_item = MenuItem.objects.get(pk=menu_item.pk)

        # Assertions to check if the instance was saved correctly
        self.assertEqual(saved_menu_item.title, "Beef Pasta")
        self.assertEqual(saved_menu_item.price, 0.21)
        self.assertEqual(saved_menu_item.inventory, 4)




# class MenuItemTest(TestCase):

#   def test_get_item(self):
#     item = MenuItem.objects.create(title="Beef Pasta", price=0.21, inventory=4)
#     self.assertEqual(item, "Beef Pasta : 0.21")

from django.test import TestCase
from lists.models import Item, ItemList


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class ItemAndListModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        item_list = ItemList()
        item_list.save()

        first_item = Item()
        first_item.text = 'The first list item'
        first_item.list = item_list
        first_item.save()

        second_item = Item()
        second_item.text = 'The second item'
        second_item.list = item_list
        second_item.save()

        saved_list = ItemList.objects.first()
        self.assertEqual(saved_list, item_list)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first list item')
        self.assertEqual(first_saved_item.list, item_list)
        self.assertEqual(second_saved_item.text, 'The second item')
        self.assertEqual(second_saved_item.list, item_list)


class ListViewTest(TestCase):

    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_all_items(self):
        item_list = ItemList.objects.create()
        Item.objects.create(text='itemey 1', list=item_list)
        Item.objects.create(text='itemey 2', list=item_list)

        response = self.client.get('/lists/the-only-list-in-the-world/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')


class NewListTest(TestCase):

    def test_can_save_a_post_request(self):
        self.client.post('/lists/new', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirect_after_post(self):
        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
        self.assertRedirects(response, '/lists/the-only-list-in-the-world/')

from django.test import TestCase
from lists.models import Item, List


class HomePageTest(TestCase):
    class ListViewTest(TestCase):


<<<<<<< HEAD
<<<<<<< HEAD
        class ListAndItemModelsTest(TestCase):
=======
    def test_can_save_a_POST_request(self):
        self.client.post('/', data={'item_text': 'A new list item'})
=======
    def test_can_save_a_POST_request(self):
        self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

>>>>>>> parent of 36ad968... URLs for forms x2, moved code in views + tests, new URL

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

>>>>>>> parent of 36ad968... URLs for forms x2, moved code in views + tests, new URL

            def test_saving_and_retrieving_items(self):
                list_ = List()
                list_.save()

                first_item = Item()
                first_item.text = 'The first (ever) list item'
                first_item.list = list_
                first_item.save()

                second_item = Item()
                second_item.text = 'Item the second'
                second_item.list = list_
                second_item.save()

                saved_list = List.objects.first()
                self.assertEqual(saved_list, list_)

                saved_items = Item.objects.all()
                self.assertEqual(saved_items.count(), 2)

                first_saved_item = saved_items[0]
                second_saved_item = saved_items[1]
                self.assertEqual(first_saved_item.text, 'The first (ever) list item')
                self.assertEqual(first_saved_item.list, list_)
                self.assertEqual(second_saved_item.text, 'Item the second')
                self.assertEqual(second_saved_item.list, list_)

<<<<<<< HEAD
        class ListViewTest(TestCase):

            def test_uses_list_template(self):
                response = self.client.get('/lists/the-only-list-in-the-world/')
                self.assertTemplateUsed(response, 'list.html')

            def test_displays_all_items(self):
                    list_ = List.objects.create()
                    Item.objects.create(text='itemey 1')
                    Item.objects.create(text='itemey 2')

                    response = self.client.get('/lists/the-only-list-in-the-world/')

<<<<<<< HEAD
                    self.assertContains(response, 'itemey 1')
                    self.assertContains(response, 'itemey 2')

        class NewListTest(TestCase):

            def test_can_save_a_POST_request(self):
                self.client.post('/lists/new', data={'item_text': 'A new list item'})
                self.assertEqual(Item.objects.count(), 1)
                new_item = Item.objects.first()
                self.assertEqual(new_item.text, 'A new list item')

            def test_redirects_after_POST(self):
                response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
                self.assertRedirects(response, '/lists/the-only-list-in-the-world/')
=======
            self.assertContains(response, 'itemey 1')
            self.assertContains(response, 'itemey 2')
>>>>>>> parent of 36ad968... URLs for forms x2, moved code in views + tests, new URL
=======
            self.assertContains(response, 'itemey 1')
            self.assertContains(response, 'itemey 2')
>>>>>>> parent of 36ad968... URLs for forms x2, moved code in views + tests, new URL

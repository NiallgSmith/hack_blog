from django.test import TestCase
from django.shortcuts import render_to_response
from blog.views import post_list,new_post,edit_post
from django.core.urlresolvers import resolve

# Create your tests here.
class SimpleTest(TestCase):
    def test_add_two_nums(self):
        self.assertAlmostEqual(1,1)

class HomePageTest(TestCase):
    def test_home_page_loads(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, post_list)

    def test_home_page_status_code(self):
        home_page = self.client.get('/')
        self.assertEqual(home_page.status_code,200)

    def test_check_homepage_content(self):
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, "base.html")
        home_page_template = render_to_response("blogposts.html").content
        self.assertEqual(home_page.content, home_page_template)

class newPostTest(TestCase):
    def test_new_page_loads(self):
        new_post_page = resolve('/post/new')
        self.assertEqual(new_post_page.func, new_post)

class editPostTest(TestCase):
    def test_edit_page_loads(self):
        edit_post_page = resolve('/blog/20/edit')
        self.assertEqual(edit_post_page.func, edit_post)

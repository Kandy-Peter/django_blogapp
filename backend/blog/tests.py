from importlib.resources import contents
from unicodedata import category
from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category

class Test_Create_Post(TestCase):
  @classmethod
  def setUpTestData(cls):
    test_category = Category.objects.create(name='django')
    test_user = User.objects.create_user(
      username='kamuntu', password='12345678'
    )
    test_post = Post.objects.create(
      category_id=1, title='Post test title', excerpt='My new post for all', content='lorem ipsum lorem ipsum lorem ipsum',
      slug='post_title', author_id=1, status='published'
    )

  def test_blog_content(self):
    post = Post.postobjects.get(id=1)
    categ = Category.objects.get(id=1)
    author = f"{post.author}"
    excerpt = f"{post.excerpt}"
    title = f"{post.title}"
    content = f"{post.content}"
    status = f"{post.status}"
    self.assertEqual(author, 'kamuntu')
    self.assertEqual(title, 'Post test title')
    self.assertEqual(content, 'lorem ipsum lorem ipsum lorem ipsum')
    self.assertEqual(status, 'published')
    self.assertEqual(str(post), 'Post test title')
    self.assertEqual(str(categ), 'django')

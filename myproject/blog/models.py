from django.db import models

class PublishedPostManager(models.Manager):
    def published(self):
        return self.filter(published_date__isnull=False)

    def by_author(self, author_name):
        return self.filter(author=author_name)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    published_date = models.DateTimeField(null=True, blank=True)
    objects = PublishedPostManager()

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)
    posts = models.ManyToManyField(Post, related_name="categories")

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'


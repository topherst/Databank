from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class NotePost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    subject = models.CharField(max_length=200, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="note_posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


from PIL import Image
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/users/', default='default/avatar.png')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.avatar:
            avatar_path = self.avatar.path
            with Image.open(avatar_path) as img:
                width, height = img.size
                if width != height:
                    new_dimension = min(width, height)
                    left = (width - new_dimension) / 2
                    top = (height - new_dimension) / 2
                    right = (width + new_dimension) / 2
                    bottom = (height + new_dimension) / 2
                    img = img.crop((left, top, right, bottom))

                img.save(avatar_path)

    def __str__(self):
        return self.username

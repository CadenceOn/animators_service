from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLES = (('parent', 'Parent'), ('animator', 'Animator'))
    role = models.CharField(max_length=10, choices=ROLES)

    # Укажем уникальные related_name для полей groups и user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='animators_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='animators_user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.username

class Request(models.Model):
    description = models.TextField()
    date = models.DateTimeField()
    status = models.CharField(max_length=20, default='pending')
    parent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')
    animator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assigned_requests')

    def __str__(self):
        return f"Заявка от {self.parent} на {self.date}"
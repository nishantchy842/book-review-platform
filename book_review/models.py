from typing import Iterable
from django.db import models
from django.contrib.auth.hashers import make_password
import uuid

class BaseModel(models.Model):
    idx = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
        

class UserModel(BaseModel):
    ADMIN = 'Admin'
    USER = 'User'
    CHOICE = (
        (ADMIN, 'Admin'),
        (USER, 'User')
    )
    
    
    name = models.CharField(max_length=1024)
    email = models.EmailField(unique=True)  
    role = models.CharField(max_length=50, choices=CHOICE, default=ADMIN)  
    password = models.CharField(max_length=255)
    
    @property
    def is_authenticated(self):
        return True
    
    def save(self, *arg, **kwargs) -> None:
        user = UserModel.objects.filter(pk=self.pk).first()
        if not user:
            self.password = make_password(self.password)
            return super().save(*arg, **kwargs)
        password_changed = self.password != user.password
        if not password_changed:
            return super().save(*arg, **kwargs)
        return super().save( *arg, **kwargs)   
    
    def __str__(self) -> str:
        return self.name
        
        
class Books(BaseModel):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField()
    language = models.CharField(max_length=225)
    created_by = models.ForeignKey(UserModel,related_name='created_books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Review(BaseModel):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    review_text = models.TextField()
    created_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'Review by {self.created_by} on {self.book}'    
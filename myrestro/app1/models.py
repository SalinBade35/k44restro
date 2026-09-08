from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

category_items = (
    ('veg', 'veg'),
    ('chicken', 'chicken'),
    ('buf', 'buf')
)

# first: x,a: stored in db
# second:y,b: label

class Momo(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(choices=category_items, max_length=100)
    images = models.ImageField(upload_to='images')
    price = models.DecimalField(max_digits=10, decimal_places=2)




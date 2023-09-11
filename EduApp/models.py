from django.db import models
from ckeditor.fields import RichTextField
from datetime import date

# Create your models here.

class category(models.Model):
    name=models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/Category/")
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    pro_image = models.ImageField(upload_to="images/Product/")
    Duration=models.CharField(max_length=100, default="")
    startDate = models.DateField()

    
    def __str__(self):
        return self.name    
    

class ProductDetails(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    description = RichTextField()
    features = RichTextField()
    requirement = RichTextField()
    duration = models.TextField()
    # stock = models.PositiveIntegerField()
    def _str_(self):
        return self.product.name    





class enquiry(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()    
    user_contact = models.CharField(max_length=10)
    user_course = models.CharField(max_length=100)
    message = models.CharField(max_length=100 )
    
    
# class registration(models.Model):
#     new_name = models.CharField(max_length=100)
#     new_email = models.CharField(max_length=100)
#     new_phone= models.CharField(max_length=100)
#     new_pass = models.CharField(max_length=100)
    
# class login(models.Model):
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100);    


class Addmission_user(models.Model):
    course= models.ForeignKey(Product, on_delete=models.CASCADE)
    firstname=models.CharField(max_length=100, default="")
    lastname=models.CharField(max_length=100, default="")
    email=models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=100, default="")
    d_o_b = models.DateField()
    address = models.CharField(max_length=100, default="")
    gender = models.CharField(max_length=100, default="")
    qualfication= models.CharField(max_length=100, default="")
    work_experience= models.CharField(max_length=100, default="")
    course_price = models.FloatField(default="")
    # duration= models.CharField(max_length=100)
    # Start_date= models.DateField()
    # payment=models.FloatField()
    Documents = models.FileField()
    Information = models.CharField(max_length=100,default="")
    
class Payment(models.Model):
   amount=models.FloatField(default="")
   description=models.CharField(max_length=100, default="")
      
    
    
class TopCourses(models.Model):
    products = models.ForeignKey(category, on_delete=models.CASCADE, )
    course = models.CharField(max_length=100, )
    Duration=models.CharField(max_length=100, )
    startDate = models.DateField()
    product_img = models.ImageField(upload_to="images/TopProducts/")
    
    
class Blog(models.Model):
    Blog_name= models.CharField(max_length=100)
    auther = models.CharField(max_length=100)    
    

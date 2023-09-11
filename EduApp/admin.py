from django.contrib import admin
from .models import category, Product, ProductDetails,enquiry, Addmission_user,Payment, TopCourses, Blog

# Register your models here.

@admin.register(category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","image")
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =('name','category','price','pro_image')    
    
    
@admin.register(ProductDetails)
class ProductDetailsAdmin(admin.ModelAdmin):
    list_display=('product','description','features','requirement','duration')
    


    
@admin.register(enquiry)
class enquiryAdmin(admin.ModelAdmin):
    list_display=('user_name','user_email','user_contact','user_course','message')    
    
    
@admin.register(Addmission_user)
class Addmission_userAdmin(admin.ModelAdmin):
    list_display= ('course','firstname','lastname','email','phone','d_o_b','address','gender','qualfication','work_experience','course_price','Documents','Information',)    
    
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('amount','description')    
    
    
@admin.register(TopCourses)
class TopCoursesAdmin(admin.ModelAdmin):
    list_display =('products','course','Duration','startDate','product_img')
         
        
         
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=('Blog_name','auther')            
            
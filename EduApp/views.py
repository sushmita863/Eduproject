from pyexpat.errors import messages
from django.shortcuts import render,redirect
from .models import category,Product,ProductDetails,enquiry,Addmission_user, TopCourses,Payment
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LogoutView
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import HttpResponse
from .forms import RegisterForm
from django.conf import settings
import razorpay


def send_email_with_context(request):
    # Get the context data (example data, you can replace with your own)
    context = {
        'username': 'John Doe',
        'message': 'Welcome to our website!',
    }

    # Render the HTML email content using a template and context data
    html_message = render_to_string('email_template.html', context)
    plain_message = strip_tags(html_message)  # Strip HTML tags for the plain text version

    # Send the email using send_mail
    send_mail(
        'Welcome to Our Website',  # Email subject
        plain_message,  # Plain text version of the email (optional)
        'miniprojectg01@gmail.com',  # From email address
        ['sushgupta7512@gmail.com'],  # List of recipient email addresses
        html_message=html_message,  # HTML version of the email
    )

    # Add any further logic or return a response as needed
    return HttpResponse('Email sent successfully!')

# Create your views here.

class SearchResultsView(ListView):
    model = Product
    template_name = "search_result.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list =Product.objects.filter(name=query)
        return object_list


def home(request):
     cd=category.objects.all()
     topCourses = TopCourses.objects.all()
     return render(request, 'home.html',{'cd':cd, 'topCourses':topCourses})

def about(request):
    return render(request, 'about.html')


def contact(request):
    allproducts = Product.objects.all()
    if request.method=='POST':
        user_course= request.POST['course']
        username= request.POST['username']
        
        useremail = request.POST['useremail']
        
        userphone = request.POST['userphone']
        messages = request.POST['message']
        newuser= enquiry(user_course=user_course, user_name=username,user_email=useremail, user_contact=userphone, message=messages)
        newuser.save()
        return render(request, 'confirmation.html',{'product_title':user_course,'uname':username})
    return render(request, 'contact.html',{'allproducts':allproducts})


def product(request, id):
    if id:
        products = Product.objects.filter(category=id)
        categories = category.objects.get(id=id)
        return render(request,'product.html',{'products':products, 'categories':categories})
    return render(request, 'product.html')


def Product_desc(request, id): 
    if id:
        pro_desc = ProductDetails.objects.get(product=id)
    
            
        if pro_desc is None:
            return render(request,'confirmation.html')
        else:
            return render(request,'Product_desc.html',{'pro_desc':pro_desc})
    return render(request,'Product_desc.html')


# def enrollment(request, id):
#     if id:
#         product=ProductDetails.objects.get(id=id)
#         product_title = product.product
        
#     if request.method=='POST':
#         name= request.POST['fname']
        
#         email = request.POST['email']
        
#         phone = request.POST['mobile']
        
#         u1 = User(product_title=product_title, uname=name, email=email, phone=phone)
#         u1.save()
#         return render(request, 'confirmation.html',{'product_title':product_title,'uname':name})
#         # return redirect(confirmation)
#     return render(request,'enrollmentform.html',{'product':product})
    
    
def confirmation(request):
     return render(request,'confirmation.html' )    
 

def admission(request):
    allproducts = Product.objects.all()

    if request.method=="POST":
        course =request.POST['course']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        phone= request.POST['phone']
        dob=request.POST['dob']
        address= request.POST['address']
        gender=request.POST['gender']
        qualification=request.POST['Qualification']
        experience=request.POST['Experience']
        course_price=request.POST['courseprice']
        document=request.POST['document']
        information=request.POST['information']
        course_obj=Product.objects.get(name=course)

      
        add_success= Addmission_user(course=course_obj,firstname=firstname, lastname=lastname, email=email, phone=phone, d_o_b=dob, address=address, gender=gender, qualfication=qualification,work_experience=experience,course_price=course_price,Documents=document, Information=information)
        add_success.save()
        return redirect('payment')
    
        
        
    return render(request, 'addmission.html',{'allproducts':allproducts})


def registration(request):
   if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'registration.html', {'form': form})    
   if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('login')
        else:
            return render(request, 'registration.html', {'form': form})


def login(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                redirect_url = request.GET.get('next', '') 
                # Get the URL from the 'next' parameter
                return redirect(redirect_url) if redirect_url else redirect('home')
                return redirect(home)
            else: 
                form.add_error(None,"Invalid username and password")
                
    auth = AuthenticationForm()      
    
    return render(request, 'login.html',{'auth':auth})


def paymentProcess(request):
    if request.method == 'POST':
        form = Payment(request.POST)
        if form.is_valid():
            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

            amount = int(form.cleaned_data['amount'] * 100)  # Amount in paise
            description = form.cleaned_data['desc']

            # Create a Razorpay order
            order = client.order.create(dict(amount=amount, currency='INR'))
            print(order)

            return render(request, 'payment.html', {'order': order})
    else:
        form = Payment()

    return render(request, 'Payment.html', {'form': form})

def payment_success(request):
    # Handle successful payment logic here
    return render(request, 'payment/success.html')


def trainerProfile(request):
    return render(request, 'trainerProfile.html')

def email_template(request):
    return render(request, 'email_template.html')

def email(request):
    html_message = render_to_string('email_template.html')
    plain_message = strip_tags(html_message)
    
    send_mail(
        'welcome to Our Website',
        plain_message,
        'miniprojectg01@gmail.com',
        ['sushgupta805@gmail.com'],
        html_message=html_message,
    )
    return HttpResponse("Email sent successfully!")



def Searchresult(request):
    if request.method =="GET":
        query = request.GET.get("q")
        #  object_list = Product.objects.filter(name__icontains=query) or category.objects.filter(name__icontains=query)
        object_list = Product.objects.filter(name__icontains=query)
        return render(request, 'search_Result.html', {'object_list':object_list})
    return render(request, 'search_Result.html')
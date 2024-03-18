from django.db import models
from user.models import UserProfile,User
from multiselectfield import MultiSelectField
# Create your models here.
class blog_card(models.Model):
    blog_id = models.AutoField
    blog_title = models.CharField(max_length=100, default='Lucknow')
    blog_desc = models.CharField(max_length=20, default=' ')
    blog_image = models.ImageField(upload_to='media',default='')

    def __str__(self):
        return self.blog_title
    
class Category(models.Model):
    cat_id = models.AutoField
    cat_name = models.CharField(max_length=20)
    cat_image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.cat_id

CATEGORY_CHOICES = [
    ('Fabric','fabric'),
    ('Kurti','kurti'),
    ('Saree','saree')
]   
class Product(models.Model):
    productId = models.CharField(unique=True,primary_key=True,max_length=20)
    name = models.CharField(max_length=20, null=True)
    price = models.IntegerField(null=True)
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES)
    main_image = models.ImageField(upload_to='media')
    img1 = models.ImageField(upload_to='media',null=True)
    img2 = models.ImageField(upload_to='media',null=True)
    img3 = models.ImageField(upload_to='media',null=True)
    color = models.CharField(max_length=20,null=True,default=' ')
    fabrics = models.CharField(max_length=20,null=True,blank=True)
    embroidery = models.CharField(max_length=20,null=True,blank=True)
    embroidery_color = models.CharField(max_length=20,null=True,blank=True)
    washing_instrutions = models.CharField(max_length=100, null=True, blank=True)
    dyeing = models.CharField(max_length=50,null=True,blank=True)
    product_description = models.CharField(max_length=200,null=True,blank=True)
    keywords = models.CharField(max_length=100,null=True)
    in_stock = models.BooleanField(default=False)

    def __str__(self):
        return self.productId
    
    @property
    def imageURLmain(self):
        try:
            url = self.main_image.url
        except:
            url = ''
        return url
    
    @property
    def imageURL1(self):
        try:
            url1 = self.img1.url
        except:
            url1 = ''
        return url1
    
    @property
    def imageURL2(self):
        try:
            url2 = self.img2.url
        except:
            url2 = ''
        return url2
    
    @property
    def imageURL3(self):
        try:
            url3 = self.img3.url
        except:
            url3 = ''
        return url3

class Kurti(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    available_sizes = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.product.name
    
class Saree(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    available_sizes = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.product.name

class Fabric(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    available_sizes = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.product.name


class Bestseller(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,default=' ')

    def __str__(self):
        return self.product.name


PAYMENT_CHOICES = [
    ( 'Cash on Delivery','cash_on_delivery'),
    ('Pay Online','pay_online'),
]

ORDER_STATUS_CHOICES = [
    ('created', 'Created'),
    ('shipped', 'Shipped'),
    ('processed', 'Processed'),
    ('completed', 'Completed'),
]

class Order(models.Model):
    orderId = models.AutoField(unique=True, primary_key=True)
    customer = models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True)
    total = models.IntegerField(null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    contact_number = models.CharField(max_length=10,null=True)  # You can adjust the max length as needed
    address = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)
    zipcode = models.CharField(max_length=6,null=True)
    
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='created')

    tracking_company = models.CharField(max_length=100,null=True)
    tracking_Id = models.CharField(max_length=100,null=True)
    
    @property
    def get_payment_completed_status(self):
        if self.payment_method == 'credit_card' or 'upi' or 'debit_card':
            return 'Completed'
        elif self.payment_method == 'cash_on_delivery':
            return 'Not Completed'
    
    @property 
    def get_cart_total(self):
        orderitems = self.orderitems_set.all()
        total_amount = sum([item.get_item_total for item in orderitems])
        return total_amount


class OrderItems(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    quantity =  models.IntegerField(default=0, null=True)
    size_selected = models.CharField(max_length=20,default="",null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_item_total(self):
        total = self.product.price * self.quantity
        return total

class Bannerimg(models.Model):
    imgid = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='media',null=True)   
    
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
class StoryContent(models.Model):
    story_title = models.CharField(max_length=20,null=True)
    story_content = models.TextField(max_length=5000,null=True)
    stroy_image = models.ImageField(upload_to='media',null=True)

    def __str__(self):
        return self.story_title
    
    @property
    def imageURL(self):
        try:
            url = self.stroy_image.url
        except:
            url = ''
        return url
    

class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=20,null=True)
    privacy_content = models.TextField(max_length=5000,null=True)

    def __str__(self):
        return self.title
    

class ShippingPolicy(models.Model):
    title = models.CharField(max_length=20,null=True)
    shipping_content = models.TextField(max_length=5000,null=True)

    def __str__(self):
        return self.title
    

class TermsAndCondn(models.Model):
    title = models.CharField(max_length=20,null=True)
    terms_content = models.TextField(max_length=5000,null=True)

    def __str__(self):
        return self.title
    

class CancelRefund(models.Model):
    title = models.CharField(max_length=50,null=True)
    cancel_content = models.TextField(max_length=5000,null=True)

    def __str__(self):
        return self.title
    
class About(models.Model):
    title = models.CharField(max_length=50,null=True)
    about = models.TextField(max_length=1500,null=True)

    def __str__(self):
        return self.title
    
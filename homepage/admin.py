from django.contrib import admin
from . models import blog_card, Bestseller, Category, Order, OrderItems, Product
from . models import Kurti,Saree,Fabric,Bannerimg,StoryContent,PrivacyPolicy,ShippingPolicy,TermsAndCondn,CancelRefund,About
# Register your models here.

admin.site.register(blog_card)

admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('productId','category','name')
    list_filter = ['category']
admin.site.register(Product,ProductAdmin)

admin.site.register(About)

admin.site.register(Kurti)

admin.site.register(Saree)

admin.site.register(Fabric)

admin.site.register(Bestseller)

admin.site.register(Bannerimg)

admin.site.register(StoryContent)

admin.site.register(PrivacyPolicy)

admin.site.register(ShippingPolicy)

admin.site.register(TermsAndCondn)

admin.site.register(CancelRefund)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('orderId','customer','payment_method','order_status')  # Add other fields as needed
    list_filter = ['order_status','customer']  # Add a filter option for order status
    actions = ['mark_shipped', 'mark_processed', 'mark_completed']  # Custom actions

    def mark_shipped(self, request, queryset):
        queryset.update(order_status='shipped')

    def mark_processed(self, request, queryset):
        queryset.update(order_status='processed')

    def mark_completed(self, request, queryset):
        queryset.update(order_status='completed')

admin.site.register(Order, OrderAdmin)

class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ('id','product','order','quantity','size_selected','date_added')
    list_filter = ['order']
admin.site.register(OrderItems,OrderItemsAdmin)
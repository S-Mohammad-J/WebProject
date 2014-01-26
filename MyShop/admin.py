from django.contrib import admin

# Register your models here.
from MyShop.models import Section, SubSection, Merchant, Customer, Product, SlideshowProduct, Comment, Bill

class SectionAdmin(admin.ModelAdmin):
    search_fields = ["title"]

class SubSectionAdmin(admin.ModelAdmin):
    list_display = ("title","section")
    list_filter = ["title"]
    search_fields = ["title","section__title"]

class MerchantAdmin(admin.ModelAdmin):
    list_display = ("username","firstName","lastName","tel","email")
    search_fields = ["useranme","firstName","lastName","tel","email","address"]

class CustomertAdmin(admin.ModelAdmin):
    list_display = ("username","firstName","lastName","tel","email")
    search_fields = ["useranme","firstName","lastName","tel","email","address"]

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","price","score","createDate","subSection","merchant")
    search_fields = ["name","price","score","createDate","subSection__title","merchant__lastName","subSection__section__title"]

class SlideshowProductAdmin(admin.ModelAdmin):
    list_display = ("product","text")
    search_fields = ["product__name","product__price","product__score","product__createDate","product__subSection__title","text"]

class CommentAdmin(admin.ModelAdmin):
    list_display = ("content","customer","product")
    search_fields = ["content","customer__username","product__name"]

class BillAdmin(admin.ModelAdmin):
    list_display = ("customer","product")
    search_fields = ["customer__username","product__name"]

admin.site.register(Section,SectionAdmin)
admin.site.register(SubSection,SubSectionAdmin)
admin.site.register(Merchant,MerchantAdmin)
admin.site.register(Customer,CustomertAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(SlideshowProduct,SlideshowProductAdmin)
admin.site.register(Comment,CommentAdmin)
#TODO bill admin
admin.site.register(Bill)


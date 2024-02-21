from django.contrib import admin
from .models import *

class ItemImageInline(admin.TabularInline):  # หรือ admin.StackedInline ตามที่คุณต้องการ
    model = ItemImage
    extra = 1  # จำนวนฟอร์มเพิ่มเติมที่แสดงในหน้าแสดงรายละเอียดของ Item

class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImageInline]

admin.site.register(Item, ItemAdmin)
admin.site.register(UserProfile)
admin.site.register(Message)
admin.site.register(Payment)
admin.site.register(Order)

from django.contrib import admin
from .models import Contact,Product,OrderUpdate,Orders

# Register your models here.
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
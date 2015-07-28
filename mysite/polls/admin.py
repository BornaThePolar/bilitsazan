from django.contrib import admin
from .models import UserProfile,Event,Buy,Scorers,Likers,Comment,Order,Ticket,Category,SubCategory
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Event)
admin.site.register(Order)
admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Buy)
admin.site.register(Ticket)

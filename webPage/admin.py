from django.contrib import admin
from .models import Activeuser, Content, Privilege, Rule, Rulelist, Surfer
# Register your models here.
admin.site.register(Activeuser)
admin.site.register(Content)
admin.site.register(Privilege)
admin.site.register(Rule)
admin.site.register(Rulelist)
admin.site.register(Surfer)

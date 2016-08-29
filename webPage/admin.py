from django.contrib import admin
from .models import ActiveUser, Content, Privilege, Rule, Surfer, RuleList
# Register your models here.
admin.site.register(ActiveUser)
admin.site.register(Content)
admin.site.register(Privilege)
admin.site.register(Rule)
admin.site.register(Surfer)
admin.site.register(RuleList)

from django.contrib import admin

from quotes.models import Quote, Like


admin.site.register(Quote)
admin.site.register(Like)

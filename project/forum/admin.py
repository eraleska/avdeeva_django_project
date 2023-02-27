from django.contrib import admin
from .models import Themes
from .models import Authors
from .models import News

admin.site.register(Themes)
admin.site.register(Authors)
admin.site.register(News)

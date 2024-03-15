from django.contrib import admin
from .models import Home,About,Category,Skills,Portfolio,Profile


admin.site.register(Home)


class ProfileInLine(admin.TabularInline):
    model=Profile
    extra=1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [ ProfileInLine,]

class SkillsInLine(admin.TabularInline):
    model = Skills
    extra=2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ SkillsInLine,]

admin.site.register(Portfolio)


# Register your models here.

from django.contrib import admin
from .models import Article

# TabularInline  bu primary key bilan foreignkeyni bir biriga boglash uchun ishlatiladi
#


# class CommentInline(admin.TabularInline):
#     model = Comment
#     extra = 0
#
# class ArticleAdmin(admin.ModelAdmin):
#     inlines = [CommentInline]
admin.site.register(Article)
# admin.site.register(Comment)
from django.contrib import admin

from .models import Question, Option, Winner


class OptionAdmin(admin.StackedInline):
    model = Option
    extra = 0
    list_display = ('id', 'question', 'choice')
    fields = ('id', 'choice')
    readonly_fields = ('id',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        OptionAdmin
    ]
    list_display = ('id', 'question', 'answer')


@admin.register(Winner)
class WinnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'modified', 'name', 'image')
    list_filter = ('created', 'modified')
    search_fields = ('name',)


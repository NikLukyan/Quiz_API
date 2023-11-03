from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "question",
        "answer",
        "created_at",)
    search_fields = ("question",)
    list_filter = ("created_at",)


admin.site.register(Question)

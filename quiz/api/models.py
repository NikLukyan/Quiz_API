from django.db import models


class Question(models.Model):
    id = models.PositiveIntegerField('Question id', primary_key=True)
    question = models.TextField('Question')
    answer = models.TextField('Answer')
    created_at = models.DateTimeField('Created at')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.id

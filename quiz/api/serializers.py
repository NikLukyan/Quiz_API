from rest_framework import serializers


class QuestionSerializer(serializers.Serializer):
    # Описываем поля и их типы
    id = serializers.IntegerField()
    question = serializers.CharField()
    answer = serializers.CharField()
    created_at = serializers.TimeField()


class QuizSerializer(serializers.Serializer):
    questions_num = serializers.IntegerField()

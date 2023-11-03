from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Question


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = (
            "id",
            "question",
            "answer",
            "created_at",
        )


class QuizSerializer(serializers.Serializer):
    questions_num = serializers.IntegerField()

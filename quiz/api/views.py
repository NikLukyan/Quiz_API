from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

import requests

from api.serializers import QuizSerializer


class Question():
    def __init__(self, id, question, answer, created_at):
        self.id = id
        self.question = question
        self.answer = answer
        self.created_at = created_at


@csrf_exempt
@api_view(['POST'])
def get_question(request):
    if request.method == 'POST':
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            response = requests.get(
                'https://jservice.io/api/random?count='
                + str(serializer.data.get("questions_num")))
            response = response.json()
            return Response(response)
        return Response(serializer.errors)
    return Response("Bad request")

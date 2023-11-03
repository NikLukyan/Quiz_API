from rest_framework.decorators import api_view
from rest_framework.response import Response

import requests

from api.models import Question
from api.serializers import QuizSerializer


@api_view(['POST'])
def get_question(request):
    if request.method == 'POST':
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            response = requests.get(
                'https://jservice.io/api/random?count='
                + str(serializer.data.get("questions_num")))
            response = response.json()
            for item in response:
                while Question.objects.filter(id=item.get('id')):
                    new_responce = (
                        requests.get('https://jservice.io/api/random'))
                    new_responce = new_responce.json()
                    item = new_responce[0]
                Question.objects.create(
                    id=item.get('id'),
                    question=item.get('question'),
                    answer=item.get('answer'),
                    created_at=item.get('created_at'))
            return Response(item)
        return Response(serializer.errors)
    return Response("Bad request, only POST method is supported")

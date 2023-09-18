from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class API_DATA_INDEX(APIView):
    permission_classes = (IsAuthenticated,)             
    
    def get(self, request):
        content = [{'id': 1, 'title': 'index_page', 'keys':[{'key_0': '0', 'key1': 1}] }]
        return Response(content)
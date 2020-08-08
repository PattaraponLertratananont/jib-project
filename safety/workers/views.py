from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Worker
from .serializers import WorkerSerializer


# class-base view
class WorkerListView(APIView):
    def get(self, req):
        workers = Worker.objects.all()
        serializer = WorkerSerializer(workers, many=True)
        return Response(serializer.data)


# class WorkerModeViewSetView(viewsets.ModelViewSet):
#     queryset = Worker.objects.all()
#     serializer_class = WorkerSerializer

#     def create(self, request):
#         print(request.data)
#         return Response()

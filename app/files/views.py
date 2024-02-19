from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from files.models import File
from files.serializers import FileSerializer
from files.tasks import process_file_task


class FileViewSet(viewsets.ModelViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()

    def list(self, request):
        queryset = File.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"])
    def upload(self, request):
        file_serializer = self.serializer_class(data=request.data)
        file_serializer.is_valid(raise_exception=True)
        file_instance = file_serializer.save()
        process_file_task(file_instance.pk)

        return Response(file_serializer.data, status=status.HTTP_201_CREATED)

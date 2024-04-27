from rest_framework import generics
from schedulings.api.permissions import IsSuperUserOrReadOnly
from schedulings.models import Scheduling
from .serializers import SchedulingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User





class SchedulingListCreateView(generics.ListCreateAPIView):
    queryset = Scheduling.objects.all()
    serializer_class = SchedulingSerializer
    permission_classes = [IsSuperUserOrReadOnly]

    def post(self, request, *args, **kwargs):
        import ipdb; ipdb.set_trace()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            new_scheduling_start = serializer.validated_data['exam_start_date']
            new_scheduling_finish = serializer.validated_data['exam_finish_date']
            existing_schedules = Scheduling.objects.filter(user=serializer.validated_data.get('user', None))
            for existing_schedule in existing_schedules:
                if (new_scheduling_start < existing_schedule.exam_finish_date and
                        new_scheduling_finish > existing_schedule.exam_start_date):
                    return Response({"hata": "Öğrencinin dersleri çakışıyor."}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save(user=serializer.validated_data.get('user', None))
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SchedulingUpdateDeleteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Scheduling.objects.all()
    serializer_class = SchedulingSerializer
    permission_classes = [IsSuperUserOrReadOnly]


class ShowStudentSchedule(generics.ListAPIView):
    serializer_class = SchedulingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Scheduling.objects.filter(user=self.request.user)
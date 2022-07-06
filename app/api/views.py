from rest_framework.views import APIView
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import CourseSerializer
from ..models import Course


class ListCourses(APIView):
    authentication_classes = (BaseAuthentication,)
    permission_classes = (IsAdminUser, IsAuthenticated,)

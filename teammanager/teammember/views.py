from rest_framework import viewsets

from .models import TeamMember
from .serializers import TeamMemberSerializer


class TeamMemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows details of TeamMember to be viewed or edited.
    """
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

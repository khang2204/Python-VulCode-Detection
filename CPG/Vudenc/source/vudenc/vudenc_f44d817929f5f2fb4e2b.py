from django.db.models import Prefetch, Q
from django.shortcuts import get_object_or_404
from rest_framework import generics
from db.map.models import State, Municipality, Locality, Action, Organization, Establishment, Submission
from api.serializers import StateSerializer, MunicipalitySerializer
from api.serializers import LocalityDetailSerializer, LocalityRawSerializer, LocalitySearchSerializer
from api.serializers import EstablishmentSerializer, SubmissionSerializer
from api.serializers import ActionSubmissionsSerializer, ActionLogSerializer, ActionDetailSerializer
from api.serializers import OrganizationSerializer, OrganizationDetailSerializer
from api.paginators import LargeNoCountPagination
from api.throttles import SearchBurstRateScopedThrottle
from api.filters import ActionFilter, EstablishmentFilter, SubmissionFilter
serializer_class = StateSerializer
def get_queryset(self):...
return self.get_serializer_class().setup_eager_loading(State.objects.all())

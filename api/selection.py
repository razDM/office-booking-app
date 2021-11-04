from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from selection.models import Office, Zone, Floor
from offices.models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        exclude = []
        depth = 2


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        exclude = []
        depth = 1


class ZoneSerializer(serializers.ModelSerializer):
    floor = FloorSerializer()

    class Meta:
        model = Zone
        exclude = []
        depth = 1


class OfficeSerializer(serializers.ModelSerializer):
    zone = ZoneSerializer()
    reservation = ReservationSerializer(many=True, source='office')

    class Meta:
        model = Office
        exclude = []


class OfficeViewSet(viewsets.ModelViewSet):
    serializer_class = OfficeSerializer
    queryset = Office.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

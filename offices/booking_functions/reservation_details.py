from selection.models import Floor, Zone, Office
from offices.models import Reservation


def office_zone_details(id):
    office_details = Office.objects.get( id=id )
    zone_details = Zone.objects.filter( id=office_details.zone_id )
    return office_details, zone_details

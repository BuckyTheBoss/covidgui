from import_export import resources
from .models import CovidData

class CovidResource(resources.ModelResource):
    class Meta:
        model = CovidData

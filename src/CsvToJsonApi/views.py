from django.http import JsonResponse
from django.views import View
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.exceptions import ValidationError
from django.core.management import call_command
from CsvToJsonApi.models import WeatherData

class DataView(View):
    def get(self, request, *args, **kwargs):
        filters = {key: value for key, value in request.GET.items()}
        
        # Extract the 'limit' parameter and remove it from filters
        limit = int(request.GET.get('limit', 0))
        filters.pop('limit', None)

        # Filter data based on query parameters
        queryset = WeatherData.objects.all()
        for key, value in filters.items():
            # Check if the attribute exists in the model
            if hasattr(WeatherData, key):
                filter_kwargs = {key: value}
                queryset = queryset.filter(**filter_kwargs)
        
         # Apply limit to the queryset
        if limit > 0:
            queryset = queryset[:limit]

        data = list(queryset.values())
        return JsonResponse(data, safe=False)

class UploadCSVView(View):
    def post(self, request, *args, **kwargs):
        csv_file = request.FILES.get('csv_file')

        if csv_file:
            # Save the uploaded file
            file_path = default_storage.save(csv_file.name, ContentFile(csv_file.read()))

            # Call the management command to load data from the CSV file
            try:
                call_command('load_data', file_path)
                return JsonResponse({'message': 'Data loaded successfully.'})
            except ValidationError as e:
                return JsonResponse({'error': str(e)}, status=400)
        else:
            return JsonResponse({'error': 'No CSV file provided.'}, status=400)
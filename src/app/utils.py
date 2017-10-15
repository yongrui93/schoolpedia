def get_coordinate_from_request(request):
    latitude = ''
    longitude = ''
    try:
        latitude = request.GET['latitude']
        longitude = request.GET['longitude']
        has_coordinate = True
    except KeyError:
        has_coordinate = False
        pass
    return [latitude, longitude, has_coordinate]

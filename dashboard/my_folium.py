# to use google earth engine
import ee

# Import the folium library.
import folium
from folium import plugins
from folium.plugins.draw import Draw
from folium import IFrame

#utils
from . import utils
import base64
import os

from django.conf import settings
from .models import ImagePredictions

def getPrivateKey():
    service_account = 'fypPaddyMonitoringSystem@fyppaddymonitoring.iam.gserviceaccount.com'
    private_key = os.path.join(settings.BASE_DIR, 'assets', 'privatekey.json')
    credentials = ee.ServiceAccountCredentials(service_account, private_key)
    ee.Initialize(credentials)
    print('private key called!')

# Authenticate to use Google Earth
def getAuth():
    ## Trigger the authentication flow. You only need to do this once
    ee.Authenticate()

    # Initialize the library.
    ee.Initialize()

def getBaseMap():
    # Add custom basemaps to folium
    basemaps = {
        'Maps': folium.TileLayer(
            tiles='https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
            attr='Google',
            name='Maps',
            overlay=True,
            control=True
        ),
        'Satellite': folium.TileLayer(
            tiles='https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
            attr='Google',
            name='Satellite',
            overlay=True,
            control=True
        ),
        'Terrain': folium.TileLayer(
            tiles='https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',
            attr='Google',
            name='Terrain',
            overlay=True,
            control=True
        ),
        'Satellite Hybrid': folium.TileLayer(
            tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
            attr='Google',
            name='Satellite',
            overlay=True,
            control=True
        ),
        'Esri Satellite': folium.TileLayer(
            tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
            attr='Esri',
            name='Esri Satellite',
            overlay=True,
            control=True
        )
    }
    return basemaps


# Define a method for displaying Earth Engine image tiles on a folium map.
def add_ee_layer(self, ee_object, vis_params, name):
    try:
        # display ee.Image()
        if isinstance(ee_object, ee.image.Image):
            map_id_dict = ee.Image(ee_object).getMapId(vis_params)
            folium.raster_layers.TileLayer(
                tiles=map_id_dict['tile_fetcher'].url_format,
                attr='Google Earth Engine',
                name=name,
                overlay=True,
                control=True
            ).add_to(self)
        # display ee.ImageCollection()
        elif isinstance(ee_object, ee.imagecollection.ImageCollection):
            ee_object_new = ee_object.mosaic()
            map_id_dict = ee.Image(ee_object_new).getMapId(vis_params)
            folium.raster_layers.TileLayer(
                tiles=map_id_dict['tile_fetcher'].url_format,
                attr='Google Earth Engine',
                name=name,
                overlay=True,
                control=True
            ).add_to(self)
        # display ee.Geometry()
        elif isinstance(ee_object, ee.geometry.Geometry):
            folium.GeoJson(
                data=ee_object.getInfo(),
                name=name,
                overlay=True,
                control=True
            ).add_to(self)
        # display ee.FeatureCollection()
        elif isinstance(ee_object, ee.featurecollection.FeatureCollection):
            ee_object_new = ee.Image().paint(ee_object, 0, 2)
            map_id_dict = ee.Image(ee_object_new).getMapId(vis_params)
            folium.raster_layers.TileLayer(
                tiles=map_id_dict['tile_fetcher'].url_format,
                attr='Google Earth Engine',
                name=name,
                overlay=True,
                control=True
            ).add_to(self)

    except:
        print("Could not display {}".format(name))

#-------------polygon----------------------------------

# Add drawing polygon method to folium.
def addDrawPolygonFunction():
    drawItem = Draw(
        export=True,
        filename="my_data.geojson",
        position="topleft",
        draw_options={
            "polyline": True,
            "rectangle": False,
            "circle": False,
            "circlemarker": False,
        },
        edit_options={"poly": {"allowIntersection": False}},
    )

    return drawItem

# Method to create a custom polygon area with pop up
# TODO pending modification
def addCustomPolygon():
    # Create feature group to add to folium.Map object
    layer = folium.FeatureGroup(name='your layer name', show=False)

    # load GEOJSON, but don't add it to anything
    temp_geojson = folium.GeoJson('map.geojson')

    # iterate over GEOJSON, style individual features, and add them to FeatureGroup
    for feature in temp_geojson.data['features']:
        # GEOJSON layer consisting of a single feature
        temp_layer = folium.GeoJson(feature
                                    )
        # lambda to add HTML
        foo = lambda name, source: f"""
            <iframe id="popupIFrame"
                title="{name}"
                width="600"
                height="500"
                align="center"
                src="{source}">
            </iframe>
            """
        # create Popup and add it to our lone feature
        # this example embeds a .png
        folium.Popup(
            html=foo('name of your IFrame',
                     f'https://www.extremetech.com/wp-content/uploads/2019/12/SONATA-hero-option1-764A5360-edit.jpg')
        ).add_to(temp_layer)

        # folium.Popup(
        #     html="Html here"
        # ).add_to(temp_layer)

        # consolidate individual features back into the main layer
        temp_layer.add_to(layer)

    # add main layer to folium.Map object
    # layer.add_to(my_map)


    # folium.Marker(
    #     location=[2.226888, 103.169322], # coordinates for the marker (Earth Lab at CU Boulder)
    #     popup='Earth Lab at CU Boulder', # pop-up label for the marker
    #     icon=folium.Icon()
    # ).add_to(my_map)

    # my_map.add_child(folium.Marker(
    #     location=[2.226888, 102.166440], # coordinates for the marker (Earth Lab at CU Boulder)
    #     popup='Earth Lab at CU Boulder', # pop-up label for the marker
    #     icon=folium.Icon()
    # ))

    # Set visualization parameters.
    # vis_params = {
    #     'min': 0,
    #     'max': 4000,
    #     'palette': ['006633', 'E5FFCC', '662A00', 'D8D8D8', 'F5F5F5']}

#map


def getMap(paddy_area_info=None, colour=None, ee=False):
    # Create a folium map object.
    # guoxuan_location = [6.130130, 102.197939]
    if paddy_area_info != None:
        my_map = folium.Map(location=[paddy_area_info[0].latitude, 
                                paddy_area_info[0].longitude], 
                        zoom_start=20)
    else:
        my_map = folium.Map(location=[2.226888, 102.166600], zoom_start=20)

    if ee:
        # Authenticate to use google earth
        getPrivateKey()

        # Get the google earth base maps
        basemaps = getBaseMap()

        # Add EE drawing method to folium.
        folium.Map.add_ee_layer = add_ee_layer

        basemaps['Maps'].add_to(my_map)
        basemaps['Satellite Hybrid'].add_to(my_map)
 
    # no pre-defined markers - Default
    if paddy_area_info == None:
        lat_lst = [2.226888, 2.226888, 2.226888]
        lng_lst = [102.166600, 102.166440, 102.166200]
        name_lst = ['aa', 'bb', 'cc']
        color_lst = ['green', 'orange', 'red']
        color_lst2 = ['purple', '#FFFF00', 'red']
        feature_group = folium.FeatureGroup("Paddy Areas")

        for lat, lng, name, col, col2 in zip(lat_lst, lng_lst, name_lst, color_lst, color_lst2):
            mark = folium.Marker(location=[lat, lng], popup=name, icon=folium.Icon(color=col, icon_color=col2))
            feature_group.add_child(mark)
    else:
        feature_group = folium.FeatureGroup("Paddy Areas")

        #declaring markers
        # for i, c in zip(paddy_area_info, colour):
        for i in paddy_area_info:
            try:
                pred_ = ImagePredictions.objects.filter(paddy_area_id = i.id)
                img_ = pred_.latest('prediction_date').image
                # tt = ImagePredictions.objects.latest('prediction_date').image
                my_image_path = utils.get_image_directory(img_)
                # my_image_path = utils.get_image_directory(i.paddy_images.url)
                
                encoded = base64.b64encode(open(my_image_path, 'rb').read())
                html = '<img src="data:image/png;base64,{}" width="200" height="200">'.format
                iframe = IFrame(html(encoded.decode('UTF-8')), width=220, height=220)
                popup = folium.Popup(iframe, max_width=300)
                # popup = folium.Popup(max_width=300)

                # marker_color = c
                # if c=='yellow':
                #     marker_color = 'orange'

                marker_color = 'green'
                c = 'green'

                mark = folium.Marker(location=[i.latitude, i.longitude], 
                                    popup=popup,
                                    tooltip=i.area_name,
                                    icon=folium.Icon(color=marker_color, icon_color=None),
                                    )
                feature_group.add_child(mark)

            except:
                marker_color = 'green'
                c = 'green'

                mark = folium.Marker(location=[i.latitude, i.longitude], 
                                    tooltip=i.area_name,
                                    icon=folium.Icon(color=marker_color, icon_color=None),
                                    )
                feature_group.add_child(mark)
                print("No image predictions")

            #circles
            circle = folium.Circle(location=[i.latitude, i.longitude], 
                                            color = c, 
                                            radius = 100, 
                                            fill = True)

            feature_group.add_child(circle)

    # add markers as folium layer
    my_map.add_child(feature_group)

    # Add a layer control panel to the map.
    my_map.add_child(folium.LayerControl(position='topleft'))
    plugins.Fullscreen().add_to(my_map)

    # add draw custom polygon function
    addDrawPolygonFunction().add_to(my_map)

    return my_map._repr_html_()
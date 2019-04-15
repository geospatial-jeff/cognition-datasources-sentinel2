from datasources import Manifest

def Sentinel2(event, context):
    manifest = Manifest()
    manifest['Sentinel2'].search(**event)
    response = manifest.execute()
    return response



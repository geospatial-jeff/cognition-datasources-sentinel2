[![CircleCI](https://circleci.com/gh/geospatial-jeff/cognition-datasources-sentinel2.svg?style=svg)](https://circleci.com/gh/geospatial-jeff/cognition-datasources-sentinel2)

## Sentinel1

| Parameter | Status |
| ----------| ------ |
| Spatial | :heavy_check_mark: |
| Temporal | :heavy_check_mark: |
| Properties | :heavy_check_mark: |
| **kwargs | [limit] |

##### Properties
| Property | Type | Example |
|--------------------------|-------|-------------|
| eo:gsd | int | 10 |
| eo:epsg | int | 32614 |
| eo:instrument | str | 'MSI' |
| eo:platform | str | 'sentinel-2b' |
| eo:off_nadir | int | 0 |
| eo:cloud_cover | int | 100 |
| sentinel:utm_zone | int | 13 |
| sentinel:latitude_band | str | 'T' |
| sentinel:grid_square | str | 'GJ' |
| sentinel:sequence | str | '0' |
def check_location(test):
    for l in lakes:
        if l == test:
            return True
    return False

# be sure to change these columns when data changes
columns = [
    'skip',
    't_utc',
    'skip',
    'ReductionPotential',
    'DissolvedOxygen',
    'PhLevel',
    'WaterTemperature',
    'ElectricalConductivity',
    'DisolvedSolids',
    'Salinity',
    'SpecificGravity',
    'skip',
    'skip',
    'skip',
    'skip',
    'Latitude',
    'Longitude'
]

lakes = {
    'cuito': {
        'original_path': '../databoat/cuito_transect_orginal.CSV',
        'ambit_path': '../databoat/ambit_data_cuito.sml',
        'working_path': '../databoat/cuito_transect_shifted.csv',
        'output_path': '../databoat/cuito_transect_processed.csv',
        'measurement_method': 'length-wise',
        'source_name': 'Cuito',
        'time_adjustment_recorded': 1491342695,
        'time_adjustment_actual': 1492948575
    },
    'cuanavale': {
        'original_path': '../databoat/cuanavale_transect_orginal.CSV',
        'ambit_path': '../databoat/ambit_data_cuanavale.sml',
        'working_path': '../databoat/cuanavale_transect_original.csv',
        'output_path': '../databoat/cuanavale_transect_processed.csv',
        'measurement_method': 'multiple-transects',
        'source_name': 'Cuanavale',
        'time_adjustment_recorded': 0,
        'time_adjustment_actual': 0
    },
    'cuanavale_2': {
        'original_path': '../databoat/cuanavale_2_transect_orginal.CSV',
        'ambit_path': '../databoat/ambit_data_cuanavale_2.sml',
        'working_path': '../databoat/cuanavale_transect_2_shifted.csv',
        'output_path': '../databoat/cuanavale_transect_2_processed.csv',
        'measurement_method': 'length-wise',
        'source_name': 'Cuanavale',
        'time_adjustment_recorded': 1493107924,
        'time_adjustment_actual': 1493104452
    }
}

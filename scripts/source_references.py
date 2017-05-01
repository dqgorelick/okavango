def check_location(test):
    for l in lakes:
        if l == test:
            return True
    return False

# be sure to change these columns when data changes
columns = [
    'TransectNumber',
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
    },
    'tchanssengwe': {
        'original_path': '../databoat/lunge_bungo_transect_original.CSV',
        'ambit_path': '../databoat/ambit_data_lunge_bungo.sml',
        'working_path': '../databoat/lunge_bungo_transect_shifted.csv',
        'output_path': '../databoat/lunge_bungo_transect_processed.csv',
        'measurement_method': 'multiple-transects',
        'source_name': 'Lunge-Bungo (Tchanssengwe)',
        'time_adjustment_recorded': 1493293153,
        'time_adjustment_actual': 1493290199
    },
    'tchanssengwe_2': {
        'original_path': '../databoat/lunge_bungo_transect_2_original.CSV',
        'ambit_path': '../databoat/ambit_data_lunge_bungo_2.sml',
        'working_path': '../databoat/lunge_bungo_transect_2_shifted.csv',
        'output_path': '../databoat/lunge_bungo_transect__2_processed.csv',
        'measurement_method': 'length-wise',
        'source_name': 'Lunge-Bungo (Tchanssengwe)',
        'time_adjustment_recorded': 1492888195,
        'time_adjustment_actual': 1493370060
    },
    'tchanssengwe_3': {
        'original_path': '../databoat/lunge_bungo_transect_3_original.CSV',
        'ambit_path': '../databoat/ambit_data_lunge_bungo_3.sml',
        'working_path': '../databoat/lunge_bungo_transect_3_shifted.csv',
        'output_path': '../databoat/lunge_bungo_transect__3_processed.csv',
        'measurement_method': 'length-wise',
        'source_name': 'Lunge-Bungo (Tchanssengwe)',
        'time_adjustment_recorded': 1493376053,
        'time_adjustment_actual': 1493375953
    }
}

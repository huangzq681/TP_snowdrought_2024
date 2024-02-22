import cdsapi

c = cdsapi.Client()
year = [str(i) for i in range(1979,2000)]
c.retrieve(
    'reanalysis-era5-land',
    {
        'variable': 'snow_depth_water_equivalent',
        'year': year,
        'month': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12'],
        'day': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31',
        ],
        'time': '00:00',
        'area': [
            46, 66, 22,
            108,
        ],
        'format': 'netcdf.zip',
        'grid':str(0.25)+'/'+str(0.25),
    },
    '/Users/zeqinhuang/Documents/paper/TB_SWE/rawData/ERA5_land_daily_1.zip')


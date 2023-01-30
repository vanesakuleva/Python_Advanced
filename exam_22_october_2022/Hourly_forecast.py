def forecast(*args):
    dict_of_location = {'Sunny': [], 'Cloudy': [], 'Rainy': []}
    sunny_list= []
    cloudy_list= []
    rainy_list=[]
    result=[]
    for information in args:
        city= information[0]
        wheter= information[1]
        if wheter == 'Sunny':
            sunny_list.append(city)
        elif wheter == 'Cloudy':
            cloudy_list.append(city)
        elif wheter == 'Rainy':
            rainy_list.append(city)
    dict_of_location['Sunny'] = sorted(sunny_list)
    dict_of_location['Cloudy'] = sorted(cloudy_list)
    dict_of_location['Rainy'] = sorted(rainy_list)

    for k, v in dict_of_location.items():
        if v !=[]:
            for i in v:
                result.append(f"{i} - {k}")
    return "\n".join(result)




print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))




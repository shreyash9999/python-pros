travel_log = [
    {
        "country" : "france",
        "cities" : 12,
        "cities_visited" : ["lille" , "Paris" , "Dijon"]
    },
    {
        "country" : "Germeny",
        "cities" : 5,
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"]
    },
]

def add_new_list(new_country_visited, new_cities, new_cities_visited):
    new_country = {}
    new_country["country"] = new_country_visited
    new_country["cities"] = new_cities
    new_country["cities_visited"] = new_cities_visited
    travel_log.append(new_country)

add_new_list("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
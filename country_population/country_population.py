import requests

def fetch_countries():
    url ="https://restcountries.com/v3.1/all"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data:{response.status_code}")

def sort_countries_by_population(countries):
    return sorted(countries,key = lambda x : x['population'], reverse= True)

def main():
    try:
        countries = fetch_countries()
        sorted_countries = sort_countries_by_population(countries)
        for country in sorted_countries:
            print(f"{country['name']['common']}: {country['population']}")
    except Exception as e:
        print(e)
    
if __name__ == "__main__":
    main()
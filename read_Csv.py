import csv

def obtain_population_to_contry(path, country):
    with open(path, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter = ',')

        # Initialize empty lists for population data
        population_data = {}

        # Iterate through each row of the CSV file
        for row in reader:
            if row['Country/Territory'] == country:  # Filter by specified country
                key_year = []
                value_year = []
                # Extract population data for each year
                for year in ['2022', '2020', '2015', '2010', '2000', '1990', '1980', '1970']:
                        population_data[year] = int(row[f'{year} Population'])
            
    return population_data.keys(), population_data.values()       

import read_Csv
import charts


#Function of ask to user country 
def ask_user_country():
    country = input('\n¿De que pais quieres ver su poblacion?\n')
    return country.capitalize()


if __name__ == '__main__':
    country_user = ask_user_country()
    key, value = read_Csv.obtain_population_to_contry('PROYECTO FINAL/world_population.csv', country_user)
    charts.generate_bar_char(key, value)
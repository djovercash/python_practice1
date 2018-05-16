cities = ['Solta', 'Greenville', 'Buenos Aires', 'Los Cabos', 'Walla Walla Valley', 'Marakesh', 'Albuquerque', 'Archipelago Sea', 'Iguazu Falls', 'Salina Island', 'Toronto', 'Pyeongchang']
countries = ['Croatia','USA','Argentina','Mexico','USA','Morocco','New Mexico','Finland','Argentina','Italy','Canada','South Korea']

#Set the variable 'italy' to be equal to the third from the last element of countries
italy = countries[-3]
print italy

#Access the fourth element and set it equal to the variable 'mexico'.
mexico = countries[3]
print mexico

#Notice that the second through fifth elements are all in a row and all in
#the Western Hemisphere. Assign that subset of elements to a variable
#called kindof_neighbors.
kindof_neighbors = countries[1:5]
print kindof_neighbors

#Add the country 'Malta'.
countries.append("Malta")
print countries

#Add the country 'Thailand'.
countries.append("Thailand")
print countries

#Change 'New Mexico' to 'USA'.
countries[6] = "USA"
print countries

#Remove 'Thailand' from the list
countries.pop()
print countries

#Use the set and list functions to return a unique list of countries.
#Set this list equal to the variable unique_countries.
unique_countries = list(set(countries))
print unique_countries

#Find the number of repeat countries
num_of_repeats = len(countries) - len(unique_countries)
print num_of_repeats

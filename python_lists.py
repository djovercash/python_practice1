cities = ['Solta', 'Greenville', 'Buenos Aires', 'Los Cabos', 'Walla Walla Valley', 'Marakesh', 'Albuquerque', 'Archipelago Sea', 'Iguazu Falls', 'Salina Island', 'Toronto', 'Pyeongchang']
print cities

countries = ['Croatia', 'USA', 'Argentina', 'Mexico', 'USA', 'Morocco', 'New Mexico', 'Finland', 'Argentina', 'Italy', 'Canada', 'South Korea']
print countries

print cities[0] #Solta
print cities[2] #Buenos Aires
print cities[-1] #Pyeongchang
print cities[-2] #Toronto

top_canadian_city = cities[-2] #Toronto
print top_canadian_city #Toronto
print type(top_canadian_city) #str
print type(cities) #list


#SLICING an element
print cities[0:2] #Solta, Greenville. First number is what index to start at and second is what index to end at
print cities[4:6] #Walla Walla Valley, Marakesh

top_two = cities[0:2]
print top_two

#Changing elements with destructive methods
cities.append('San Antonio')
print cities #Added San Antonio to the end of cities

cities.pop()
print cities #Removes last element (San Antonio) from cities

cities[4] = "WHAT?"
print cities #Changes the element at index 4

cities[4] = "Walla Walla Valley"
print cities #Changes it back

#Use SET to find unique value (undestructively)
cities.append("Solta") #Added Solta to cities
print cities
unique_cities = set(cities)
print unique_cities

print type(set()) #set

# A set is just like a list, except elements do not have order and each element appears just once.
# i.e. unique_cities[4] returns an error


unique_cities_list = list(unique_cities)
print unique_cities_list

print len(unique_cities_list)
print len(cities)

neighborhoods = ['Palermo', 'Ricoleta', 'Santelmo', 'Puerto Madero', 'Belgrano', 'La Boca']
palermo = neighborhoods[0]
la_boca = neighborhoods[-1]


#Set the latitude of Buenos Aires equal to ba_latitude and set the longitude
#to be Buenos Aires to be ba_longitude.

coordinates = [-34.6037, -58.3816]
ba_latitude = coordinates[0]
ba_longitude = coordinates[-1]

#First we download a mapping library with pip.
#Remember a library is simply a tool comprised of code hosted somewhere else
#on the internet and which we download to use in our current project.
#Pip is another tool that allows us to easily download various Python
#libraries from the Internet.
!pip install folium

#RESEARCH PIP AND FOLIUM LATER

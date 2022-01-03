'''
This program contains functions required for the project:

load_ID(), store_ID(), print_ID(), load_shapes(), store_points(), print_points(), load_stops(),
store_stops(), print_stops(), read_shapes_ids_stops(), write_shapes_ids_stops(), map_window(), map_route(), 
map_stops(), haversine(), menu(), and main() functions that help to load the ETS files into data structures, 
implement a menu to access the data, and an interactive map window to display the bus stops and routes.
   
This program is my own work.

author: VIGHNESH SAJEEV
'''   
from graphics import *
import pickle
from math import radians, sin, cos, sqrt, asin

def load_ID():
    '''
    Purpose: Take user input for name of file with error check, read the file and call store_ID()
    Parameter: none
    Return: function - store_ID(file, name)
    ''' 
    
    f_name = input("Enter a file name [data/trips.txt]: ")
    
    # try opening file specified by user, and give exception if failed, 
    # otherwise open trips.txt by default if user does not provide an input
    if f_name == "":
        
        file = open("data/trips.txt", "r")
   
    else:
        
        path = f"data/{f_name}.txt"
        
        try:
            
            file = open(path, "r")
        
        except:
            
            print(f"\n{f_name}.txt does not exist in the directory!") 
            return None
    
    line = file.readline()
    line = file.readline()
    
    
    return store_ID(file, line)



def store_ID(file, line):
    '''
    Purpose: Read file line by line, and store the routes and shape ids into contents dictionary
    Parameter: file, line - opened file, first line to read
    Return: dictionary - contents{} containing route ids as keys, shape ids as values
    '''    
    
    contents = {}
    
    # read file line by line, read the route ID and shape ID, and store them in 
    # a dictionary of routes as keys, and shapes as values
    while(line != ''):
        
        parts = line.split(",")
        route = parts[0]
        shape = parts[-1]
        
        # making new list of shape ids for a new route id
        if route not in contents:
            
            shapes = []
            shapes.append(shape)
            contents[route] = shapes
        
        elif route in contents:
            
            if shape not in shapes:
                
                shapes.append(shape)
                
            contents[route] = shapes
            
        line = file.readline()
    
    
    return contents 



def print_ID(data):
    '''
    Purpose: take user input for route, error check if in data, and print its relevant shape ID's
    Parameter: dictionary - returned from load_ID() 
    Return: None
    '''       
    
    user = input("Route? ")
    
    # error checking if user input is a number or not
    while(user.isnumeric() == False):
        user = input("Route? ")
    
    # print the shape id's for the particular route id, if it exists in dictionary
    if user not in data:
        
        print(f"ShapeIDs for {user}:\n\t** NOT FOUND **")

    elif user in data:
        
        print(f"Shape IDs for {user}: ")
        
        for route in data[user]:
            
            print("\t" + route, end = "")
     
     
        
def load_shapes():
    '''
    Purpose: Take user input for name of file with error check, read the file and call store_points()
    Parameter: none
    Return: function - store_points(file, name)
    '''    
    
    f_name = input("Enter a file name [data/shapes.txt]: ")
    
    # try opening file specified by user, and give exception if failed, 
    # otherwise open shapes.txt by default if user does not provide an input    
    if f_name == "":
        
        file = open("data/shapes.txt", "r")
   
    else:
        
        path = f"data/{f_name}.txt"
        
        try:
            
            file = open(path, "r")
        
        except:
            
            print(f"{f_name}.txt does not exist in the directory!") 
            return None
    
    line = file.readline()
    line = file.readline()
    
    
    return store_points(file, line)
   
   

def store_points(file, line):
    '''
    Purpose: Read file line by line, and store the shape id and coordinates into contents dictionary
    Parameter: file, line - opened file, first line to read
    Return: dictionary - contents{} containing shape id as keys, and coordinates as values
    '''      
    
    contents = {}
    
    # read file line by line, read the shape id, latitude, longitude, and store them in 
    # a dictionary of shape id as keys, and coordinates as values   
    while(line != ''):
    
        parts = line.split(",")
        
        shape = parts[0]
        latitude = parts[1]
        longitude = parts[2]
        
        coordinates = f"({latitude}, {longitude})"
        
        if shape not in contents:
            
            points = []
            points.append(coordinates)
            contents[shape] = points
        
        elif shape in contents:
                
            points.append(coordinates)
                
            contents[shape] = points
            
        line = file.readline()
        

    return contents



def print_points(data):
    '''
    Purpose: take user input for shape id, error check if in data, and print its relevant coordinates
    Parameter: dictionary - returned from load_shapes() 
    Return: None
    '''      
    
    user = input("Shape ID? ")
    
    # print the coordinates for the particular shape id, if it exists in dictionary
    if user not in data:
        
        print(f"Shape for {user}:\n\t** NOT FOUND **")

    elif user in data:
        
        print(f"Shape for {user}: ")
        
        for points in data[user]:
            
            print("\t" + points)



def load_stops():
    '''
    Purpose: Take user input for name of file with error check, read the file and call store_stops()
    Parameter: none
    Return: function - store_stops(file, line)
    ''' 
    
    f_name = input("Enter a file name [data/stops.txt]: ")
    
    # try opening file specified by user, and give exception if failed, 
    # otherwise open stops.txt by default if user does not provide an input
    if f_name == "":
        
        file = open("data/stops.txt", "r")
   
    else:
        
        path = f"data/{f_name}.txt"
        
        try:
            
            file = open(path, "r")
        
        except:
            
            print(f"\n{f_name}.txt does not exist in the directory!") 
            return None
    
    line = file.readline()
    line = file.readline()
    
    
    return store_stops(file, line)



def store_stops(file, line):
    '''
    Purpose: Read file line by line, and store the stop ids, name, and coordinates into contents dictionary
    Parameter: file, line - opened file, first line to read
    Return: dictionary - contents{} containing coordinates as keys, and list of ids and names as values
    '''    
    
    contents = {}
    
    # read file line by line, read the stop ids, name, and coordinates, and store them in 
    # a dictionary of coordinates as keys, and list of ids and names as values
    while(line != ''):
        
        parts = line.split(",")
        stop_id = parts[0]
        stop_name = parts[2]
        stop_lat = parts[4].strip()
        stop_lon = parts[5]
        
        coordinates = f"({stop_lat}, {stop_lon})"
        
        # making new list of stop ids and stop names for a new coordinate
        if coordinates not in contents:
            
            stops = []
            stops.append(stop_id)
            stops.append(stop_name.strip('"'))
            contents[coordinates] = stops
    
        elif coordinates in contents:
            
            if stop_id not in stops:
                
                stops.append(stop_id)
                stops.append(stop_name.strip('"'))
                
            contents[coordinates] = stops
            
        line = file.readline()
    
    
    return contents 



def print_stops(data):
    '''
    Purpose: take user input for coordinate, error check if in data, and print its relevant stop ID and name
    Parameter: dictionary - returned from load_stops() 
    Return: None
    '''       
    
    user = input("Location as 'lat, lon'? ")
    
    # error checking if user input is a number or not
    while(user.count(",") != 1):
        
        user = input("Location as 'lat, lon'? ")
    
    user = user.split(",")
    
    coords = f"({float(user[0].strip())}, {float(user[1].strip())})"
    
    # print the shape id's for the particular route id, if it exists in dictionary
    if coords not in data:
        
        
        print(f"\nStops for {coords}:\n\t** NOT FOUND **")

    elif coords in data:
        
        
        print(f"\nStops for {coords}: ")
        
        for stop in data[coords]:
            
            print(f"\t{stop}", end = "\t")
            
            
            
def write_shapes_ID_stops(shapes, shape_ID, stops):
    '''
    Purpose: take the data (shape, shape IDs, stops) and pickle them into a file
    Parameter: dictionaries : shapes, shape IDs, stops
    Return: None
    ''' 
    
    contents = [shapes, shape_ID, stops]
    
    filename = input("Enter a file name [etsdata.p]: ")
    
    # If no filename is provided, 'etsdata.p' will be used as filename
    if filename == "":
        
        file = open("etsdata.p", "wb")
   
    else:
        
        path = f"{filename}.p"
        file = open(path, "wb")
    
    pickle.dump(contents, file)
    
    file.close()
    
    
    
def read_shapes_ID_stops():
    '''
    Purpose: read the data from the pickled file
    Parameter: None
    Return: list contents - list of dictionaries shapes, shape_ID, stops
    '''     
    filename = input("Enter a file name [etsdata.p]: ")
    
    # If no filename is provided, 'etsdata.p' will be used as filename
    if filename == "":
        
        file = open("etsdata.p", "rb")
   
    else:
        
        # Print an exception if file not found in the directory
        try:
            
            path = f"{filename}.p"
            file = open(path, "rb")
        
        except:
            
            print(f"file named {filename} does not exist in the directory!")
            return None
        
    contents = pickle.load(file)
    
    file.close()
    
    
    return contents

    
    
def map_window(shape_ID, shapes, stops):
    '''
    Purpose: Make a window; set coordinates; display map, text entry box, button; 
             obtain and print Geographic and Pixel; call map_stops() and map_route()
             functions 
    Parameter: Dictionaries : shape_ID,  shapes, stops
    Return: None
    '''  
    
    win = GraphWin("ETS Bus Routes", 630, 768)
    win.setCoords(-113.7136, 53.39576, -113.2714, 53.71605)
    
    x, y = win.toWorld(315, 384)
    
    map = Image(Point(x, y), "background.gif")
    map.draw(win)
    
    x, y = win.toWorld(80, 40)
    
    textEntry = Entry(Point(x, y), 10)
    textEntry.draw(win)
    
    a, b = win.toWorld(130, 29)
    x, y = win.toWorld(190, 49)
    
    button = Rectangle(Point(a, b), Point(x, y))
    button.setFill("SkyBlue")
    button.draw(win)
    
    x, y = win.toWorld(160, 39)
    
    buttontext = Text(Point(x, y), "Plot")
    buttontext.draw(win)    
    
    # Get mouse click location, print coordinates in geographic and pixel form, 
    # call map_stops to plot the closest 5 stops
    # call map_route to draw the routes
    while True:
        
        where = win.getMouse()
        
        lat, lon = (where.getY(), where.getX())
        x, y = win.toScreen(where.getX(), where.getY())
        
        print(f"\nGeographic (lat, lon): ({lat}, {lon})\nPixel (x, y): ({x}, {y})")
        
        print(f"\n")
        
        map_stops(win, lat, lon, stops)
        map_route(win, where, button, textEntry, shape_ID, shapes)
        
          
    win.close()
     
     
        
def map_route(win, where, button, textEntry, shape_ID, shapes):
    '''
    Purpose: Take user input from textEntry at button click, draw the longest path of
             specified route with the help of shape_ID and shapes dictionary
    Parameter: win - window
               where - click location
               button - plot button
               textEntry - Input box for user
               shape_ID - dictionary of ids and routes
               shapes - dictionary of routes and coordinates
    Return: None
    '''      
    
    px, py = where.getX(), where.getY()
        
    x0, y0 = button.getP1().getX(), button.getP1().getY()
    
    x1, y1 = button.getP2().getX(), button.getP2().getY()

    
    # Checking IF the click location is on the button 
    if ((min(x0,x1) <= px <= max(x0,x1)) and (min(y0,y1) <= py <= max(y0,y1))):
        
        user = textEntry.getText()

        
        # Checking if input in entry box is a valid ID
        if user in shape_ID:
            
            routes = []

            
            # Making a list of routes for the specific shape_ID
            for route in shape_ID[user]:
                
                route = route[:-1]
                routes.append(route)
            
            coords = shapes[routes[0]]

            
            # Finding the longest route
            for num in range(1, len(routes)):
                
                if len(shapes[routes[num]]) > len(coords):
                    
                    coords = shapes[routes[num]]


            # Drawing the longest route on the map window
            for num in range(0, len(coords) - 1):
                
                x0, y0 = coords[num][1:-1].split(", ")
        
                x1, y1 = coords[num + 1][1:-1].split(", ")

                path = Line(Point(y0, x0), Point(y1, x1))
                path.setWidth(3)
                path.draw(win)    
                    

# function copied from https://rosettacode.org/wiki/Haversine_formula#Python.
def haversine(lat1, lon1, lat2, lon2):
    
    R = 6372.8  # Earth radius in kilometers
 
    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
 
    a = sin(dLat / 2)**2 + cos(lat1) * cos(lat2) * sin(dLon / 2)**2
    c = 2 * asin(sqrt(a))
 
    return R * c
    


def map_stops(win, lat, lon, stops):
    '''
    Purpose: Make a dictionary, calculates distances using Haversine(), and plot the closest 5
            stops on the map
    Parameter: win - window
               lat, lon - click coordinates
               stops - dict of stops
    Return: None
    '''      
    
    distdict = {}
    
    # Calculate and store distances of all the stops from the click location
    for coord in stops.keys():
        
        coordcut = coord[1:-1]
        lat2, lon2 = coordcut.split(", ")
        
        dist = haversine(lat, lon, float(lat2), float(lon2))
        
        distdict[dist] = coord
    
    distlist = distdict.keys()
    
    print("Nearest stops:")
    print("\tDistance  Stop  Description")
    
    # Print the ids and names of 5 closest stops on the map, and plots the points on map
    for dist in sorted(distlist)[:5]:   
        
        print("\t  ", round(dist * 1000, 1), end = "  " )
    
        for item in stops[distdict[dist]]:
            
            print(item.strip('"'), end = "\t")
        
        print("")
        
        x_pt, y_pt = distdict[dist][1:-1].split(", ")
        
        stop_plot = Circle(Point(float(y_pt), float(x_pt)), 0.0001)
        stop_plot.setFill("Black")
        stop_plot.draw(win)    



def menu():
    '''
    Purpose: helper function to display a menu and return user input after error check
    Parameter: none
    Return: int - answer - user input of option
    '''    
    while True:
        
        print("\n\n    Edmonton Transit System")
        print("--------------------------------")
        print("(1) Load shape IDs from GTFS file")
        print("(2) Load shapes from GTFS file")
        print("(3) Load stops from GTFS file")
        print("\n(4) Print shape IDs for a route")
        print("(5) Print points for a shape ID")
        print("(6) Print stops for a location")
        print("\n(7) Save shapes, shape IDs, and stops in a pickle")
        print("(8) Load shapes, shape IDs, and stops from a pickle")
        print("\n(9) Display interactive map")
        print("\n(0) Quit")
        print()
        
        answer = input("Enter command: ")
        
        #Error checking user input
        while( len(answer) != 1 or answer not in "1234567890"):
            
            answer = input("Enter a valid number: ")
            
            
        return int(answer)  


    
if __name__ == "__main__":
    '''
    Purpose: displays menu, and calls all the other helper functions
    Parameter: none
    Return: none
    '''      
    
    
    choice = menu()
    
    # While loop to keep going through choices and displaying menu 
    # until the 0 is selected, after which the program exits
    while not(choice == 0):
        
        if choice == 1:
            
            shape_ID = load_ID()
            
        elif choice == 2:
            
            shapes = load_shapes()
            
        elif choice == 3:
            
            stops = load_stops()
        
        elif choice == 4:
            
            try:
                
                print_ID(shape_ID)
            
            except:
                
                print("\nShape IDs not loaded yet!")
            
        elif choice == 5:
            
            try:
                
                print_points(shapes)
            
            except:

                print("\nShapes not loaded yet!")
        
        elif choice == 6:
            
            try:
                
                print_stops(stops)
            
            except:

                print("\nStops not loaded yet!")        
        
        elif choice == 7:
            
            try:
                
                write_shapes_ID_stops(shapes, shape_ID, stops)
            
            except:
                
                print("\nLoad shapes, shape IDs, and stops first!")
                
        elif choice == 8:
            
            try:
                
                contents = read_shapes_ID_stops()
                shapes, shape_ID, stops = contents
            
            except:
                
                print("\nNo file found!")   
            
        elif choice == 9:
            
            try:
                
                map_window(shape_ID, shapes, stops)
            
            except:
                
                print("\nLoad shapes, shape IDs, and stops first!")
                
            
        choice = menu()
    

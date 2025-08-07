import pickle
from collections import defaultdict

def load_ID():
    '''
    Purpose: Read the trips.txt file and build a dictionary of route-to-shape mappings.
    Return: A dictionary where keys are route IDs and values are lists of shape IDs.
    '''
    contents = defaultdict(list)
    try:
        with open("data/trips.txt", "r") as file:
            next(file)  # Skip header
            for line in file:
                try:
                    parts = line.split(",")
                    route = parts[0]
                    shape = parts[-1].strip()
                    if shape not in contents[route]:
                        contents[route].append(shape)
                except IndexError:
                    print(f"Skipping malformed line in trips.txt: {line.strip()}")
    except FileNotFoundError:
        print("\nError: data/trips.txt not found!")
        return None
    return dict(contents)

def load_shapes():
    '''
    Purpose: Read the shapes.txt file and build a dictionary of shape-to-coordinate mappings.
    Return: A dictionary where keys are shape IDs and values are lists of (lat, lon) tuples.
    '''
    contents = defaultdict(list)
    try:
        with open("data/shapes.txt", "r") as file:
            next(file)  # Skip header
            for line in file:
                try:
                    parts = line.split(",")
                    shape = parts[0]
                    coordinates = (float(parts[1]), float(parts[2].strip()))
                    contents[shape].append(coordinates)
                except (IndexError, ValueError):
                    print(f"Skipping malformed line in shapes.txt: {line.strip()}")
    except FileNotFoundError:
        print("\nError: data/shapes.txt not found!")
        return None
    return dict(contents)

def load_stops():
    '''
    Purpose: Read the stops.txt file and build a dictionary of coordinate-to-stop mappings.
    Return: A dictionary where keys are (lat, lon) tuples and values are lists of stop info.
    '''
    contents = defaultdict(list)
    try:
        with open("data/stops.txt", "r") as file:
            next(file)  # Skip header
            for line in file:
                try:
                    parts = line.split(",")
                    stop_id = parts[0]
                    stop_name = parts[2].strip('"')
                    coordinates = (float(parts[4].strip()), float(parts[5].strip()))

                    existing_ids = contents[coordinates][0::2]
                    if stop_id not in existing_ids:
                        contents[coordinates].append(stop_id)
                        contents[coordinates].append(stop_name)
                except (IndexError, ValueError):
                    print(f"Skipping malformed line in stops.txt: {line.strip()}")
    except FileNotFoundError:
        print("\nError: data/stops.txt not found!")
        return None
    return dict(contents)

def write_shapes_ID_stops(shapes, shape_ID, stops):
    '''
    Purpose: take the data (shape, shape IDs, stops) and pickle them into a file
    Parameter: dictionaries : shapes, shape IDs, stops
    Return: None
    '''
    contents = [shapes, shape_ID, stops]
    filename = "etsdata.p"
    try:
        with open(filename, "wb") as file:
            pickle.dump(contents, file)
        print(f"\nData successfully saved to {filename}")
    except IOError as e:
        print(f"\nError writing to file: {e}")

def read_shapes_ID_stops():
    '''
    Purpose: read the data from the pickled file
    Parameter: None
    Return: list contents - list of dictionaries shapes, shape_ID, stops
    '''
    filename = "etsdata.p"
    try:
        with open(filename, "rb") as file:
            contents = pickle.load(file)
            print(f"\nData successfully loaded from {filename}")
            return contents
    except FileNotFoundError:
        print(f"\nFile '{filename}' not found.")
        return None
    except pickle.UnpicklingError:
        print(f"\nError: Could not read data from '{filename}'. The file may be corrupted.")
        return None

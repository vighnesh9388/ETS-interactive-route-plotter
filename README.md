# Edmonton Transit System (ETS) Bus Route Plotter
<p align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Edmonton_Transit_System_logo_with_text.svg/474px-Edmonton_Transit_System_logo_with_text.svg.png">
</p>
This **Python** project is designed to parse and interact with **Edmonton Transit Service (ETS)** data available from the [**City of Edmonton Open Data Catalogue**](https://data.edmonton.ca/), facilitating both command-line and graphical user interfaces for exploring transit routes and stops. The project is structured around several milestones, each adding functionality ranging from basic data handling in Python to advanced GUI operations.

## Getting Started

To run this project, ensure you have Python 3 and the required libraries installed. Clone the repository and navigate to the directory containing the project.

```bash
git clone https://github.com/vighnesh9388/ETS-interactive-route-plotter.git
cd ETS-interactive-route-plotter
```

## Project Structure

- **Milestone 1**: Implements a text-based menu system for loading and querying transit data from text files.
- **Milestone 2**: Extends the functionality with a graphical user interface (GUI) using [`graphics.py`](https://pypi.org/project/graphics.py/) to plot bus routes.
- **Milestone 3**: Further develops the GUI to include interactive features like plotting bus stops based on user clicks.

## Features

- Load transit data from [GTFS](https://github.com/google/transit) files.
- Text-based querying of shape IDs and route data.
- GUI for visually exploring bus routes and stops.
- Error handling for file operations and user input.
- Use of pickling for saving and loading processed data.

## Technologies Used

- [**Python 3**](https://www.python.org/downloads/): Primary programming language.
- [**graphics.py**](https://pypi.org/project/graphics.py/): Library for creating GUI elements.
- **Pickle**: For object serialization and persistence.
- Text/mutability
- File input
- Lists
- Tuples
- Sets
- Dictionaries
- Algorithms

## Technologies/Features To Add/Improve

- Optimize code for better performance and readability.
- Enhance the GUI for a more user-friendly experience.
- Implement a feature to automatically fetch, format, and update the GTFS files to the latest version periodically (current data is from 2016).
- Deploy the application to a fully functional website.

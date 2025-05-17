# PortfolioOptimizer

# TSP City-Tour Optimizer

A Python implementation of the Travelling Salesman Problem (TSP) solver optimized for city tours.

## Features

- CSV parsing for place coordinates
- Haversine distance calculation for accurate distance between geographical points
- Multiple TSP solving algorithms:
  - Greedy algorithm
  - 2-opt improvement
  - Simulated annealing
- GeoJSON export for visualizing the route on mapping tools
- Matplotlib visualization with directional arrows
- Command-line interface for easy use

## Installation

No additional installation is required beyond standard Python libraries:
- matplotlib
- argparse
- csv
- json
- random
- math

## Usage

### Basic Usage

```bash
python tsp.py --csv paris_places.csv
```

### Specify Starting Point

```bash
python tsp.py --csv paris_places.csv --start "Eiffel Tower"
```

### Return to Starting Point

```bash
python tsp.py --csv paris_places.csv --start "Eiffel Tower" --return
```

### Choose a Different Algorithm

```bash
python tsp.py --csv paris_places.csv --algo simulated-annealing
```

### Generate a Plot

```bash
python tsp.py --csv paris_places.csv --plot
```

## Input Format

The program expects a CSV file with the following columns:
- Name: Name of the place
- Lat: Latitude in decimal degrees
- Lon: Longitude in decimal degrees

Example:
```
Name,Lat,Lon
Eiffel Tower,48.8584,2.2945
Louvre Museum,48.8606,2.3376
```

## Output

- Terminal output with the optimal tour and total distance
- GeoJSON file (`route.geojson`) that can be imported into mapping tools
- Optional matplotlib plot saved as `tour_plot.png`

## Project Structure

- `tsp.py`: Main program
- `distance.py`: Distance calculation module
- `tsp_solver.py`: TSP solver implementations
- `paris_places.csv`: Sample data file

## Example Output

```
Optimal tour (returns to start):
1) Eiffel Tower
2) Arc de Triomphe
3) Champs-Élysées
4) Tuileries Garden
5) Louvre Museum
6) Musée d'Orsay
7) Notre-Dame Cathedral
8) Luxembourg Gardens
9) Montmartre
10) Sacré-Cœur Basilica
11) Eiffel Tower
Total distance: 14.3 km
Route written to route.geojson
```

## Viewing Routes

The generated GeoJSON file can be dragged and dropped into:
- Google Maps
- geojson.io
- QGIS
- Any GIS software that supports GeoJSON

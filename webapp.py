from flask import Flask, render_template, jsonify
import data_handler

app = Flask(__name__)

# Load data on startup
print("Loading ETS data...")
shape_ID = data_handler.load_ID()
shapes = data_handler.load_shapes()
stops = data_handler.load_stops()
if shape_ID and shapes and stops:
    print("ETS data loaded successfully.")
else:
    print("Error: Failed to load one or more data files. The application may not function correctly.")

@app.route('/')
def index():
    """
    Purpose: Renders the main map page.
    """
    return render_template('index.html')

@app.route('/api/route/<route_id>')
def get_route(route_id):
    """
    Purpose: Provides the coordinates for a given route ID as JSON.
    """
    if shape_ID and shapes and route_id in shape_ID:
        # Find the longest shape for the route
        longest_shape_id = max(shape_ID[route_id], key=lambda sid: len(shapes.get(sid, [])))
        if longest_shape_id in shapes:
            return jsonify(shapes[longest_shape_id])

    return jsonify({"error": "Route not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)

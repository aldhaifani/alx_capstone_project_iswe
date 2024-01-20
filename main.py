"""
The main script for the webapp
"""
from fundtrack import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

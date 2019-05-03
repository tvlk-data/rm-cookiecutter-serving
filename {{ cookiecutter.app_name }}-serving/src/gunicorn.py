"""
The one that will be executed by `serve` command.
"""

from src.app import app

if __name__ == "__main__":
    app.run()
from app import create_app
import os
from app.api.v2.models.dbconfig import Database


config_name = os.getenv("APP_SETTINGS")
app = create_app(config_name)


@app.cli.command()
def create():
    Database().create_tables()


@app.cli.command()
def destroy():
    Database().destroy_tables()


if __name__ == "__main__":
    app.run(debug=True)

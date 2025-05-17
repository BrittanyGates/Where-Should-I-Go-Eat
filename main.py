#!/usr/bin/env python3
"""Where Should I Go Eat?
Creator: Brittany Gates (https://github.com/BrittanyGates) | (https://www.linkedin.com/in/brittanycgates) |
(https://brittbot.com/)
About: If you're hungry and unsure of where to go to get something to eat, this app randomly tells you where to go
eat with a click of a button.
"""

from flask import Flask, render_template, jsonify, Response
from static.files.restaurants_urls import restaurant_urls
import random

app = Flask(__name__)


@app.route("/")
def index() -> render_template:
    """Displays the index.html template.
    :return: Home page displaying the randomly-chosen restaurant.
    """
    return render_template("index.html")


def get_random_restaurant() -> tuple:
    """Gets a random restaurant from a text file.
    :return: The random restaurant and its restaurant URL as a string in a tuple.
    """
    with open("static/files/restaurants.txt", "r") as restaurants:
        restaurant_list: list[str] = restaurants.readlines()

    # Choose a random restaurant
    random_restaurant: str = random.choice(restaurant_list).strip()

    # Initializing variable
    found_restaurant_url: str = ""

    # Search the nested tuples for the correct restaurant URLs matching the chosen random restaurant
    for restaurant in restaurant_urls:
        if random_restaurant in restaurant:
            found_restaurant_url: str = restaurant[1]

    return random_restaurant, found_restaurant_url


@app.route("/restaurant-result")
def get_restaurant() -> Response:
    """Allows the JavaScript event handler to run the main function.
    :return: The random restaurant inside a dictionary.
    """
    restaurant, restaurant_link = get_random_restaurant()
    return jsonify({"restaurant": restaurant, "link": restaurant_link})


@app.route("/", methods=["GET", "POST"])
def main() -> render_template:
    """Gathers the random restaurant to display on the index.html template.
    :return: The name and URL of the randomly-chosen restaurant.
    """

    return render_template("index.html")


if __name__ == "__main__":
    main()

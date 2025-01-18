#!/usr/bin/env python3
"""Where Should I Go Eat?
Creator: Brittany Gates (https://github.com/BrittanyGates) | (https://www.linkedin.com/in/brittanycgates) |
(https://brittbot.com/)
About: If you're hungry and unsure of where to go to get something to eat, this app randomly tells you where to go
eat with a click of a button.
"""

from flask import Flask, render_template
from static.files.restaurants_urls import restaurant_urls
import random

app = Flask(__name__)


@app.route("/")
def index() -> render_template:
    """Displays the index.html template.
    :return: Home page displaying the randomly-chosen restaurant.
    """
    return render_template("index.html")


@app.route("/", methods=["GET", "POST"])
def main() -> render_template:
    """Gathers the random restaurant to display on the index.html template.
    :return: The name and URL of the randomly-chosen restaurant.
    """
    with open("static/files/restaurants.txt", "r") as restaurants:
        restaurant_list: [str] = restaurants.readlines()

    # Choose a random restaurant
    random_restaurant: [str] = random.choice(restaurant_list)

    # Strip the newline character from the end so the search is successful
    random_restaurant: [str] = random_restaurant.strip()

    # Initializing variable
    found_restaurant_url: str = ""

    # Search the nested tuples for the correct restaurant URLs matching the chosen random restaurant
    for restaurant in restaurant_urls:
        if random_restaurant in restaurant:
            found_restaurant_url: str = restaurant[1]

    return render_template("index.html", restaurant=random_restaurant, restaurant_link=found_restaurant_url)


if __name__ == "__main__":
    main()

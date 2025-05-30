# Where Should I Go Eat?

![A fast food restaurant on a sunny afternoon with vehicles parked in the parking lot attached to the restaurant. Above the restaurant is a sign with the phrase: Where Should I Go Eat](static/images/where_should_I_go_eat_gemini_generated.jpeg)

Hungry? Don't know where to go to eat? This website tells you at the click of a button.

## About The Program

This web applications uses the Bootstrap on the Front-End and Python/Flask on the Back-End to display either a
randomly-chosen chain restaurant and its URL for visitors to order food online, or a link to open Google Maps for a
visitor to choose a local restaurant.

## Program Dependencies

A modern web browser (like Google Chrome) with JavaScript enabled.

## Website

[whereshouldigoeat.com](https://www.whereshouldigoeat.com/)

## Found A Bug? Need Help?

Please file a new issue using the Issues tab on the repo.

## Version History

* Latest release notes as of May 2025:
    - Replaced some CSS rules with various Bootstrap ultilities.
    - Created a base template.
    - Changed the background image.
    - Moved the logic in the main.py file to find the random restaurant and its URL into a new function.
    - Added a new Event Listerned to the main.js file to disable the "Chain Restaurant" button after the user clicks it once.
    - Added additional screen sizes of the mobile media queries.
    - Added `if` statements to the Jinja index.html template.
    - Added a JavaScript function to display the results on the website after the visitor clicks the Chain Restaurant button.
        - Before this change when the page loaded the website displayed `You Should Go Eat At` and `Order Online At here`.
* Latest release notes as of April 2025:
    - Removed the inline onclick event handler from index.html.
    - Created index.js to contain the event handlers.
* Latest release notes as of February 2025:
    - Updated the README.
* Latest release notes as of January 2025:
    - Updated the footer on all pages to display all my social media links.
* Latest release notes as of late December 2024:
    - Refactored the program to use nested tuples instead of a SQLite database.
    - Improved the README.
    - Fixed typos and comment formatting.
    - Completed the CSS rules for desktop and mobile devices.
    - Updated the social media links in the index.html footer.
    - Removed unnecessary files from the repo.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

[Dominique Pizzie](https://gist.github.com/DomPizzie) for the simple README template.

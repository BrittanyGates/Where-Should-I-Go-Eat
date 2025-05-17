const chainRestaurantButton = document.querySelector("#chainRestaurantButton");
const localRestaurantButton = document.querySelector("#localRestaurantButton");
const resetButton = document.querySelector("#resetButton");
const restaurantResultElement = document.querySelector(".restaurant-result");
const restaurantLinkResultElement = document.querySelector(".restaurant-link")

chainRestaurantButton.addEventListener("click", (event) => {
    // Prevent the default form submission
    event.preventDefault();

    // Disable the button immediately after click
    chainRestaurantButton.disabled = true;

    fetch("/restaurant-result")
        .then(response => {
            // Check if the response is OK (status code 200-299)
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            return response.json();
        })
        .then(data => {
            if (data && data.restaurant && data.link) {
                restaurantResultElement.textContent = `You Should Go Eat At ${data.restaurant}`;
                restaurantLinkResultElement.innerHTML = `Order Online At ${data.restaurant} <a href="${data.link}" target="_blank">here</a>`;
            } else {
                restaurantResultElement.textContent = "Could not retrieve restaurant information.";
                restaurantLinkResultElement.textContent = "Could not retrieve restaurant URL.";
            }
        })
        .catch(error => {
            // Handle any errors during the fetch process
            console.error("Error fetching the restaurant:", error);
            restaurantResultElement.textContent = "An error occurred while finding a restaurant.";
            restaurantLinkResultElement.textContent = "An error occured while getting the restaurant URL.";
            // Re-enable button in case of error to allow retry
            chainRestaurantButton.disabled = false;
        });
});

localRestaurantButton.addEventListener("click", () => {
    window.open("https://www.google.com/maps/search/Restaurants/", "_blank");
});

resetButton.addEventListener("click", () => {
    location.reload();
});
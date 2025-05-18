const chainRestaurantButton = document.querySelector("#chainRestaurantButton");
const localRestaurantButton = document.querySelector("#localRestaurantButton");
const resetButton = document.querySelector("#resetButton");
const restaurantResultElement = document.querySelector(".restaurant-result");
const restaurantLinkElement = document.querySelector(".restaurant-link");

function showRestaurantLink() {
    if (restaurantLinkElement) {
        restaurantLinkElement.classList.add("is-visible");
    }
}

chainRestaurantButton.addEventListener("click", (event) => {
    // Prevent the default form submission
    event.preventDefault();

    // Disable the button immediately after click
    chainRestaurantButton.disabled = true;

    fetch("/restaurant-result")
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            return response.json();
        })
        .then(data => {
            if (data && data.restaurant && data.link) {
                restaurantResultElement.textContent = `You Should Go Eat At ${data.restaurant}`;

                if (restaurantLinkElement) {
                    restaurantLinkElement.innerHTML = `Order Online At ${data.restaurant} <a href="${data.link}" target="_blank">here</a>`;
                    showRestaurantLink();
                }
            } else {
                restaurantResultElement.textContent = "Could not retrieve restaurant information.";
                if (restaurantLinkElement) {
                    restaurantLinkElement.textContent = "";
                    restaurantLinkElement.classList.remove("is-visible");
                }
            }
        })
        .catch(error => {
            console.error("Error fetching the restaurant:", error);
            restaurantResultElement.textContent = "An error occurred while finding a restaurant.";
            if (restaurantLinkElement) {
                restaurantLinkElement.textContent = "";
                restaurantLinkElement.classList.remove("is-visible");
            }

            chainRestaurantButton.disabled = false;
        });
});

localRestaurantButton.addEventListener("click", () => {
    window.open("https://www.google.com/maps/search/Restaurants/", "_blank");
});

resetButton.addEventListener("click", () => {
    location.reload();
});
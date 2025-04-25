const chainRestaurantButton = document.querySelector("#chainRestaurantButton");
const localRestaurantButton = document.querySelector("#localRestaurantButton");
const resetButton = document.querySelector("#resetButton");

chainRestaurantButton.addEventListener("click", () => {
    fetch("/")
    .then(response => {
        return response.json();
    });
});

localRestaurantButton.addEventListener("click", () => {
    window.open("https://www.google.com/maps/search/?api=1&query=restaurants", "_blank");
});

resetButton.addEventListener("click", () => {
    location.href = location.href;
});
document.getElementById("fetch-btn").addEventListener("click", function() {
    const city = document.getElementById("city").value.trim();
    if (!city) {
        document.getElementById("error").innerText = "Please enter a city name.";
        document.getElementById("error").classList.remove("hidden");
        document.getElementById("result").classList.add("hidden");
        return;
    }

    const formData = new FormData();
    formData.append("city", city);

    fetch("/fetch_data", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById("error").innerText = data.error;
            document.getElementById("error").classList.remove("hidden");
            document.getElementById("result").classList.add("hidden");
        } else {
            document.getElementById("city-name").innerText = data.city;
            document.getElementById("temperature").innerText = data.temperature;
            document.getElementById("humidity").innerText = data.humidity;
            document.getElementById("ndvi").innerText = data.ndvi;
            document.getElementById("recommendation").innerText = data.recommendation;

            document.getElementById("result").classList.remove("hidden");
            document.getElementById("error").classList.add("hidden");
        }
    })
    .catch(error => {
        document.getElementById("error").innerText = "An error occurred. Please try again.";
        document.getElementById("error").classList.remove("hidden");
        document.getElementById("result").classList.add("hidden");
    });
});
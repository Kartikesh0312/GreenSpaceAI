document.getElementById("fetch-btn").addEventListener("click", function() {
    const latitude = document.getElementById("latitude").value;
    const longitude = document.getElementById("longitude").value;

    const formData = new FormData();
    formData.append("latitude", latitude);
    formData.append("longitude", longitude);

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
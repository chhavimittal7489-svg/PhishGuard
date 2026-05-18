document.getElementById("scanBtn")
.addEventListener("click", async () => {

    const [tab] = await chrome.tabs.query({
        active: true,
        currentWindow: true
    });

    const currentURL = tab.url;

    const resultDiv = document.getElementById("result");

    resultDiv.innerHTML = "Scanning...";


    try {

        const response = await fetch(

            `http://127.0.0.1:8000/predict?url=${encodeURIComponent(currentURL)}`,

            {
                method: "POST"
            }
        );

        const data = await response.json();

        resultDiv.innerHTML = `

            <h3 style="color:
            ${data.prediction === "Phishing" ? "red" : "lightgreen"}">

            ${data.prediction}

            </h3>

            <p>Risk Score:
            ${data.risk_score}%</p>

        `;

    }

    catch (error) {

        resultDiv.innerHTML =
        "Error connecting to backend";
    }
});
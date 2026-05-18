async function scanURL() {

    const url = document.getElementById("urlInput").value;

    const resultDiv = document.getElementById("result");

    resultDiv.innerHTML = "Scanning...";


    try {

        const response = await fetch(
            `http://127.0.0.1:8000/predict?url=${encodeURIComponent(url)}`,
            {
                method: "POST"
            }
        );

        const data = await response.json();

        resultDiv.innerHTML = `

            <h3>Prediction: ${data.prediction}</h3>

            <p>Risk Score: ${data.risk_score}%</p>

            <p><b>Registrar:</b>
            ${data.domain_info.registrar}</p>

            <p><b>Creation Date:</b>
            ${data.domain_info.creation_date}</p>

        `;

    }

    catch (error) {

        resultDiv.innerHTML = `
            Error connecting to backend
        `;
    }
}
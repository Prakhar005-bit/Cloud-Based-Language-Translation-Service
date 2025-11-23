async function translateText() {
    const text = document.getElementById("inputText").value;
    const target = document.getElementById("languageSelect").value;

    const API_URL = "YOUR_API_URL_HERE";  

    const response = await fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            text: text,
            target_language: target
        })
    });

    const data = await response.json();
    document.getElementById("outputText").innerText = data.translated_text;
}

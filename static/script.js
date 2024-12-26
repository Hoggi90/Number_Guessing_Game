document.getElementById("submitGuess").addEventListener("click", function () {
    const userGuess = document.getElementById("guessInput").value;

    fetch("/guess", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ guess: userGuess }),
    })
        .then((response) => response.json())
        .then(data => {
            document.getElementById('message').textContent = data.message;
            if (data.message.includes("correct")) {  // Check if the guess was correct
                document.querySelector('.tryAgainButton').style.display = 'inline-block';  // Show the button
            }
        })
        .catch((error) => {
            console.error("Error:", error);
        });
});
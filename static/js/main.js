const timerElement = document.getElementById("timer");
let seconds = {{q}};

function updateTimer() {
    const minutes = Math.floor(seconds / 60);
    const secondsRemaining = seconds % 60;

    const timerText = `${minutes.toString().padStart(2, '0')}:${secondsRemaining.toString().padStart(2, '0')}`;
    timerElement.textContent = timerText;

    if (seconds > 0) {
        seconds--;
        setTimeout(updateTimer, 1000);
    } else {
      document.getElementById("sa").submit();

    }
}

updateTimer();
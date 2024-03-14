<script>
    import './kevin.css'
    /**
	 * @type {HTMLDivElement}
	 */
    var body;
    /**
	 * @type {HTMLAudioElement}
	 */
    var audio;
    /**
	 * @type {HTMLDivElement}
	 */
    var epilepsyWarning;
    function displayRandomWord() {
        var words = ['WOW', 'MUCH LOVE', 'VERY AMAZE', 'DOGE', 'SUCH RAINBOW', '1 SHIBES', '2 SHIBES', '3 SHIBES', '4 SHIBES', '5 SHIBES', 'WOW', 'MUCH LOVE', 'VERY AMAZE', 'DOGE', 'SUCH RAINBOW',]; // doge words
        var randomWord = words[Math.floor(Math.random() * words.length)];
        var randomWordElement = document.createElement('div');
        randomWordElement.textContent = randomWord;
        randomWordElement.classList.add('randomWord');
        randomWordElement.style.left = Math.random() * (window.innerWidth - randomWordElement.offsetWidth) + 'px'; // Random horizontal position
        randomWordElement.style.top = Math.random() * (window.innerHeight - randomWordElement.offsetHeight) + 'px'; // Random vertical position
        body.appendChild(randomWordElement);
        setTimeout(function () {
            randomWordElement.remove(); // Remove the element after 2 seconds
        }, 2000);
    }

    /**
	 * @this {any}
	 */
    function onClick() {
        audio.play();
        audio.style.display = 'none'; // Hide the audio element
        this.style.display = 'none'; // Hide the play button once clicked

        // Hide the epilepsy warning
        epilepsyWarning.style.display = 'none';

        // Display random words
        setInterval(displayRandomWord, 100); // Display a new word every second

        // Function to change background color in a loop
        var colors = ['#770000', '#772700', '#777700', '#007700', '#000077', '#220077', '#770077']; // Rainbow colors
        var currentIndex = 0;

        function changeBackgroundColor() {
            body.style.backgroundColor = colors[currentIndex];
            currentIndex = (currentIndex + 1) % colors.length;
            setTimeout(changeBackgroundColor, 10); // Change color every 1 second
        }

        changeBackgroundColor(); // Start the color changing loop
    };
</script>

<div bind:this={body}>
    <div id="epilepsyWarning" bind:this={epilepsyWarning}>!! EPILEPSY WARNING !!</div>
        <!-- <h1>The Age of Exploration</h1> -->
        <button id="playButton">CLICK ME NOW</button>
        <audio id="audio" loop controls style="display: none;" bind:this={audio}>
            <source src="https://edwardmwild.github.io/assets/kevin-1.mp3" type="audio/mpeg">
            Your browser does not support the audio element.
        </audio>
</div>
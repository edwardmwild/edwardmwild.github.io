<script>
    // User's birthday (YYYY-MM-DD format)
    const birthday = '2008-08-21';

    // User's timezone
    const timezone = 'Europe/London';

    // Function to calculate age based on birthday
    /**
	 * @param {string | number | Date} birthday
	 */
    function calculateAge(birthday) {
        const today = new Date();
        const birthDate = new Date(birthday);
        let age = today.getFullYear() - birthDate.getFullYear();
        const monthDiff = today.getMonth() - birthDate.getMonth();
        if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
            age--;
        }
        return age;
    }

    /**
	 * @param {any} timezone
	 */
    function getCurrentDateTime(timezone) {
        const options = {
            timeZone: timezone,
            weekday: 'long',
            year: 'numeric',
            month: 'long',
            day: 'numeric',
            hour: 'numeric',
        };
        // @ts-ignore
        return new Intl.DateTimeFormat('en-US', options).format(new Date());
    }
</script>

<div class="pronouns-container">
    <div class="profile-header">
        <!-- svelte-ignore a11y-img-redundant-alt -->
        <img class="profile-picture" src="profile.jpg" alt="Profile Picture">
        <h1>@edwardwild_</h1>
    </div>
    <div class="flag">
        <img src="aro-flag.png" style="width: 20px; margin-right: 5px" alt="Aromantic flag">
        <span>Aromantic</span>
    </div>
    <div class="flag">
        <img src="ace-flag.png" style="width: 20px; margin-right: 5px" alt="Asexual flag">
        <span>Asexual</span>
    </div>
    <div class="bio">
        <p>
            <br>
            tl;dr:
            <br>
            - male, gender-inspecific, & platonic terms good
            <br>
            - female, romantic, & sexual terms bad</p>
        </div>
    <div class="age">
        <p id="user-age">Age: I am currently {calculateAge(birthday)} years old.</p>
    </div>

    <div class="timezone">
        <!-- <p id="user-timezone">Timezone: Calculating...</p> -->
        <p id="user-date">Date & Time: In my timezone ({timezone}), it is currently {getCurrentDateTime(timezone)}</p>
    </div>
    <div class="words">
        <div class="group">
            <!-- <h3 class="group-heading">Group One</h3> -->
            <div class="columns">
                <div class="column">
                    <h3 class="group-heading">Names</h3>
                    <p><span class="material-icons teal" title="preferred">favorite</span><span class="teal" title="preferred">Ed</span></p>
                    <p><span class="material-icons white" title="okay">thumb_up</span><span class="white" title="okay">Edward</span></p>
                    <p><span class="material-icons pale-red" title="i will unalive you">highlight_off</span><span class="pale-red" title="i will unalive you">if you know it, no you don't</span></p>
                </div>
                <div class="column">
                    <h3 class="group-heading">Pronouns</h3>
                    <p><span class="material-icons teal" title="preferred">favorite</span><span class="teal" title="preferred">he/him</span></p>
                    <p><span class="material-icons teal" title="preferred">favorite</span><span class="teal" title="preferred">they/them</span></p>
                    <p><span class="material-icons pale-red" title="i will unalive you">highlight_off</span><span class="pale-red" title="i will unalive you">she/her</span></p>
                    <p><span class="material-icons grey" title="try not to">thumb_down</span><span class="grey" title="try not to">anything/else</span></p>
                </div>
                <div class="column">
                    <h3 class="group-heading">Links</h3>
                    <p><a href="https://example.com" target="_blank"><span class="material-icons teal" title="preferred">favorite</span><span class="teal" title="preferred">Example</span></a></p>
                </div>
            </div>
        </div>
        <div class="group">
            <h3 class="group-heading">Words</h3>
            <div class="columns">
                <div class="column">
                    <!-- [no honorific]
                        mr.
                        sir
                        comrade
                        mrs.
                        ms.
                        mx.
                        ma'am
                        madam -->
                        <h2 class="column-heading">Honorifics/Titles</h2>
                        <p><span class="material-icons teal" title="preferred">favorite</span><span class="teal" title="preferred">[no honorific]</span></p>
                        <p><span class="material-icons teal" title="preferred">favorite</span><span class="teal" title="preferred">mr.</span></p>
                        <p><span class="material-icons white" title="okay">thumb_up</span><span class="white" title="okay">sir</span></p>
                        <p><span class="material-icons white" title="okay">thumb_up</span><span class="white" title="okay">comrade</span></p>
                        <p><span class="material-icons pale-red" title="i will unalive you">highlight_off</span><span class="pale-red" title="i will unalive you">mrs.</span></p>
                        <p><span class="material-icons pale-red" title="i will unalive you">highlight_off</span><span class="pale-red" title="i will unalive you">ms.</span></p>
                        <p><span class="material-icons pale-red" title="i will unalive you">highlight_off</span><span class="pale-red" title="i will unalive you">ma'am</span></p>
                        <p><span class="material-icons pale-red" title="i will unalive you">highlight_off</span><span class="pale-red" title="i will unalive you">madam</span></p>
                    </div>
                    <div class="column">
                        <!-- person
                            man
                            pal
                            bro
                            buddy
                            dude
                            boy
                            woman
                            lady
                            girl -->
                            <h2 class="column-heading">Person & Family descriptions</h2>
                                <p><span class="material-icons white" title="okay">thumb_up</span><span class="white" title="okay">person</span></p>
                                <p><span class="material-icons white" title="okay">thumb_up</span><span class="white" title="okay">man</span></p>
                                <p><span class="material-icons white" title="okay">thumb_up</span><span class="white" title="okay">mate</span></p>
                                <p><span class="material-icons white" title="okay">thumb_up</span><span class="white" title="okay">pal</span></p>
                                <p><span class="material-icons white" title="okay">thumb_up</span><span class="white" title="okay">bro</span></p>
                                <p><span class="material-icons white" title="okay">thumb_up</span><span class="white" title="okay">buddy</span></p>
                                <p><span class="material-icons white" title="okay">thumb_up</span><span class="white" title="okay">dude (in a stereotypical american accent)</span></p>
                                <p><span class="material-icons grey" title="try not to">thumb_down</span><span class="grey" title="try not to">boy</span></p>
                                <p><span class="material-icons pale-red" title="i will unalive you">highlight_off</span><span class="pale-red" title="i will unalive you">woman</span></p>
                                <p><span class="material-icons pale-red" title="i will unalive you">highlight_off</span><span class="pale-red" title="i will unalive you">lady</span></p>
                                <p><span class="material-icons pale-red" title="i will unalive you">highlight_off</span><span class="pale-red" title="i will unalive you">girl</span></p>
                            </div>
                            <div class="column">
                                <h2 class="column-heading">Compliments</h2>
                                    <p><span class="material-icons teal" title="preferred">favorite</span><span class="teal" title="preferred">pretty</span></p>
                                    <p><span class="material-icons white" title="okay">thumb_up</span><span class="white" title="okay">handsome</span></p>
                                    <p><span class="material-icons grey" title="try not to">thumb_down</span><span class="grey" title="try not to">cute</span></p>
                                    <p><span class="material-icons pale-red" title="i will unalive you">highlight_off</span><span class="pale-red" title="i will unalive you">hot</span></p>
                                    <p><span class="material-icons pale-red" title="i will unalive you">highlight_off</span><span class="pale-red" title="i will unalive you">sexy</span></p>
                                </div>
                                <div class="column">
                                    <!-- friend
                                        partner
                                        boyfriend
                                        husband
                                        darling
                                        wife -->
                                        <h2 class="column-heading">Relationship descriptions</h2>
                                            <p><span class="material-icons teal" title="preferred">favorite</span><span class="teal" title="preferred">friend</span></p>
                                            <p><span class="material-icons white" title="okay">thumb_up</span><span class="white" title="okay">boyfriend (if we're "dating")</span></p>
                                            <p><span class="material-icons grey" title="try not to">thumb_down</span><span class="grey" title="try not to">darling</span></p>
                                            <p><span class="material-icons grey" title="try not to">thumb_down</span><span class="grey" title="try not to">partner</span></p>
                                            <p><span class="material-icons grey" title="try not to">thumb_down</span><span class="grey" title="try not to">husband</span></p>
                                            <p><span class="material-icons pale-red" title="i will unalive you">highlight_off</span><span class="pale-red" title="i will unalive you">wife</span></p>
                                        </div>
            </div>
        </div>
    </div>
    <div class="footer">
        <p>
            <span class="material-icons teal">favorite</span> yes &bull; 
            <span class="material-icons white">thumb_up</span> okay &bull; 
            <span class="material-icons grey">thumb_down</span> not preferred &bull; 
            <span class="material-icons pale-red">highlight_off</span> i will unalive you
        </p>
    </div>
</div>
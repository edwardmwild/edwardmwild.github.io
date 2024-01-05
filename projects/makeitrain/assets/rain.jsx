export const className = `
    div#main {
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: -100;
        display: flex;
        position: fixed;
    }

    video {
        flex: 1 0 auto;
        object-fit: cover;
        width: 100vw;
        height: 100vh;
        top: 0;
        left: 0;
        position: fixed;
        z-index: 0;
        transition: opacity 2s;
        opacity: 0.2;
    }
`;

const play = (url) => {
    const video = document.getElementById("video");
    video.setAttribute("src", url);
    video.autoplay = true;
    video.load();
}

export const render = (urls) => {
    return (
        <div id="main">
            <video id="video" loop="true" playsInline autoPlay/>
        </div>
    );
};

// to anyone looking through this code: i have no clue what this bit does, but if i remove it, the thing breaks. it's not currently doing anything afaik
export const init = async (dispatch) => {
    await fetch("http://127.0.0.1:41417/https://bzamayo.com/extras/apple-tv-screensavers.json").then(res => res.json()).then(res => {
        dispatch(res.data);
    });
}

export const updateState = (data, previousState) => {
    const url = "https://edwardwild10.github.io/projects/makeitrain/assets/rain.mp4";
    play(url);
};

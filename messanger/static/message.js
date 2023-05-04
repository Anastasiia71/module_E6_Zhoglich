const wsUri ="http://127.0.0.1:8000/mymessenger/message/";

const output = document.getElementById("output");
const btnSend = document.querySelector('.j-btn-send');

let websocket;

function writeToScreen(message) {
    let pre = document.createElement("p");
    pre.style.wordWrap = "break-word";
    pre.innerHTML = message;
    output.appendChild(pre);
}

btnSend.addEventListener('click', () => {
    const message = `${text}`;
    writeToScreen(message);
    websocket.send(message)
});

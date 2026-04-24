async function sendMessage() {
    let input = document.getElementById("message");
    let text = input.value;
    if (!text) return;

    let chat = document.getElementById("chat-box");

    chat.innerHTML += `<div class="message user">🧑 ${text}</div>`;
    input.value = "";

    let response = await fetch("http://localhost:5000/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({text: text})
    });

    let data = await response.json();

    chat.innerHTML += `<div class="message bot">🤖 ${data.reply}</div>`;
    chat.scrollTop = chat.scrollHeight;
}

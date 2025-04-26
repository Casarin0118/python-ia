async function fetchBotResponse(messageText) {
    try {
        const response = await fetch(`${window.location.href}search?prompt=${messageText}`);
        if (!response.ok) {
            const errorData = await response.json();
            console.error('Erro na requisição:', response.status, errorData);
            return `Desculpe, ocorreu um erro: ${errorData.error || response.statusText}`;
        }
        const data = await response.json();
        return data.message;
    } catch (error) {
        console.error('Erro ao buscar dados:', error);
        return 'Desculpe, não consegui buscar uma resposta agora.';
    }
}

async function sendMessage() {
    const userInput = document.getElementById('userInput');
    const chatWindow = document.getElementById('chatWindow');
    const messageText = userInput.value.trim();

    if (messageText) {
        const userMessage = document.createElement('div');
        userMessage.className = 'message user';
        userMessage.innerHTML = `<span>${messageText}</span>`;
        chatWindow.appendChild(userMessage);

        userInput.value = '';

        const loadingMessage = document.createElement('div');
        loadingMessage.className = 'message bot loading';
        loadingMessage.innerHTML = `<span>Carregando...</span>`;
        chatWindow.appendChild(loadingMessage);
        chatWindow.scrollTop = chatWindow.scrollHeight;

        const botResponse = await fetchBotResponse(messageText);

        chatWindow.removeChild(loadingMessage);
        const botMessage = document.createElement('div');
        botMessage.className = 'message bot';
        botMessage.innerHTML = `<span>${botResponse}</span>`;
        chatWindow.appendChild(botMessage);

        chatWindow.scrollTop = chatWindow.scrollHeight;
    }
}

function checkEnter(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}
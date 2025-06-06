document.addEventListener('DOMContentLoaded', () => {
    const cityInput = document.getElementById('cityInput');
    const getWeatherBtn = document.getElementById('getWeatherBtn');
    const weatherResult = document.getElementById('weatherResult');
    const errorMessage = document.getElementById('errorMessage');

    getWeatherBtn.addEventListener('click', async () => {
        const city = cityInput.value.trim(); // Pega o valor e remove espaços em branco

        // Limpa mensagens anteriores
        weatherResult.innerHTML = '';
        errorMessage.textContent = '';
        errorMessage.style.display = 'none'; // Esconde a mensagem de erro

        if (city === '') {
            errorMessage.textContent = 'Por favor, digite o nome de uma cidade.';
            errorMessage.style.display = 'block';
            return; // Sai da função se a cidade estiver vazia
        }

        try {
            // Usando a Fetch API para fazer a requisição GET
            const response = await fetch(`/get_weather/?city=${encodeURIComponent(city)}`);
            const data = await response.json();

            if (response.ok) { // Verifica se a resposta foi bem-sucedida (status 2xx)
                displayWeather(data);
            } else { // Se houver um erro no servidor (4xx, 5xx)
                errorMessage.textContent = data.error || 'Ocorreu um erro ao obter a previsão.';
                errorMessage.style.display = 'block';
            }
        } catch (error) {
            console.error('Erro na requisição:', error);
            errorMessage.textContent = 'Não foi possível conectar ao servidor. Verifique sua conexão.';
            errorMessage.style.display = 'block';
        }
    });

    const displayWeather = (data) => {
        weatherResult.innerHTML = `
            <h2>Previsão do Tempo para ${data.city}</h2>
            <p><strong>Temperatura:</strong> ${data.temperatura}</p>
            <p><strong>Condição:</strong> ${data.condicao}</p>
            <p><strong>Umidade:</strong> ${data.umidade}</p>
        `;
    };
});
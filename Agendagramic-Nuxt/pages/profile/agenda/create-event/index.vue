<template>
  <div class="min-h-screen bg-gradient-green-inverse flex flex-col justify-between">
    <!-- Cabeçalho -->
    <header class="flex justify-between items-center px-8 py-4">
      <h1 class="text-4xl font-bold text-white">Criar Novo Evento</h1>
      <h3 class="text-3xl font-semibold text-white">AgendaGramic</h3>
    </header>

    <!-- Formulário de criação de evento -->
    <main class="flex flex-col items-center flex-1 px-6">
      <div class="bg-medium-gray shadow-green w-full max-w-4xl rounded-3xl p-8 border-white border-2">
        <h2 class="text-2xl font-semibold text-white mb-4">Detalhes do Evento</h2>

        <!-- Título do Evento -->
        <div class="mb-4">
          <label for="eventTitle" class="block text-white text-sm font-bold mb-2">Título do Evento</label>
          <input
            v-model="eventTitle"
            id="eventTitle"
            type="text"
            placeholder="Digite o título do evento"
            class="bg-input-gray shadow appearance-none border rounded-full w-full py-2 px-3 text-white"
          />
        </div>

        <!-- Descrição do Evento -->
        <div class="mb-4">
          <label for="eventDescription" class="block text-white text-sm font-bold mb-2">Descrição</label>
          <textarea
            v-model="eventDescription"
            id="eventDescription"
            rows="4"
            placeholder="Descreva o evento"
            class="bg-input-gray shadow appearance-none border rounded-lg w-full py-2 px-3 text-white"
          ></textarea>
        </div>

        <!-- Local do Evento -->
        <div class="mb-4">
          <label for="eventLocation" class="block text-white text-sm font-bold mb-2">Local do Evento</label>
          <input
            v-model="eventLocation"
            id="eventLocation"
            type="text"
            placeholder="Digite o local do evento"
            class="bg-input-gray shadow appearance-none border rounded-full w-full py-2 px-3 text-white"
          />
        </div>

        <!-- Data do Evento -->
        <div class="mb-4">
          <label for="eventDate" class="block text-white text-sm font-bold mb-2">Data do Evento</label>
          <input
            v-model="eventDate"
            id="eventDate"
            type="date"
            class="bg-input-gray shadow appearance-none border rounded-full w-full py-2 px-3 text-white"
          />
        </div>

        <!-- Horário do Evento -->
        <div class="mb-4">
          <label for="eventTime" class="block text-white text-sm font-bold mb-2">Horário do Evento</label>
          <input
            v-model="eventTime"
            id="eventTime"
            type="time"
            class="bg-input-gray shadow appearance-none border rounded-full w-full py-2 px-3 text-white"
          />
        </div>

        <!-- ID do Grupo -->
        <div class="mb-4">
          <label for="eventGroup" class="block text-white text-sm font-bold mb-2">ID do Grupo</label>
          <input
            v-model="eventGroup"
            id="eventGroup"
            type="text"
            placeholder="Digite o ID do grupo"
            class="bg-input-gray shadow appearance-none border rounded-full w-full py-2 px-3 text-white"
          />
        </div>

        <!-- Botões -->
        <div class="flex flex-col space-y-4">
          <button
            @click="createEvent"
            class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-6 rounded-full"
          >
            Criar Evento
          </button>
          <button
            @click="testConnection"
            class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-6 rounded-full"
          >
            Testar Conexão DB
          </button>
        </div>
      </div>
    </main>

    <!-- Rodapé -->
    <footer class="flex justify-between items-center px-8 py-4">
      <button
        @click="goBack"
        class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-6 rounded-full"
      >
        Voltar
      </button>
      <div class="text-gray-300">
        AgendaGramic Alpha 0.0.1
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const eventTitle = ref('');
const eventDescription = ref('');
const eventLocation = ref('');
const eventDate = ref('');
const eventTime = ref('');
const eventGroup = ref('');
const eventCreator = ref('default_user');

// Criar evento
const createEvent = async () => {
  if (!eventTitle.value || !eventDate.value || !eventGroup.value) {
    alert('Por favor, preencha todos os campos obrigatórios.');
    return;
  }

  const newEvent = {
    eventTitle: eventTitle.value,
    eventDescription: eventDescription.value || null,
    eventLocation: eventLocation.value || null,
    eventDate: eventDate.value,
    eventTime: eventTime.value || null,
    eventGroup: eventGroup.value,
    eventCreator: eventCreator.value,
  };

  try {
    const response = await axios.post('/api/addEvent', newEvent);

    if (response.data.success) {
      alert(`Evento criado com sucesso! ID do Evento: ${response.data.insertId}`);
    } else {
      alert('Erro ao criar o evento.');
    }
  } catch (error) {
    console.error('Erro ao criar evento:', error);
    alert('Erro ao criar evento no banco.');
  }
};

// Testar conexão com o banco
const testConnection = async () => {
  const dateToTest = eventDate.value || new Date().toISOString().split('T')[0]; // Usar a data de hoje se não fornecida

  try {
    const response = await axios.get('/api/getEvents', {
      params: { userTelegram: eventCreator.value, selectedDate: dateToTest },
    });

    if (response.data.success) {
      console.log('Eventos encontrados:', response.data.events);
      alert(`Conexão bem-sucedida! Eventos encontrados: ${response.data.events.length}`);
    } else {
      alert('Erro ao conectar ao banco de dados.');
    }
  } catch (error) {
    console.error('Erro ao testar conexão com o banco:', error);
    alert('Erro ao conectar ao banco de dados.');
  }
};

// Voltar para a página anterior
const goBack = () => {
  window.history.back();
};
</script>

<style scoped>
.bg-gradient-green-inverse {
  background: linear-gradient(to bottom, #32cd32, #1e1e1e);
}

.bg-medium-gray {
  background-color: #3c3c3c;
}

.bg-input-gray {
  background-color: #2e2e2e;
  color: white;
}

.shadow-green {
  box-shadow: 0 10px 15px rgba(50, 205, 50, 0.3);
}

button {
  transition: background-color 0.3s;
}

.bg-green-500 {
  background-color: #32cd32;
}

.bg-green-600:hover {
  background-color: #28a745;
}

.bg-blue-500 {
  background-color: #007bff;
}

.bg-blue-600:hover {
  background-color: #0056b3;
}

.bg-gray-500 {
  background-color: #6c757d;
}

.bg-gray-600:hover {
  background-color: #5a6268;
}

.rounded-full {
  border-radius: 9999px;
}
</style>

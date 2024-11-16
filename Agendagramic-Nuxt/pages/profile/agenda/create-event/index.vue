<template>
  <div class="min-h-screen bg-gradient-green-inverse flex flex-col justify-between">
    <!-- Cabeçalho -->
    <header class="flex justify-between items-center px-8 py-4">
      <h1 class="text-4xl font-bold text-white">Criar Evento</h1>
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
            class="bg-input-gray shadow appearance-none border rounded-full w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline"
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
            class="bg-input-gray shadow appearance-none border rounded-lg w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline"
          ></textarea>
        </div>

        <!-- Data do Evento -->
        <div class="mb-4">
          <label for="eventBeginDate" class="block text-white text-sm font-bold mb-2">Data do Evento</label>
          <input
            v-model="eventBeginDate"
            id="eventBeginDate"
            type="date"
            class="bg-input-gray shadow appearance-none border rounded-full w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline"
          />
        </div>

        <!-- Checkbox para evento de vários dias -->
        <div class="mb-4 flex items-center">
          <input
            v-model="showField"
            type="checkbox"
            id="additionalInfo"
            class="mr-2 h-5 w-5 text-blue-500 rounded focus:ring-2 focus:ring-blue-400 focus:ring-opacity-50"
          />
          <label for="additionalInfo" class="text-white text-sm font-semibold">Evento com duração maior que um dia.</label>
        </div>

        <!-- Data Final -->
        <div v-if="showField" class="mb-4">
          <label for="eventEndDate" class="block text-white text-sm font-bold mb-2">Data Final</label>
          <input
            v-model="eventEndDate"
            id="eventEndDate"
            type="date"
            class="bg-input-gray shadow appearance-none border rounded-full w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline"
          />
        </div>

        <!-- Horário de Início -->
        <div class="mb-4">
          <label for="eventBeginTime" class="block text-white text-sm font-bold mb-2">Horário de Início</label>
          <input
            v-model="eventBeginTime"
            id="eventBeginTime"
            type="time"
            class="bg-input-gray shadow appearance-none border rounded-full w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline"
          />
        </div>

        <!-- Horário de Término -->
        <div class="mb-4">
          <label for="eventEndTime" class="block text-white text-sm font-bold mb-2">Horário de Término</label>
          <input
            v-model="eventEndTime"
            id="eventEndTime"
            type="time"
            class="bg-input-gray shadow appearance-none border rounded-full w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline"
          />
        </div>

        <!-- Status do Evento -->
        <div class="mb-4">
          <label for="eventStatus" class="block text-white text-sm font-bold mb-2">Status do Evento</label>
          <select
            v-model="eventStatus"
            id="eventStatus"
            class="bg-input-gray shadow appearance-none border rounded-full w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline"
          >
            <option :value="0">Pendente</option>
            <option :value="1">Em Progresso</option>
            <option :value="2">Concluído</option>
          </select>
        </div>

        <!-- Grupo do Evento -->
        <div class="mb-4">
          <label for="eventGroup" class="block text-white text-sm font-bold mb-2">Grupo do Evento</label>
          <select
            v-model="eventGroup"
            id="eventGroup"
            class="bg-input-gray shadow appearance-none border rounded-full w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline"
          >
            <option :value="0">Nenhum</option>
            <option :value="1">Grupo 1</option>
            <option :value="2">Grupo 2</option>
          </select>
        </div>

        <!-- Botões -->
        <div class="text-center space-x-4">
          <button
            @click="createEvent"
            class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-6 rounded-full border-white border-2 transition"
          >
            Criar Evento
          </button>
          <button
            @click="testConnection"
            class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-6 rounded-full border-white border-2 transition"
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
        class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-6 rounded-full border-white border-2 transition"
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
import { useRouter, useRoute } from 'vue-router';
import axios from 'axios';

const router = useRouter();
const route = useRoute();
const day = route.params.id; // Obtém o dia da URL

const showField = ref(false); // Exibe o campo de data final

const eventTitle = ref('');
const eventDescription = ref('');
const eventBeginDate = ref('');
const eventEndDate = ref('');
const eventBeginTime = ref('');
const eventEndTime = ref('');
const eventStatus = ref(0);
const eventGroup = ref(0);

const createEvent = () => {
  if (!showField.value) eventEndDate.value = eventBeginDate.value;

  const eventBeginDateTime = `${eventBeginDate.value} ${eventBeginTime.value}`;
  const eventEndDateTime = `${eventEndDate.value} ${eventEndTime.value}`;

  const newEvent = {
    eventTitle: eventTitle.value,
    eventDescription: eventDescription.value,
    eventBeginDateTime,
    eventEndDateTime,
    eventStatus: eventStatus.value,
    eventGroup: eventGroup.value,
  };

  const eventsData = JSON.parse(localStorage.getItem('events')) || {};
  if (!eventsData[day]) eventsData[day] = [];
  eventsData[day].push(newEvent);
  localStorage.setItem('events', JSON.stringify(eventsData));

  router.push(`/profile/agenda/day/${day}`);
};

const goBack = () => {
  router.push(`/profile/agenda/day/${day}`);
};

const testConnection = async () => {
  try {
    const response = await axios.get('/api/testDbConnection');
    alert('Conexão bem-sucedida: ' + response.data.message);
  } catch (error) {
    alert('Erro ao conectar ao banco de dados.');
  }
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

.bg-blue-500:hover {
  background-color: #2563eb;
}

.rounded-full {
  border-radius: 9999px;
}
</style>

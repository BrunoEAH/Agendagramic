<template>
  <div class="min-h-screen bg-dark-gray p-6 flex flex-col justify-between border-white border-2">
    <div class="bg-gradient-green-inverse shadow-green min-h-screen flex flex-col justify-between">
      <!-- Cabeçalho da página com AgendaGramic -->
      <div class="flex justify-between items-center mb-6">
        <!-- Título da página -->
        <div>
          <h1 class="text-4xl font-bold text-white">Criar Evento</h1>
        </div>
        <!-- Nome do Projeto com fonte maior -->
        <div>
          <h3 class="text-3xl font-semibold text-white">AgendaGramic</h3> <!-- Fonte aumentada para 3xl -->
        </div>
      </div>

      <!-- Formulário de criação de evento -->
      <div class="bg-medium-gray p-6 rounded-lg shadow-md mb-6 border-lighter-gray border-2">
        <h2 class="text-2xl font-semibold text-white mb-4">Detalhes do Evento</h2>
        <!-- Título do Evento -->
        <div class="mb-4">
          <label class="block text-white text-sm font-bold mb-2" for="eventTitle">Título do Evento</label>
          <input v-model="eventTitle" class="bg-input-gray shadow appearance-none border rounded-lg w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline" id="eventTitle" type="text" placeholder="Digite o título do evento">
        </div>
        <!-- Data do Evento -->
        <div class="mb-4">
          <label class="block text-white text-sm font-bold mb-2" for="eventDate">Data do Evento</label>
          <input v-model="eventDate" class="bg-input-gray shadow appearance-none border rounded-lg w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline" id="eventDate" type="date">
        </div>
        <!-- Localização -->
        <div class="mb-4">
          <label class="block text-white text-sm font-bold mb-2" for="eventLocation">Localização</label>
          <input v-model="eventLocation" class="bg-input-gray shadow appearance-none border rounded-lg w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline" id="eventLocation" type="text" placeholder="Digite o local do evento">
        </div>
        <!-- Horário -->
        <div class="mb-4">
          <label class="block text-white text-sm font-bold mb-2" for="eventTime">Horário</label>
          <input v-model="eventTime" class="bg-input-gray shadow appearance-none border rounded-lg w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline" id="eventTime" type="time">
        </div>
        <button @click="createEvent" class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-full focus:outline-none focus:shadow-outline">Criar Evento</button>
      </div>

      <!-- Botão Voltar -->
      <div class="mt-6 flex justify-start">
        <button @click="goBack" class="bg-blue-500 text-white py-2 px-4 rounded-full hover:bg-blue-600 border-white border-2">Voltar</button>
      </div>

      <div class="text-center text-gray-300 mt-4">
        AgendaGramic Alpha 0.0.1
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter, useRoute } from 'vue-router';

const router = useRouter();
const route = useRoute();
const day = route.params.id;  // Pega o dia a partir da URL

const eventTitle = ref('');
const eventDate = ref('');
const eventLocation = ref('');
const eventTime = ref('');

// Função para criar um novo evento
const createEvent = () => {
  const newEvent = {
    eventTitle: eventTitle.value,
    eventDate: eventDate.value,
    eventLocation: eventLocation.value,
    eventTime: eventTime.value,
  };

  // Pega os eventos existentes no localStorage ou cria uma nova estrutura
  let eventsData = JSON.parse(localStorage.getItem('events')) || {};

  // Verifica se há eventos para o dia, se não, cria um array vazio para esse dia
  if (!eventsData[day]) {
    eventsData[day] = [];
  }

  // Adiciona o novo evento ao array do dia
  eventsData[day].push(newEvent);

  // Atualiza o localStorage com os novos dados
  localStorage.setItem('events', JSON.stringify(eventsData));

  // Redireciona de volta para a página do dia
  router.push(`/profile/agenda/day/${day}`);
};

// Função para voltar à página de agenda do dia
const goBack = () => {
  router.push(`/profile/agenda/day/${day}`);
};
</script>

<style scoped>
/* Fundo cinza escuro */
.bg-dark-gray {
  background-color: #1e1e1e;
}

/* Degradê verde de baixo para cima */
.bg-gradient-green-inverse {
  background: linear-gradient(to top, #32cd32, transparent 50%);
}

/* Sombra verde */
.shadow-green {
  box-shadow: 0 10px 15px rgba(50, 205, 50, 0.3);
}

/* Estilos para contêiner */
.bg-medium-gray {
  background-color: #3c3c3c;
}

.border-lighter-gray {
  border-color: #5a5a5a;
}

/* Input */
.bg-input-gray {
  background-color: #2e2e2e;
  color: white;
}

/* Estilo de sombra */
.shadow-md {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
}

/* Botões */
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

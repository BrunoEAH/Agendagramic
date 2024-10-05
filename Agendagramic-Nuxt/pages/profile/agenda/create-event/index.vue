<template>
  <div class="min-h-screen bg-gray-100 p-6 flex flex-col justify-between">
    <!-- Cabeçalho da página -->
    <div class="flex justify-between items-center mb-6">
      <div>
        <h1 class="text-4xl font-bold">Criar Evento</h1>
      </div>
      <div class="text-center">
        <h3 class="text-lg font-medium">AgendaGramic</h3>
      </div>
    </div>

    <!-- Formulário de criação de evento -->
    <div class="bg-white p-6 rounded-lg shadow-md">
      <h2 class="text-2xl font-semibold mb-4">Detalhes do Evento</h2>
      <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="eventTitle">Título do Evento</label>
        <input v-model="eventTitle" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="eventTitle" type="text" placeholder="Digite o título do evento">
      </div>
      <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="eventDate">Data do Evento</label>
        <input v-model="eventDate" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="eventDate" type="date">
      </div>
      <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="eventLocation">Localização</label>
        <input v-model="eventLocation" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="eventLocation" type="text" placeholder="Digite o local do evento">
      </div>
      <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="eventTime">Horário</label>
        <input v-model="eventTime" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="eventTime" type="time">
      </div>
      <button @click="createEvent" class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">Criar Evento</button>
    </div>

    <!-- Botão Voltar -->
    <div class="mt-6 flex justify-start">
      <button @click="goBack" class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">Voltar</button>
    </div>

    <div class="text-center text-gray-500 mt-4">
      AgendaGramic Alpha 0.0.1
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
.shadow {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
</style>

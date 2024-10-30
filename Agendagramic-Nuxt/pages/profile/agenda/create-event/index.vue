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

        <!-- Descrição da Tarefa -->
        <div class="mb-4">
          <label for="eventDescription" class="block text-white text-sm font-bold mb-2">Descrição</label>
          <textarea
            v-model="eventDescription"
            class="bg-input-gray shadow appearance-none border rounded-lg w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline"
            id="eventDescription"
            rows="4"
            placeholder="Descreva o evento"
          ></textarea>
        </div>

        <!-- Data do Evento -->
        <div class="mb-4">
          <label class="block text-white text-sm font-bold mb-2" for="eventBeginDate">Data do Evento</label>
          <input v-model="eventBeginDate" class="bg-input-gray shadow appearance-none border rounded-lg w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline" id="eventBeginDate" type="date">
        </div>

        <!---Botao para um evento com mais de um dia-->
        <div class="mb-4 flex items-center">
          <input v-model="showField" type="checkbox" id="additionalInfo" class="mr-2 h-5 w-5 text-blue-500 rounded focus:ring-2 focus:ring-blue-400 focus:ring-opacity-50">
          <label for="additionalInfo" class="text-white text-sm font-semibold">Evento com duração maior que um dia.</label>
        </div>

        <div v-if="showField" class="mb-4">
          <label class="block text-white text-sm font-bold mb-2" for="eventEndDate">Data do Evento</label>
          <input v-model="eventEndDate" class="bg-input-gray shadow appearance-none border rounded-lg w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline" id="eventEndDate" type="date">
        </div>


        <!--Localização 
        <div class="mb-4">
          <label class="block text-white text-sm font-bold mb-2" for="eventLocation">Localização</label>
          <input v-model="eventLocation" class="bg-input-gray shadow appearance-none border rounded-lg w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline" id="eventLocation" type="text" placeholder="Digite o local do evento">
        </div> -->

        <!-- Horário Comeco-->
        <div class="mb-4">
          <label class="block text-white text-sm font-bold mb-2" for="eventBeginTime">Horário de início</label>
          <input v-model="eventBeginTime" class="bg-input-gray shadow appearance-none border rounded-lg w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline" id="eventBeginTime" type="time">
        </div>


        <!-- Horário Fim-->
        <div class="mb-4">
          <label class="block text-white text-sm font-bold mb-2" for="eventEndTime">Horário do fim</label>
          <input v-model="eventEndTime" class="bg-input-gray shadow appearance-none border rounded-lg w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline" id="eventEndTime" type="time">
        </div>

          <!-- Status do Evento -->
            <div class="mb-4">
          <label for="eventStatus" class="block text-white text-sm font-bold mb-2">Status do Evento</label>
          <select
            v-model="eventStatus"
            class="bg-input-gray shadow appearance-none border rounded-lg w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline"
            id="eventStatus"
          >
            <option :value="0">Pendente</option>
            <option :value="1">Em Progresso</option>
            <option :value="2">Concluído</option>
          </select>
        </div>

        <!-- Grupo para o Evento -->
        <div class="mb-4">
          <label for="eventGroup" class="block text-white text-sm font-bold mb-2">Grupo para o Evento</label>
          <select
            v-model="eventGroup"
            class="bg-input-gray shadow appearance-none border rounded-lg w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline"
            id="eventGroup"
          >
            <option :value="0">Nenhum</option>
            <option :value="1">Grupo 1</option>
            <option :value="2">Grupo 2</option>
          </select>
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

const showField = ref(false);// Botao de exibir a data final

var event_ID = 3;
const eventTitle = ref('');
const eventDescription = ref('');
const eventBeginDate = ref('');
const eventEndDate = ref('');
//const eventLocation = ref('');
const eventBeginTime = ref('');
const eventEndTime = ref('');
const eventStatus = ref(0);
const eventCreator = "@SeuUsuario";
const eventGroup = ref(0);


// Função para criar um novo evento
const createEvent = async () => {
  
  if(!showField.value)
    eventEndDate.value = eventBeginDate.value;
  
  const eventBeginDateTime = `${eventBeginDate.value} ${eventBeginTime.value}`;
  const eventEndDateTime = `${eventEndDate.value} ${eventEndTime.value}`;

  event_ID++;

  const newEvent = {
    event_ID: event_ID,
    eventTitle: eventTitle.value,
    eventDescription: eventDescription.value,
    eventBeginDateTime,  // Start date and time
    eventEndDateTime,    // End date and time
    eventGroup: eventGroup.value,
    eventCreator,
    eventStatus: eventStatus.value
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

  try {
    const { data, error } = await $fetch('/api/addEvent', {
      method: 'POST',
      body: newEvent,
    });

    if (error.value) {
      throw new Error(error.value); // Handle fetch error
    }

    console.log('Usuario adicionado com sucesso!', data.value);
    // Redireciona de volta para a página do dia
    router.push(`/profile/agenda/day/${day}`);
  } catch (error) {
    console.error('Errado ao adicionar o evento:', error);
    alert('Errado ao adicionar o evento.');
  }

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

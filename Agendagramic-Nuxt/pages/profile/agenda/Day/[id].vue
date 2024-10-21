<template>
  <div class="min-h-screen bg-dark-gray p-6 flex flex-col justify-between border-white border-2">
    <div class="bg-gradient-green-inverse shadow-green min-h-screen flex flex-col justify-between">
      <!-- Cabeçalho da página com AgendaGramic -->
      <div class="flex justify-between items-center mb-6">
        <!-- Nome da página e o dia -->
        <div>
          <h1 class="text-4xl font-bold text-white">Eventos e Tarefas</h1>
          <h2 class="text-xl text-gray-300">Dia: {{ day }}</h2>
        </div>

        <!-- Nome do Projeto com fonte maior -->
        <div>
          <h3 class="text-3xl font-semibold text-white">AgendaGramic</h3>
        </div>
      </div>

      <!-- Listagem de Tarefas -->
      <div class="bg-medium-gray p-6 rounded-lg shadow-md mb-6 border-lighter-gray border-2">
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-2xl font-semibold text-white">Tarefas</h2>
          <button @click="goToCreateTask" class="bg-green-500 text-white py-2 px-4 rounded-full hover:bg-green-600 border-white border-2">
            Criar Tarefa
          </button>
        </div>
        <div v-if="tasks.length > 0">
          <ul>
            <li v-for="(task, index) in tasks" :key="index" class="mt-2 text-white">
              <strong>{{ task.taskName }}</strong> - Status: {{ task.taskStatus }}
            </li>
          </ul>
        </div>
        <div v-else>
          <p class="text-lg text-gray-400">Sem tarefas para esse dia.</p>
        </div>
      </div>

      <!-- Listagem de Eventos -->
      <div class="bg-medium-gray p-6 rounded-lg shadow-md mb-6 border-lighter-gray border-2">
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-2xl font-semibold text-white">Eventos</h2>
          <button @click="goToCreateEvent" class="bg-green-500 text-white py-2 px-4 rounded-full hover:bg-green-600 border-white border-2">
            Criar Evento
          </button>
        </div>
        <div v-if="events.length > 0">
          <ul>
            <li v-for="(event, index) in events" :key="index" class="mt-2 text-white">
              <strong>{{ event.eventTitle }}</strong> - Local: {{ event.eventLocation }} - Horário: {{ event.eventTime }}
            </li>
          </ul>
        </div>
        <div v-else>
          <p class="text-lg text-gray-400">Sem eventos para esse dia.</p>
        </div>
      </div>

      <!-- Botão Voltar no canto inferior esquerdo -->
      <div class="mt-6 flex justify-start">
        <button @click="goBackToAgenda" class="bg-blue-500 text-white py-2 px-4 rounded-full hover:bg-blue-600 border-white border-2">
          Voltar
        </button>
      </div>

      <!-- Rodapé com versão -->
      <div class="text-center text-gray-300 mt-4">
        AgendaGramic Alpha 0.0.1
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();
const day = route.params.id; // Obtém o parâmetro 'id' da URL para representar o dia

const tasks = ref([]);
const events = ref([]);

// Função para redirecionar para a página de erro
const redirectToErrorPage = () => {
  router.push('/profile/error');
};

// Função para buscar dados de tarefas e eventos do localStorage
onMounted(() => {
  // Verifica se o dia é inválido
  if (day < 1 || day > 31) {
    redirectToErrorPage();
    return;
  }

  const tasksData = JSON.parse(localStorage.getItem('tasks')) || {};
  const eventsData = JSON.parse(localStorage.getItem('events')) || {};

  // Verifica se há dados de tarefas e eventos para o dia atual
  tasks.value = tasksData[day] || [];
  events.value = eventsData[day] || [];
});

// Função para redirecionar para a criação de tarefa
const goToCreateTask = () => {
  router.push(`/profile/agenda/create-task?day=${day}`);
};

// Função para redirecionar para a criação de evento
const goToCreateEvent = () => {
  router.push(`/profile/agenda/create-event?day=${day}`);
};

// Função para voltar para a página de Agenda
const goBackToAgenda = () => {
  router.push(`/profile/agenda`);
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

/* Contêiner de tarefas e eventos */
.bg-medium-gray {
  background-color: #3c3c3c;
}

.border-lighter-gray {
  border-color: #5a5a5a;
}

/* Estilo de textos */
.text-white {
  color: white;
}

.text-gray-300 {
  color: #d1d5db;
}

.text-gray-400 {
  color: #9ca3af;
}

/* Estilos para botões arredondados */
button {
  transition: background-color 0.3s;
  border-radius: 99px; /* Totalmente arredondado */
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

/* Estilo de sombra */
.shadow-md {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
}

.rounded-lg {
  border-radius: 48px;
}
</style>

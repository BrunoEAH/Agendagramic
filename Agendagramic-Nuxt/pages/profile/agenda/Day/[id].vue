<template>
  <div class="min-h-screen bg-gray-100 p-6 flex flex-col justify-between">
    <!-- Cabeçalho da página com AgendaGramic -->
    <div class="flex justify-between items-center mb-6">
      <!-- Nome da página e o dia -->
      <div>
        <h1 class="text-4xl font-bold">Eventos e Tarefas</h1>
        <h2 class="text-xl text-gray-500">Dia: {{ day }}</h2>
      </div>

      <!-- Nome do Projeto -->
      <div>
        <h3 class="text-xl font-medium">AgendaGramic</h3>
      </div>
    </div>

    <!-- Listagem de Tarefas -->
    <div class="bg-white p-6 rounded-lg shadow-md mb-6">
      <div class="flex justify-between items-center mb-4">
        <h2 class="text-2xl font-semibold">Tarefas</h2>
        <button @click="goToCreateTask" class="bg-green-500 text-white py-2 px-4 rounded hover:bg-green-600">
          Criar Tarefa
        </button>
      </div>
      <div v-if="tasks.length > 0">
        <ul>
          <li v-for="(task, index) in tasks" :key="index" class="mt-2">
            <strong>{{ task.taskName }}</strong> - Status: {{ task.taskStatus }}
          </li>
        </ul>
      </div>
      <div v-else>
        <p class="text-lg text-gray-600">Sem tarefas para esse dia.</p>
      </div>
    </div>

    <!-- Listagem de Eventos -->
    <div class="bg-white p-6 rounded-lg shadow-md mb-6">
      <div class="flex justify-between items-center mb-4">
        <h2 class="text-2xl font-semibold">Eventos</h2>
        <button @click="goToCreateEvent" class="bg-green-500 text-white py-2 px-4 rounded hover:bg-green-600">
          Criar Evento
        </button>
      </div>
      <div v-if="events.length > 0">
        <ul>
          <li v-for="(event, index) in events" :key="index" class="mt-2">
            <strong>{{ event.eventTitle }}</strong> - Local: {{ event.eventLocation }} - Horário: {{ event.eventTime }}
          </li>
        </ul>
      </div>
      <div v-else>
        <p class="text-lg text-gray-600">Sem eventos para esse dia.</p>
      </div>
    </div>

    <!-- Botão Voltar no canto inferior esquerdo -->
    <div class="mt-6 flex justify-start">
      <button @click="goBackToAgenda" class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
        Voltar
      </button>
    </div>

    <!-- Rodapé com versão -->
    <div class="text-center text-gray-500 mt-4">
      AgendaGramic Alpha 0.0.1
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();
const day = route.params.id;
const tasks = ref([]);
const events = ref([]);

// Função para buscar dados de tarefas e eventos do localStorage
onMounted(() => {
  const tasksData = JSON.parse(localStorage.getItem('tasks')) || {};
  const eventsData = JSON.parse(localStorage.getItem('events')) || {};

  tasks.value = tasksData[day] || [];
  events.value = eventsData[day] || [];
});

// Função para redirecionar para a criação de tarefa
const goToCreateTask = () => {
  router.push(`/profile/agenda/create-task`);
};

// Função para redirecionar para a criação de evento
const goToCreateEvent = () => {
  router.push(`/profile/agenda/create-event`);
};

// Função para voltar para a página de Agenda
const goBackToAgenda = () => {
  router.push(`/profile/agenda`);
};
</script>

<style scoped>
/* Estilos para manter o padrão visual */
.bg-gray-100 {
  background-color: #f7fafc;
}

.bg-white {
  background-color: white;
}

.rounded-lg {
  border-radius: 0.5rem;
}

.shadow-md {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.text-gray-600 {
  color: #4b5563;
}

.text-gray-500 {
  color: #6b7280;
}

.text-xl {
  font-size: 1.25rem;
}

.text-2xl {
  font-size: 1.5rem;
}

.text-4xl {
  font-size: 2.25rem;
}

.flex {
  display: flex;
}

.items-center {
  align-items: center;
}

.justify-between {
  justify-content: space-between;
}

.bg-green-500 {
  background-color: #10b981;
}

.bg-green-600:hover {
  background-color: #059669;
}

.bg-blue-500:hover {
  background-color: #2563eb;
}
</style>

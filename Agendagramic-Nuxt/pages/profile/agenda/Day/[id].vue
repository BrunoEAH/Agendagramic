<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';

const route = useRoute();
const router = useRouter();

// Extraindo a data da rota
const selectedDate = ref(route.params.id || new Date().toISOString().split('T')[0]);

const tasks = ref([]);
const events = ref([]);

// Função para formatar data e hora
const formatDateTime = (dateTime) => {
  return new Date(dateTime).toLocaleString('pt-BR', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  });
};

// Função para redirecionar à página de erro com mensagem personalizada
const redirectToErrorPage = (message = 'Erro ao carregar dados.') => {
  router.push({
    path: '/profile/error',
    query: { message },
  });
};

// Função para carregar tarefas e eventos
const loadTasksAndEvents = async () => {
  try {
    const userTelegram = localStorage.getItem('userTelegram') || 'default_user';

    const [tasksResponse, eventsResponse] = await Promise.all([
      axios.get('/api/getTasks', { params: { userTelegram, selectedDate: selectedDate.value } }),
      axios.get('/api/getEvents', { params: { userTelegram, selectedDate: selectedDate.value } }),
    ]);

    // Atualiza tarefas e eventos
    tasks.value = tasksResponse.data.tasks.map((task) => ({
      ...task,
      esta_completa: Boolean(task.esta_completa),
    }));
    events.value = eventsResponse.data.events;

    console.log('Tarefas carregadas:', tasks.value);
    console.log('Eventos carregados:', events.value);
  } catch (error) {
    console.error('Erro ao carregar tarefas e eventos:', error);
    redirectToErrorPage('Erro ao carregar tarefas e eventos.');
  }
};

// Função para testar conexão com tarefas e eventos
const testConnection = async () => {
  try {
    const userTelegram = localStorage.getItem('userTelegram') || 'default_user';
    const testDate = selectedDate.value;

    // Testa conexão com tarefas
    const tasksResponse = await axios.get('/api/getTasks', {
      params: { userTelegram, selectedDate: testDate },
    });
    console.log('Teste de conexão - Tarefas:', tasksResponse.data.tasks);

    // Testa conexão com eventos
    const eventsResponse = await axios.get('/api/getEvents', {
      params: { userTelegram, selectedDate: testDate },
    });
    console.log('Teste de conexão - Eventos:', eventsResponse.data.events);

    alert('Conexão testada com sucesso! Confira os resultados no console.');
  } catch (error) {
    console.error('Erro ao testar conexão:', error);
    alert('Erro ao testar conexão. Confira o console para mais detalhes.');
  }
};

// Navegar para criação de tarefa
const goToCreateTask = () => {
  router.push(`/profile/agenda/create-task?day=${selectedDate.value}`);
};

// Navegar para criação de evento
const goToCreateEvent = () => {
  router.push(`/profile/agenda/create-event?day=${selectedDate.value}`);
};

// Voltar para a agenda
const goBackToAgenda = () => {
  router.push('/profile/agenda');
};

// Carregar dados ao montar o componente
onMounted(() => {
  loadTasksAndEvents();
});
</script>

<template>
  <div class="min-h-screen bg-gradient-green-inverse flex flex-col justify-between">
    <!-- Cabeçalho -->
    <header class="flex justify-between items-center px-8 py-4">
      <div>
        <h1 class="text-4xl font-bold text-white">Eventos e Tarefas</h1>
        <h2 class="text-xl text-gray-300">Data: {{ selectedDate }}</h2>
      </div>
      <h3 class="text-3xl font-semibold text-white">AgendaGramic</h3>
    </header>

    <!-- Conteúdo principal -->
    <main class="flex flex-col items-center justify-center flex-1 px-6">
      <!-- Botão para testar a conexão -->
      <div class="mb-6">
        <button
          @click="testConnection"
          class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-6 rounded-full border-white border-2 transition"
        >
          Testar Conexão com Tarefas e Eventos
        </button>
      </div>

      <!-- Caixa de Tarefas -->
      <div class="bg-medium-gray shadow-green w-full max-w-4xl rounded-3xl p-8 border-white border-2 mb-6">
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-2xl font-semibold text-white">Tarefas</h2>
          <button
            @click="goToCreateTask"
            class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-6 rounded-full border-white border-2 transition"
          >
            Criar Tarefa
          </button>
        </div>
        <div v-if="tasks.length > 0">
          <ul>
            <li v-for="task in tasks" :key="task.task_id" class="mt-2 text-white">
              <strong>{{ task.titulo }}</strong> - 
              Status: {{ task.esta_completa ? 'Concluída' : 'Pendente' }} -
              Prioridade: {{ task.prioridade }}
              <p class="text-sm text-gray-300">{{ task.info_task }}</p>
            </li>
          </ul>
        </div>
        <div v-else>
          <p class="text-lg text-gray-400">Sem tarefas para esse dia.</p>
        </div>
      </div>

      <!-- Caixa de Eventos -->
      <div class="bg-medium-gray shadow-green w-full max-w-4xl rounded-3xl p-8 border-white border-2">
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-2xl font-semibold text-white">Eventos</h2>
          <button
            @click="goToCreateEvent"
            class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-6 rounded-full border-white border-2 transition"
          >
            Criar Evento
          </button>
        </div>
        <div v-if="events.length > 0">
          <ul>
            <li v-for="event in events" :key="event.event_id" class="mt-2 text-white">
              <strong>{{ event.titulo }}</strong>
              <p class="text-sm">Início: {{ formatDateTime(event.data) }} às {{ event.horario }}</p>
              <p class="text-sm text-gray-300">{{ event.descricao }}</p>
              <p class="text-sm">Local: {{ event.local }}</p>
            </li>
          </ul>
        </div>
        <div v-else>
          <p class="text-lg text-gray-400">Sem eventos para esse dia.</p>
        </div>
      </div>
    </main>

    <!-- Rodapé -->
    <footer class="flex justify-between items-center px-8 py-4">
      <button
        @click="goBackToAgenda"
        class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-6 rounded-full border-white border-2 transition"
      >
        Voltar
      </button>
      <div class="text-gray-300">
        AgendaGramic Beta 0.1
      </div>
    </footer>
  </div>
</template>

<style scoped>
.bg-gradient-green-inverse {
  background: linear-gradient(to bottom, #32cd32, #1e1e1e);
}

.shadow-green {
  box-shadow: 0 10px 15px rgba(50, 205, 50, 0.3);
}

.bg-medium-gray {
  background-color: #3c3c3c;
}

.bg-blue-500:hover {
  background-color: #2563eb;
}

.bg-green-500:hover {
  background-color: #2ea043;
}

.rounded-3xl {
  border-radius: 2rem;
}
</style>

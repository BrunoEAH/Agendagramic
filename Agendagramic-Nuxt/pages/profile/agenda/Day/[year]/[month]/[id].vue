<template>
  <div class="min-h-screen bg-gradient-green-inverse flex flex-col justify-between">
    <!-- Cabeçalho -->
    <header class="flex justify-between items-center px-8 py-4">
      <div>
        <h1 class="text-4xl font-bold text-white">Eventos e Tarefas</h1>
        <h2 class="text-xl text-gray-300">Dia: {{ ano }}-{{ mes }}-{{ dia }}</h2>
      </div>
      <div>
        <h3 class="text-3xl font-semibold text-white">AgendaGramic</h3>
      </div>
    </header>

    <!-- Conteúdo Principal -->
    <main class="flex flex-col items-center justify-center flex-1 px-6">
      <!-- Tarefas -->
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
            <li v-for="(task, index) in tasks" :key="index" class="mt-2 text-white">
              <strong>{{ task.name }}</strong> - Status: {{ task.esta_completa ? 'Concluída' : 'Pendente' }}
            </li>
          </ul>
        </div>
        <div v-else>
          <p class="text-lg text-gray-400">Sem tarefas para esse dia.</p>
        </div>
      </div>

      <!-- Eventos -->
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
            <li v-for="(event, index) in events" :key="index" class="mt-2 text-white">
              <strong>{{ event.name }}</strong> - Local: {{ event.location }} - Horário: {{ event.eventTime }}
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
        AgendaGramic
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';

const route = useRoute();
const router = useRouter();
//const day = route.params.id; // Obtém o parâmetro 'id' da URL para representar o dia

const tasks = ref([]);
const events = ref([]);

const user = ref('default_user');

const ano = ref(parseInt(route.params.year));
const mes = ref(parseInt(route.params.month));
const dia = ref(parseInt(route.params.id));



console.log(`Eventos e tarefas para ${ano.value}-${mes.value}-${dia.value}`);

// Redireciona para a página de erro se o dia for inválido
const redirectToErrorPage = () => {
  router.push('/profile/error');
};

// Carrega tarefas e eventos do banco de dados para o dia selecionado
const loadTasksAndEvents = async() => {
  try {
        const response = await axios.get(`http://localhost:5000/api/eventsetask`, {
          params: {
            userTelegram: user.value,
            year: ano.value,
            month: mes.value,
            day: dia.value,
          },
        });
        console.log('API Response:', response.data);
        if (response.data.success) {
            tasks.value = response.data.tasks || [];
            events.value = response.data.events || [];
        } else {
          console.error('Failed to fetch groups:', response.data.message);
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
};

// Navega para a criação de tarefas
const goToCreateTask = () => {
  router.push(`/profile/agenda/create-task`);
};

// Navega para a criação de eventos
const goToCreateEvent = () => {
  router.push(`/profile/agenda/create-event`);
};


const validateDate = () => {
  if (!ano || !mes || !dia || ano < 1900 || mes < 1 || mes > 12 || dia < 1 || dia > 31) {
    router.push('/profile/error');
    return false;
  }
  return true;
};


// Retorna para a página de Agenda
const goBackToAgenda = () => {
  router.push('/profile/agenda');
};

// Chamada inicial para carregar os dados ao montar o componente
onMounted(() => {
  if (!validateDate()) return;
  if (process.client) {
    const storedTelegram = localStorage.getItem('userTelegram');
    if (storedTelegram) {
      user.value = storedTelegram;
      loadTasksAndEvents();
    } else {
      console.warn('No Telegram ID found in local storage.');
    }
  }
});
</script>

<style scoped>
/* Fundo e gradiente */
.bg-gradient-green-inverse {
  background: linear-gradient(to bottom, #32cd32, #1e1e1e);
}
.bg-medium-gray {
  background-color: #3c3c3c;
}

/* Sombra verde */
.shadow-green {
  box-shadow: 0 10px 15px rgba(50, 205, 50, 0.3);
}

/* Estilo de texto */
.text-gray-300 {
  color: #d1d5db;
}
.text-gray-400 {
  color: #9ca3af;
}

/* Botões arredondados */
button {
  transition: background-color 0.3s;
}
.bg-green-700 {
  background-color: #32cd32;
}
.bg-green-600:hover {
  background-color: #28a745;
}
.bg-blue-500:hover {
  background-color: #2563eb;
}

/* Bordas arredondadas */
.rounded-3xl {
  border-radius: 4rem;
}
</style>

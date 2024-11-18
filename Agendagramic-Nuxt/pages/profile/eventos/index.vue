<template>
  <div class="min-h-screen bg-gradient-green-inverse flex flex-col justify-between">
    <header class="flex justify-between items-center px-8 py-4">
      <h1 class="text-4xl font-bold text-white">AgendaGramic</h1>
    </header>
    <main class="flex flex-col items-center justify-center flex-1 px-6">
      <div class="bg-medium-gray shadow-green w-full max-w-2xl rounded-3xl overflow-hidden p-8 border-white border-2">
        <header class="text-center mb-8">
          <h1 class="text-4xl font-bold text-white">Meus Eventos</h1>
          <p class="text-gray-300">Gerencie seus eventos de forma prática e eficiente.</p>
        </header>
        <div class="bg-dark-gray p-6 rounded-3xl shadow-md border-lighter-gray border-2 mb-6">
          <h2 class="text-2xl font-semibold text-white mb-4 text-center">Eventos do Usuário</h2>
          <div v-if="Userevents.length > 0" class="space-y-4">
            <div
              v-for="(event, index) in Userevents"
              :key="index"
              class="p-4 rounded-lg bg-light-gray shadow-lg"
            >
              <h3 class="text-xl font-semibold text-white">{{ event.name }}</h3>
              <p class="text-gray-300">{{ event.description }}</p>
              <p class="text-gray-300">Data de inicio: {{ new Date(event.date_begin).toLocaleString() }}</p>
              <p class="text-gray-300">Data de termino: {{ new Date(event.date_end).toLocaleString() }}</p>
              <p class="text-gray-400 text-sm">
              Status: 
              <span v-if="event.status === 0">Pendente</span>
              <span v-else-if="event.status === 1">Em Progresso</span>
              <span v-else-if="event.status === 2">Completa</span>
              <span v-else>Desconhecido</span>
            </p>
            </div>
          </div>
          <div v-else class="text-center">
            <p class="text-gray-400 text-lg">Nenhum evento encontrado para este usuário.</p>
          </div>
        </div>
        <div class="text-center space-y-4">
          <button
            @click="goToCreateEvent"
            class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-6 rounded-full border-white border-2 transition"
          >
            Criar Novo Evento
          </button>
          <button
            @click="testConnection"
            class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-6 rounded-full border-white border-2 transition"
          >
            Testar Conexão
          </button>
        </div>
      </div>
    </main>
    <footer class="flex justify-start items-center px-8 py-4">
      <button
        @click="goBack"
        class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-full border-white border-2 transition"
      >
        Voltar
      </button>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

const router = useRouter();
const Userevents = ref([]);
const user = ref('default_user');

// Função para carregar eventos do backend
const loadEvents = async () => {
  try {
    const userTelegram = user.value;
    const response = await $fetch(`/api/getEvents?userTelegram=${encodeURIComponent(userTelegram)}`);
    console.log('API Response:', response);

    if (response.success) {
      let event_arr = [];

      if (response.events && typeof response.events === 'object') {
        event_arr = [response.events];
      } else if (Array.isArray(response.events)) {
        event_arr = response.events;
      }

      Userevents.value = event_arr.map(event => ({
        name: event.name || 'Sem nome',
        description: event.description || 'Sem descrição',
        date_begin : event.date_begin,
        date_end : event.date_end,
        status: event.status, // Assuming 1 means completed
      }));
    } else {
      console.error('Failed to fetch tasks.');
    }
  } catch (error) {
    console.error('Error fetching tasks:', error);
  }
};

// Função para testar a conexão com o banco de dados
const testConnection = async () => {
  try {
    const response = await axios.get('/api/getEvents', {
      params: { userTelegram: 'test_user' }, // Usuário fictício para teste
    });
    if (response.status === 200) {
      if (response.data.events && response.data.events.length > 0) {
        alert('Conexão bem-sucedida! Eventos encontrados.');
      } else {
        alert('Conexão bem-sucedida, mas nenhum evento foi encontrado.');
      }
    } else {
      alert('Conexão falhou!');
    }
  } catch (error) {
    alert('Erro ao testar conexão com o banco de dados.');
    console.error(error);
  }
};

// Redirecionar para criar novo evento
const goToCreateEvent = () => {
  router.push('/profile/agenda/create-event');
};

// Função de voltar
const goBack = () => {
  router.push('/profile');
};

// Carregar eventos ao montar o componente
onMounted(async () => {
  if (process.client) {
    const storedTelegram = localStorage.getItem('userTelegram');
    if (storedTelegram) {
      user.value = storedTelegram;
      await loadEvents();
    } else {
      console.warn('No Telegram ID found in local storage.');
    }
  }
});

</script>

<style scoped>
/* Estilização */
.bg-dark-gray {
  background-color: #1e1e1e;
}
.bg-gradient-green-inverse {
  background: linear-gradient(to bottom, #32cd32, #1e1e1e);
}
.shadow-green {
  box-shadow: 0 10px 15px rgba(50, 205, 50, 0.3);
}
.bg-medium-gray {
  background-color: #3c3c3c;
}
.bg-light-gray {
  background-color: #2e2e2e;
}
.border-lighter-gray {
  border-color: #5a5a5a;
}
.text-gray-300 {
  color: #d1d5db;
}
.text-gray-400 {
  color: #9ca3af;
}
button {
  transition: background-color 0.3s, border-color 0.3s;
}
.bg-blue-500:hover {
  background-color: #2563eb;
}
.bg-green-500:hover {
  background-color: #2ea043;
}
.bg-gray-500:hover {
  background-color: #4a5568;
}
.rounded-3xl {
  border-radius: 1.5rem;
}
.rounded-lg {
  border-radius: 0.5rem;
}
.rounded-full {
  border-radius: 9999px;
}
</style>

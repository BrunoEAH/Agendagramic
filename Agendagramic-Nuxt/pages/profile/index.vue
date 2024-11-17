<template>
  <div class="min-h-screen bg-gradient-green-inverse flex flex-col justify-between">
    <!-- Cabeçalho -->
    <header class="flex justify-between items-center px-8 py-4">
      <h1 class="text-4xl font-bold text-white">AgendaGramic</h1>
    </header>

    <!-- Conteúdo principal -->
    <main class="flex flex-col items-center justify-center flex-1 px-6">
      <div class="bg-medium-gray shadow-green w-full max-w-2xl rounded-3xl overflow-hidden p-8 border-white border-2">
        <header class="text-center mb-8">
          <h1 class="text-4xl font-bold text-white">Bem-vindo, {{ userName }}</h1>
        </header>

        <div class="space-y-6">
          <!-- Gerenciamento de Tarefas -->
          <section class="bg-dark-gray p-6 rounded-3xl shadow-md border-lighter-gray border-2">
            <h2 class="text-2xl font-semibold text-white mb-4 text-center">Gerenciamento de Tarefas</h2>
            <p class="text-gray-300 mb-4 text-center">Crie, edite e acompanhe suas tarefas diárias.</p>
            <button @click="goToTasks" class="bg-light-gray text-black py-2 px-4 rounded-full hover:bg-gray-300 border-white border-2 transition">
              Acessar Tarefas
            </button>
          </section>

          <!-- Gerenciamento de Eventos -->
          <section class="bg-dark-gray p-6 rounded-3xl shadow-md border-lighter-gray border-2">
            <h2 class="text-2xl font-semibold text-white mb-4 text-center">Gerenciamento de Eventos</h2>
            <p class="text-gray-300 mb-4 text-center">Organize, visualize e gerencie todos os seus eventos em um só lugar.</p>
            <button @click="goToEvents" class="bg-light-gray text-black py-2 px-4 rounded-full hover:bg-gray-300 border-white border-2 transition">
              Acessar Eventos
            </button>
          </section>

          <!-- Compromissos e Agendas -->
          <section class="bg-dark-gray p-6 rounded-3xl shadow-md border-lighter-gray border-2">
            <h2 class="text-2xl font-semibold text-white mb-4 text-center">Compromissos e Agendas</h2>
            <p class="text-gray-300 mb-4 text-center">Visualize, compartilhe e gerencie seus compromissos de forma prática.</p>
            <button @click="goToSchedules" class="bg-light-gray text-black py-2 px-4 rounded-full hover:bg-gray-300 border-white border-2 transition">
              Acessar Agendas
            </button>
          </section>

          <!-- Gerenciamento de Equipes -->
          <section class="bg-dark-gray p-6 rounded-3xl shadow-md border-lighter-gray border-2">
            <h2 class="text-2xl font-semibold text-white mb-4 text-center">Gerenciamento de Equipes</h2>
            <p class="text-gray-300 mb-4 text-center">Adicione ou remova membros da sua equipe com facilidade!</p>
            <button @click="goToTeams" class="bg-light-gray text-black py-2 px-4 rounded-full hover:bg-gray-300 border-white border-2 transition">
              Acessar Equipes
            </button>
          </section>

          <!-- Configurações da Conta -->
          <section class="bg-dark-gray p-6 rounded-3xl shadow-md border-lighter-gray border-2">
            <h2 class="text-2xl font-semibold text-white mb-4 text-center">Configurações da Conta</h2>
            <p class="text-gray-300 mb-4 text-center">Gerencie suas informações e preferências de conta.</p>
            <button @click="goToSettings" class="bg-light-gray text-black py-2 px-4 rounded-full hover:bg-gray-300 border-white border-2 transition">
              Acessar Configurações
            </button>
          </section>
        </div>
      </div>
    </main>

    <!-- Rodapé -->
    <footer class="flex justify-start items-center px-8 py-4">
      <button @click="goToHome" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-full border-white border-2 transition">
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
const userName = ref('');

// Carregar o nome do usuário
const loadUserName = async () => {
  const token = localStorage.getItem('token');
  if (!token) {
    router.push('/login');
    return;
  }
  try {
    const response = await axios.get('/api/getUserName', {
      headers: { Authorization: `Bearer ${token}` },
    });
    userName.value = response.data.userName;
  } catch (error) {
    router.push('/login');
  }
};

onMounted(loadUserName);

// Funções de navegação
const goToTasks = () => router.push('/profile/tarefas');
const goToEvents = () => router.push('/profile/eventos');
const goToSchedules = () => router.push('/profile/agenda');
const goToTeams = () => router.push('/profile/settings/team-management');
const goToSettings = () => router.push('/profile/settings');
const goToHome = () => router.push('/');
</script>

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

.bg-dark-gray {
  background-color: #1e1e1e;
}

.border-lighter-gray {
  border-color: #5a5a5a;
}

.text-gray-300 {
  color: #d1d5db;
}

button {
  transition: background-color 0.3s, border-color 0.3s;
}

.bg-light-gray {
  background-color: #d4d4d4;
}

.bg-light-gray:hover {
  background-color: #e0e0e0;
}

.bg-gray-500:hover {
  background-color: #4a5568;
}

.rounded-3xl {
  border-radius: 1.5rem;
}

.rounded-full {
  border-radius: 9999px;
}
</style>


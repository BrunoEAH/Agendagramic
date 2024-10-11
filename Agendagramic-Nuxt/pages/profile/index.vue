<template>
  <div class="min-h-screen bg-dark-gray p-6 flex flex-col justify-between border-white border-2">
    <!-- Degradê Verde com Sombra -->
    <div class="bg-gradient-green-inverse shadow-green min-h-screen flex flex-col justify-between">
      <!-- Barra superior com Botões e Nome do Projeto -->
      <div class="flex justify-between items-start mb-6">
        <!-- Botões do Telegram, Configurações e Logout -->
        <div class="flex flex-col space-y-2">
          <button 
            @click="goToTelegram" 
            class="bg-blue-500 text-white py-2 px-4 rounded-full hover:bg-blue-600 border-white border-2">
            Bot do Telegram
          </button>
          <button 
            @click="goToSettings" 
            class="bg-gray-500 text-white py-2 px-4 rounded-full hover:bg-gray-600 border-white border-2">
            Configurações
          </button>
          <button 
            @click="logout" 
            class="bg-gray-500 text-white py-2 px-4 rounded-full hover:bg-gray-600 border-white border-2">
            Logout
          </button>
        </div>

        <!-- Logo e Nome do Projeto -->
        <div class="flex items-center">
          <h1 class="text-2xl font-bold text-white mr-2">AgendaGramic</h1>
          <button @click="goToHome" class="bg-white p-2 rounded-full shadow-lg flex items-center justify-center logo-button">
            <img src="@/assets/images/logo.png" alt="Logo" class="logo-image">
          </button>
        </div>
      </div>

      <!-- TÍTULO PRINCIPAL DA PÁGINA LOGADA -->
      <h1 class="text-3xl font-bold text-center text-white mb-6">Bem-vindo, {{ userName }}!</h1>

      <!-- LAYOUT VERTICAL PARA AS FUNCIONALIDADES -->
      <div class="flex flex-col space-y-6 max-w-lg mx-auto">
        
        <!-- CARD DE GERENCIAMENTO DE TAREFAS -->
        <div class="bg-medium-gray p-6 rounded-3xl shadow-md border-lighter-gray border-2">
          <h2 class="text-2xl font-semibold mb-4 text-white">Gerenciamento de Tarefas</h2>
          <p class="text-gray-300 mb-4">
            Crie, edite e acompanhe suas tarefas diárias. Mantenha o controle de suas atividades e receba lembretes automáticos.
          </p>
          <p class="text-red-500 font-semibold mb-4">*Em breve</p>
          <button @click="showDevelopmentAlert" class="bg-light-gray text-black py-2 px-4 rounded-full hover:bg-green-500 border-white border-2 transition">
            Acessar Tarefas
          </button>
        </div>

        <!-- CARD DE COMPROMISSOS E AGENDAS -->
        <div class="bg-medium-gray p-6 rounded-3xl shadow-md border-lighter-gray border-2">
          <h2 class="text-2xl font-semibold mb-4 text-white">Compromissos e Agendas</h2>
          <p class="text-gray-300 mb-4">
            Visualize, compartilhe e gerencie seus compromissos. Sincronize sua agenda de forma fácil.
          </p>
          <button @click="goToAgenda" class="bg-light-gray text-black py-2 px-4 rounded-full hover:bg-green-500 border-white border-2 transition">
            Acessar Agendas
          </button>
        </div>

        <!-- CARD DE GERENCIAMENTO DE EQUIPES -->
        <div class="bg-medium-gray p-6 rounded-3xl shadow-md border-lighter-gray border-2">
          <h2 class="text-2xl font-semibold mb-4 text-white">Gerenciamento de Equipes</h2>
          <p class="text-gray-300 mb-4">
            Adicione ou remova membros da sua equipe!
          </p>
          <button @click="goToTeamManagement" class="bg-light-gray text-black py-2 px-4 rounded-full hover:bg-green-500 border-white border-2 transition">
            Acessar Equipes
          </button>
        </div>
        
      </div>

      <!-- Rodapé com a versão do Projeto -->
      <div class="text-center text-gray-300 mt-6">
        AgendaGramic Alpha 0.0.1
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

// Nome genérico do usuário (isso será substituído por uma chamada ao backend posteriormente)
const userName = ref('Usuário');

// Função para exibir o alerta de "Em Desenvolvimento"
const showDevelopmentAlert = () => {
  alert('Calma ai amostradinho, estamos desenvolvendo!');
};

// Função para redirecionar ao Bot do Telegram
const goToTelegram = () => {
  window.open('https://t.me/agendagramic_bot', '_blank');
};

// Função para redirecionar à página de configurações
const goToSettings = () => {
  router.push('/profile/settings'); 
};

// Função para redirecionar à página de gerenciamento de equipes
const goToTeamManagement = () => {
  router.push('/profile/settings/team-management');
};

// Função para redirecionar à página de agendas
const goToAgenda = () => {
  router.push('/profile/agenda');
};

// Função de logout
const logout = () => {
  localStorage.removeItem('token');
  router.push('/');
};

// Função para redirecionar à página inicial
const goToHome = () => {
  router.push('/');
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

/* Botão da logo com formato circular */
button.logo-button {
  height: 48px;
  width: 48px;
  border-radius: 50%;
  transition: transform 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: white;
  overflow: hidden;
}

button.logo-button:hover {
  transform: scale(1.05);
}

/* Ajuste para a imagem da logo */
.logo-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Estilo para caixas e botões */
.bg-medium-gray {
  background-color: #3c3c3c;
}

.text-gray-300 {
  color: #d1d5db;
}

.border-lighter-gray {
  border-color: #5a5a5a;
}

.bg-light-gray {
  background-color: #d1d5db;
}

button, .form-checkbox {
  transition: background-color 0.3s, border-color 0.3s;
}

.bg-green-500:hover {
  background-color: #32cd32;
}

.shadow-md {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
}

/* Estilo arredondado */
.rounded-full {
  border-radius: 9999px;
}

.rounded-3xl {
  border-radius: 1.5rem;
}
</style>

<template>
  <div class="min-h-screen bg-gradient-green-inverse flex flex-col justify-between">
    <!-- Barra superior com botões de navegação e Nome do Projeto -->
    <header class="flex justify-between items-start px-8 py-4">
      <!-- Botões de "Página Inicial" e "Logout" -->
      <div class="flex flex-col space-y-2">
        <button 
          @click="goToHome" 
          class="bg-gray-500 text-white py-2 px-4 rounded-full border-white border-2 transition hover:bg-green-500">
          Página Inicial
        </button>
        <button 
          @click="logout" 
          class="bg-gray-500 text-white py-2 px-4 rounded-full border-white border-2 transition hover:bg-green-500">
          Logout
        </button>
      </div>
      <!-- Nome do projeto -->
      <h1 class="text-3xl font-bold text-white">AgendaGramic</h1>
    </header>

    <!-- Conteúdo Principal da Página de Configurações -->
    <main class="flex flex-col items-center flex-1 px-6">
      <div class="flex flex-col space-y-6 max-w-lg w-full">
        <!-- Caixa de Ajustes de Conta -->
        <section class="bg-medium-gray p-6 rounded-3xl shadow-green border-white border-2">
          <h2 class="text-2xl font-semibold text-white mb-4">Ajustes de Conta</h2>
          <p class="text-green-500 font-semibold">*Em desenvolvimento!</p>
          <p class="text-gray-400 mb-4">Visualize e edite suas informações pessoais, como nome, email e senha.</p>
          <button 
            @click="goToAccountSettings" 
            class="bg-light-gray text-black py-2 px-4 rounded-full border-white border-2 transition hover:bg-green-500 w-full">
            Ajustar Conta
          </button>
        </section>

        <!-- Caixa de Gerenciamento de Equipes -->
        <section class="bg-medium-gray p-6 rounded-3xl shadow-green border-white border-2">
          <h2 class="text-2xl font-semibold text-white mb-4">Gerenciamento de Equipes</h2>
          <p class="text-gray-400 mb-2">Adicione, remova membros e ajuste permissões da sua equipe.</p>
          <button 
            @click="goToTeamManagement" 
            class="bg-light-gray text-black py-2 px-4 rounded-full border-white border-2 transition hover:bg-green-500 w-full">
            Gerenciar Equipes
          </button>
        </section>

        <!-- Caixa de Ajustes de Notificações -->
        <section class="bg-medium-gray p-6 rounded-3xl shadow-green border-white border-2">
          <h2 class="text-2xl font-semibold text-white mb-4">Ajustes de Notificações</h2>
          <p class="text-gray-400 mb-2">Configure as preferências de notificações por WhatsApp e email.</p>
          <button 
            @click="goToNotifications" 
            class="bg-light-gray text-black py-2 px-4 rounded-full border-white border-2 transition hover:bg-green-500 w-full">
            Ajustar Notificações
          </button>
        </section>

        <!-- Caixa de Privacidade e Segurança -->
        <section class="bg-medium-gray p-6 rounded-3xl shadow-green border-white border-2">
          <h2 class="text-2xl font-semibold text-white mb-4">Privacidade e Segurança</h2>
          <p class="text-gray-400 mb-2">Gerencie as configurações de segurança da sua conta.</p>
          <button 
            @click="goToPrivacy" 
            class="bg-light-gray text-black py-2 px-4 rounded-full border-white border-2 transition hover:bg-green-500 w-full">
            Ajustar Privacidade
          </button>
        </section>
      </div>
    </main>

    <!-- Rodapé -->
    <footer class="text-center text-gray-300 py-4">
      AgendaGramic Alpha 0.0.1
    </footer>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

// Função para redirecionar à página inicial (logado)
const goToHome = () => {
  router.push('/profile');
};

// Função de logout que redireciona para a página inicial
const logout = () => {
  localStorage.removeItem('token'); // Exemplo de remoção de token de autenticação
  router.push('/');
};

// Funções de redirecionamento para páginas específicas
const goToAccountSettings = () => {
  router.push('/profile/settings/account-settings');
};

const goToTeamManagement = () => {
  router.push('/profile/settings/team-management');
};

const goToNotifications = () => {
  router.push('/profile/settings/notifications');
};

const goToPrivacy = () => {
  router.push('/profile/settings/privacy');
};
</script>

<style scoped>
/* Fundo com gradiente de baixo para cima */
.bg-gradient-green-inverse {
  background: linear-gradient(to bottom, #32cd32, #1e1e1e);
}

/* Fundo cinza médio */
.bg-medium-gray {
  background-color: #3c3c3c;
}

/* Bordas mais claras */
.border-white {
  border-color: white;
}

/* Textos */
.text-gray-400 {
  color: #9ca3af;
}
.text-green-500 {
  color: #10b981;
}

/* Botões */
button {
  transition: background-color 0.3s, border-color 0.3s;
}

.bg-light-gray {
  background-color: #d1d5db;
}

.bg-green-500:hover {
  background-color: #32cd32;
}

/* Bordas arredondadas */
.rounded-full {
  border-radius: 9999px;
}

.rounded-3xl {
  border-radius: 1.5rem;
}

/* Sombra */
.shadow-green {
  box-shadow: 0 10px 15px rgba(50, 205, 50, 0.3);
}
</style>

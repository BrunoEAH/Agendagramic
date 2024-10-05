<template>
  <div class="min-h-screen bg-gray-100 p-6 flex flex-col justify-between">
    
    <!-- Barra superior com botões de navegação e Nome do Projeto -->
    <div class="flex justify-between items-start mb-6">
      <!-- Botões de "Página Inicial" e "Logout" no canto superior esquerdo -->
      <div class="flex flex-col space-y-2">
        <button 
          @click="goToHome" 
          class="bg-gray-500 text-white py-2 px-4 rounded hover:bg-gray-600">
          Página Inicial
        </button>
        <button 
          @click="logout" 
          class="bg-gray-500 text-white py-2 px-4 rounded hover:bg-gray-600">
          Logout
        </button>
      </div>

      <!-- Nome do projeto no canto superior direito -->
      <h1 class="text-xl font-bold">AgendaGramic</h1>
    </div>

    <!-- Conteúdo Principal da Página de Configurações -->
    <div class="flex flex-col space-y-6 max-w-lg mx-auto">

      <!-- Caixa de Ajustes de Conta -->
      <div class="bg-white p-6 rounded-lg shadow-md">
        <h2 class="text-xl font-semibold mb-4">Ajustes de Conta</h2>
        <p class="text-green-500 font-semibold">*Em desenvolvimento!</p>
        <p class="text-gray-600 mb-4">Visualize e edite suas informações pessoais, como nome, email e senha.</p>
        <button @click="goToAccountSettings" class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
          Ajustar Conta
        </button>
      </div>

      <!-- Caixa de Gerenciamento de Equipes -->
      <div class="bg-white p-6 rounded-lg shadow-md">
        <h2 class="text-xl font-semibold mb-4">Gerenciamento de Equipes</h2>
        <p class="text-gray-600 mb-2">Adicione, remova membros e ajuste permissões da sua equipe.</p>
        <p class="text-red-500 font-semibold">*Em breve</p>
        <button @click="goToTeamManagement" class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
          Gerenciar Equipes
        </button>
      </div>

      <!-- Caixa de Ajustes de Notificações -->
      <div class="bg-white p-6 rounded-lg shadow-md">
        <h2 class="text-xl font-semibold mb-4">Ajustes de Notificações</h2>
        <p class="text-gray-600 mb-2">Configure as preferências de notificações por WhatsApp e email.</p>
        <p class="text-red-500 font-semibold">*Em breve</p>
        <button @click="goToNotificationSettings" class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
          Ajustar Notificações
        </button>
      </div>

      <!-- Caixa de Privacidade e Segurança -->
      <div class="bg-white p-6 rounded-lg shadow-md">
        <h2 class="text-xl font-semibold mb-4">Privacidade e Segurança</h2>
        <p class="text-gray-600 mb-2">Gerencie as configurações de segurança da sua conta.</p>
        <p class="text-red-500 font-semibold">*Em breve</p>
        <button @click="goToPrivacySettings" class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
          Ajustar Privacidade
        </button>
      </div>

    </div>

    <!-- Rodapé com a versão do site -->
    <div class="text-center text-gray-500 mt-6">
      AgendaGramic Alpha 0.0.1
    </div>
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

// Funções de redirecionamento para as respectivas páginas
const goToAccountSettings = () => {
  router.push('/profile/settings/account-settings');
};

const goToTeamManagement = () => {
  router.push('/team-management');
};

const goToNotificationSettings = () => {
  router.push('/notification-settings');
};

const goToPrivacySettings = () => {
  router.push('/privacy-settings');
};
</script>

<style scoped>
/* Estilos personalizados */
.bg-gray-100 {
  background-color: #f7fafc;
}

.bg-gray-500:hover {
  background-color: #4b5563;
}

.text-gray-600 {
  color: #4b5563;
}

.rounded {
  border-radius: 0.375rem;
}

.shadow-md {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.text-gray-500 {
  color: #6b7280;
}

.bg-blue-500:hover {
  background-color: #2563eb;
}

.text-red-500 {
  color: #ef4444;
}

.text-green-500 {
  color: #10b981;
}
</style>

<template>
  <div class="min-h-screen bg-gray-100 p-6 flex flex-col justify-between">
    
    <!-- Barra superior com Nome do Projeto e Botões -->
    <div class="flex justify-between items-start mb-6">
      <!-- Botões do Telegram, Configurações e Logout no canto superior esquerdo -->
      <div class="flex flex-col space-y-2">
        <button 
          @click="goToTelegram" 
          class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
          Bot do Telegram
        </button>
        <button 
          @click="goToSettings" 
          class="bg-gray-500 text-white py-2 px-4 rounded hover:bg-gray-600">
          Configurações
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

    <!-- Título principal da página logada -->
    <h1 class="text-3xl font-bold text-center mb-6">Bem-vindo, {{ userName }}!</h1>

    <!-- Layout vertical para as funcionalidades -->
    <div class="flex flex-col space-y-6 max-w-lg mx-auto">
      
      <!-- Gerenciamento de Tarefas -->
      <div class="bg-white p-4 rounded-lg shadow-md">
        <h2 class="text-xl font-semibold mb-4">Gerenciamento de Tarefas</h2>
        <p class="text-gray-600 mb-4">
          Crie, edite e acompanhe suas tarefas diárias. Mantenha o controle de suas atividades e receba lembretes automáticos.
        </p>
        <p class="text-red-500 font-semibold mb-4">*Em breve</p> <!-- Aviso de Em Breve -->
        <button class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
          Acessar Tarefas
        </button>
      </div>

      <!-- Compromissos e Agendas -->
      <div class="bg-white p-4 rounded-lg shadow-md">
        <h2 class="text-xl font-semibold mb-4">Compromissos e Agendas</h2>
        <p class="text-gray-600 mb-4">
          Visualize, compartilhe e gerencie seus compromissos. 
          Sincronize sua agenda de forma fácil.
        </p>
        <button @click="goToAgenda" class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
          Acessar Agendas
        </button>
      </div>

      <!-- Lembretes -->
      <div class="bg-white p-4 rounded-lg shadow-md">
        <h2 class="text-xl font-semibold mb-4">Lembretes</h2>
        <p class="text-gray-600 mb-4">
          Configure lembretes personalizados e receba notificações diretamente pelo WhatsApp. Nunca perca um compromisso!
        </p>
        <p class="text-red-500 font-semibold mb-4">*Em breve</p> <!-- Aviso de Em Breve -->
        <button class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
          Acessar Lembretes
        </button>
      </div>

      <!-- Gerenciamento de Equipes -->
      <div class="bg-white p-4 rounded-lg shadow-md">
        <h2 class="text-xl font-semibold mb-4">Gerenciamento de Equipes</h2>
        <p class="text-gray-600 mb-4">
          Adicione ou remova membros da sua equipe e organize tarefas em conjunto com um sistema hierárquico eficiente.
        </p>
        <p class="text-red-500 font-semibold mb-4">*Em breve</p> <!-- Aviso de Em Breve -->
        <button class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
          Acessar Equipes
        </button>
      </div>
      
    </div>

    <!-- Versão do sistema no rodapé -->
    <div class="text-center text-gray-500">
      AgendaGramic Alpha 0.0.1
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

// Nome genérico do usuário (pode ser ajustado futuramente para chamar do backend)
const userName = ref('Usuário');

// Função para redirecionar ao Bot do Telegram
const goToTelegram = () => {
  window.open('https://t.me/agendagramic_bot', '_blank'); // Abre o link do Bot em uma nova aba
};

// Função para redirecionar à página de configurações
const goToSettings = () => {
  router.push('/settings'); // Redireciona para a página de configurações
};

// Função para redirecionar à página de agendas
const goToAgenda = () => {
  router.push('/profile/agenda'); // Certifique-se de que a rota '/agenda' está corretamente configurada no seu arquivo de rotas
};

// Função de logout
const logout = () => {
  localStorage.removeItem('token'); // Remover token de autenticação
  router.push('/'); // Redireciona para a página inicial (index)
};
</script>

<style scoped>
/* Estilos personalizados para os cartões */
.bg-white {
  background-color: white;
}

.rounded {
  border-radius: 0.375rem;
}

.shadow-md {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.focus\:ring-blue-500 {
  outline-color: #4299e1;
}

.hover\:bg-blue-600:hover {
  background-color: #2563eb;
}

.bg-gray-100 {
  background-color: #f7fafc;
}

.bg-blue-500:hover {
  background-color: #2563eb;
}

.bg-gray-500:hover {
  background-color: #4b5563;
}

.text-red-500 {
  color: #ef4444;
}
</style>

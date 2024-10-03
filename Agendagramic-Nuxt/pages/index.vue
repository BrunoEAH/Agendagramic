<template>
  <div class="min-h-screen bg-gray-100 p-6 flex flex-col justify-between">
    
    <!-- Barra Superior -->
    <div class="flex justify-between items-center mb-6">
      <!-- Barra de Menus com Login, Cadastro e Bot do Telegram -->
      <div class="flex space-x-4">
        <button @click="goToLogin" class="bg-green-500 text-white py-2 px-4 rounded hover:bg-green-600">
          Login
        </button>
        <button @click="goToSignup" class="bg-green-500 text-white py-2 px-4 rounded hover:bg-green-600">
          Cadastro
        </button>
        <a href="https://t.me/agendagramic_bot" target="_blank" class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
          Telegram
        </a>
      </div>
      <!-- Nome do Programa no Canto Superior Direito -->
      <div>
        <h1 class="text-xl font-bold">AgendaGramic</h1>
      </div>
    </div>

    <!-- Descrição do Projeto Centralizada -->
    <div class="flex flex-col items-center justify-center flex-1 text-center">
      <h2 class="text-2xl font-semibold mb-4">Bem-vindo ao AgendaGramic!</h2>
      <p class="text-gray-700 mb-4 max-w-2xl">
        AgendaGramic é um sistema de gerenciamento de agendas dinâmico, permitindo que você organize suas tarefas e compromissos de forma simples e eficiente. Nossa versão Alpha inclui funcionalidades como:
      </p>
      <ul class="list-disc list-inside text-gray-600 mb-6">
        <li>Possibilidade de login e cadastro de novos usuários.</li>
        <li>Organização de eventos e compromissos na agenda.</li>
      </ul>
      <p class="text-gray-700 max-w-2xl mb-4">
        Continue acompanhando para mais atualizações e novas funcionalidades!
      </p>
    </div>

    <!-- Versão do Projeto no Rodapé -->
    <div class="text-center text-gray-500">
      AgendaGramic Alpha 0.0.1
    </div>

  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

// Função para redirecionar para a página de login
const router = useRouter();
const goToLogin = () => {
  router.push('/profile');
};

// Função para redirecionar para a página de cadastro
const goToSignup = () => {
  router.push('/cadastro'); // Certifique-se de que a rota para cadastro.vue está registrada como '/cadastro'
};
</script>

<style scoped>
/* Estilo básico para a organização e alinhamento */
</style>

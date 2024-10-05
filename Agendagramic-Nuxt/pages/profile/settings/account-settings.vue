<template>
    <div class="min-h-screen bg-gray-100 p-6 flex flex-col justify-between">
      <!-- Cabeçalho da página com Ajustes de Conta no canto esquerdo e AgendaGramic no direito -->
      <div class="flex justify-between items-center mb-6">
        <!-- Ajustes de Conta no canto superior esquerdo -->
        <h1 class="text-3xl font-bold">Ajustes de Conta</h1>
  
        <!-- AgendaGramic no canto superior direito -->
        <div>
          <h3 class="text-xl font-medium">AgendaGramic</h3>
        </div>
      </div>
  
      <!-- Botão Voltar logo abaixo de "Ajustes de Conta" -->
      <div class="mb-6">
        <button @click="goBack" class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
          Voltar
        </button>
      </div>
  
      <!-- Centralizar conteúdo com mensagem de desenvolvimento -->
      <div class="text-green-500 text-xl font-bold text-center mb-6">
        *Em desenvolvimento!
      </div>
  
      <!-- Centralizar caixa de ajustes de conta -->
      <div class="flex flex-col items-center justify-center flex-1">
        <div class="bg-white p-6 rounded-lg shadow-md w-full max-w-md">
          <h2 class="text-xl font-semibold mb-4 text-center">Editar Informações da Conta</h2>
  
          <!-- Nome Atual e Novo -->
          <div class="mb-6">
            <label class="block text-gray-700 text-sm font-bold mb-2">Nome Atual:</label>
            <p class="mb-4 text-gray-600">teste</p>
  
            <label for="newName" class="block text-gray-700 text-sm font-bold mb-2">Nome Novo:</label>
            <input
              v-model="newName"
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="newName"
              type="text"
              placeholder="Digite seu novo nome"
            />
          </div>
  
          <!-- Email Atual e Novo -->
          <div class="mb-6">
            <label class="block text-gray-700 text-sm font-bold mb-2">Email Atual:</label>
            <p class="mb-4 text-gray-600">teste</p>
  
            <label for="newEmail" class="block text-gray-700 text-sm font-bold mb-2">Email Novo:</label>
            <input
              v-model="newEmail"
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="newEmail"
              type="email"
              placeholder="Digite seu novo email"
            />
          </div>
  
          <!-- Senha Atual e Nova -->
          <div class="mb-6">
            <label class="block text-gray-700 text-sm font-bold mb-2">Senha Atual:</label>
            <p class="mb-4 text-gray-600">teste</p>
  
            <label for="newPassword" class="block text-gray-700 text-sm font-bold mb-2">Senha Nova:</label>
            <input
              v-model="newPassword"
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="newPassword"
              type="password"
              placeholder="Digite sua nova senha"
            />
          </div>
  
          <!-- Botão de salvar -->
          <button @click="saveChanges" class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full">
            Salvar Alterações
          </button>
        </div>
      </div>
  
      <!-- Rodapé -->
      <div class="text-center text-gray-500 mt-6">
        AgendaGramic Alpha 0.0.1
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  
  const newName = ref('');
  const newEmail = ref('');
  const newPassword = ref('');
  const router = useRouter();
  
  const saveChanges = () => {
    // Exibe a mensagem de alerta
    alert('Alterações salv... Calma ai amostradinho, estamos desenvolvendo!');
  };
  
  const goBack = () => {
    router.push('/profile/settings');
  };
  </script>
  
  <style scoped>
  /* Estilos para a página */
  .shadow {
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  .text-green-500 {
    color: #10b981;
  }
  </style>
  
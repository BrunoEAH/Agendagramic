<template>
    <div class="min-h-screen bg-gray-100 p-6 flex flex-col justify-between">
      <!-- Nome do Programa no Centro -->
      <div class="flex flex-col items-center">
        <h1 class="text-3xl font-bold mb-6">AgendaGramic</h1>
        <!-- Botões de Login e Cadastro Centralizados -->
        <div class="flex space-x-4">
          <button @click="goToLogin" class="bg-green-500 text-white py-2 px-4 rounded hover:bg-green-600">
            Login
          </button>
          <button @click="goToSignup" class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
            Cadastro
          </button>
        </div>
      </div>
  
      <!-- Versão do Projeto no Rodapé -->
      <div class="text-center text-gray-500 mt-6">
        AgendaGramic Alpha 0.0.1
      </div>
    </div>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router';
  
  // Função para redirecionar para a página de login
  const router = useRouter();
  const goToLogin = () => {
    router.push('/login');
  };
  
  // Função para redirecionar para a página de cadastro
  const goToSignup = () => {
    router.push('/cadastro'); // Certifique-se de que a rota para cadastro.vue está registrada como '/cadastro'
  };
  </script>
  
  <style scoped>
  /* Estilo básico com foco na simplicidade */
  </style>
  
<template>
    <div class="min-h-screen bg-dark-gray p-6 flex flex-col justify-center items-center border-white border-2">
      <div class="bg-gradient-green-inverse shadow-green flex flex-col justify-center items-center p-6 rounded-lg">
        <!-- Error message -->
        <h1 class="text-4xl font-bold text-white mb-4">Opa! Alguma coisa deu errada.</h1>
        <p class="text-xl text-gray-300 mb-6">Não conseguimos te encaminhar para a página.</p>
  
        <!-- Button to return home -->
        <button @click="goToHome" class="bg-blue-500 text-white py-2 px-4 rounded-full hover:bg-blue-600 border-white border-2">
          Voltar para o perfil
        </button>
      </div>
  
      <!-- Footer with version -->
      <div class="text-center text-gray-300 mt-6">
        AgendaGramic Alpha 0.0.1
      </div>
    </div>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router';
  
  const router = useRouter();
  
  // Function to navigate back to the homepage
  function goToHome() {
    router.push('/profile');
  }
  </script>
  
  <style scoped>
  .bg-dark-gray {
    background-color: #2b2b2b;
  }
  
  .bg-gradient-green-inverse {
    background: linear-gradient(135deg, #4caf50 0%, #2b2b2b 100%);
  }
  
  .shadow-green {
    box-shadow: 0 4px 6px rgba(76, 175, 80, 0.1), 0 2px 4px rgba(76, 175, 80, 0.06);
  }
  
  .border-white {
    border-color: white;
  }
  
  .text-gray-300 {
    color: #d1d5db;
  }
  
  .text-white {
    color: white;
  }
  
  .bg-blue-500 {
    background-color: #3b82f6;
  }
  
  .hover\:bg-blue-600:hover {
    background-color: #2563eb;
  }
  </style>
  
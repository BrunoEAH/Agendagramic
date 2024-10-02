<template>
    <div class="min-h-screen bg-gray-100 p-6 flex items-center justify-center">
      <!-- Formulário de Cadastro Centralizado -->
      <form @submit.prevent="handleSignup" class="bg-white p-6 rounded shadow-md w-96">
        <!-- Título do Formulário de Cadastro -->
        <h2 class="text-2xl font-bold mb-6 text-center">Cadastro</h2>
  
        <!-- Campo de Entrada para Nome -->
        <div class="mb-4">
          <label for="name" class="block text-sm font-medium text-gray-700">Nome</label>
          <input
            type="text"
            id="name"
            v-model="name"
            required
            class="mt-1 block w-full p-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
          />
        </div>
  
        <!-- Campo de Entrada para Email -->
        <div class="mb-4">
          <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
          <input
            type="email"
            id="email"
            v-model="email"
            required
            class="mt-1 block w-full p-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
          />
        </div>
  
        <!-- Campo de Entrada para Senha -->
        <div class="mb-4">
          <label for="password" class="block text-sm font-medium text-gray-700">Senha</label>
          <input
            type="password"
            id="password"
            v-model="password"
            required
            class="mt-1 block w-full p-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
          />
        </div>
  
        <!-- Campo de Entrada para Confirmação de Senha -->
        <div class="mb-6">
          <label for="confirmPassword" class="block text-sm font-medium text-gray-700">Confirmar Senha</label>
          <input
            type="password"
            id="confirmPassword"
            v-model="confirmPassword"
            required
            class="mt-1 block w-full p-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
          />
        </div>
  
        <!-- Botão de Submissão -->
        <button type="submit" class="w-full bg-blue-500 text-white font-semibold py-2 rounded hover:bg-blue-600">
          Cadastrar
        </button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  import axios from 'axios'; // Para fazer requisições HTTP
  
  // Definir variáveis reativas para o formulário de cadastro
  const name = ref('');
  const email = ref('');
  const password = ref('');
  const confirmPassword = ref('');
  
  const router = useRouter(); // Para redirecionar o usuário após o cadastro
  
  // Função de manipulação do cadastro
  const handleSignup = async () => {
    if (password.value !== confirmPassword.value) {
      alert('As senhas não coincidem!');
      return;
    }
  
    try {
      // Requisição para a API de cadastro (substitua pela sua API real)
      const response = await axios.post('http://localhost:3000/logado', {
        name: name.value,
        email: email.value,
        password: password.value,
      });
  
      // Se o cadastro for bem-sucedido, redirecionar para a página de login
      alert('Cadastro realizado com sucesso!');
      router.push('/login');
    } catch (error) {
      alert('Erro no cadastro: ' + error.response.data.message);
    }
  };
  </script>
  
  <style scoped>
  /* Estilos para o formulário */
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
    background-color: #2b6cb0;
  }
  </style>
  
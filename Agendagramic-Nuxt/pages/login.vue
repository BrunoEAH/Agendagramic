<template>
  <div class="min-h-screen bg-gray-100 p-6 flex flex-col justify-between">
    
    <!-- Barra superior com Nome do Projeto e Botão de Início -->
    <div class="flex justify-between items-center mb-6">
      <button @click="goToHome" class="bg-green-500 text-white py-2 px-4 rounded hover:bg-green-600">
        Início
      </button>
      <div>
        <h1 class="text-xl font-bold">AgendaGramic</h1>
      </div>
    </div>

    <!-- Formulário de Login Centralizado -->
    <div class="flex justify-center items-center flex-1">
      <form @submit.prevent="handleLogin" class="bg-white p-6 rounded shadow-md w-96">
        <h2 class="text-2xl font-bold mb-4 text-center">Login</h2>

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

        <div class="mb-6">
          <label for="password" class="block text-sm font-medium text-gray-700">Senha</label>
          <input
            type="password"
            id="password"
            v-model="password"
            required
            class="mt-1 block w-full p-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
          />
        </div>

        <button type="submit" class="w-full bg-blue-500 text-white font-semibold py-2 rounded hover:bg-blue-600">
          Login
        </button>
      </form>
    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

const email = ref('');
const password = ref('');
const router = useRouter();

const handleLogin = async () => {
  try {
    // Fazendo a requisição POST para a API de login (ajuste a URL conforme necessário)
    const response = await axios.post('http://localhost:3001/login', {
      email: email.value,
      password: password.value,
    });

    // Se o login for bem-sucedido, salvar o token no localStorage
    localStorage.setItem('token', response.data.token);

    // Redirecionar para a página logada ou home após o login bem-sucedido
    router.push('/logado'); 
  } catch (error) {
    alert('Erro no login: ' + error.response?.data?.message || 'Erro inesperado');
  }
};

// Redirecionar para a página inicial
const goToHome = () => {
  router.push('/');
};
</script>

<style scoped>
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

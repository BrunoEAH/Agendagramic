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

    <!-- Formulário de Cadastro Centralizado -->
    <div class="flex justify-center items-center flex-1">
      <form @submit.prevent="handleSignup" class="bg-white p-6 rounded shadow-md w-96">
        <h2 class="text-2xl font-bold mb-6 text-center">Cadastro</h2>

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

        <p class="text-red-500 font-semibold text-center mb-4">*Em breve</p> <!-- Aviso de Em Breve -->

        <button type="submit" class="w-full bg-blue-500 text-white font-semibold py-2 rounded hover:bg-blue-600">
          Cadastrar
        </button>
      </form>
    </div>

    <div class="text-center text-gray-500">
      AgendaGramic Alpha 0.0.1
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

// Variáveis reativas para armazenar os dados do formulário
const name = ref('');
const email = ref('');
const password = ref('');
const confirmPassword = ref('');

const router = useRouter();

// Função de manipulação de cadastro com tratamento de erros
const handleSignup = async () => {
  if (password.value !== confirmPassword.value) {
    alert('As senhas não coincidem!');
    return;
  }

  try {
    // Requisição para a API de cadastro (substitua a URL se necessário)
    const response = await axios.post('http://localhost:3001/signup', {
      name: name.value,
      email: email.value,
      password: password.value,
    });

    // Exibir mensagem de sucesso e redirecionar para a página de login
    alert('Cadastro realizado com sucesso!');
    router.push('/login');
  } catch (error) {
    // Tratamento de erro aprimorado com mensagens claras
    if (error.response && error.response.data && error.response.data.message) {
      alert('Erro no cadastro: ' + error.response.data.message);
    } else {
      alert('Erro no cadastro: Ocorreu um erro inesperado');
    }
  }
};

// Função para redirecionar para a página inicial
const goToHome = () => {
  router.push('/');
};
</script>

// Descrição do estilo que vamos usar nas páginas
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

.text-red-500 {
  color: #ef4444;
}
</style>

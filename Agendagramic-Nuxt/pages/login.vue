<template>
  <!-- DIV PRINCIPAL PARA CENTRALIZAR O FORMULÁRIO NA PÁGINA -->
  <div class="flex items-center justify-center min-h-screen bg-gray-100">
    
    <!-- FORMULÁRIO DE LOGIN COM SUBMISSÃO PREVENIDA PARA LIDAR VIA JAVASCRIPT -->
    <form @submit.prevent="handleLogin" class="bg-white p-6 rounded shadow-md w-96">
      
      <!-- TÍTULO DO FORMULÁRIO DE LOGIN -->
      <h2 class="text-2xl font-bold mb-4 text-center">Login</h2>
  
      <!-- CAMPO DE ENTRADA PARA O EMAIL -->
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
  
      <!-- CAMPO DE ENTRADA PARA A SENHA -->
      <div class="mb-6">
        <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
        <input
          type="password"
          id="password"
          v-model="password"
          required
          class="mt-1 block w-full p-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
        />
      </div>
  
      <!-- BOTÃO DE SUBMISSÃO DO FORMULÁRIO -->
      <button
        type="submit"
        class="w-full bg-blue-500 text-white font-semibold py-2 rounded hover:bg-blue-600"
      >
        Login
      </button>
    </form>
  </div>
</template>

<script setup>
  import { ref } from 'vue'; // Importar a função ref para gerenciar estado reativo
  import { useRouter } from 'vue-router'; // Para realizar o redirecionamento
  import axios from 'axios'; // Importando Axios para requisições HTTP

  // Variáveis reativas para email e senha
  const email = ref('');
  const password = ref('');
  
  // Roteador para redirecionamento
  const router = useRouter();

  // Função que lida com o login e faz a requisição POST para a API
  const handleLogin = async () => {
    try {
      // Fazendo a requisição POST para a API de login
      const response = await axios.post('http://localhost:3000/login', {
        email: email.value,
        password: password.value,
      });
      
      // Se o login for bem-sucedido, salvar o token no localStorage
      localStorage.setItem('token', response.data.token);
      
      // Redirecionar para a página inicial após login bem-sucedido
      router.push('/home'); 
    } catch (error) {
      // Exibir mensagem de erro se houver problemas com o login
      alert('Erro no login: ' + error.response.data.message);
    }
  };
</script>

<style scoped>
  /* Estilos personalizados para o formulário de login */
  .bg-white {
    background-color: white;
  }

  .rounded {
    border-radius: 0.375rem;
  }

  .shadow-md {
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }

  .bg-gray-100 {
    background-color: #f7fafc;
  }

  .focus\:ring-blue-500 {
    outline-color: #4299e1;
  }

  .hover\:bg-blue-600:hover {
    background-color: #2b6cb0;
  }
</style>

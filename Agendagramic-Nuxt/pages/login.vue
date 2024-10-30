<template>
  <div class="min-h-screen bg-dark-gray p-6 flex flex-col justify-between">
    <!-- Barra superior com Nome do Projeto e Botão de Início -->
    <div class="flex justify-between items-center mb-6 justify-end">
      <div class="flex items-center space-x-2">
        <h1 class="text-3xl font-bold text-white">AgendaGramic</h1>
        <button @click="goToHome" class="bg-white p-2 rounded-full shadow-lg">
          <img src="@/assets/images/logo.png" alt="Logo" class="w-6 h-6"/>
        </button>
      </div>
    </div>

    <!-- Formulário de Login Centralizado -->
    <div class="flex justify-center items-center flex-1">
      <form @submit.prevent="handleLogin" class="bg-medium-gray p-6 rounded-3xl shadow-md w-96 border-lighter-gray border-2">
        <h2 class="text-2xl font-bold mb-4 text-center text-white">Login</h2>

        <div class="mb-4">
          <label for="email" class="block text-sm font-medium text-white">Email</label>
          <input
            type="email"
            id="email"
            v-model="email"
            required
            class="mt-1 block w-full p-2 border border-lighter-gray rounded-full bg-input-gray text-white focus:outline-none focus:shadow-outline"
          />
        </div>

        <div class="mb-6">
          <label for="password" class="block text-sm font-medium text-white">Senha</label>
          <input
            type="password"
            id="password"
            v-model="password"
            required
            class="mt-1 block w-full p-2 border border-lighter-gray rounded-full bg-input-gray text-white focus:outline-none focus:shadow-outline"
          />
        </div>

        <button type="submit" class="w-full bg-light-gray text-black py-2 rounded-full border-white border-2 hover:bg-green-500 transition">
          Login
        </button>

        <!-- Botão de Cadastro -->
        <button @click="goToSignup" type="button" class="w-full bg-light-gray text-black py-2 mt-4 rounded-full border-white border-2 hover:bg-green-500 transition">
          Criar Conta
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const email = ref('');
const password = ref('');
const router = useRouter();

const handleLogin = async () => {
  const newLogin = { email: email.value, password: password.value };

  try {
    // Envia a requisição de login para o backend
    const response = await $fetch('/api/login', {
      method: 'POST',
      body: newLogin,
    });

    console.log('API Response:', response); // Check the API response

    if (!response || !response.token) {
      throw new Error(response?.error || 'Erro inesperado');
    }

    // Armazena o token no localStorage e redireciona para o perfil
    localStorage.setItem('token', response.token);
    router.push('/profile/');
  } catch (error) {
    alert('Erro no login: ' + (error.message || 'Erro inesperado'));
  }
};


const goToHome = () => {
  router.push('/');
};

const goToSignup = () => {
  router.push('/cadastro');
};
</script>

<style scoped>
.bg-dark-gray {
  background-color: #1a1a1a;
  background-image: linear-gradient(to bottom, transparent 50%, #32cd32 100%);
}

.bg-medium-gray {
  background-color: #3c3c3c;
}

.bg-input-gray {
  background-color: #2a2a2a; /* Cinza escuro para os campos de entrada */
}

.border-lighter-gray {
  border-color: #5a5a5a;
}

.shadow-md {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
}

.text-white {
  color: white;
}

.bg-light-gray {
  background-color: #d1d5db;
}

.rounded-full {
  border-radius: 9999px;
}
</style>

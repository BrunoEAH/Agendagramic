<template>
  <div class="min-h-screen bg-dark-gray p-6 flex flex-col justify-between border-white border-2">
    <!-- Degradê Verde com Sombra -->
    <div class="bg-gradient-green-inverse shadow-green min-h-screen flex flex-col justify-between">
      <!-- Barra superior com Botão de Início e Nome do Projeto -->
      <div class="flex justify-between items-start mb-6">
        <button @click="goToHome" class="bg-gray-500 text-white py-2 px-4 rounded-full hover:bg-gray-600 border-white border-2">
          Início
        </button>
        <div>
          <h1 class="text-3xl font-bold text-white">AgendaGramic</h1>
        </div>
      </div>

      <!-- Formulário de Cadastro Centralizado -->
      <div class="flex justify-center items-center flex-1">
        <form @submit.prevent="handleSignup" class="bg-medium-gray p-6 rounded-3xl shadow-md border-lighter-gray border-2 w-full max-w-md">
          <h2 class="text-2xl font-bold mb-6 text-center text-white">Cadastro</h2>

          <div class="mb-4">
            <label for="nome" class="block text-sm font-medium text-white">Nome</label>
            <input
              type="text"
              id="nome"
              v-model="nome"
              required
              class="mt-1 block w-full py-2 px-3 border border-white rounded-full bg-dark-gray text-white focus:outline-none focus:ring-2 focus:ring-green-500"
            />
          </div>

          <div class="mb-4">
            <label for="tgUser" class="block text-sm font-medium text-white">Usuário do Telegram</label>
            <input
              type="text"
              id="tgUser"
              v-model="tgUser"
              required
              class="mt-1 block w-full py-2 px-3 border border-white rounded-full bg-dark-gray text-white focus:outline-none focus:ring-2 focus:ring-green-500"
            />
          </div>



          <div class="mb-4">
            <label for="email" class="block text-sm font-medium text-white">Email</label>
            <input
              type="email"
              id="email"
              v-model="email"
              required
              class="mt-1 block w-full py-2 px-3 border border-white rounded-full bg-dark-gray text-white focus:outline-none focus:ring-2 focus:ring-green-500"
            />
          </div>

          <div class="mb-4">
            <label for="password" class="block text-sm font-medium text-white">Senha</label>
            <input
              type="password"
              id="password"
              v-model="password"
              required
              class="mt-1 block w-full py-2 px-3 border border-white rounded-full bg-dark-gray text-white focus:outline-none focus:ring-2 focus:ring-green-500"
            />
          </div>

          <div class="mb-6">
            <label for="confirmPassword" class="block text-sm font-medium text-white">Confirmar Senha</label>
            <input
              type="password"
              id="confirmPassword"
              v-model="confirmPassword"
              required
              class="mt-1 block w-full py-2 px-3 border border-white rounded-full bg-dark-gray text-white focus:outline-none focus:ring-2 focus:ring-green-500"
            />
          </div>

          <p v-if="errorMessage" class="text-red-500 font-semibold text-center mb-4">{{ errorMessage }}</p> <!-- Exibe mensagem de erro -->
          <p v-if="successMessage" class="text-green-500 font-semibold text-center mb-4">{{ successMessage }}</p> <!-- Exibe mensagem de sucesso -->

          <button type="submit" class="w-full bg-light-gray text-black font-semibold py-2 rounded-full hover:bg-green-500 border-white border-2 transition mb-4">
            Cadastrar
          </button>

          <button @click="goToLogin" class="w-full bg-light-gray text-black font-semibold py-2 rounded-full hover:bg-green-500 border-white border-2 transition">
            Já tem uma conta? Faça login
          </button>
        </form>
      </div>

      <!-- Rodapé com a versão do projeto -->
      <div class="text-center text-gray-300 mt-6">
        AgendaGramic Alpha 0.0.1
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

// Variáveis reativas para armazenar os dados do formulário
const nome = ref('');
const email = ref('');
const password = ref('');
const tgUser = ref('');
const confirmPassword = ref('');
const errorMessage = ref('');
const successMessage = ref('');

const router = useRouter();

// Função de manipulação de cadastro para salvar as informações no banco de dados
const handleSignup = async () => {
  errorMessage.value = '';
  successMessage.value = '';

  if (password.value !== confirmPassword.value) {
    errorMessage.value = 'As senhas não coincidem!';
    return;
  }

  const newUser = {
    name: nome.value,
    email: email.value,
    password: confirmPassword.value,
    tgUser: tgUser.value
  }

  try {
    const { data, error } = await $fetch('/api/registerUser', {
      method: 'POST',
      body: newUser,
    });
    
    if (error.value) {
      throw new Error(error.value); // Handle fetch error
    }

    // Verifica se o cadastro foi bem-sucedido
    if (response.data.success) {
      successMessage.value = 'Cadastro realizado com sucesso!';
      // Redireciona para o login após um tempo
      setTimeout(() => router.push('/login'), 2000);
    } else {
      errorMessage.value = response.data.message || 'Erro ao realizar cadastro.';
    }
  } catch (error) {
    errorMessage.value = 'Erro ao conectar com o servidor. Tente novamente mais tarde.';
  }
};

// Função para redirecionar para a página inicial
const goToHome = () => {
  router.push('/');
};

// Função para redirecionar para a página de login
const goToLogin = () => {
  router.push('/login');
};
</script>

<style scoped>
/* Fundo cinza escuro */
.bg-dark-gray {
  background-color: #1e1e1e;
}

/* Fundo mais claro para caixas */
.bg-medium-gray {
  background-color: #3c3c3c;
}

/* Fundo ainda mais claro para bordas */
.border-lighter-gray {
  border-color: #5a5a5a;
}

.bg-light-gray {
  background-color: #d1d5db;
}

/* Degradê verde de baixo para cima */
.bg-gradient-green-inverse {
  background: linear-gradient(to top, #32cd32, transparent 50%);
}

/* Sombra verde */
.shadow-green {
  box-shadow: 0 10px 15px rgba(50, 205, 50, 0.3);
}

.text-gray-300 {
  color: #d1d5db;
}

/* Botões */
button {
  transition: background-color 0.3s, border-color 0.3s;
}

.bg-green-500:hover {
  background-color: #32cd32;
}

.shadow-md {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
}

/* Estilo arredondado */
.rounded-full {
  border-radius: 9999px;
}

.rounded-3xl {
  border-radius: 1.5rem;
}
</style>

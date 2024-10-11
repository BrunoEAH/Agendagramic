<template>
  <div class="min-h-screen bg-dark-gray p-6 flex flex-col justify-between border-white border-2">
    <div class="bg-gradient-green-inverse shadow-green min-h-screen flex flex-col justify-between">
      
      <!-- Barra superior com Nome do Projeto e Logo -->
      <div class="flex justify-between items-center mb-6 justify-end">
        <div class="flex items-center space-x-2">
          <h1 class="text-3xl font-bold text-white">AgendaGramic</h1>
          <button @click="goToHome" class="bg-white p-2 rounded-full shadow-lg">
            <img src="@/assets/images/logo.png" alt="Logo" class="w-6 h-6"/>
          </button>
        </div>
      </div>

      <!-- Conteúdo Principal -->
      <div class="flex flex-col items-center justify-center flex-1 space-y-6">
        <!-- Caixa de boas-vindas -->
        <div class="bg-medium-gray p-4 rounded-3xl shadow-md border-lighter-gray border-2 w-full max-w-3xl mx-auto">
          <h2 class="text-4xl font-bold mb-4 text-center text-white">Bem-vindo ao AgendaGramic!</h2>
        </div>

        <!-- Caixa de descrição do projeto -->
        <div class="bg-medium-gray p-6 rounded-3xl shadow-md border-lighter-gray border-2 w-full max-w-3xl mx-auto">
          <p class="text-gray-300 mb-4">
            AgendaGramic é um sistema de gerenciamento de agendas dinâmico, permitindo que você organize suas tarefas e compromissos de forma simples e eficiente. Nossa versão Alpha inclui funcionalidades como:
          </p>
          <ul class="list-disc list-inside text-gray-300 mb-4">
            <li>Possibilidade de login e cadastro de novos usuários.</li>
            <li>Organização de eventos e compromissos na agenda.</li>
          </ul>
          <p class="text-gray-300">
            Continue acompanhando para mais atualizações e novas funcionalidades!
          </p>
        </div>

        <!-- Botões alinhados em uma linha -->
        <div class="flex space-x-4 mt-6">
          <button @click="goToTest" class="bg-green-500 text-white py-2 px-4 rounded-full hover:bg-green-600 border-white border-2">
            Testes
          </button>
          <button @click="goToLogin" class="bg-green-500 text-white py-2 px-4 rounded-full hover:bg-green-600 border-white border-2">
            Login
          </button>
          <button @click="goToSignup" class="bg-green-500 text-white py-2 px-4 rounded-full hover:bg-green-600 border-white border-2">
            Cadastro
          </button>
          <a href="https://t.me/agendagramic_bot" target="_blank" class="bg-blue-500 text-white py-2 px-4 rounded-full hover:bg-blue-600 border-white border-2">
            Telegram
          </a>
        </div>
      </div>

      <!-- Rodapé com a versão do projeto -->
      <div class="text-center text-gray-300 mt-6">
        AgendaGramic Alpha 0.0.1
      </div>
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
  router.push('/cadastro');
};

// Função para redirecionar para o início da página
const goToHome = () => {
  router.push('/');
};

// Função para redirecionar para a página de teste (profile/index)
const goToTest = () => {
  router.push('/profile');
};
</script>

<style scoped>
/* Fundo cinza escuro */
.bg-dark-gray {
  background-color: #1e1e1e;
}

/* Degradê verde de baixo para cima */
.bg-gradient-green-inverse {
  background: linear-gradient(to top, #32cd32, transparent 50%);
}

/* Sombra verde */
.shadow-green {
  box-shadow: 0 10px 15px rgba(50, 205, 50, 0.3);
}

/* Estilos para caixas de conteúdo */
.bg-medium-gray {
  background-color: #3c3c3c;
}

.border-lighter-gray {
  border-color: #5a5a5a;
}

.text-gray-300 {
  color: #d1d5db;
}

/* Estilo arredondado */
.rounded-3xl {
  border-radius: 1.5rem;
}

/* Estilos para botões */
button {
  border-radius: 5px;
  padding: 10px 20px;
  border: 2px solid white;
  transition: background-color 0.3s, transform 0.2s;
}

button:hover {
  transform: scale(1.05);
}

.text-white {
  color: white;
}

.rounded-full {
  border-radius: 9999px;
}
</style>

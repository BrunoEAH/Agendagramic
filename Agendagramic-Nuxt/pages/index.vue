<template>
  <div class="min-h-screen bg-dark-gray p-6 flex flex-col justify-between border-white border-2">
    <div class="bg-gradient-green shadow-green min-h-screen flex flex-col justify-between rounded-lg overflow-hidden">
      
      <!-- Cabeçalho com Nome do Projeto e Logo -->
      <header class="flex justify-between items-center p-4 bg-dark-gray bg-opacity-90">
        <div class="flex items-center space-x-3">
          <h1 class="text-3xl font-extrabold text-green-500">AgendaGramic</h1>
          <button @click="goToHome" class="bg-white p-2 rounded-full shadow-lg hover:scale-105 transition-transform">
            <img src="@/assets/images/logo.png" alt="Logo" class="w-8 h-8"/>
          </button>
        </div>
      </header>

      <!-- Conteúdo Principal -->
      <main class="flex flex-1 p-6 justify-center items-center space-x-12">
        <!-- Seção de informações à esquerda -->
        <div class="flex flex-col space-y-8 w-1/2 max-w-md">
          <!-- Caixa de boas-vindas -->
          <section class="bg-medium-gray p-6 rounded-3xl shadow-md border-lighter-gray border-2">
            <h2 class="text-4xl font-semibold text-green-400 mb-2 text-center">Bem-vindo ao AgendaGramic!</h2>
            <p class="text-gray-400 text-center">Organize suas tarefas e compromissos de maneira fácil e prática.</p>
          </section>

          <!-- Caixa de descrição do projeto -->
          <section class="bg-medium-gray p-8 rounded-3xl shadow-md border-lighter-gray border-2">
            <h3 class="text-2xl font-semibold text-green-400 text-center">Sobre o AgendaGramic</h3>
            <p class="text-gray-300 leading-relaxed mt-4 text-center">
              AgendaGramic é um sistema de gerenciamento de agendas dinâmico, permitindo que você organize suas tarefas e compromissos de forma prática e eficiente.
            </p>
            <ul class="text-gray-300 list-disc list-inside mt-4 space-y-2">
              <li>Login e cadastro de novos usuários.</li>
              <li>Organização de eventos e compromissos na agenda.</li>
              <li>Integração de eventos,tarefas e grupos com o bot do telegram.</li>
            </ul>
            <p class="text-gray-400 italic mt-4 text-center">* Continue acompanhando para mais atualizações e novas funcionalidades!</p>
          </section>
        </div>

        <!-- Barra divisória ao centro -->
        <div class="divider"></div>

        <!-- Caixa para botões de ação, ajustada para uma altura menor -->
        <div class="bg-medium-gray p-6 rounded-3xl shadow-md border-lighter-gray border-2 flex flex-col items-center space-y-4 w-1/4 max-w-xs" style="height: auto; padding-top: 1.5rem; padding-bottom: 1.5rem;">
          <!-- Botões na ordem solicitada -->
          <a href="https://t.me/agendagramic_bot" target="_blank" class="action-button bg-blue-500 hover:bg-blue-600">Telegram</a>
          <button @click="goToLogin" class="action-button bg-gray-600 text-white hover:bg-gray-700">Login</button>
          <button @click="goToSignup" class="action-button bg-gray-600 text-white hover:bg-gray-700">Cadastro</button>
          <!-- <button @click="goToTest" class="action-button bg-gray-600 text-white hover:bg-gray-700">Testes</button>
          <button @click="testConnection" class="action-button bg-green-500 hover:bg-green-600">Testar Conexão DB</button>
          <button @click="clearDatabase" class="action-button bg-green-500 hover:bg-green-600">Limpar Banco de Dados</button> -->
        </div>
      </main>

      <!-- Rodapé com a versão do projeto -->
      <footer class="text-center text-gray-400 p-4 bg-dark-gray bg-opacity-90">
        AgendaGramic Beta 0.1
      </footer>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import axios from 'axios';

const router = useRouter();

// Funções de navegação e ações
const goToLogin = () => router.push('/login');
const goToSignup = () => router.push('/cadastro');
const goToHome = () => router.push('/');
// const goToTest = () => router.push('/profile');

// const testConnection = async () => {
//   try {
//     const response = await axios.get('/api/testDbConnection');
//     alert(response.data.message);
//   } catch {
//     alert('Erro ao testar conexão com o banco de dados');
//   }
// };

// const clearDatabase = async () => {
//   try {
//     const response = await axios.get('/api/clearDatabase');
//     alert(response.data.message);
//   } catch {
//     alert('Erro ao limpar o banco de dados');
//   }
// };
</script>

<style scoped>
/* Fundo cinza escuro */
.bg-dark-gray {
  background-color: #1e1e1e;
}

/* Degradê verde e sombra */
.bg-gradient-green {
  background: linear-gradient(to top, #32cd32, transparent 50%);
}
.shadow-green {
  box-shadow: 0 10px 15px rgba(50, 205, 50, 0.3);
}

/* Estilo para o cabeçalho */
header {
  background-color: rgba(0, 0, 0, 0.6);
  border-bottom: 1px solid #333;
}

/* Divisória transparente */
.divider {
  width: 2px;
  height: 80%;
  background-color: rgba(200, 200, 200, 0.3);
}

/* Estilo para botões de ação */
.action-button {
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  font-weight: 600;
  border-radius: 9999px;
  border: 2px solid white;
  color: white;
  transition: background-color 0.3s, transform 0.2s;
}
.action-button:hover {
  transform: scale(1.05);
}

/* Fundo e cor para caixas de conteúdo */
.bg-medium-gray {
  background-color: #3c3c3c;
}
.border-lighter-gray {
  border-color: #5a5a5a;
}

.text-gray-300 {
  color: #d1d5db;
}

.text-gray-400 {
  color: #9ca3af;
}

/* Estilo para bordas e botões */
.rounded-full {
  border-radius: 9999px;
}
.rounded-3xl {
  border-radius: 3.5rem;
}
</style>

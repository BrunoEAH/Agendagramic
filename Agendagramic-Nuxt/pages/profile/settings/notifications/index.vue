<template>
  <div class="min-h-screen bg-gradient-green-inverse flex flex-col justify-between">
    <!-- Barra superior com botões de navegação e Nome do Projeto -->
    <header class="flex justify-between items-start px-8 py-4">
      <!-- Botões de "Página Inicial" e "Voltar" -->
      <div class="flex flex-col space-y-2">
        <button 
          @click="goToHome" 
          class="bg-gray-500 text-white py-2 px-4 rounded-full border-white border-2 transition hover:bg-green-500">
          Página Inicial
        </button>
        <button 
          @click="goBack" 
          class="bg-gray-500 text-white py-2 px-4 rounded-full border-white border-2 transition hover:bg-green-500">
          Voltar
        </button>
      </div>
      <!-- Nome do projeto -->
      <h1 class="text-3xl font-bold text-white">AgendaGramic</h1>
    </header>

    <!-- Conteúdo Principal da Página de Notificações -->
    <main class="flex flex-col items-center justify-center flex-1 px-6">
      <div class="bg-medium-gray p-6 rounded-3xl shadow-green w-full max-w-lg border-white border-2">
        <h2 class="text-2xl font-semibold mb-4 text-center text-white">Ajustes de Notificações</h2>
        <p class="text-gray-400 mb-4 text-center">Configure as preferências de notificações por Telegram e email para ficar sempre atualizado.</p>

        <!-- Notificações por Telegram -->
        <h3 class="text-xl font-semibold text-white mb-2">Notificações por Telegram</h3>
        <div class="mb-4">
          <label class="flex items-center space-x-2">
            <input type="checkbox" class="form-checkbox bg-dark-gray border-white rounded focus:ring-green-500">
            <span class="text-white">Receber lembretes diários</span>
          </label>
          <label class="flex items-center space-x-2 mt-2">
            <input type="checkbox" class="form-checkbox bg-dark-gray border-white rounded focus:ring-green-500">
            <span class="text-white">Receber atualizações de eventos</span>
          </label>
        </div>

        <!-- Notificações por Email -->
        <h3 class="text-xl font-semibold text-white mb-2">Notificações por Email</h3>
        <div class="mb-4">
          <label class="flex items-center space-x-2">
            <input type="checkbox" class="form-checkbox bg-dark-gray border-white rounded focus:ring-green-500">
            <span class="text-white">Receber lembretes diários</span>
          </label>
          <label class="flex items-center space-x-2 mt-2">
            <input type="checkbox" class="form-checkbox bg-dark-gray border-white rounded focus:ring-green-500">
            <span class="text-white">Receber atualizações de eventos</span>
          </label>
        </div>

        <!-- Botão para salvar as configurações -->
        <button 
          class="bg-light-gray text-black py-2 px-4 rounded-full border-white border-2 hover:bg-green-500 transition w-full">
          Salvar Configurações
        </button>
      </div>
    </main>

    <!-- Rodapé -->
    <footer class="text-center text-gray-300 py-4">
      AgendaGramic Alpha 0.0.1
    </footer>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

// Função para redirecionar à página inicial (logado)
const goToHome = () => {
  router.push('/profile');
};

// Função para voltar à página anterior
const goBack = () => {
  router.push('/profile/settings');
};
</script>

<style scoped>
/* Fundo com gradiente de baixo para cima */
.bg-gradient-green-inverse {
  background: linear-gradient(to bottom, #32cd32, #1e1e1e);
}

/* Fundo cinza médio */
.bg-medium-gray {
  background-color: #3c3c3c;
}

/* Fundo claro */
.bg-light-gray {
  background-color: #d1d5db;
}

/* Bordas */
.border-white {
  border-color: white;
}

/* Textos */
.text-gray-400 {
  color: #9ca3af;
}

/* Botões */
button, .form-checkbox {
  transition: background-color 0.3s, border-color 0.3s;
}

.bg-green-500:hover {
  background-color: #32cd32;
}

/* Bordas arredondadas */
.rounded-full {
  border-radius: 9999px;
}

.rounded-3xl {
  border-radius: 1.5rem;
}

/* Sombra */
.shadow-green {
  box-shadow: 0 10px 15px rgba(50, 205, 50, 0.3);
}
</style>

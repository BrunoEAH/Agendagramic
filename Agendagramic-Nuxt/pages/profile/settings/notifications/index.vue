<template>
  <div class="min-h-screen bg-dark-gray p-6 flex flex-col justify-between border-white border-2">
    <div class="bg-gradient-green-inverse shadow-green min-h-screen flex flex-col justify-between">
      <!-- Barra superior com botões de navegação e Nome do Projeto -->
      <div class="flex justify-between items-start mb-6">
        <!-- Botões de "Página Inicial" e "Voltar" no canto superior esquerdo -->
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

        <!-- Nome do projeto no canto superior direito -->
        <h1 class="text-3xl font-bold text-white">AgendaGramic</h1>
      </div>

      <!-- Quadro de Desenvolvimento -->
      <div class="flex items-center justify-center mb-6">
        <div class="bg-white p-4 rounded-3xl shadow-md w-full max-w-md text-center">
          <p class="text-lg font-semibold text-black">*Em desenvolvimento*</p>
        </div>
      </div>

      <!-- Conteúdo Principal da Página de Notificações -->
      <div class="flex flex-col items-center justify-center flex-1">
        <div class="bg-medium-gray p-6 rounded-3xl shadow-md w-full max-w-md border-lighter-gray border-2">
          <h2 class="text-2xl font-semibold mb-4 text-center text-white">Ajustes de Notificações</h2>
          <p class="text-gray-400 mb-4 text-center">Configure as preferências de notificações por Telegram e email para ficar sempre atualizado.</p>

          <!-- Notificações por Telegram -->
          <h3 class="text-xl font-semibold text-white mb-2">Notificações por Telegram</h3>
          <div class="mb-4">
            <label class="flex items-center space-x-2">
              <input type="checkbox" class="form-checkbox bg-dark-gray border-lighter-gray rounded focus:ring-green-500">
              <span class="text-white">Receber lembretes diários</span>
            </label>
            <label class="flex items-center space-x-2 mt-2">
              <input type="checkbox" class="form-checkbox bg-dark-gray border-lighter-gray rounded focus:ring-green-500">
              <span class="text-white">Receber atualizações de eventos</span>
            </label>
          </div>

          <!-- Notificações por Email -->
          <h3 class="text-xl font-semibold text-white mb-2">Notificações por Email</h3>
          <div class="mb-4">
            <label class="flex items-center space-x-2">
              <input type="checkbox" class="form-checkbox bg-dark-gray border-lighter-gray rounded focus:ring-green-500">
              <span class="text-white">Receber lembretes diários</span>
            </label>
            <label class="flex items-center space-x-2 mt-2">
              <input type="checkbox" class="form-checkbox bg-dark-gray border-lighter-gray rounded focus:ring-green-500">
              <span class="text-white">Receber atualizações de eventos</span>
            </label>
          </div>

          <!-- Botão para salvar as configurações -->
          <button class="bg-light-gray text-black py-2 px-4 rounded-full border-white border-2 hover:bg-green-500 transition w-full">
            Salvar Configurações
          </button>
        </div>
      </div>

      <!-- Rodapé com a versão do site -->
      <div class="text-center text-gray-300 mt-6">
        AgendaGramic Alpha 0.0.1
      </div>
    </div>
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
/* Fundo cinza escuro */
.bg-dark-gray {
  background-color: #1e1e1e;
}

/* Fundo mais claro */
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

.text-gray-400 {
  color: #9ca3af;
}

/* Estilo arredondado */
.rounded-full {
  border-radius: 9999px;
}

.rounded-3xl {
  border-radius: 1.5rem;
}

/* Botões */
button, .form-checkbox {
  transition: background-color 0.3s, border-color 0.3s;
}

/* Transição para hover */
.bg-green-500:hover {
  background-color: #32cd32;
}

.shadow-md {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
}
</style>

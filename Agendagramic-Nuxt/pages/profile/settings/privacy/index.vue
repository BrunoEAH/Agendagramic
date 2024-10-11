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

      <!-- Conteúdo Principal da Página de Privacidade -->
      <div class="flex flex-col items-center justify-center flex-1">
        <div class="bg-medium-gray p-6 rounded-3xl shadow-md w-full max-w-md border-lighter-gray border-2 mb-6">
          <h2 class="text-2xl font-semibold mb-4 text-center text-white">Privacidade e Segurança</h2>
          <p class="text-gray-400 mb-4 text-center">Gerencie as configurações de privacidade e segurança da sua conta para proteger suas informações.</p>
          
          <!-- Opções de Privacidade -->
          <div class="mb-6">
            <h3 class="text-lg font-semibold text-white mb-2">Configurações de Privacidade</h3>
            <label class="flex items-center mb-2">
              <input type="checkbox" v-model="showEmail" class="form-checkbox rounded-full bg-light-gray border-white border-2 transition focus:ring-0 hover:bg-green-500">
              <span class="ml-2 text-gray-300">Mostrar email para outros usuários</span>
            </label>
            <label class="flex items-center">
              <input type="checkbox" v-model="showPhoneNumber" class="form-checkbox rounded-full bg-light-gray border-white border-2 transition focus:ring-0 hover:bg-green-500">
              <span class="ml-2 text-gray-300">Mostrar número de telefone para outros usuários</span>
            </label>
          </div>

          <!-- Opções de Segurança -->
          <div>
            <h3 class="text-lg font-semibold text-white mb-2">Configurações de Segurança</h3>
            <label class="flex items-center mb-2">
              <input type="checkbox" v-model="twoFactorAuth" class="form-checkbox rounded-full bg-light-gray border-white border-2 transition focus:ring-0 hover:bg-green-500">
              <span class="ml-2 text-gray-300">Habilitar autenticação de dois fatores</span>
            </label>
            <label class="flex items-center">
              <input type="checkbox" v-model="passwordChangeReminder" class="form-checkbox rounded-full bg-light-gray border-white border-2 transition focus:ring-0 hover:bg-green-500">
              <span class="ml-2 text-gray-300">Lembrar de alterar a senha periodicamente</span>
            </label>
          </div>

          <!-- Botão para salvar as configurações -->
          <button @click="savePrivacySettings" class="bg-light-gray text-black py-2 px-4 mt-6 rounded-full border-white border-2 transition hover:bg-green-500 w-full">
            Salvar Configurações
          </button>
        </div>

        <!-- Caixa de Ajuste de Conta com estilo de botão -->
        <button @click="goToAccountSettings" class="bg-light-gray text-black py-2 px-4 mt-4 rounded-full border-white border-2 transition hover:bg-green-500 w-full max-w-md">
          Ajustes de Conta
        </button>
      </div>

      <!-- Rodapé com a versão do site -->
      <div class="text-center text-gray-300 mt-6">
        AgendaGramic Alpha 0.0.1
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

// Variáveis para os estados das configurações de privacidade e segurança
const showEmail = ref(false);
const showPhoneNumber = ref(false);
const twoFactorAuth = ref(false);
const passwordChangeReminder = ref(false);

// Função para redirecionar à página inicial (logado)
const goToHome = () => {
  router.push('/profile');
};

// Função para voltar à página de configurações
const goBack = () => {
  router.push('/profile/settings');
};

// Função para redirecionar à página de Ajustes de Conta
const goToAccountSettings = () => {
  router.push('/profile/settings/account-settings');
};

// Função para salvar as configurações de privacidade e segurança
const savePrivacySettings = () => {
  const privacySettings = {
    showEmail: showEmail.value,
    showPhoneNumber: showPhoneNumber.value,
    twoFactorAuth: twoFactorAuth.value,
    passwordChangeReminder: passwordChangeReminder.value,
  };

  // Salvar as configurações no localStorage (ou em uma API)
  localStorage.setItem('privacySettings', JSON.stringify(privacySettings));

  alert('Configurações de privacidade e segurança salvas com sucesso!');
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

.text-gray-300 {
  color: #d1d5db;
}

/* Botões e caixas de seleção */
button, .form-checkbox {
  transition: background-color 0.3s, border-color 0.3s;
}

/* Transição para hover */
.bg-green-500:hover {
  background-color: #32cd32;
}

/* Sombra */
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

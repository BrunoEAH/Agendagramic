<template>
  <div class="min-h-screen bg-gradient-green-inverse flex flex-col justify-between">
    <!-- Cabeçalho -->
    <header class="flex justify-between items-start px-8 py-4">
      <!-- Botões de navegação -->
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

    <!-- Quadro de Desenvolvimento -->
    <main class="flex flex-col items-center px-6">
      <div class="bg-white p-4 rounded-3xl shadow-green w-full max-w-md text-center mb-6">
        <p class="text-lg font-semibold text-black">*Em desenvolvimento*</p>
      </div>

      <!-- Configurações de Privacidade -->
      <section class="bg-medium-gray p-6 rounded-3xl shadow-green w-full max-w-md border-white border-2">
        <h2 class="text-2xl font-semibold mb-4 text-center text-white">Privacidade e Segurança</h2>
        <p class="text-gray-300 mb-6 text-center">Gerencie as configurações para proteger suas informações pessoais.</p>

        <!-- Privacidade -->
        <div class="mb-6">
          <h3 class="text-lg font-semibold text-white mb-2">Configurações de Privacidade</h3>
          <label class="flex items-center mb-4">
            <input type="checkbox" v-model="showEmail" class="form-checkbox rounded-full bg-dark-gray border-white border-2 focus:ring-0 transition">
            <span class="ml-2 text-gray-300">Mostrar email para outros usuários</span>
          </label>
          <label class="flex items-center">
            <input type="checkbox" v-model="showPhoneNumber" class="form-checkbox rounded-full bg-dark-gray border-white border-2 focus:ring-0 transition">
            <span class="ml-2 text-gray-300">Mostrar número de telefone para outros usuários</span>
          </label>
        </div>

        <!-- Segurança -->
        <div class="mb-6">
          <h3 class="text-lg font-semibold text-white mb-2">Configurações de Segurança</h3>
          <label class="flex items-center mb-4">
            <input type="checkbox" v-model="twoFactorAuth" class="form-checkbox rounded-full bg-dark-gray border-white border-2 focus:ring-0 transition">
            <span class="ml-2 text-gray-300">Habilitar autenticação de dois fatores</span>
          </label>
          <label class="flex items-center">
            <input type="checkbox" v-model="passwordChangeReminder" class="form-checkbox rounded-full bg-dark-gray border-white border-2 focus:ring-0 transition">
            <span class="ml-2 text-gray-300">Lembrar de alterar a senha periodicamente</span>
          </label>
        </div>

        <!-- Botão de salvar -->
        <button 
          @click="savePrivacySettings" 
          class="bg-light-gray text-black py-2 px-4 rounded-full border-white border-2 hover:bg-green-500 transition w-full">
          Salvar Configurações
        </button>
      </section>

      <!-- Ajustes de Conta -->
      <button 
        @click="goToAccountSettings" 
        class="bg-light-gray text-black py-2 px-4 mt-4 rounded-full border-white border-2 hover:bg-green-500 transition w-full max-w-md">
        Ajustes de Conta
      </button>
    </main>

    <!-- Rodapé -->
    <footer class="text-center text-gray-300 py-4">
      AgendaGramic Alpha 0.0.1
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

// Estados para configurações de privacidade e segurança
const showEmail = ref(false);
const showPhoneNumber = ref(false);
const twoFactorAuth = ref(false);
const passwordChangeReminder = ref(false);

// Função para redirecionar à página inicial
const goToHome = () => {
  router.push('/profile');
};

// Função para voltar à página anterior
const goBack = () => {
  router.push('/profile/settings');
};

// Função para ir para Ajustes de Conta
const goToAccountSettings = () => {
  router.push('/profile/settings/account-settings');
};

// Função para salvar as configurações
const savePrivacySettings = () => {
  const privacySettings = {
    showEmail: showEmail.value,
    showPhoneNumber: showPhoneNumber.value,
    twoFactorAuth: twoFactorAuth.value,
    passwordChangeReminder: passwordChangeReminder.value,
  };

  // Salvar as configurações no localStorage (simulação)
  localStorage.setItem('privacySettings', JSON.stringify(privacySettings));

  alert('Configurações de privacidade e segurança salvas com sucesso!');
};
</script>

<style scoped>
/* Fundo com gradiente */
.bg-gradient-green-inverse {
  background: linear-gradient(to bottom, #32cd32, #1e1e1e);
}

/* Fundo médio */
.bg-medium-gray {
  background-color: #3c3c3c;
}

/* Fundo escuro */
.bg-dark-gray {
  background-color: #1e1e1e;
}

/* Fundo claro */
.bg-light-gray {
  background-color: #d1d5db;
}

/* Textos */
.text-gray-300 {
  color: #d1d5db;
}

/* Bordas */
.border-white {
  border-color: white;
}

/* Botões e caixas de seleção */
button, .form-checkbox {
  transition: background-color 0.3s, border-color 0.3s;
}

/* Hover */
.bg-green-500:hover {
  background-color: #32cd32;
}

/* Arredondamento */
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

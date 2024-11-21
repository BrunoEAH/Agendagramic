<template>
  <div class="min-h-screen bg-gradient-green-inverse flex flex-col justify-between">
    <!-- Cabeçalho -->
    <header class="flex justify-between items-center px-8 py-4">
      <!-- Título da Página -->
      <h1 class="text-4xl font-bold text-white">Ajustes de Conta</h1>
      <!-- Nome do Projeto -->
      <h3 class="text-3xl font-semibold text-white">AgendaGramic</h3>
    </header>

    <!-- Botão Voltar -->
    <div class="px-8 mb-4">
      <button 
        @click="goBack" 
        class="bg-light-gray text-black font-bold py-2 px-4 rounded-full border-white border-2 hover:bg-green-500 transition">
        Voltar
      </button>
    </div>

    <!-- Formulário de Ajustes -->
    <main class="flex flex-col items-center px-6">
      <section class="bg-medium-gray p-6 rounded-3xl shadow-green w-full max-w-md border-white border-2">
        <h2 class="text-2xl font-semibold mb-4 text-center text-white">Editar Informações da Conta</h2>

        <!-- Nome -->
        <div class="mb-6">
          <label class="block text-white text-sm font-bold mb-2">Nome Atual:</label>
          <p class="mb-4 text-gray-400">teste</p>
          <label for="newName" class="block text-white text-sm font-bold mb-2">Nome Novo:</label>
          <input
            v-model="newName"
            id="newName"
            type="text"
            placeholder="Digite seu novo nome"
            class="input-field"
          />
        </div>

        <!-- Email -->
        <div class="mb-6">
          <label class="block text-white text-sm font-bold mb-2">Email Atual:</label>
          <p class="mb-4 text-gray-400">teste</p>
          <label for="newEmail" class="block text-white text-sm font-bold mb-2">Email Novo:</label>
          <input
            v-model="newEmail"
            id="newEmail"
            type="email"
            placeholder="Digite seu novo email"
            class="input-field"
          />
        </div>

        <!-- Usuário do Telegram -->
        <div class="mb-6">
          <label class="block text-white text-sm font-bold mb-2">Usuário do Telegram Atual:</label>
          <p class="mb-4 text-gray-400">@teste</p>
          <label for="newUser" class="block text-white text-sm font-bold mb-2">Usuário Novo:</label>
          <input
            v-model="newUser"
            id="newUser"
            type="text"
            placeholder="Digite seu novo usuário"
            class="input-field"
          />
        </div>

        <!-- Senha -->
        <div class="mb-6">
          <label class="block text-white text-sm font-bold mb-2">Senha Atual:</label>
          <p class="mb-4 text-gray-400">teste</p>
          <label for="newPassword" class="block text-white text-sm font-bold mb-2">Senha Nova:</label>
          <input
            v-model="newPassword"
            id="newPassword"
            type="password"
            placeholder="Digite sua nova senha"
            class="input-field"
          />
        </div>

        <!-- Botão Salvar -->
        <button 
          @click="saveChanges" 
          class="bg-light-gray text-black font-bold py-2 px-4 rounded-full border-white border-2 hover:bg-green-500 transition w-full">
          Salvar Alterações
        </button>
      </section>
    </main>

    <!-- Rodapé -->
    <footer class="text-center text-gray-300 py-4">
      AgendaGramic
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const newName = ref('');
const newEmail = ref('');
const newUser = ref('');
const newPassword = ref('');
const router = useRouter();

const saveChanges = () => {
  alert('Alterações salvas... calma aí, ainda em desenvolvimento!');
};

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

/* Campos de entrada */
.input-field {
  background-color: #2e2e2e;
  color: white;
  border: 1px solid #5a5a5a;
  border-radius: 9999px;
  width: 100%;
  padding: 0.5rem 1rem;
  outline: none;
  transition: border-color 0.3s;
}

.input-field:focus {
  border-color: #32cd32;
}

/* Textos */
.text-gray-400 {
  color: #9ca3af;
}

/* Bordas */
.border-white {
  border-color: white;
}

.border-lighter-gray {
  border-color: #5a5a5a;
}

/* Botões */
button {
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

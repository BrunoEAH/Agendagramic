<template>
  <div class="min-h-screen bg-dark-gray p-6 flex flex-col justify-between border-white border-2">
    <div class="bg-gradient-green-inverse shadow-green min-h-screen flex flex-col justify-between">
      <!-- Cabeçalho da página com Ajustes de Conta no canto esquerdo e AgendaGramic no direito -->
      <div class="flex justify-between items-center mb-6">
        <!-- Ajustes de Conta no canto superior esquerdo -->
        <h1 class="text-4xl font-bold text-white">Ajustes de Conta</h1>

        <!-- AgendaGramic no canto superior direito -->
        <div>
          <h3 class="text-3xl font-semibold text-white">AgendaGramic</h3>
        </div>
      </div>

      <!-- Botão Voltar logo abaixo de "Ajustes de Conta" -->
      <div class="mb-6">
        <button @click="goBack" class="bg-light-gray text-black font-bold py-2 px-4 rounded-full border-white border-2 hover:bg-green-500 transition">
          Voltar
        </button>
      </div>

      <!-- Quadro de Desenvolvimento -->
      <div class="flex items-center justify-center mb-6">
        <div class="bg-white p-4 rounded-3xl shadow-md w-full max-w-md text-center">
          <p class="text-lg font-semibold text-black">*Desenvolvimento*</p>
        </div>
      </div>

      <!-- Centralizar caixa de ajustes de conta -->
      <div class="flex flex-col items-center justify-center flex-1">
        <div class="bg-medium-gray p-6 rounded-3xl shadow-md w-full max-w-md border-lighter-gray border-2">
          <h2 class="text-2xl font-semibold mb-4 text-center text-white">Editar Informações da Conta</h2>

          <!-- Nome Atual e Novo -->
          <div class="mb-6">
            <label class="block text-white text-sm font-bold mb-2">Nome Atual:</label>
            <p class="mb-4 text-gray-400">teste</p>

            <label for="newName" class="block text-white text-sm font-bold mb-2">Nome Novo:</label>
            <input
              v-model="newName"
              class="shadow appearance-none border border-lighter-gray rounded-full w-full py-2 px-3 text-white bg-dark-gray focus:outline-none focus:shadow-outline"
              id="newName"
              type="text"
              placeholder="Digite seu novo nome"
            />
          </div>

          <!-- Email Atual e Novo -->
          <div class="mb-6">
            <label class="block text-white text-sm font-bold mb-2">Email Atual:</label>
            <p class="mb-4 text-gray-400">teste</p>

            <label for="newEmail" class="block text-white text-sm font-bold mb-2">Email Novo:</label>
            <input
              v-model="newEmail"
              class="shadow appearance-none border border-lighter-gray rounded-full w-full py-2 px-3 text-white bg-dark-gray focus:outline-none focus:shadow-outline"
              id="newEmail"
              type="email"
              placeholder="Digite seu novo email"
            />
          </div>

                    
          
          <!-- Usuario Atual e Novo -->
         <div class="mb-6">
            <label class="block text-white text-sm font-bold mb-2">Usuário do telegram Atual:</label>
            <p class="mb-4 text-gray-400">@teste</p>

            <label for="newUser" class="block text-white text-sm font-bold mb-2">Usuário Novo:</label>
            <input
              v-model="newUser"
              class="shadow appearance-none border border-lighter-gray rounded-full w-full py-2 px-3 text-white bg-dark-gray focus:outline-none focus:shadow-outline"
              id="newUser"
              type="text"
              placeholder="Digite seu novo usuário"
            />
          </div>


          <!-- Senha Atual e Nova -->
          <div class="mb-6">
            <label class="block text-white text-sm font-bold mb-2">Senha Atual:</label>
            <p class="mb-4 text-gray-400">teste</p>

            <label for="newPassword" class="block text-white text-sm font-bold mb-2">Senha Nova:</label>
            <input
              v-model="newPassword"
              class="shadow appearance-none border border-lighter-gray rounded-full w-full py-2 px-3 text-white bg-dark-gray focus:outline-none focus:shadow-outline"
              id="newPassword"
              type="password"
              placeholder="Digite sua nova senha"
            />
          </div>

          <!-- Botão de salvar -->
          <button @click="saveChanges" class="bg-light-gray text-black font-bold py-2 px-4 rounded-full border-white border-2 hover:bg-green-500 transition w-full">
            Salvar Alterações
          </button>
        </div>
      </div>

      <!-- Rodapé -->
      <div class="text-center text-gray-300 mt-6">
        AgendaGramic Alpha 0.0.1
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const newName = ref('');
const newEmail = ref('');
const newPassword = ref('');
const router = useRouter();

const saveChanges = () => {
  alert('Alterações salv... Calma ai amostradinho, estamos desenvolvendo!');
};

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
button {
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

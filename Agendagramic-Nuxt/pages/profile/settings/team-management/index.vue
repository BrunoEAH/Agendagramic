<template>
  <div class="min-h-screen bg-gradient-green-inverse flex flex-col justify-between">
    <!-- Header -->
    <header class="flex justify-between items-start px-8 py-4">
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
      <h1 class="text-3xl font-bold text-white">AgendaGramic</h1>
    </header>

    <!-- Main Content -->
    <main class="flex flex-col items-center px-6">
      <div class="bg-white p-4 rounded-3xl shadow-md w-full max-w-md text-center mb-6">
        <p class="text-lg font-semibold text-black">Gerenciamento de Equipes</p>
      </div>

      <!-- Groups Management -->
      <div class="flex flex-col space-y-6 max-w-lg w-full">
        <!-- Existing Groups -->
        <section class="bg-medium-gray p-6 rounded-3xl shadow-md border-lighter-gray border-2">
          <h2 class="text-2xl font-semibold text-white mb-4">Grupos Atuais</h2>
          <div v-if="teams.length > 0" class="space-y-4">
            <div 
              v-for="(team, index) in teams" 
              :key="team.group_id" 
              class="bg-light-gray p-4 rounded-3xl border-white border-2"
            >
              <h3 class="text-xl font-semibold text-black mb-2">{{ team.group_name }}</h3>
              <ul>
                <li class="text-gray-400">Grupo ID: {{ team.group_id }}</li>
              </ul>
            </div>
          </div>
          <p v-else class="text-gray-300">Nenhum grupo criado ainda.</p>
        </section>

        <!-- Create New Group -->
        <section class="bg-medium-gray p-6 rounded-3xl shadow-md border-lighter-gray border-2">
          <h2 class="text-2xl font-semibold text-white mb-4">Criar Novo Grupo</h2>
          <input
            v-model="newGroupName"
            class="bg-light-gray text-black py-2 px-4 mb-4 rounded-full border-white border-2 w-full"
            type="text"
            placeholder="Digite o nome do grupo"
          />
          <button 
            @click="createTeam" 
            class="bg-light-gray text-black py-2 px-4 rounded-full border-white border-2 transition hover:bg-green-500 w-full"
          >
            Criar Grupo
          </button>
        </section>

        <!-- Test Buttons -->
        <section class="bg-medium-gray p-6 rounded-3xl shadow-md border-lighter-gray border-2">
          <h2 class="text-2xl font-semibold text-white mb-4">Testar Funcionalidades</h2>
          <div class="flex flex-col space-y-4">
            <button 
              @click="testConnection" 
              class="bg-blue-500 text-white py-2 px-4 rounded-full border-white border-2 transition hover:bg-blue-600 w-full"
            >
              Testar Conexão com Grupos
            </button>
            <button 
              @click="manualLoadGroups" 
              class="bg-yellow-500 text-white py-2 px-4 rounded-full border-white border-2 transition hover:bg-yellow-600 w-full"
            >
              Carregar Grupos Manualmente
            </button>
          </div>
        </section>
      </div>
    </main>

    <footer class="text-center text-gray-300 py-4">
      AgendaGramic Beta 0.1
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const newGroupName = ref('');
const teams = ref([]);
const groupAdmin = ref('default_user');

// Garantir que userTelegram está definido corretamente
if (process.client) {
  const savedUserTelegram = localStorage.getItem('userTelegram');
  if (savedUserTelegram) {
    groupAdmin.value = savedUserTelegram;
  } else {
    alert('UserTelegram não encontrado. Certifique-se de fazer login.');
    localStorage.setItem('userTelegram', '@teste'); // Ajuste conforme necessário
    groupAdmin.value = '@teste';
  }
  console.log('Valor de groupAdmin:', groupAdmin.value);
}

// Navegar para a página inicial
const goToHome = () => router.push('/profile');

// Voltar para a página anterior
const goBack = () => router.back();

// Carregar Grupos
const loadGroups = async () => {
  try {
    console.log('Iniciando carregamento dos grupos...');
    const response = await $fetch('/api/getGroups', {
      method: 'GET',
      params: { userTelegram: groupAdmin.value },
    });

    console.log('Resposta completa da API:', response);

    if (response.groups && Array.isArray(response.groups)) {
      teams.value = response.groups.map((group) => ({
        group_id: group.group_id,
        group_name: group.group_name,
      }));
      console.log('Grupos formatados para exibição:', teams.value);
    } else {
      teams.value = [];
      console.warn('Nenhum grupo encontrado ou formato inesperado:', response.groups);
    }
  } catch (error) {
    console.error('Erro ao carregar grupos:', error.message, error);
    alert('Erro ao carregar grupos. Verifique sua conexão.');
  }
};

// Criar Novo Grupo
const createTeam = async () => {
  if (!newGroupName.value.trim()) {
    alert('Por favor, insira um nome válido para o grupo.');
    return;
  }

  try {
    console.log('Criando novo grupo...');
    const response = await $fetch('/api/addGroup', {
      method: 'POST',
      body: { groupName: newGroupName.value, groupAdmin: groupAdmin.value },
    });

    console.log('Resposta da API ao criar grupo:', response);

    if (response.success) {
      alert('Grupo criado com sucesso!');
      newGroupName.value = ''; // Limpar entrada
      await loadGroups(); // Recarregar lista de grupos
    } else {
      alert('Erro ao criar o grupo.');
    }
  } catch (error) {
    console.error('Erro ao criar grupo:', error.message, error);
    alert('Erro ao criar o grupo. Tente novamente mais tarde.');
  }
};

// Testar Conexão
const testConnection = async () => {
  try {
    const response = await $fetch('/api/getGroups', {
      method: 'GET',
      params: { userTelegram: groupAdmin.value },
    });

    if (response.groups) {
      alert('Conexão com a tabela de grupos bem-sucedida!');
    } else {
      alert('Não foi possível conectar à tabela de grupos.');
    }
  } catch (error) {
    console.error('Erro ao testar conexão:', error.message, error);
    alert('Erro ao conectar à tabela de grupos.');
  }
};

// Carregar Grupos Manualmente
const manualLoadGroups = async () => {
  console.log('Carregando grupos manualmente...');
  await loadGroups();
  alert(`Grupos carregados manualmente: ${teams.value.length}`);
};

// Carregar grupos ao montar o componente
onMounted(() => {
  console.log('Montando o componente e carregando grupos...');
  loadGroups();
});
</script>

<style scoped>
.bg-gradient-green-inverse {
  background: linear-gradient(to bottom, #32cd32, #1e1e1e);
}
.bg-medium-gray {
  background-color: #3c3c3c;
}
.bg-light-gray {
  background-color: #d1d5db;
}
.border-lighter-gray {
  border-color: #5a5a5a;
}
button {
  transition: background-color 0.3s, border-color 0.3s;
}
.bg-green-500:hover {
  background-color: #32cd32;
}
.bg-blue-500:hover {
  background-color: #2563eb;
}
.bg-yellow-500:hover {
  background-color: #facc15;
}
.bg-red-500:hover {
  background-color: #dc2626;
}
.rounded-full {
  border-radius: 9999px;
}
.rounded-3xl {
  border-radius: 1.5rem;
}
</style>

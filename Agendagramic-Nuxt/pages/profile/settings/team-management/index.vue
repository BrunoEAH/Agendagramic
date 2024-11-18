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

    <!-- Quadro de Desenvolvimento -->
    <main class="flex flex-col items-center px-6">
      <div class="bg-white p-4 rounded-3xl shadow-md w-full max-w-md text-center mb-6">
        <p class="text-lg font-semibold text-black">*Em Desenvolvimento*</p>
      </div>

        <section class="bg-medium-gray p-6 rounded-3xl shadow-md border-lighter-gray border-2">
    <h2 class="text-2xl font-semibold text-white mb-4">Suas Equipes</h2>
    <div v-if="userGroups.length" class="space-y-4">
      <div 
        v-for="(group, index) in userGroups" 
        :key="index" 
        class="bg-light-gray p-4 rounded-3xl border-white border-2"
      >
        <h3 class="text-xl font-semibold text-black mb-2">{{ group.name }}</h3>
      </div>
    </div>
    <p v-else class="text-gray-300">Você ainda não está registrado em nenhuma equipe.</p>
  </section>


      <!-- Conteúdo Principal da Página de Gerenciamento de Equipe -->
      <div class="flex flex-col space-y-6 max-w-lg w-full">
        <!-- Caixa de Gerenciar Equipes -->
        <section class="bg-medium-gray p-6 rounded-3xl shadow-md border-lighter-gray border-2">
          <h2 class="text-2xl font-semibold text-white mb-4">Equipes Atuais</h2>
          <div v-if="teams.length" class="space-y-4">
            <div 
              v-for="(team, index) in teams" 
              :key="index" 
              class="bg-light-gray p-4 rounded-3xl border-white border-2"
            >
              <h3 class="text-xl font-semibold text-black mb-2">{{ team.name }}</h3>
              <ul class="space-y-2">
                <li 
                  v-for="(member, memberIndex) in team.members" 
                  :key="memberIndex" 
                  class="flex justify-between items-center bg-gray-300 p-2 rounded-full"
                >
                  <span class="text-black">{{ member }}</span>
                  <button 
                    @click="removeMember(index, memberIndex)" 
                    class="bg-red-500 text-white py-1 px-2 rounded-full transition hover:bg-red-600"
                  >
                    Remover
                  </button>
                </li>
              </ul>
              <button 
                @click="addMemberToTeam(index)" 
                class="bg-green-500 text-white py-2 px-4 mt-4 rounded-full transition hover:bg-green-600 w-full"
              >
                Adicionar Membro
              </button>
            </div>
          </div>
          <p v-else class="text-gray-300">Nenhuma equipe criada ainda.</p>
        </section>

        <!-- Caixa para Criar Nova Equipe -->
        <section class="bg-medium-gray p-6 rounded-3xl shadow-md border-lighter-gray border-2">
          <h2 class="text-2xl font-semibold text-white mb-4">Criar Nova Equipe</h2>
          <input
            v-model="newTeamName"
            class="bg-light-gray text-black py-2 px-4 mb-4 rounded-full border-white border-2 w-full"
            type="text"
            placeholder="Digite o nome da equipe"
          />
          <button 
            @click="createTeam" 
            class="bg-light-gray text-black py-2 px-4 rounded-full border-white border-2 transition hover:bg-green-500 w-full"
          >
            Criar Equipe
          </button>
        </section>
      </div>
    </main>

    <!-- Rodapé com a versão do site -->
    <footer class="text-center text-gray-300 py-4">
      AgendaGramic Alpha 0.0.1
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useFetch } from '#app';

const router = useRouter();

// Estado para armazenar o nome da nova equipe
const newTeamName = ref('');

// Estado para armazenar as equipes e seus membros
const teams = ref([]);

const groupAdmin = ref('default_user');

const userGroups = ref([]);


const fetchUserGroups = async () => {
  try {

    const userTelegram = groupAdmin.value;

    const response = await $fetch(`/api/getGroupsName?userTelegram=${encodeURIComponent(userTelegram)}`);
    console.log('API Response:', response);
    
    if (response.success) {
      const groups = Array.isArray(response.groups) ? response.groups : [response.groups];
      userGroups.value = groups.map(group => ({
        name: group.group_name,
      }));
    } else {
      console.error('Failed to fetch user groups.');
    }
  } catch (error) {
    console.error('Error fetching user groups:', error);
  }
};


// Função para redirecionar à página inicial (logado)
const goToHome = () => {
  router.push('/profile');
};

// Função para voltar para a página anterior
const goBack = () => {
  router.back();
};

// Função para criar uma nova equipe
const createTeam = async () => {
  if (newTeamName.value) {
    const userTelegram = groupAdmin.value;

    const newTeam = {groupName: newTeamName.value, userTelegram };

    try {
      const response = await $fetch('/api/addGroup', {
        method: 'POST',
        body: newTeam,
      });

      console.log('Response:', response);

      if (response.success) {
        teams.value.push({ name: newTeamName.value, members: [] });
        newTeamName.value = ''; // Clear the input field after team creation
        console.log('Grupo adicionado:', response); // Log the response data
      } else {
        throw new Error('Erro ao adicionar o grupo.'); // If not successful, throw error
      }
    } catch (error) {
      console.error('Erro ao adicionar o grupo:', error);
      alert('Erro ao adicionar o grupo.');
    }
  } else {
    alert('Por favor, insira um nome válido para a equipe.');
  }
};

// Função para adicionar um membro a uma equipe
const addMemberToTeam = async (teamIndex) => {
  const email = prompt('Digite o email do membro:');
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Regex para email
  if (emailRegex.test(email)) {
    try {
      const response = await fetch(`/api/checkEmail?email=${encodeURIComponent(email)}`);
      const data = await response.json();

      if (data.exists) {
        teams.value[teamIndex].members.push(email);
        alert('Membro adicionado com sucesso!');
      } else {
        alert('Email não encontrado no banco de dados. Por favor, verifique o email.');
      }
    } catch (error) {
      console.error('Erro ao checar o email:', error);
      alert('Erro ao verificar o email. Tente novamente mais tarde.');
    }
  } else {
    alert('Por favor, insira um email válido.');
  }
};

// Função para remover um membro da equipe
const removeMember = (teamIndex, memberIndex) => {
  teams.value[teamIndex].members.splice(memberIndex, 1);
};

onMounted(async () => {
  if (process.client) {
    const storedTelegram = localStorage.getItem('userTelegram');
    if (storedTelegram) {
      groupAdmin.value = storedTelegram;
      await fetchUserGroups();
    } else {
      console.warn('No Telegram ID found in local storage.');
    }
  }
});


</script>

<style scoped>
/* Fundo com gradiente de baixo para cima */
.bg-gradient-green-inverse {
  background: linear-gradient(to bottom, #32cd32, #1e1e1e);
}

/* Estilos gerais */
.bg-medium-gray {
  background-color: #3c3c3c;
}
.bg-light-gray {
  background-color: #d1d5db;
}
.border-lighter-gray {
  border-color: #5a5a5a;
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
.bg-red-500:hover {
  background-color: #dc2626;
}

/* Bordas */
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
.shadow-md {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
}
</style>

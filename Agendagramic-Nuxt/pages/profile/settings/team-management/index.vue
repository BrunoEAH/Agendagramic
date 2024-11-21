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

  <section class="bg-medium-gray p-6 rounded-3xl shadow-md border-lighter-gray border-2">
  <h2 class="text-2xl font-semibold text-white mb-4">Grupos em que Você é Membro</h2>
  <div v-if="memberGroups.length" class="space-y-4">
    <div 
      v-for="(group, index) in memberGroups" 
      :key="index" 
      class="bg-light-gray p-4 rounded-3xl border-white border-2"
    >
      <h3 class="text-xl font-semibold text-black mb-2">{{ group.name }}</h3>
    </div>
  </div>
  <p v-else class="text-gray-300">Você não é membro de nenhum grupo ainda.</p>
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
import axios from 'axios';

const router = useRouter();

// Estado para armazenar o nome da nova equipe
const newTeamName = ref('');

// Estado para armazenar as equipes e seus membros
const teams = ref([]);

const memberGroups = ref([]);

const groupAdmin = ref('default_user');

const userGroups = ref([]);

const fetchUserGroups = async() => {
      try {
        const response = await axios.get(`http://localhost:5000/api/groups`, {
          params: {
            userTelegram: groupAdmin.value,
          },
        });
        console.log('API Response:', response.data);
        if (response.data.success) {
          userGroups.value = response.data.groups.map(group => ({
          name: group[0] || group.name || group,
          }));
        } else {
          console.error('Failed to fetch groups:', response.data.message);
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
};

const fetchUserMembership = async() => {
  try {
        const response = await axios.get(`http://localhost:5000/api/groups_membro`, {
          params: {
            userTelegram: groupAdmin.value,
          },
        });
        console.log('API Response:', response.data);
        if (response.data.success) {
          memberGroups.value = response.data.groups.map(group => ({
          name: group[0] || group.name || group,
          }));
        } else {
          console.error('Failed to fetch groups:', response.data.message);
        }
      } catch (error) {
        console.error('Error fetching data:', error);
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

  const storedTelegram = localStorage.getItem('userTelegram');

  if (!storedTelegram) {
    alert('Telegram ID não encontrado. Por favor, faça login.');
    return;
  }
  
  groupAdmin.value = storedTelegram; 
  const userTelegram = groupAdmin.value;

  if (newTeamName.value) {

    const newTeam = {groupName: newTeamName.value, groupAdmin: userTelegram };

    try {
      const response = await $fetch('/api/addGroup', {
        method: 'POST',
        body: newTeam,
      });

      console.log('Response:', response);

      if (response.success) {
        teams.value.push({ name: newTeamName.value, members: [] });
        newTeamName.value = '';
        console.log('Grupo adicionado:', response); 
      } else {
        throw new Error('Erro ao adicionar o grupo.');
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
  const usuario_telegram = prompt('Digite o telegram do membro:');
  const tgRegex = /^@[A-Za-z0-9_]{5,32}$/; // Regex para user do telegram
  if (tgRegex.test(usuario_telegram)) {
    try {

      const storedTelegram = localStorage.getItem('userTelegram');
      groupAdmin.value = storedTelegram;
      const admin = groupAdmin.value;
      const response = await fetch(`/api/checkTgUser?user=${encodeURIComponent(usuario_telegram)}`);
      const data = await response.json();
      console.log(newTeamName.value)

      if (data.exists) {
        teams.value[teamIndex].members.push(usuario_telegram);

        const nome_grupo = teams.value[teamIndex].name;

        const memberData = {nomeGrupo:nome_grupo,userMember:usuario_telegram,admin:admin};

        const addMemberResponse = await $fetch('/api/addMembers', {
          method: 'POST',
          body: memberData,
        });

        if (addMemberResponse.success) {
          alert('Membro adicionado com sucesso!');
        } else {
          alert('Erro ao adicionar o membro.');
        }
      } else {
        alert('Usuario não encontrado no banco de dados. Por favor, verifique o @.');
      }
    } catch (error) {
      console.error('Erro ao checar o usuario:', error);
      alert('Erro ao verificar o usuario. Tente novamente mais tarde.');
    }
  } else {
    alert('Por favor, insira um usuario válido.');
  }
};

// Função para remover um membro da equipe
const removeMember = async (teamIndex, memberIndex) => {
  const memberToRemove = teams.value[teamIndex].members[memberIndex];
  
  const confirmation = confirm(`Tem certeza que deseja remover ${memberToRemove} da equipe?`);
  if (!confirmation) return;

  teams.value[teamIndex].members.splice(memberIndex, 1);
  
  const teamName = teams.value[teamIndex].name;
  const admin = groupAdmin.value;

  const removeData = { nomeGrupo: teamName, userMember: memberToRemove, admin: admin };

  try {
    const response = await $fetch('/api/removeMember', {
      method: 'POST',
      body: removeData,
    });

    if (response.success) {
      alert(`${memberToRemove} removido da equipe com sucesso!`);
    } else {
      throw new Error('Erro ao remover o membro.');
    }
  } catch (error) {
    console.error('Erro ao remover o membro:', error);
    alert('Erro ao remover o membro. Tente novamente.');
  }

};

onMounted(async () => {
  if (process.client) {
    const storedTelegram = localStorage.getItem('userTelegram');
    if (storedTelegram) {
      groupAdmin.value = storedTelegram;
      await fetchUserGroups();
      await fetchUserMembership()
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

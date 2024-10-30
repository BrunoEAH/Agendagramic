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
          <p class="text-lg font-semibold text-black">*Em Desenvolvimento*</p>
        </div>
      </div>

      <!-- Conteúdo Principal da Página de Gerenciamento de Equipe -->
      <div class="flex flex-col space-y-6 max-w-lg mx-auto">
        <!-- Caixa de Gerenciar Equipes -->
        <div class="bg-medium-gray p-6 rounded-3xl shadow-md border-lighter-gray border-2">
          <h2 class="text-2xl font-semibold text-white mb-4">Equipes Atuais</h2>
          <div v-if="teams.length" class="space-y-4">
            <div v-for="(team, index) in teams" :key="index" class="bg-light-gray p-4 rounded-3xl border-white border-2">
              <h3 class="text-xl font-semibold text-black mb-2">{{ team.name }}</h3>
              <ul class="space-y-2">
                <li v-for="(member, memberIndex) in team.members" :key="memberIndex" class="flex justify-between items-center bg-gray-300 p-2 rounded-full">
                  <span class="text-black">{{ member }}</span>
                  <button @click="removeMember(index, memberIndex)" class="bg-red-500 text-white py-1 px-2 rounded-full transition hover:bg-red-600">
                    Remover
                  </button>
                </li>
              </ul>
              <button @click="addMemberToTeam(index)" class="bg-green-500 text-white py-2 px-4 mt-4 rounded-full transition hover:bg-green-600 w-full">
                Adicionar Membro
              </button>
            </div>
          </div>
          <p v-else class="text-gray-300">Nenhuma equipe criada ainda.</p>
        </div>

        <!-- Caixa para Criar Nova Equipe -->
        <div class="bg-medium-gray p-6 rounded-3xl shadow-md border-lighter-gray border-2">
          <h2 class="text-2xl font-semibold text-white mb-4">Criar Nova Equipe</h2>
          <input
            v-model="newTeamName"
            class="bg-light-gray text-black py-2 px-4 mb-4 rounded-full border-white border-2 w-full"
            type="text"
            placeholder="Digite o nome da equipe"
          />
          <button @click="createTeam" class="bg-light-gray text-black py-2 px-4 rounded-full border-white border-2 transition hover:bg-green-500 w-full">
            Criar Equipe
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
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

// Estado para armazenar o nome da nova equipe
const newTeamName = ref('');

// Estado para armazenar as equipes e seus membros
const teams = ref([]);

var group_ID = 2;

const groupAdmin = "@Usuario"


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

    const newTeam = {group_ID : group_ID, groupName:newTeamName.value, groupAdmin:groupAdmin};

    try {
    const { data,error } = await $fetch('/api/addGroup', {
      method: 'POST',
      body: newTeam,
    });
    
    if (error.value) {
      throw new Error(error.value); // Handle fetch error
    }

    teams.value.push({ name: newTeamName.value, members: [] });
    newTeamName.value = ''; // Limpa o campo após criar a equipe
    console.log('Grupo adicionado:', data.value);

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
    try{
      const response = await fetch(`/api/checkEmail?email=${encodeURIComponent(email)}`);
      const data = await response.json();

      if(data.exists){
        teams.value[teamIndex].members.push(email);
        alert('Membro adicionado com sucesso!');
      } else {
      alert('Email não encontrado no banco de dados. Por favor, verifique o email.');
      }
    }
    catch(error) {
      console.error('Erro ao checar o email:', error);
      alert('Erro ao verificar o email. Tente novamente mais tarde.');
    }
  }
  else{
    alert('Por favor, insira um email válido.');
  }
};

// Função para remover um membro da equipe
const removeMember = (teamIndex, memberIndex) => {
  teams.value[teamIndex].members.splice(memberIndex, 1);
};
</script>

<style scoped>
/* Fundo cinza escuro */
.bg-dark-gray {
  background-color: #1e1e1e;
}

/* Degradê verde de baixo para cima */
.bg-gradient-green-inverse {
  background: linear-gradient(to top, #32cd32, transparent 50%);
}

/* Sombra verde */
.shadow-green {
  box-shadow: 0 10px 15px rgba(50, 205, 50, 0.3);
}

/* Estilos para caixas de conteúdo */
.bg-medium-gray {
  background-color: #3c3c3c;
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

.bg-light-gray {
  background-color: #d1d5db;
}

.bg-green-500:hover {
  background-color: #32cd32;
}

.bg-red-500:hover {
  background-color: #dc2626;
}

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

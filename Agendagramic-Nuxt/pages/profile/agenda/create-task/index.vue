<template>
  <div class="min-h-screen bg-gradient-green-inverse flex flex-col justify-between">
    <!-- Cabeçalho -->
    <header class="flex justify-between items-center px-8 py-4">
      <h1 class="text-4xl font-bold text-white">Criar Nova Tarefa</h1>
      <h3 class="text-3xl font-semibold text-white">AgendaGramic</h3>
    </header>

    <!-- Formulário de criação de tarefa -->
    <main class="flex flex-col items-center flex-1 px-6">
      <div class="bg-medium-gray shadow-green w-full max-w-4xl rounded-3xl p-8 border-white border-2">
        <h2 class="text-2xl font-semibold mb-4 text-white">Detalhes da Tarefa</h2>

        <!-- Nome da Tarefa -->
        <div class="mb-4">
          <label for="taskName" class="block text-white text-sm font-bold mb-2">Nome da Tarefa</label>
          <input
            v-model="taskName"
            class="bg-light-gray shadow appearance-none border rounded-full w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline"
            id="taskName"
            type="text"
            placeholder="Digite o nome da tarefa"
          />
        </div>

        <!-- Descrição da Tarefa -->
        <div class="mb-4">
          <label for="taskDescription" class="block text-white text-sm font-bold mb-2">Descrição</label>
          <textarea
            v-model="taskDescription"
            class="bg-light-gray shadow appearance-none border rounded-lg w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline"
            id="taskDescription"
            rows="4"
            placeholder="Descreva a tarefa"
          ></textarea>
        </div>

        <!-- Data de Conclusão -->
        <div class="mb-4">
          <label for="dueDate" class="block text-white text-sm font-bold mb-2">Data de Conclusão</label>
          <input
            v-model="dueDate"
            class="bg-light-gray shadow appearance-none border rounded-full w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline"
            id="dueDate"
            type="date"
          />
        </div>

        <!-- Prioridade da Tarefa -->
        <div class="mb-4">
          <label for="taskPriority" class="block text-white text-sm font-bold mb-2">Prioridade da Tarefa</label>
          <select
            v-model="taskPriority"
            class="bg-light-gray shadow appearance-none border rounded-full w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline"
            id="taskPriority"
          >
            <option value="alta">Alta</option>
            <option value="media">Média</option>
            <option value="baixa">Baixa</option>
          </select>
        </div>

        <!-- Status da Tarefa -->
        <div class="mb-4">
          <label for="taskStatus" class="block text-white text-sm font-bold mb-2">Status da Tarefa</label>
          <select
            v-model="taskStatus"
            class="bg-light-gray shadow appearance-none border rounded-full w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline"
            id="taskStatus"
          >
            <option :value="0">Pendente</option>
            <option :value="1">Em Progresso</option>
            <option :value="2">Concluída</option>
          </select>
        </div>

        <!-- Responsáveis -->
        <div class="mb-4">
          <label for="taskMembers" class="block text-white text-sm font-bold mb-2">Responsáveis pela tarefa</label>
          <textarea
            v-model="taskMembers"
            class="bg-light-gray shadow appearance-none border rounded-lg w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline"
            id="taskMembers"
            rows="4"
            placeholder="Escreva o nome dos responsáveis"
          ></textarea>
        </div>

        <!-- Grupo -->
        <div class="mb-4">
          <label for="group" class="block text-white text-sm font-bold mb-2">Grupo</label>
          <select
            v-model="taskGroup"
            class="bg-light-gray shadow appearance-none border rounded-full w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline"
            id="group"
          >
            <option value="" disabled>Selecione um grupo</option>
            <option v-for="group in groups" :key="group.group_id" :value="group.group_id">
              {{ group.group_name }}
            </option>
          </select>
        </div>

        <!-- Botões -->
        <div class="flex justify-between items-center">
          <button
            @click="createTask"
            class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-6 rounded-full border-white border-2 transition"
          >
            Criar Tarefa
          </button>
          <button
            @click="testDatabaseConnection"
            class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-6 rounded-full border-white border-2 transition"
          >
            Testar Banco de Dados
          </button>
        </div>
      </div>
    </main>

    <!-- Footer -->
    <footer class="flex justify-between items-center px-8 py-4">
      <button
        @click="goBack"
        class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-6 rounded-full border-white border-2 transition"
      >
        Voltar
      </button>
      <div class="text-gray-300">
        AgendaGramic Alpha 0.0.1
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const taskName = ref('');
const taskPriority = ref('');
const taskDescription = ref('');
const dueDate = ref('');
const taskStatus = ref(0);
const taskGroup = ref('');
const taskMembers = ref('');
const groups = ref([]);
const userTelegram = ref('');

onMounted(() => {
  loadGroups();
});

// Carregar usuários e grupos
const loadGroups = async () => {
  try {
        const userTelegram = localStorage.getItem('userTelegram') || 'default_user';
        const response = await axios.get(`/api/getGroups?userTelegram=${userTelegram}`);
        groups.value = response.data.groups || [];
      } catch (error) {
        console.error('Erro ao carregar grupos:', error);
      }
};

// Criar tarefa no banco de dados
const createTask = async () => {
  const newTask = {
    taskName: taskName.value,
    taskDescription: taskDescription.value,
    dueDate: dueDate.value,
    taskStatus: taskStatus.value,
    taskPriority: taskPriority.value,
    taskGroup: taskGroup.value,
    taskMembers: taskMembers.value,
    taskCreator: userTelegram.value,
  };

  try {
    const response = await axios.post('/api/addTask', newTask);
    if (response.data.success) {
      alert('Tarefa criada com sucesso!');
      goBack();
    } else {
      alert('Erro ao criar a tarefa no banco de dados.');
    }
  } catch (error) {
    console.error('Erro ao criar tarefa:', error);
  }
};

// Testar conexão com o banco de dados
const testDatabaseConnection = async () => {
  try {
    const response = await axios.get('/api/getTasks');
    if (response.status === 200) {
      alert('Conexão com o banco de dados bem-sucedida!');
    } else {
      alert('Erro ao conectar ao banco de dados.');
    }
  } catch (error) {
    console.error('Erro ao testar conexão com o banco:', error);
    alert('Erro ao conectar ao banco de dados.');
  }
};

// Voltar para a página anterior
const goBack = () => {
  window.history.back();
};


</script>

<style scoped>
/* Gradiente e fundos */
.bg-gradient-green-inverse {
  background: linear-gradient(to bottom, #32cd32, #1e1e1e);
}
.bg-medium-gray {
  background-color: #3c3c3c;
}
.bg-light-gray {
  background-color: #2e2e2e;
}

/* Sombra */
.shadow-green {
  box-shadow: 0 10px 15px rgba(50, 205, 50, 0.3);
}

/* Botões */
button {
  transition: background-color 0.3s;
}
.bg-green-500 {
  background-color: #32cd32;
}
.bg-green-600:hover {
  background-color: #28a745;
}
.bg-blue-500:hover {
  background-color: #2563eb;
}

/* Bordas */
.rounded-3xl {
  border-radius: 1.5rem;
}
</style>

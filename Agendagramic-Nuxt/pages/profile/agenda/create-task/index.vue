<template>
  <div class="min-h-screen bg-gradient-green-inverse flex flex-col justify-between">
    <header class="flex justify-between items-center px-8 py-4">
      <h1 class="text-4xl font-bold text-white">Criar Nova Tarefa</h1>
      <h3 class="text-3xl font-semibold text-white">AgendaGramic</h3>
    </header>

    <main class="flex flex-col items-center flex-1 px-6">
      <div class="bg-medium-gray shadow-green w-full max-w-4xl rounded-3xl p-8 border-white border-2">
        <h2 class="text-2xl font-semibold mb-4 text-white">Detalhes da Tarefa</h2>

        <!-- Nome da Tarefa -->
        <div class="mb-4">
          <label for="taskName" class="block text-white text-sm font-bold mb-2">Nome da Tarefa</label>
          <input
            v-model="taskName"
            class="bg-light-gray shadow appearance-none border rounded-full w-full py-2 px-3 text-white"
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
            class="bg-light-gray shadow appearance-none border rounded-lg w-full py-2 px-3 text-white"
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
            class="bg-light-gray shadow appearance-none border rounded-full w-full py-2 px-3 text-white"
            id="dueDate"
            type="date"
          />
        </div>

        <!-- Prioridade da Tarefa -->
        <div class="mb-4">
          <label for="taskPriority" class="block text-white text-sm font-bold mb-2">Prioridade da Tarefa</label>
          <select
            v-model="taskPriority"
            class="bg-light-gray shadow appearance-none border rounded-full w-full py-2 px-3 text-white"
            id="taskPriority"
          >
            <option value="alta">Alta</option>
            <option value="media">Média</option>
            <option value="baixa">Baixa</option>
          </select>
        </div>

        <!-- Grupo -->
        <div class="mb-4">
          <label for="group" class="block text-white text-sm font-bold mb-2">Grupo</label>
          <input
            v-model="taskGroup"
            class="bg-light-gray shadow appearance-none border rounded-full w-full py-2 px-3 text-white"
            id="group"
            type="text"
            placeholder="Digite o ID do grupo"
          />
        </div>

        <!-- Responsáveis -->
        <div class="mb-4">
          <label for="taskMembers" class="block text-white text-sm font-bold mb-2">Responsáveis</label>
          <input
            v-model="taskMembers"
            class="bg-light-gray shadow appearance-none border rounded-full w-full py-2 px-3 text-white"
            id="taskMembers"
            type="text"
            placeholder="Digite os responsáveis separados por vírgulas"
          />
        </div>

        <!-- Botões -->
        <div class="flex flex-col space-y-4">
          <button
            @click="validateAndCreateTask"
            class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-6 rounded-full"
          >
            Criar Tarefa
          </button>
          <button
            @click="testConnection"
            class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-6 rounded-full"
          >
            Testar Conexão com Tarefas
          </button>
        </div>
      </div>
    </main>

    <!-- Footer -->
    <footer class="flex justify-between items-center px-8 py-4">
      <button
        @click="goBack"
        class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-6 rounded-full"
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
import { ref } from 'vue';
import axios from 'axios';

const taskName = ref('');
const taskDescription = ref('');
const dueDate = ref('');
const taskPriority = ref('');
const taskGroup = ref('');
const taskMembers = ref('');
const userTelegram = ref('default_user');

// Criar tarefa
const validateAndCreateTask = async () => {
  if (!taskName.value || !dueDate.value || !taskPriority.value || !taskGroup.value) {
    alert('Por favor, preencha todos os campos obrigatórios.');
    return;
  }

  const newTask = {
    taskName: taskName.value,
    taskDescription: taskDescription.value || null,
    dueDate: dueDate.value,
    taskPriority: taskPriority.value,
    taskGroup: taskGroup.value,
    taskMembers: taskMembers.value || null,
    taskCreator: userTelegram.value,
  };

  try {
    const response = await axios.post('/api/addTask', newTask);

    if (response.data.success) {
      alert(`Tarefa criada com sucesso! ID da Tarefa: ${response.data.insertId}`);
    } else {
      alert('Erro ao criar a tarefa.');
    }
  } catch (error) {
    console.error('Erro ao criar tarefa:', error);
    alert('Erro ao criar tarefa no banco.');
  }
};

// Testar conexão com a tabela tarefas
const testConnection = async () => {
  try {
    const response = await axios.get('/api/getTasks', {
      params: { userTelegram: userTelegram.value },
    });

    if (response.data.success) {
      alert(`Conexão com a tabela de tarefas bem-sucedida! Tarefas encontradas: ${response.data.tasks.length}`);
    } else {
      alert('Erro ao conectar à tabela de tarefas.');
    }
  } catch (error) {
    console.error('Erro ao testar conexão:', error);
    alert('Erro ao conectar à tabela de tarefas.');
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
  color: white; /* Cor do texto ajustada */
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
.bg-blue-500 {
  background-color: #007bff;
}
.bg-blue-600:hover {
  background-color: #0056b3;
}
.bg-gray-500 {
  background-color: #6c757d;
}
.bg-gray-600:hover {
  background-color: #5a6268;
}
</style>

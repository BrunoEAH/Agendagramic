<template>
  <div class="min-h-screen bg-dark-gray p-6 flex flex-col justify-between border-white border-2">
    <div class="bg-gradient-green-inverse shadow-green min-h-screen flex flex-col justify-between">
      <!-- Cabeçalho da página com AgendaGramic -->
      <div class="flex justify-between items-center mb-6">
        <!-- Título da página -->
        <div>
          <h1 class="text-4xl font-bold text-white">Criar Nova Tarefa</h1>
        </div>

        <!-- Nome do Projeto com fonte maior -->
        <div class="text-center">
          <h3 class="text-3xl font-semibold text-white">AgendaGramic</h3>
        </div>
      </div>

      <!-- Formulário de criação de tarefa -->
      <div class="bg-medium-gray p-6 rounded-lg shadow-md border-lighter-gray border-2 mb-6">
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

        <!-- Grupo para Tarefa -->
                <div class="mb-4">
          <label for="taskGroup" class="block text-white text-sm font-bold mb-2">Grupo da Tarefa</label>
          <select
            v-model="taskGroup"
            class="bg-light-gray shadow appearance-none border rounded-full w-full py-2 px-3 text-white leading-tight focus:outline-none focus:shadow-outline"
            id="taskGroup"
          >
            <option :value="0">Nenhum</option>
            <option :value="1">Grupo 1</option>
            <option :value="2">Grupo 2</option>
          </select>
        </div>


        <!-- Descrição da Tarefa -->
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

        <!-- Botão para criar a tarefa -->
        <button
          @click="createTask"
          class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-full focus:outline-none focus:shadow-outline border-white border-2"
        >
          Criar Tarefa
        </button>
      </div>

      <!-- Botão Voltar no canto inferior esquerdo -->
      <div class="mt-6 flex justify-start">
        <button @click="goBack" class="bg-blue-500 text-white py-2 px-4 rounded-full hover:bg-blue-600 border-white border-2">
          Voltar
        </button>
      </div>

      <!-- Rodapé com versão -->
      <div class="text-center text-gray-300 mt-4">
        AgendaGramic Alpha 0.0.1
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter, useRoute } from 'vue-router';

const router = useRouter();
const route = useRoute();
const day = route.params.id;

var task_ID = 0;
const taskName = ref('');
const taskDescription = ref('');
const dueDate = ref('');
const taskStatus = ref(0);
const taskPriority = ref('alta');
const taskGroup = ref(0);
const taskCreator = "@SeuUsuario";
const taskMembers = ref('');

// Função para criar uma nova tarefa
const createTask = async () => {
  const newTask = {
    task_ID: task_ID++,
    taskName: taskName.value,
    taskDescription: taskDescription.value,
    dueDate: dueDate.value,
    taskStatus: taskStatus.value,
    taskPriority: taskPriority.value,
    taskGroup : taskGroup.value,
    taskMembers: taskMembers.value,
    taskCreator: taskCreator,
  };

  // Pega as tarefas existentes no localStorage ou cria uma nova estrutura
  let tasksData = JSON.parse(localStorage.getItem('tasks')) || {};

  // Verifica se há tarefas para o dia, se não, cria um array vazio para esse dia
  if (!tasksData[day]) {
    tasksData[day] = [];
  }

  // Adiciona a nova tarefa ao array do dia
  tasksData[day].push(newTask);

  // Atualiza o localStorage com os novos dados
  localStorage.setItem('tasks', JSON.stringify(tasksData));

  try {
    const { data,error } = await $fetch('/api/addTask', {
      method: 'POST',
      body: newTask,
    });
    
    if (error.value) {
      throw new Error(error.value); // Handle fetch error
    }

    console.log('Tarefa adicionada:', data.value);

    // Redireciona de volta para a página do dia
    router.push(`/profile/agenda/day/${day}`);

  } catch (error) {
    console.error('Erro ao adicionar a tarefa:', error);
    alert('Errado ao adicionar a tarefa.');
  }


};

// Função para voltar à página de agenda
const goBack = () => {
  router.push(`/profile/agenda/day/${day}`);
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

/* Contêiner com cor cinza médio */
.bg-medium-gray {
  background-color: #3c3c3c;
}

.border-lighter-gray {
  border-color: #5a5a5a;
}

/* Campos de entrada */
.bg-light-gray {
  background-color: #2e2e2e;
  color: white;
}

/* Botões arredondados */
button {
  transition: background-color 0.3s;
  border-radius: 9999px;
}

/* Estilo de sombra */
.shadow-md {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
}

/* Estilo para o ícone do calendário dentro do campo de data */
input[type="date"]::-webkit-calendar-picker-indicator {
  filter: invert(1); /* Inverte as cores para branco */
  opacity: 0.8;
}

</style>

<template>
    <div class="min-h-screen bg-gray-100 p-6 flex flex-col justify-between">
      <!-- Cabeçalho da página com AgendaGramic -->
      <div class="flex justify-between items-center mb-6">
        <!-- Título da página -->
        <div>
          <h1 class="text-4xl font-bold">Criar Nova Tarefa</h1>
        </div>
  
        <!-- Nome do Projeto -->
        <div class="text-center">
          <h3 class="text-lg font-medium">AgendaGramic</h3>
        </div>
      </div>
  
      <!-- Formulário de criação de tarefa -->
      <div class="bg-white p-6 rounded-lg shadow-md">
        <h2 class="text-2xl font-semibold mb-4">Detalhes da Tarefa</h2>
  
        <!-- Nome da Tarefa -->
        <div class="mb-4">
          <label for="taskName" class="block text-gray-700 text-sm font-bold mb-2">Nome da Tarefa</label>
          <input
            v-model="taskName"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            id="taskName"
            type="text"
            placeholder="Digite o nome da tarefa"
          />
        </div>
  
        <!-- Descrição da Tarefa -->
        <div class="mb-4">
          <label for="taskDescription" class="block text-gray-700 text-sm font-bold mb-2">Descrição</label>
          <textarea
            v-model="taskDescription"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            id="taskDescription"
            rows="4"
            placeholder="Descreva a tarefa"
          ></textarea>
        </div>
  
        <!-- Data de Conclusão -->
        <div class="mb-4">
          <label for="dueDate" class="block text-gray-700 text-sm font-bold mb-2">Data de Conclusão</label>
          <input
            v-model="dueDate"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            id="dueDate"
            type="date"
          />
        </div>
  
        <!-- Status da Tarefa -->
        <div class="mb-4">
          <label for="taskStatus" class="block text-gray-700 text-sm font-bold mb-2">Status da Tarefa</label>
          <select
            v-model="taskStatus"
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            id="taskStatus"
          >
            <option value="pendente">Pendente</option>
            <option value="em progresso">Em Progresso</option>
            <option value="concluída">Concluída</option>
          </select>
        </div>
  
        <!-- Botão para criar a tarefa -->
        <button
          @click="createTask"
          class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
        >
          Criar Tarefa
        </button>
      </div>
  
      <!-- Botão Voltar no canto inferior esquerdo -->
      <div class="mt-6 flex justify-start">
        <button @click="goBack" class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
          Voltar
        </button>
      </div>
  
      <!-- Rodapé com versão -->
      <div class="text-center text-gray-500 mt-4">
        AgendaGramic Alpha 0.0.1
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  
  const router = useRouter();
  
  const taskName = ref('');
  const taskDescription = ref('');
  const dueDate = ref('');
  const taskStatus = ref('pendente');
  
  // Função para criar uma nova tarefa
  const createTask = () => {
    const newTask = {
      taskName: taskName.value,
      taskDescription: taskDescription.value,
      dueDate: dueDate.value,
      taskStatus: taskStatus.value,
    };
  
    // Pega as tarefas existentes no localStorage ou cria uma nova estrutura
    let tasksData = JSON.parse(localStorage.getItem('tasks')) || {};
    const day = new Date(dueDate.value).getDate(); // Pega o dia a partir da data
  
    // Se não houver tarefas para o dia, cria uma lista vazia
    if (!tasksData[day]) {
      tasksData[day] = [];
    }
  
    // Adiciona a nova tarefa ao dia
    tasksData[day].push(newTask);
  
    // Salva a tarefa no localStorage
    localStorage.setItem('tasks', JSON.stringify(tasksData));
  
    // Redirecionar de volta para a página de agenda
    router.push(`/profile/agenda`);
  };
  
  // Função para voltar à página de agenda
  const goBack = () => {
    router.push(`/profile/agenda`);
  };
  </script>
  
  <style scoped>
  /* Adicionando estilos para o formulário e a página */
  .shadow {
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  </style>
  
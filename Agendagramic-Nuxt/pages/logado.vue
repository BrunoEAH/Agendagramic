<template>
    <div class="min-h-screen bg-gray-100 p-6">
      <div class="max-w-4xl mx-auto">
        
        <!-- TÍTULO PRINCIPAL DA PÁGINA LOGADA -->
        <h1 class="text-3xl font-bold text-center mb-6">Bem-vindo ao AgendaGramic!</h1>
  
        <!-- LAYOUT EM GRADE PARA DISTRIBUIR OS CARTÕES NA PÁGINA -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          
          <!-- CARD DE GERENCIAMENTO DE TAREFAS, COM TÍTULO, DESCRIÇÃO E BOTÃO -->
          <div class="bg-white p-4 rounded-lg shadow-md">
            <h2 class="text-xl font-semibold mb-4">Gerenciamento de Tarefas</h2>
            <p class="text-gray-600 mb-4">
              Crie, edite e acompanhe suas tarefas diárias. Mantenha o controle de suas atividades e receba lembretes automáticos.
            </p>
            <button class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
              Acessar Tarefas
            </button>
          </div>
  
          <!-- CARD DE COMPROMISSOS E AGENDAS, COM TÍTULO, DESCRIÇÃO E BOTÃO DE AÇÃO -->
          <div class="bg-white p-4 rounded-lg shadow-md">
            <h2 class="text-xl font-semibold mb-4">Compromissos e Agendas</h2>
            <p class="text-gray-600 mb-4">
              Visualize, compartilhe e gerencie seus compromissos com familiares, amigos e equipes. Sincronize sua agenda de forma fácil.
            </p>
            <button class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
              Acessar Agendas
            </button>
          </div>
  
          <!-- CARD DE LEMBRETES, QUE OFERECE A OPÇÃO DE CONFIGURAR E GERENCIAR LEMBRETES -->
          <div class="bg-white p-4 rounded-lg shadow-md">
            <h2 class="text-xl font-semibold mb-4">Lembretes</h2>
            <p class="text-gray-600 mb-4">
              Configure lembretes personalizados e receba notificações diretamente pelo WhatsApp. Nunca perca um compromisso!
            </p>
            <button class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
              Acessar Lembretes
            </button>
          </div>
  
          <!-- CARD DE GERENCIAMENTO DE EQUIPES, COM FUNCIONALIDADES DE CONTROLE DE MEMBROS -->
          <div class="bg-white p-4 rounded-lg shadow-md">
            <h2 class="text-xl font-semibold mb-4">Gerenciamento de Equipes</h2>
            <p class="text-gray-600 mb-4">
              Adicione ou remova membros da sua equipe e organize tarefas em conjunto com um sistema hierárquico eficiente.
            </p>
            <button class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
              Acessar Equipes
            </button>
          </div>
  
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  // Nenhuma lógica adicional necessária neste momento
  </script>
  
  <style scoped>
  /* Estilos personalizados para os cartões */
  </style>
  
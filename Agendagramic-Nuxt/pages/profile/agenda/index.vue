<template>
  <div class="min-h-screen bg-gray-100 p-6 flex flex-col justify-between">
    
    <!-- Cabeçalho do calendário com título e mês -->
    <div class="flex justify-between items-center mb-6">
      <!-- Nome grande "Agenda" e mês -->
      <div>
        <h1 class="text-6xl font-bold">Agenda</h1>
        <h2 class="text-3xl font-normal">Outubro</h2> <!-- Mês em uma fonte menor -->
      </div>

      <!-- Nome do Projeto e Ano -->
      <div class="text-center">
        <h3 class="text-lg font-medium">AgendaGramic</h3> <!-- Nome do sistema -->
        <div class="border-2 border-gray-400 rounded-full px-6 py-2 text-xl mt-2">
          {{ currentYear }}
        </div>
      </div>
    </div>

    <!-- Dias da semana em português -->
    <div class="grid grid-cols-7 gap-4 text-center text-gray-500 mb-2">
      <span>DOM</span>
      <span>SEG</span>
      <span>TER</span>
      <span>QUA</span>
      <span>QUI</span>
      <span>SEX</span>
      <span>SÁB</span>
    </div>

    <!-- Números do calendário com linhas suaves -->
    <div class="grid grid-cols-7 gap-4">
      <div v-for="(day, index) in calendarDays" :key="index"
           class="p-6 text-center text-lg cursor-pointer hover:bg-gray-200 shadow-lg"
           :class="{'invisible': !day}"
           @click="day && goToDate(day)">
        <span class="text-gray-700 shadow-sm">{{ day || '' }}</span> <!-- Adicionando leve sombra nos números -->
      </div>
    </div>

    <!-- Botão Voltar no canto inferior esquerdo -->
    <div class="mt-6">
      <button @click="goToProfile" class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
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

// Nome dos meses
const months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];

// Pegar o mês e ano atual
const currentMonth = months[new Date().getMonth()];
const currentYear = new Date().getFullYear();

// Ajustar o calendário para o mês de Outubro de 2024, começando na terça-feira
const daysInMonth = 30; // Dias em Outubro
const firstDayOffset = 2; // Dia 1 de outubro é uma terça-feira (offset = 2)

const calendarDays = ref(
  Array.from({ length: firstDayOffset }, () => null).concat(
    Array.from({ length: daysInMonth }, (_, i) => i + 1)
  )
);

const router = useRouter();

const goToDate = (day) => {
  // Redireciona para a rota do dia selecionado
  router.push(`/profile/agenda/day/${day}`);
};

// Função para voltar para o perfil (logado)
const goToProfile = () => {
  router.push('/profile');
};
</script>

<style scoped>
/* Estilos para o calendário */
.bg-gray-100 {
  background-color: #f7fafc;
}

.text-lg {
  font-size: 1.125rem;
}

.text-xl {
  font-size: 1.25rem;
}

.grid {
  display: grid;
}

.grid-cols-7 {
  grid-template-columns: repeat(7, 1fr);
}

.cursor-pointer:hover {
  background-color: #e2e8f0;
}

.invisible {
  visibility: hidden;
}

/* Leve sombra nos números */
.shadow-sm {
  text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.1);
}

/* Sombra nos dias do calendário */
.shadow-lg {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
</style>

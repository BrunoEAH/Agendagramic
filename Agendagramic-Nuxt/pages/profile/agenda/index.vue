<template>
  <div class="min-h-screen bg-dark-gray p-6 flex flex-col justify-between border-white border-2">
    <div class="bg-gradient-green-inverse shadow-green min-h-screen flex flex-col justify-between">
      <!-- Cabeçalho do calendário com título e mês -->
      <div class="flex justify-between items-center mb-6">
        <!-- Nome grande "Agenda" e mês -->
        <div>
          <h1 class="text-6xl font-bold text-white">Agenda</h1>
          <h2 class="text-3xl font-normal text-gray-300">{{ currentMonth }}</h2>
        </div>

        <!-- Nome do Projeto e Ano -->
        <div class="text-center">
          <h3 class="text-lg font-medium text-white">AgendaGramic</h3>
          <div class="border-2 border-white rounded-full px-6 py-2 text-xl mt-2 text-white">
            {{ currentYear }}
          </div>
        </div>
      </div>

      <!-- Contêiner do calendário com bordas arredondadas e borda cinza clara -->
      <div class="bg-light-gray p-4 rounded-3xl mx-4 shadow-lg border-2 border-lighter-gray">
        <!-- Dias da semana em português -->
        <div class="grid grid-cols-7 gap-4 text-center text-white text-lg mb-4">
          <span>DOM</span>
          <span>SEG</span>
          <span>TER</span>
          <span>QUA</span>
          <span>QUI</span>
          <span>SEX</span>
          <span>SÁB</span>
        </div>

        <!-- Números do calendário com estilo atualizado -->
        <div class="grid grid-cols-7 gap-4">
          <div
            v-for="(day, index) in calendarDays"
            :key="index"
            class="flex items-center justify-center h-12 w-full text-center text-md cursor-pointer bg-medium-gray text-black rounded-md shadow-sm hover:bg-green-500 transition"
            :class="{'invisible': !day}"
            @click="day && goToDate(day)"
          >
            <span>{{ day || '' }}</span>
          </div>
        </div>
      </div>

      <!-- Caixa do dia atual -->
      <div class="bg-medium-gray p-4 rounded-3xl shadow-md border-lighter-gray border-2 max-w-3xl w-full mx-auto mt-6">
        <h3 class="text-xl text-white text-center">Hoje é: {{ currentDateString }}</h3>
      </div>

      <!-- Contêiner das duas caixas principais -->
      <div class="flex space-x-4 mt-6 max-w-5xl mx-auto">
        <!-- Caixa de Atividades do Dia -->
        <div class="bg-medium-gray p-6 rounded-3xl shadow-md border-lighter-gray border-2 flex-1">
          <h3 class="text-xl text-white mb-4">Atividades do Dia</h3>
          <p class="text-gray-300">Nenhuma atividade programada para hoje.</p>
        </div>

        <!-- Caixa de Eventos do Dia -->
        <div class="bg-medium-gray p-6 rounded-3xl shadow-md border-lighter-gray border-2 flex-1">
          <h3 class="text-xl text-white mb-4">Eventos do Dia</h3>
          <p class="text-gray-300">Nenhum evento programado para hoje.</p>
        </div>
      </div>

      <!-- Botão Voltar no canto inferior esquerdo -->
      <div class="mt-6">
        <button @click="goToProfile" class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 border-white border-2">
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
import { useRouter } from 'vue-router';

// Nome dos meses
const months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];

// Pegar o mês e ano atual
const currentDate = new Date();
const currentMonthIndex = currentDate.getMonth();
const currentMonth = months[currentMonthIndex];
const currentYear = currentDate.getFullYear();
const currentDateString = currentDate.toLocaleDateString('pt-BR', { weekday: 'long', day: 'numeric', month: 'long' });

// Obter o número de dias no mês atual
const daysInMonth = new Date(currentYear, currentMonthIndex + 1, 0).getDate();
// Obter o dia da semana do primeiro dia do mês (0 = Domingo, 6 = Sábado)
const firstDayOffset = new Date(currentYear, currentMonthIndex, 1).getDay();

const calendarDays = ref(
  Array.from({ length: firstDayOffset }, () => null).concat(
    Array.from({ length: daysInMonth }, (_, i) => i + 1)
  )
);

const router = useRouter();

const goToDate = (day) => {
  router.push(`/profile/agenda/day/${day}`);
};

// Função para voltar para o perfil (logado)
const goToProfile = () => {
  router.push('/profile');
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

/* Contêiner do calendário com bordas arredondadas */
.bg-light-gray {
  background-color: #2e2e2e;
}

.border-lighter-gray {
  border-color: #4a4a4a;
}

.rounded-3xl {
  border-radius: 48px;
}

/* Estilos para os dias do calendário */
.bg-medium-gray {
  background-color: #3c3c3c;
}

.text-black {
  color: rgb(211, 211, 211);
}

.text-lg {
  font-size: 1.25rem;
}

.text-white {
  color: white;
}

/* Estilo para o efeito de hover */
.hover\:bg-green-500:hover {
  background-color: #32cd32;
}

.rounded-md {
  border-radius: 1024px;
}

/* Estilos de sombra para os dias */
.shadow-sm {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* Transição suave ao passar o mouse */
.transition {
  transition: background-color 0.3s, box-shadow 0.3s;
}

/* Ajustes de tamanho para os dias */
.h-12 {
  height: 3rem;
}

.text-md {
  font-size: 1rem;
}

/* Centralizar o texto nos dias */
.flex {
  display: flex;
}

.items-center {
  align-items: center;
}

.justify-center {
  justify-content: center;
}

/* Invisibilidade dos dias vazios */
.invisible {
  visibility: hidden;
}
</style>

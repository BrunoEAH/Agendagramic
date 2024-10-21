<template>
  <div class="min-h-screen bg-dark-gray p-6 flex flex-col justify-between border-white border-2">
    <div class="bg-gradient-green-inverse shadow-green min-h-screen flex flex-col justify-between">
      <!-- Cabeçalho do calendário com título e seleção de mês e ano -->
      <div class="flex justify-between items-center mb-6">
        <!-- Nome grande "Agenda" -->
        <div>
          <h1 class="text-6xl font-bold text-white">Agenda</h1>

          <!-- Seleção de mês e ano -->
          <input
            type="month"
            v-model="selectedDate"
            class="text-3xl font-normal text-gray-300 bg-transparent border-none focus:outline-none cursor-pointer mt-2"
          />
        </div>
      </div>

      <!-- Contêiner do calendário com bordas arredondadas -->
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

        <!-- Números do calendário com destaque no dia atual -->
        <div class="grid grid-cols-7 gap-4">
          <div
            v-for="(day, index) in calendarDays"
            :key="index"
            class="flex items-center justify-center h-12 w-full text-center text-md cursor-pointer bg-medium-gray text-black rounded-md shadow-sm hover:bg-green-500 transition"
            :class="{
              'invisible': !day,
              'border-2 border-white': isToday(day)
            }"
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

      <!-- Contêiner das caixas de Tarefas e Eventos, organizadas em duas colunas -->
      <div class="grid grid-cols-2 gap-6 max-w-6xl w-full mx-auto mt-6">
        <!-- Caixa de Tarefas -->
        <div class="bg-medium-gray p-8 rounded-3xl shadow-md border-lighter-gray border-2">
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-2xl font-semibold text-white">Tarefas</h2>
          </div>
          <div v-if="tasks.length > 0">
            <ul>
              <li v-for="(task, index) in tasks" :key="index" class="mt-2 text-white">
                <strong>{{ task.taskName }}</strong> - Status: {{ task.taskStatus }}
              </li>
            </ul>
          </div>
          <div v-else>
            <p class="text-lg text-gray-400">Sem tarefas para esse dia.</p>
          </div>
        </div>

        <!-- Caixa de Eventos -->
        <div class="bg-medium-gray p-8 rounded-3xl shadow-md border-lighter-gray border-2">
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-2xl font-semibold text-white">Eventos</h2>
          </div>
          <div v-if="events.length > 0">
            <ul>
              <li v-for="(event, index) in events" :key="index" class="mt-2 text-white">
                <strong>{{ event.eventTitle }}</strong> - Local: {{ event.eventLocation }} - Horário: {{ event.eventTime }}
              </li>
            </ul>
          </div>
          <div v-else>
            <p class="text-lg text-gray-400">Sem eventos para esse dia.</p>
          </div>
        </div>
      </div>

      <!-- Botão Voltar -->
      <div class="mt-6 text-center">
        <button @click="goToProfile" class="bg-gray-500 text-white py-2 px-4 rounded-full hover:bg-green-500 border-white border-2">
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
import { ref, watch, onMounted } from 'vue';
import { useRouter } from 'vue-router';

// Nome dos meses
const months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];

const currentDate = new Date();
const today = currentDate.getDate();
const todayMonth = currentDate.getMonth();
const todayYear = currentDate.getFullYear();

const selectedDate = ref(`${todayYear}-${String(todayMonth + 1).padStart(2, '0')}`);
const currentMonth = ref(months[todayMonth]);
const currentYear = ref(todayYear);
const currentDateString = currentDate.toLocaleDateString('pt-BR', { weekday: 'long', day: 'numeric', month: 'long' });

// Função para verificar se o dia é hoje
const isToday = (day) => day === today && currentMonth.value === months[todayMonth] && currentYear.value === todayYear;

const updateCalendar = () => {
  const [year, month] = selectedDate.value.split("-");
  currentYear.value = parseInt(year, 10);
  currentMonth.value = months[parseInt(month, 10) - 1];
  updateCalendarDays();
};

// Obter os dias no mês selecionado
const getDaysInMonth = (monthIndex, year) => {
  const daysInMonth = new Date(year, monthIndex + 1, 0).getDate();
  const firstDayOffset = new Date(year, monthIndex, 1).getDay();
  return Array.from({ length: firstDayOffset }, () => null).concat(
    Array.from({ length: daysInMonth }, (_, i) => i + 1)
  );
};

// Função para atualizar os dias do calendário ao mudar de mês ou ano
const updateCalendarDays = () => {
  calendarDays.value = getDaysInMonth(months.indexOf(currentMonth.value), currentYear.value);
};

// Observa quando a data selecionada (mês/ano) é alterada e atualiza o calendário
watch(selectedDate, () => {
  updateCalendar();
});

// Dias no calendário atual
const calendarDays = ref([]);
updateCalendarDays();

const router = useRouter();

// Funções para manipular tarefas e eventos
const tasks = ref([]);
const events = ref([]);

const goToDate = (day) => {
  router.push(`/profile/agenda/day/${day}`);
};

// Carregar dados de tarefas e eventos para o dia atual
onMounted(() => {
  const tasksData = JSON.parse(localStorage.getItem('tasks')) || {};
  const eventsData = JSON.parse(localStorage.getItem('events')) || {};

  // Verifica se há dados de tarefas e eventos para o dia atual
  tasks.value = tasksData[today] || [];
  events.value = eventsData[today] || [];
});

const goToProfile = () => {
  router.push('/profile');
};
</script>

<style scoped>
.bg-dark-gray {
  background-color: #1e1e1e;
}

.bg-gradient-green-inverse {
  background: linear-gradient(to top, #32cd32, transparent 50%);
}

.shadow-green {
  box-shadow: 0 10px 15px rgba(50, 205, 50, 0.3);
}

.bg-light-gray {
  background-color: #2e2e2e;
}

.border-lighter-gray {
  border-color: #4a4a4a;
}

.rounded-3xl {
  border-radius: 48px;
}

.bg-medium-gray {
  background-color: #3c3c3c;
}

.text-black {
  color: rgb(211, 211, 211);
}

.hover\:bg-green-500:hover {
  background-color: #32cd32;
}

.rounded-md {
  border-radius: 1024px;
}

.shadow-sm {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.h-12 {
  height: 3rem;
}

.invisible {
  visibility: hidden;
}

.border-white {
  border-color: white;
}

input[type="month"]::-webkit-calendar-picker-indicator {
  filter: invert(1);
  opacity: 0.8;
}
</style>

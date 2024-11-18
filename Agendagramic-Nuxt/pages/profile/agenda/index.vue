<template>
  <div class="min-h-screen bg-gradient-green-inverse flex flex-col justify-between">
    <!-- Header -->
    <header class="flex justify-between items-center px-8 py-4">
      <h1 class="text-6xl font-bold text-white">AgendaGramic</h1>
      <!-- Seleção de mês e ano -->
      <input
        type="month"
        v-model="selectedDate"
        class="text-3xl font-normal text-gray-300 bg-transparent border-none focus:outline-none cursor-pointer mt-2"
      />
    </header>

    <!-- Main Content -->
    <main class="flex flex-col items-center justify-center flex-1 px-6">
      <!-- Calendar Container -->
      <div class="bg-medium-gray shadow-green w-full max-w-4xl rounded-3xl overflow-hidden p-8 border-white border-2">
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
            class="flex items-center justify-center h-12 w-full text-center text-md cursor-pointer bg-light-gray text-white rounded-md shadow-sm hover:bg-green-500 transition"
            :class="{ invisible: !day, 'border-2 border-white': isToday(day) }"
            @click="day && goToDate(day)"
          >
            <span>{{ day || '' }}</span>
          </div>
        </div>
      </div>

      <!-- Today's Date -->
      <div class="bg-dark-gray p-4 rounded-3xl shadow-md border-lighter-gray border-2 max-w-3xl w-full mx-auto mt-6">
        <h3 class="text-xl text-white text-center">Hoje é: {{ currentDateString }}</h3>
      </div>

      <!-- Tasks and Events Container -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-6xl w-full mx-auto mt-6">
        <!-- Tasks Box -->
        <div class="bg-medium-gray p-8 rounded-3xl shadow-md border-white border-2">
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

        <!-- Events Box -->
        <div class="bg-medium-gray p-8 rounded-3xl shadow-md border-white border-2">
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
    </main>

    <!-- Footer with Back Button and Version -->
    <footer class="flex justify-between items-center px-8 py-4">
      <button
        @click="goToProfile"
        class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-full border-white border-2 transition"
      >
        Voltar
      </button>
      <div class="text-gray-300">
        AgendaGramic Beta 0.1
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue';
import { useRouter } from 'vue-router';

// Nomes dos meses e dias da semana
const months = [
  "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
  "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
];
const weekDays = ["DOM", "SEG", "TER", "QUA", "QUI", "SEX", "SÁB"];

const currentDate = new Date();
const today = currentDate.getDate();
const todayMonth = currentDate.getMonth();
const todayYear = currentDate.getFullYear();

const selectedDate = ref(`${todayYear}-${String(todayMonth + 1).padStart(2, '0')}`);
const currentMonth = ref(months[todayMonth]);
const currentYear = ref(todayYear);
const currentDateString = currentDate.toLocaleDateString('pt-BR', {
  weekday: 'long', day: 'numeric', month: 'long'
});

// Função para verificar se o dia é hoje
const isToday = (day) => {
  return (
    day === today &&
    currentMonth.value === months[todayMonth] &&
    currentYear.value === todayYear
  );
};

// Atualiza o calendário quando o mês ou ano é alterado
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
  return [
    ...Array(firstDayOffset).fill(null),
    ...Array.from({ length: daysInMonth }, (_, i) => i + 1)
  ];
};

// Atualiza os dias do calendário quando o mês ou ano muda
const updateCalendarDays = () => {
  calendarDays.value = getDaysInMonth(
    months.indexOf(currentMonth.value),
    currentYear.value
  );
};

// Observa quando a data selecionada é alterada e atualiza o calendário
watch(selectedDate, updateCalendar);

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

// Carrega dados de tarefas e eventos para o dia atual
onMounted(() => {
  const tasksData = JSON.parse(localStorage.getItem('tasks')) || {};
  const eventsData = JSON.parse(localStorage.getItem('events')) || {};

  tasks.value = tasksData[today] || [];
  events.value = eventsData[today] || [];
});

const goToProfile = () => {
  router.push('/profile');
};
</script>

<style scoped>
/* Estilização */
.bg-dark-gray {
  background-color: #1e1e1e;
}

.bg-gradient-green-inverse {
  background: linear-gradient(to bottom, #32cd32, #1e1e1e);
}

.shadow-green {
  box-shadow: 0 10px 15px rgba(50, 205, 50, 0.3);
}

.bg-medium-gray {
  background-color: #3c3c3c;
}

.bg-light-gray {
  background-color: #2e2e2e;
}

.border-lighter-gray {
  border-color: #5a5a5a;
}

.text-gray-300 {
  color: #d1d5db;
}

.text-gray-400 {
  color: #9ca3af;
}

button {
  transition: background-color 0.3s, border-color 0.3s;
}

.bg-blue-500:hover {
  background-color: #2563eb;
}

.bg-green-500:hover {
  background-color: #2ea043;
}

.bg-gray-500:hover {
  background-color: #4a5568;
}

.rounded-3xl {
  border-radius: 4rem;
}

.rounded-md {
  border-radius:  4rem;
}

.rounded-full {
  border-radius: 9999px;
}

input[type="month"]::-webkit-calendar-picker-indicator {
  filter: invert(1);
  opacity: 0.8;
}
</style>


<template>
  <div class="container mx-auto p-6">
    <h1 class="text-3xl font-bold mb-4">Eventos e tarefas para o dia : {{ day }}</h1>

    <h2 class="text-2xl mt-4">Tarefas:</h2>
    <div v-if="tasks.length > 0">
      <ul>
        <li v-for="(task, index) in tasks" :key="index" class="mt-2">
          <strong>{{ task.task }}</strong> - Status: {{ task.status }}
        </li>
      </ul>
    </div>
    <div v-else>
      <p class="text-lg">Sem tarefas para esse dia.</p>
    </div>

    <h2 class="text-2xl mt-4">Eventos:</h2>
    <div v-if="events.length > 0">
      <ul>
        <li v-for="(event, index) in events" :key="index" class="mt-2">
          <strong>{{ event.event }}</strong> at {{ event.location }} - {{ event.time }}
        </li>
      </ul>
    </div>
    <div v-else>
      <p class="text-lg">Sem eventos para esse dia.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const day = route.params.id;
const tasks = ref([]); 
const events = ref([]); 

onMounted(async () => {
  try {
    const tasksResponse = await fetch('/tasks.json');
    const eventsResponse = await fetch('/events.json'); 

    const tasksData = await tasksResponse.json();
    const eventsData = await eventsResponse.json();

    
    tasks.value = tasksData[day] || []; 
    events.value = eventsData[day] || [];
  } catch (error) {
    console.error('Error fetching tasks or events data:', error);
  }
});
</script>


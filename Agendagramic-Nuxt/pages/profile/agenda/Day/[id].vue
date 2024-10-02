<template>
  <div class="container mx-auto p-6">
    <h1 class="text-3xl font-bold mb-4">Agenda for Day: {{ route.params.id }}</h1>
    <p class="text-lg">Details for day {{ route.params.id }} will go here.</p>
    <!-- Add more details or functionality here -->
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';

const route = useRoute();
</script>

<style scoped>
/* Add any additional styles here */
</style>

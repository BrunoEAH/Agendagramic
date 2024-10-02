<template>
    <div class="container mx-auto p-6">
      <h1 class="text-2xl font-bold mb-4">Agenda</h1>
      <div class="grid grid-cols-7 gap-4">
        <div
          v-for="day in days"
          :key="day"
          class="bg-gray-100 p-4 rounded shadow text-center cursor-pointer hover:bg-gray-200"
          @click="goToDate(day)"
        >
          {{ day }}
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  
  const days = Array.from({ length: 30 }, (_, i) => i + 1); // Create an array for 30 days
  const router = useRouter();
  
  const goToDate = (day) => {
    // Redirect to the route for the selected day
    router.push(`/profile/agenda/day/${day}`);
  };
  </script>
  
  <style scoped>
  /* Add any additional styles here */
  </style>
  
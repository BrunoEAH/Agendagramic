import { defineNuxtConfig } from 'nuxt/config';
import { resolve } from 'path';

export default defineNuxtConfig({
  alias: {
    '@': resolve(__dirname, './'), // Alias para facilitar importações
  },

  css: ['~/assets/main.scss'], // Importação do arquivo global de estilos

  devtools: {
    enabled: true, // Habilita as ferramentas de desenvolvimento
  },

  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },

  modules: ['@nuxtjs/tailwindcss'], // Importa o módulo Tailwind CSS para o Nuxt

  runtimeConfig: {
    public: {
      compatibilityDate: '2024-10-04', // Variável de configuração pública
    },
  },

  
  compatibilityDate: '2024-10-30', // Compatibilidade com o projeto

  nitro: {
    plugins: ['~/server/api/getTasks.js'], // Adiciona o plugin para acessar tarefas
  },
  
});

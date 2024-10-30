import { defineNuxtConfig } from 'nuxt/config';
import { resolve } from 'path';

export default defineNuxtConfig({
  alias: {
    '@': resolve(__dirname, './'), // Alias para facilitar importações
  },

  // Importação do arquivo global de estilos
  css: ['~/assets/main.scss'],

  // Habilita as ferramentas de desenvolvimento
  devtools: { enabled: true },

  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },

  // Importa o módulo Tailwind CSS para a configuração do Nuxt
  modules: ['@nuxtjs/tailwindcss'],

  runtimeConfig: {
    public: {
      compatibilityDate: '2024-10-04', // Variável de configuração pública (personalizada, se necessário)
    },
  },

  compatibilityDate: '2024-10-30',
});
// https://nuxt.com/docs/api/configuration/nuxt-config
import { resolve } from "path";
import react from '@vitejs/plugin-react';

export default {
  alias:{
    '@' : resolve(__dirname,"/"),
  },

  css: ["~/assets/main.scss"],
  devtools: { enabled: true },

  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },

  modules: ["@nuxtjs/tailwindcss"],

  vite: {
    plugins: [react()] // Adiciona o plugin React
  }
}

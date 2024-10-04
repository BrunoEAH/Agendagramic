/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./components/**/*.{js,vue,ts,jsx,tsx}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./app.vue",
    "./error.vue",
    "./app/**/*.{vue,js,ts,jsx,tsx}", // Inclui todos os arquivos Vue e React dentro da pasta app
    "./nuxt.config.{js,ts}" // Inclui o arquivo de configuração do Nuxt
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

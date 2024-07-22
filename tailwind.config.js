/** @type {import('tailwindcss').Config} */
const colors = require('tailwindcss/colors')
module.exports = {
  content: ["./Projeto/**/*.{html,js}",
    './Projeto/templates/pages/*.html',
    './node_modules/flowbite/**/*.js'
  
  ],
  theme: {
    colors:{
      blue: colors.blue,     // Inclui todas as variantes de azul
      green: colors.green,   // Inclui todas as variantes de verde
      purple: colors.purple, // Inclui todas as variantes de roxo
      sky: colors.sky,
      teal: colors.teal,
    },
    extend: {},
  },
  plugins: [ require('flowbite/plugin')],
}


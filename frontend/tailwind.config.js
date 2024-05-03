/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.{html,js}"],
  theme: {
    extend: {},
    colors: {
      primary: "#EEF7FF",
      secondary: "#CDE8E5",
      third: "#7AB2B2",
      fourth: "#4D869C",
      fifth: "#CD0033",
      transparent: 'transparent',
      black: 'black',
      'white': '#ffffff',
    },
    fontFamily: {
      'cabin': ["'Cabin'", 'sans-serif'],
      'rubik': ["'Rubik'", 'sans-serif']
    }
  },
  plugins: [],
}

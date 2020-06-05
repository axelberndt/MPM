/*
** TailwindCSS Configuration File
**
** Docs: https://tailwindcss.com/docs/configuration
** Default: https://github.com/tailwindcss/tailwindcss/blob/master/stubs/defaultConfig.stub.js
*/
const { colors } = require("tailwindcss/defaultTheme");

module.exports = {
  theme: {
    fontFamily: {
      sans: ["Inter"],
      mono: ["Source Code Pro", "Menlo", "Monaco", "Consolas", "Liberation Mono", "Courier New", "monospace"]
    },
    extend: {
      colors: {
        gray: {
          ...colors.gray,
          "50": "#FCFEFF"
        }
      },
      borderWidth: {
        "16": "16px"
      }
    }
  },
  variants: {
    backgroundColor: ["responsive", "hover"]
  },
  plugins: [],
  purge: false,
};
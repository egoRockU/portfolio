/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./main/templates/*.html"],
  daisyui: {
    themes: [
      {
        mydark: {
          primary: "#111827",
          secondary: "#f3f4f6",
          accent: "#1e40af",
          neutral: "#374151",
          "base-100": "#111827",
          info: "#155e75",
          success: "#4d7c0f",
          warning: "#b91c1c",
          error: "#dc2626",
        },
      },
      {
        mylight: {
          primary: "#f3f4f6",
          secondary: "#111827",
          accent: "#1e40af",
          neutral: "#374151",
          "base-100": "#f3f4f6",
          info: "#155e75",
          success: "#4d7c0f",
          warning: "#b91c1c",
          error: "#dc2626",
        },
      },
    ],
    extend: {},
  },
  plugins: [require("daisyui")],
};

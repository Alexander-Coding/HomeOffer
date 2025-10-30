import path from 'path'
import react from '@vitejs/plugin-react'

import { defineConfig } from 'vite'


// https://vite.dev/config/
export default defineConfig({
    plugins: [
        react({
            babel: {
                plugins: [['babel-plugin-react-compiler']],
            },
        }),
    ],
    resolve: {
        alias: {
            "@features": path.resolve(__dirname, "src/features"),
            "@layouts":  path.resolve(__dirname, "src/layouts"),
            "@pages":    path.resolve(__dirname, "src/pages"),
            "@shared":   path.resolve(__dirname, "src/shared"),
            "@root":     path.resolve(__dirname, "src"),
        }
    }
})

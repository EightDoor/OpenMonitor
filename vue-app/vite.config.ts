import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
import {fileURLToPath} from 'node:url';
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import {ElementPlusResolver} from 'unplugin-vue-components/resolvers'


// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        vue(),
        AutoImport({
            resolvers: [ElementPlusResolver()],
        }),
        Components({
            resolvers: [ElementPlusResolver(
                {
                    importStyle: "sass",
                }
            )],
        }),
    ],
    server: {
      proxy: {
          '/api': {
              target: 'http://localhost:8200',
              changeOrigin: true,
              rewrite: (path) => path.replace(/^\/api/, ''),
          },
      }
    },
    resolve: {
        // extensions: [".js", ".jsx", ".ejs", '.mjs'], // 之前忽略了 .mjs
        alias: {
            "@": fileURLToPath(new URL("./src", import.meta.url)),
        },
    },
    css: {
        preprocessorOptions: {
            scss: {
                // 自动导入定制化样式文件进行样式覆盖
                additionalData: `
          @use "@/assets/styles/element.scss" as *;
        `,
            }
        }
    }
})

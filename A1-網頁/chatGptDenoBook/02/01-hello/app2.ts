import { Application } from "https://deno.land/x/oak/mod.ts";
import { Router } from "https://deno.land/x/oak/mod.ts";

const router = new Router();

router.get("/", (ctx) => {
  ctx.response.body = "Hello, world!";
});

const app = new Application();

// 設置應用的視圖引擎
app.use(router.routes());

console.log('app started at http://127.0.0.1:8000')
// 啟動應用
await app.listen({ port: 8000 });

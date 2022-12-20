import { Router } from "https://deno.land/x/oak/mod.ts";

const router = new Router();

router.get("/", (ctx) => {
  ctx.response.body = "Hello, world!";
});

export default router;

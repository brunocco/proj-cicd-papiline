import express from "express";

import { Router, Request, Response } from "express";

const app = express();

const route = Router();

app.use(express.json());

route.get("/health", (_: Request, res: Response) => {
  res.json({ message: "API is OK!" });
});

route.get("/home", (_: Request, res: Response) => {
  res.json({ message: "Welcome" });
});

app.use(route);

app.listen(3000, () => "server running on port 3000");

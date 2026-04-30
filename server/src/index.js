import express from "express";
import morgan from "morgan";
import { PORT } from "./config.js";
import transcriptRoutes from "./routes/transcripts.routes.js";

const app = express();

app.use(morgan("dev"));
app.use(express.json());

app.use(transcriptRoutes);

app.listen(PORT);
console.log("Server on port:", PORT);

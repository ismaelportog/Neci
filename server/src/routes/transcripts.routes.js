import { Router } from "express";
import { getTranscript } from "../controllers/transcripts.controller.js";

const router = Router();

router.get('/transcript', getTranscript);

export default router;
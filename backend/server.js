const express = require("express");
const cors = require("cors");
const multer = require("multer");

const app = express();
app.use(cors());
app.use(express.json());

const upload = multer({ dest: "uploads/" });

app.get("/", (req, res) => {
  res.send("Backend is running...");
});

app.post("/upload", upload.single("file"), (req, res) => {
  if (!req.file) {
    return res.status(400).json({ error: "No file uploaded" });
  }

  // Placeholder: Process the file for plagiarism check
  res.json({
    message: "File uploaded successfully",
    filename: req.file.filename,
  });
});

const PORT = 5173;
app.listen(PORT, () => {
  console.log(`Backend running on http://localhost:${PORT}`);
});

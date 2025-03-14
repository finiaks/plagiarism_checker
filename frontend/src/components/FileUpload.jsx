import { useState } from "react";
import axios from "axios";

const FileUpload = ({ setResult }) => {
  const [file, setFile] = useState(null);
  const [refFile, setRefFile] = useState(null);

  const handleUpload = async () => {
    if (!file || !refFile) return alert("Please upload both files!");

    const formData = new FormData();
    formData.append("file", file);
    formData.append("reference_file", refFile);

    try {
      const res = await axios.post("http://localhost:5173/", formData);
      setResult(res.data);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <input type="file" onChange={(e) => setRefFile(e.target.files[0])} />
      <button onClick={handleUpload}>Check Plagiarism</button>
    </div>
  );
};

export default FileUpload;

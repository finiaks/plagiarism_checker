import { useState } from "react";
import FileUpload from "./components/FileUpload";
import ResultDisplay from "./components/ResultDisplay";
import "./index.css"; // ✅ Import global styles

const App = () => {
  const [result, setResult] = useState(null);

  return (
    <div className="container">
      {" "}
      {/* ✅ Add container class for styling */}
      <h1>Plagiarism Checker</h1>
      <FileUpload setResult={setResult} />
      <ResultDisplay result={result} />
    </div>
  );
};

export default App;

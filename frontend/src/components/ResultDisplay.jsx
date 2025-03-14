const ResultDisplay = ({ result }) => {
  return result ? (
    <div>
      <h2>Plagiarism Result</h2>
      <p>File: {result.filename}</p>
      <p>Similarity Score: {result.score}%</p>
      <p>{result.result}</p>
    </div>
  ) : null;
};

export default ResultDisplay;

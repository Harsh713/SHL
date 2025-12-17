import { useState } from "react";
import { scoreAudio } from "../src/api/scoreApi";

export default function AnalyzeButton({
  selectedFile,
  setScore,
  setTranscript,
  setExplanation,
}) {
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    if (!selectedFile) {
      alert("Please upload an audio file first");
      return;
    }

    setLoading(true);
    try {
      const result = await scoreAudio(selectedFile);

      setScore(result.score);
      setTranscript(result.transcript);

      // 🔹 Generate explanation (TEMP logic)
      const explanation = [];
      if (result.score >= 80) {
        explanation.push("Strong sentence structure");
        explanation.push("Appropriate verb tense usage");
        explanation.push("Good grammatical consistency");
      } else if (result.score >= 60) {
        explanation.push("Minor grammatical inconsistencies");
        explanation.push("Some sentence structure issues");
      } else {
        explanation.push("Frequent grammatical errors detected");
      }

      setExplanation(explanation);

    } catch (err) {
      console.error(err);
      alert("Error analyzing audio");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex justify-center mt-6">
      <button
        onClick={handleAnalyze}
        disabled={loading}
        className="px-6 py-3 bg-[#0067B1] text-white rounded-lg"
      >
        {loading ? "Analyzing..." : "Analyze"}
      </button>
    </div>
  );
}

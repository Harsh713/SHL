import { useState } from "react";
import Header from "../components/header";
import AudioUpload from "../components/AudioUpload";
import AnalyzeButton from "../components/AnalyzeButton";
import TranscriptBox from "../components/TranscriptBox";
import ScoreCard from "../components/Scorecard";
import ExplanationBox from "../components/ExplanationBox";

function App() {
  const [audioFile, setAudioFile] = useState(null);
  const [transcript, setTranscript] = useState("");
  const [score, setScore] = useState(null);
  const [explanation, setExplanation] = useState([]);

  return (
    <>
      <Header />

      <AudioUpload
        audioFile={audioFile}
        setAudioFile={setAudioFile}
      />

      <AnalyzeButton
        selectedFile={audioFile}
        setScore={setScore}
        setTranscript={setTranscript}
        setExplanation={setExplanation}
      />


      <TranscriptBox transcript={transcript} />
      <ScoreCard score={score} />
      <ExplanationBox explanation={explanation} />
    </>
  );
}

export default App;

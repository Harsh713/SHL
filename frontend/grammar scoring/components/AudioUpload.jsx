import { useRef } from "react";

const AudioUpload = ({ audioFile, setAudioFile }) => {
  const fileInputRef = useRef(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (!file) return;

    // Accept only audio files
    if (!file.type.startsWith("audio/")) {
      alert("Please upload a valid audio file (.wav or .m4a)");
      return;
    }

    setAudioFile(file);
  };

  return (
    <section className="w-full max-w-4xl mx-auto px-6 mt-8">
      <div className="bg-white border border-gray-200 rounded-lg p-6">
        <h2 className="text-lg font-medium text-gray-900">
          Upload Audio Sample
        </h2>

        <p className="mt-1 text-sm text-gray-600">
          Supported formats: .wav, .m4a
        </p>

        {/* Upload Button */}
        <div className="mt-4">
          <input
            ref={fileInputRef}
            type="file"
            accept=".wav,.m4a,audio/*"
            onChange={handleFileChange}
            className="hidden"
          />

          <button
            onClick={() => fileInputRef.current.click()}
            className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition"
          >
            Choose Audio File
          </button>
        </div>

        {/* Selected File Info */}
        {audioFile && (
          <div className="mt-4">
            <p className="text-sm text-gray-700">
              <span className="font-medium">Selected file:</span>{" "}
              {audioFile.name}
            </p>

            {/* Audio Preview */}
            <audio
              controls
              className="mt-3 w-full"
              src={URL.createObjectURL(audioFile)}
            />
          </div>
        )}
      </div>
    </section>
  );
};

export default AudioUpload;

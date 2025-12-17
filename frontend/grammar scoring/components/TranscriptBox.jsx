const TranscriptBox = ({ transcript }) => {
  return (
    <section className="w-full max-w-4xl mx-auto px-6 mt-8">
      <div className="bg-white border border-gray-200 rounded-lg p-6">
        <h2 className="text-lg font-medium text-gray-900">
          Generated Transcript
        </h2>

        <div className="mt-4 p-4 bg-gray-50 border border-gray-200 rounded-md min-h-[120px]">
          {transcript ? (
            <p className="text-gray-800 leading-relaxed whitespace-pre-wrap">
              {transcript}
            </p>
          ) : (
            <p className="text-gray-500 italic">
              Transcript will appear here after analysis.
            </p>
          )}
        </div>
      </div>
    </section>
  );
};

export default TranscriptBox;

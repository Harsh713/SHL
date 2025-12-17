const ExplanationBox = ({ explanation }) => {
  return (
    <section className="w-full max-w-4xl mx-auto px-6 mt-8">
      <div className="bg-white border border-gray-200 rounded-lg p-6">
        <h2 className="text-lg font-medium text-gray-900">
          Score Explanation
        </h2>

        <div className="mt-4">
          {explanation && explanation.length > 0 ? (
            <ul className="list-disc list-inside text-gray-700 space-y-2">
              {explanation.map((item, index) => (
                <li key={index}>{item}</li>
              ))}
            </ul>
          ) : (
            <p className="text-gray-500 italic">
              A brief explanation of the grammar score will appear here after analysis.
            </p>
          )}
        </div>
      </div>
    </section>
  );
};

export default ExplanationBox;

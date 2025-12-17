const ScoreCard = ({ score }) => {
  return (
    <section className="w-full max-w-4xl mx-auto px-6 mt-8 mb-12">
      <div className="bg-white border border-gray-200 rounded-lg p-6">
        <h2 className="text-lg font-medium text-gray-900">
          Grammar Score
        </h2>

        <div className="mt-6 flex items-center justify-center">
          {score !== null && score !== undefined ? (
            <div className="text-center">
              <div className="text-5xl font-semibold text-blue-600">
                {score}
              </div>
              <p className="mt-2 text-sm text-gray-600">
                Predicted grammar quality score
              </p>
            </div>
          ) : (
            <p className="text-gray-500 italic">
              Grammar score will appear here after analysis.
            </p>
          )}
        </div>
      </div>
    </section>
  );
};

export default ScoreCard;

const Header = () => {
  return (
    <header className="w-full bg-white border-b border-gray-800">
      <div className="max-w-4xl mx-auto px-6 py-6">
        <h1 className="text-3xl font-semibold text-gray-900">
          Grammar Scoring Engine
        </h1>

        <p className="mt-2 text-gray-600">
          Upload a spoken English audio sample to receive a grammar quality score.
        </p>

        <p className="mt-1 text-sm text-gray-500">
          Designed as part of an AI research assessment.
        </p>
      </div>
    </header>
  );
};

export default Header;

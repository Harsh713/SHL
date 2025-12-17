export async function scoreAudio(file) {
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch("http://127.0.0.1:8000/score", {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    throw new Error("Failed to score audio");
  }

  return response.json();
}

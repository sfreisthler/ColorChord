import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import DragAndDropImage from "./DropImage";
import ProcessedPage from "./ProcessedPage";

function App() {
  const deployedBackend = "https://colorchord.onrender.com/upload"
  const localBackend = "http://127.0.0.1:5000/upload"

  const handleImageUpload = async (file) => {
    console.log("Image uploaded:", file);

    const formData = new FormData();
    formData.append("file", file);

    try {
        //WHEN TESTING SERVER.PY LOCALLY UPDATE TO localBackend
        //Make sure you use deployedBackend when you pushif you are going to host backend on render
        const response = await fetch(deployedBackend, {
          method: "POST",
          body: formData,
        });
  
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
  
        const data = await response.json();
        console.log("Server Response:", data);
      } catch (error) {
        console.error("Error uploading image:", error);
      }
    
    };

  return (
    <div>
      <h1>Welcome to ColorChord!!</h1>
      <DragAndDropImage onImageUpload={handleImageUpload} />
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter basename="/ColorChord">
    <Routes>
      <Route path="/" element={<App />} />
      <Route path="/processed" element={<ProcessedPage />} />
    </Routes>
  </BrowserRouter>
);



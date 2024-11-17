import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import DragAndDropImage from "./DropImage";
import ProcessedPage from "./ProcessedPage";

function App() {
  const handleImageUpload = (file) => {
    console.log("Image uploaded:", file);
    // Add your image processing logic here
  };

  return (
    <div>
      <h1>Welcome to ColorChord!!</h1>
      <DragAndDropImage onImageUpload={handleImageUpload} />
    </div>
  );
}

// Correctly set the basename for the subpath
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter basename="/ColorChord">
    <Routes>
      <Route path="/" element={<App />} />
      <Route path="/processed" element={<ProcessedPage />} />
    </Routes>
  </BrowserRouter>
);



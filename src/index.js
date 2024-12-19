import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route, useNavigate } from 'react-router-dom';
import ProcessedPage from "./ProcessedPage";
import "./style.css"; // Ensure you have your stylesheet

function App() {
  const deployedBackend = "https://colorchord.onrender.com/upload";
  const localBackend = "http://127.0.0.1:50000/upload";

  const navigate = useNavigate();
  const fileInputRef = React.useRef(null);

  const handleImageUpload = async (file) => {
    console.log("Image selected:", file);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch(deployedBackend, {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      console.log("Server Response:", data);

      // Navigate to "/processed" after successful upload
      navigate("/processed");
    } catch (error) {
      console.error("Error uploading image:", error);
    }
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      handleImageUpload(file);
    }
  };

  const handleButtonClick = () => {
    fileInputRef.current.click();
  };

  return (
    <div className="desktop">
      <div className="overlap-group-wrapper">
        <div className="overlap-group">
          <div className="overlap">
            <div className="div" />
            <div className="text-wrapper">ColorChord</div>
          </div>

          <div className="overlap-2" onClick={handleButtonClick} style={{ cursor: "pointer" }}>
            <div className="rectangle-2" />
            <div className="text-wrapper-2">Upload Image</div>
          </div>

          {/* Hidden file input */}
          <input
            type="file"
            ref={fileInputRef}
            style={{ display: 'none' }}
            accept="image/*"
            onChange={handleFileChange}
          />
        </div>
      </div>
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

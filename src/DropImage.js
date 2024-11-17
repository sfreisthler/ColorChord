import React, { useState, useRef } from "react";
import { useNavigate } from "react-router-dom";

const DragAndDropImage = ({ onImageUpload }) => {
  const [isDragging, setIsDragging] = useState(false);
  const [imagePreview, setImagePreview] = useState(null);
  const [isSubmitEnabled, setIsSubmitEnabled] = useState(false);
  const fileInputRef = useRef(null);
  const navigate = useNavigate();

  const handleDragOver = (e) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = () => {
    setIsDragging(false);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setIsDragging(false);

    const file = e.dataTransfer.files[0];
    processFile(file);
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    processFile(file);
  };

  const processFile = (file) => {
    if (file && file.type.startsWith("image/")) {
      const reader = new FileReader();
      reader.onload = () => {
        setImagePreview(reader.result);
        onImageUpload(file); 
        setIsSubmitEnabled(true);
      };
      reader.readAsDataURL(file);
    } else {
      alert("Please upload a valid image file.");
    }
  };

  const handleClick = () => {
    fileInputRef.current.click();
  };

  const handleSubmit = () => {
    navigate("/processed"); 
  };

  return (
    <div>
      <div
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
        onClick={handleClick}
        style={{
          border: "2px dashed gray",
          borderRadius: "10px",
          padding: "20px",
          textAlign: "center",
          backgroundColor: isDragging ? "#f0f8ff" : "#fff",
          cursor: "pointer",
        }}
      >
        {imagePreview ? (
          <img
            src={imagePreview}
            alt="Uploaded Preview"
            style={{ maxWidth: "100%", height: "auto", marginTop: "10px" }}
          />
        ) : (
          <p>Drag and drop an image here, or click to upload.</p>
        )}
        <input
          type="file"
          accept="image/*"
          ref={fileInputRef}
          style={{ display: "none" }}
          onChange={handleFileChange}
        />
      </div>
      <button
        onClick={handleSubmit}
        disabled={!isSubmitEnabled} 
        style={{
          marginTop: "20px",
          padding: "10px 20px",
          fontSize: "16px",
          cursor: isSubmitEnabled ? "pointer" : "not-allowed",
          backgroundColor: isSubmitEnabled ? "#4caf50" : "#ccc",
          color: "white",
          border: "none",
          borderRadius: "5px",
        }}
      >
        Submit
      </button>
    </div>
  );
};

export default DragAndDropImage;

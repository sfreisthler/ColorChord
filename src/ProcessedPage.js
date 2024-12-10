import React from "react";

const ProcessedPage = () => {
    const deployedBackend = "https://colorchord.onrender.com/sound"
    const localBackend = "http://127.0.0.1:50000/sound"

    const playSound = async () => {
        try {
            const response = await fetch(deployedBackend);
            if (!response.ok) {
              throw new Error("Failed to fetch sound");
            }
            const audioBlob = await response.blob();
            const audioUrl = URL.createObjectURL(audioBlob);
            const audio = new Audio(audioUrl);
            audio.play();
        }
        catch (error) {
            console.error("Error playing sound:", error);
        };
    }
    return (
        <div>
        <h1>Image Successfully Uploaded!</h1>
        <p>Pretend a lovely little tune is playing.</p>
        <button onClick={playSound}>Play Sound</button>
        </div>
    );
};

export default ProcessedPage;
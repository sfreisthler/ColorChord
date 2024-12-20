import React from "react";

const ProcessedPage = () => {
    const localBackend = "http://127.0.0.1:50000/sound";
    const deployedBackend = "https://colorchord.onrender.com/upload";

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
        } catch (error) {
            console.error("Error playing sound:", error);
        }
    };

    return (
        <div
            style={{
                height: "100vh",
                width: "100vw",
                backgroundColor: "#003049",
                display: "flex",
                flexDirection: "column",
                justifyContent: "center",
                alignItems: "center",
                fontFamily: "'Climate Crisis', sans-serif",
                gap: "20px",
            }}
        >
            <h1
                style={{
                    color: "#f77f00",
                    fontSize: "30px",
                    margin: 0,
                    textAlign: "center"
                }}
            >
                Image Successfully Processed!
            </h1>
            <button
                onClick={playSound}
                style={{
                    backgroundColor: "#fcbf49",
                    border: "5px solid #eae2b7",
                    borderRadius: "8px",
                    color: "#f77f00",
                    fontSize: "18px",
                    cursor: "pointer",
                    padding: "10px 20px",
                    fontFamily: "'Climate Crisis', sans-serif",
                }}
            >
                Play Sound
            </button>
        </div>
    );
};

export default ProcessedPage;

import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./LandingPage.css";

export default function LandingPage() {
  const navigate = useNavigate();

  useEffect(() => {
    // Smooth fade-in class
    document.body.classList.add("dg-body-fade");
    return () => document.body.classList.remove("dg-body-fade");
  }, []);

  return (
    <div className="dg-landing">
      {/* Floating Particles */}
      <div className="dg-particles"></div>

      {/* Grid Overlay */}
      <div className="dg-grid-overlay"></div>

      {/* Main Visual */}
      <img
        className="dg-hero-img"
        src="https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819909/ChatGPT_Image_Nov_10_2025_05_56_10_PM_su5gye.png"
        alt="Dream Grid Visual"
      />

      {/* Hero Text */}
      <div className="dg-hero-content">
        <h1 className="dg-title">Dream Grid Interactive Studios</h1>
        <p className="dg-subtitle">
          High-impact visuals, immersive interactions, and modern web experiences.
        </p>

        <div className="dg-cta">
          <button onClick={() => navigate("/solutions")} className="dg-btn dg-btn-primary">
            View Solutions
          </button>
          <button onClick={() => navigate("/contact")} className="dg-btn dg-btn-outline">
            Contact Us
          </button>
        </div>
      </div>
    </div>
  );
}

import "./Footer.css";

export default function Footer() {
  const year = new Date().getFullYear();

  return (
    <footer className="footer">
      <div className="footer-left">
        Copyright © {year} Dream Grid Interactive Studios llc  - All Rights Reserved.
      </div>
      <div className="footer-right">
        Powered by <span className="footer-brand">Dream Grid Interactive Studios</span>
      </div>
    </footer>
  );
}

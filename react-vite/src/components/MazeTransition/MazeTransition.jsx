import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import "./MazeTransition.css";

export default function MazeTransition() {
  const location = useLocation();
  const [show, setShow] = useState(false);

  useEffect(() => {
    setShow(true);
    const timer = setTimeout(() => setShow(false), 3000); // Duration
    return () => clearTimeout(timer);
  }, [location]);

  return (
    <>
      {show && (
        <div className="maze-transition">
          <img
            src="https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762821006/7Obz_vh42iu.gif"
            alt="Dream Grid animation"
            className="maze-gif"
          />
        </div>
      )}
    </>
  );
}

// src/components/Navigation/Navigation.jsx
import { NavLink } from "react-router-dom";
// import { FiShoppingCart } from "react-icons/fi";
import ProfileButton from "./ProfileButton";
// import CartBadge from "../CartPage/CartBadge";
// import CartDrawer from "../CartPage/CartDrawer";
import "./Navigation.css";
// import { useState } from "react";

function Navigation() {
  // const [showCart, setShowCart] = useState(false);

  // const openCart = () => setShowCart(true);
  // const closeCart = () => setShowCart(false);

  return (
    <div className={`navigation-container`}>
      {/* Logo */}
          <ProfileButton  />


      {/* Links */}
      <nav className={`page-links-container-top`}>
        <div className="page-links-cont">
          <div className="link-word-group">
            <NavLink to="/" className="nav-bar-text">Home</NavLink>
            <NavLink to="/solutions" className="nav-bar-text">Solutions</NavLink>
            {/* <NavLink to="/company" className="nav-bar-text">Company</NavLink> */}
            {/* <NavLink to="/blog" className="nav-bar-text">Blog</NavLink> */}
            <NavLink to="/contact" className="nav-bar-text">Contact</NavLink>
            {/* <NavLink to="/cart" className="nav-bar-text">Cart</NavLink> */}
          </div>
        </div>
      </nav>

      <div className="icons-group">


        {/* Cart Icon + Badge */}
        <span className="cart-icon-wrapper">
          {/* <FiShoppingCart
            className="nav-bar-text-shop-link"
            onClick={openCart}
            role="button"
            aria-label="Open cart"
            tabIndex={0}
          /> */}
          {/* <CartBadge onClick={openCart} /> */}
        </span>

        {/* Profile stays the same */}

        {/* Drawer */}
        {/* <CartDrawer open={showCart} onClose={closeCart} /> */}
      </div>
    </div>
  );
}

export default Navigation;

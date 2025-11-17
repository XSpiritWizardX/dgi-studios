import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { fetchAllProducts } from "../../redux/products";
import "./ProductsPage.css";

export default function ProductsPage() {
  const dispatch = useDispatch();
  const allProducts = useSelector((state) => state.products.all || []);

  useEffect(() => {
    dispatch(fetchAllProducts());
  }, [dispatch]);

  // ---------------------------------------------
  // CATEGORY CONFIG — MAIN IMAGE + 3 TIER IMAGES
  // ---------------------------------------------
  const CATEGORY_CONFIG = {
    "Websites": {
      main: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
      tiers: {
        1: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
        2: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
        3: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
      }
    },

    "Enterprise": {
      main: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
      tiers: {
        1: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
        2: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
        3: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
      }
    },

    "AI Engineering": {
      main: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
      tiers: {
        1: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
        2: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
        3: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
      }
    },

    "Scientific Software": {
      main: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
      tiers: {
        1: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
        2: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
        3: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
      }
    },

    "Creative Tools": {
      main: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
      tiers: {
        1: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
        2: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
        3: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
      }
    },

    "Developer Tools": {
      main: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
      tiers: {
        1: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
        2: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
        3: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
      }
    },

    "Mobile Apps": {
      main: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
      tiers: {
        1: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
        2: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
        3: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
      }
    },

    "Games": {
      main: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
      tiers: {
        1: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
        2: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
        3: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
      }
    },

    "Design": {
      main: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
      tiers: {
        1: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
        2: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
        3: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
      }
    },

    "Marketing": {
      main: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
      tiers: {
        1: "htthttps://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
        2: "htthttps://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
        3: "htthttps://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
      }
    },

    "Content": {
      main: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
      tiers: {
        1: "hhttps://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
        2: "hhttps://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
        3: "hhttps://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
      }
    },

    "Hosting": {
      main: "https://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
      tiers: {
        1: "hhttps://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
        2: "hhttps://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
        3: "hhttps://res.cloudinary.com/dl6ls3rgu/image/upload/v1762819908/ChatGPT_Image_Nov_10_2025_05_59_28_PM_r51opu.png",
      }
    }
  };

  const FALLBACK_IMAGE = "https://via.placeholder.com/350x200?text=No+Image";

  // ---------------------------------------------
  // GROUP INTO CATEGORIES
  // ---------------------------------------------
  const categories = Object.keys(CATEGORY_CONFIG);

  const categorized = categories.map((catName) => {
    const items = allProducts.filter((p) => p.category === catName);

    const tiers = items.filter((p) => p.type === "Tier");
    const addons = items.filter((p) => p.type === "Add-On");

    return {
      name: catName,
      mainImage: CATEGORY_CONFIG[catName].main || FALLBACK_IMAGE,
      tierImages: CATEGORY_CONFIG[catName].tiers || {},
      tiers,
      addons
    };
  });

  return (
    <div className="products-page">
      <div className="dg-grid-overlay"></div>
      <div className="dg-particles"></div>

      <h1 className="products-title">Dream Grid Solutions</h1>

      {categorized.map((cat) => (
        <section key={cat.name} className="category-section">

          {/* CATEGORY HEADER */}
          <div className="category-header">
            <img
              src={cat.mainImage}
              alt={cat.name}
              className="category-img"
              onError={(e) => (e.target.src = FALLBACK_IMAGE)}
            />
            <h2>{cat.name}</h2>
          </div>

          {/* TIERS */}
          {cat.tiers.map((tier, i) => (
            <div key={tier.sku} className={`tier-row ${i % 2 !== 0 ? "reverse" : ""}`}>

              <div className="tier-details">
                <h3 className="tier-name">{tier.name}</h3>
                <p className="tier-description">{tier.description}</p>
                <p className="tier-price">
                  packages starting at ${tier.price.toLocaleString()}
                </p>
              </div>

              <div className="tier-image-wrapper">
                <img
                  src={
                    cat.tierImages[i + 1] ||
                    cat.mainImage ||
                    FALLBACK_IMAGE
                  }
                  alt={`${cat.name} Tier ${i + 1}`}
                  className="tier-image"
                  onError={(e) => (e.target.src = FALLBACK_IMAGE)}
                />
              </div>
            </div>
          ))}

          {/* ADDONS */}
          {cat.addons.length > 0 && (
            <div className="addons-section">
              <h3 className="addons-title">Add-Ons</h3>
              <ul className="addons-list">
                {cat.addons.map((addon) => (
                  <li key={addon.sku} className="addon-item">
                    <span className="product-span">
                      {addon.name}:<br />{addon.description}
                    </span>
                    <span className="addon-price">
                      starting at ${addon.price.toLocaleString()}
                    </span>
                  </li>
                ))}
              </ul>
            </div>
          )}

        </section>
      ))}
    </div>
  );
}

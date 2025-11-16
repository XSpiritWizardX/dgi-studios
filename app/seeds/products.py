from app.models import db, Product, environment, SCHEMA
from sqlalchemy.sql import text

# ===============================================================
# Batch Seeder Helper
# ===============================================================

def batch_insert(items):
    """Inserts a batch of product dicts with safety."""
    try:
        for item in items:
            db.session.add(Product(**item))
        db.session.commit()
        print(f"✔ Seeded {len(items)} items successfully.")
    except Exception as e:
        db.session.rollback()
        print("❌ Batch failed, rolled back:", e)


# ===============================================================
# CATEGORY SEEDERS
# ===============================================================

def seed_websites():
    items = [
        # WEBSITE SEEDS GO HERE (tiers + addons)


        # ============================================================
        # WEBSITE TIERS
        # ============================================================
        {
            "sku": "DG-WEB-T-001",
            "category": "Websites",
            "type": "Tier",
            "name": "Website Tier 1 - Basic",
            "description": "Full-stack website; Home/About/Services/Contact; backend API; DB; admin login; admin panel; responsive; animations",
            "price": 8000
        },
        {
            "sku": "DG-WEB-T-002",
            "category": "Websites",
            "type": "Tier",
            "name": "Website Tier 2 - Business",
            "description": "Everything in Tier 1 + role-based backend; email system; notifications; logs; business architecture",
            "price": 35000
        },
        {
            "sku": "DG-WEB-T-003",
            "category": "Websites",
            "type": "Tier",
            "name": "Website Tier 3 - Advanced",
            "description": "Everything in Tier 1 & 2 + enterprise backend; AI-ready; vector DB support; automation pipelines; scaling infrastructure",
            "price": 75000
        },

        # ============================================================
        # WEBSITE ADD-ONS
        # ============================================================
        {
            "sku": "DG-WEB-A-001",
            "category": "Websites",
            "type": "Add-On",
            "name": "Extra Page",
            "description": "Full custom additional page",
            "price": 450
        },
        {
            "sku": "DG-WEB-A-002",
            "category": "Websites",
            "type": "Add-On",
            "name": "FAQ Page",
            "description": "Expandable FAQ system with categories",
            "price": 600
        },
        {
            "sku": "DG-WEB-A-003",
            "category": "Websites",
            "type": "Add-On",
            "name": "Testimonials Page",
            "description": "Testimonials layout with responsive cards",
            "price": 650
        },
        {
            "sku": "DG-WEB-A-004",
            "category": "Websites",
            "type": "Add-On",
            "name": "Gallery System",
            "description": "Image gallery with lightbox and smooth transitions",
            "price": 900
        },
        {
            "sku": "DG-WEB-A-005",
            "category": "Websites",
            "type": "Add-On",
            "name": "Custom Hero Section",
            "description": "High-end hero with GSAP or Lottie animations",
            "price": 1200
        },
        {
            "sku": "DG-WEB-A-006",
            "category": "Websites",
            "type": "Add-On",
            "name": "Page Transitions",
            "description": "Advanced GSAP routing transitions",
            "price": 950
        },
        {
            "sku": "DG-WEB-A-007",
            "category": "Websites",
            "type": "Add-On",
            "name": "Custom Footer",
            "description": "Fully responsive custom-designed footer",
            "price": 850
        },
        {
            "sku": "DG-WEB-A-008",
            "category": "Websites",
            "type": "Add-On",
            "name": "Mobile Menu Redesign",
            "description": "Animated modern mobile menu",
            "price": 700
        },
        {
            "sku": "DG-WEB-A-009",
            "category": "Websites",
            "type": "Add-On",
            "name": "Multi-Language Support",
            "description": "Language switcher with localized routing",
            "price": 1500
        },
        {
            "sku": "DG-WEB-A-010",
            "category": "Websites",
            "type": "Add-On",
            "name": "Blog CMS",
            "description": "Full CMS with categories, tags, and WYSIWYG editor",
            "price": 3500
        },
        {
            "sku": "DG-WEB-A-011",
            "category": "Websites",
            "type": "Add-On",
            "name": "SEO Boost Package",
            "description": "SEO metadata, sitemap, robots.txt, and speed optimizations",
            "price": 1500
        },
        {
            "sku": "DG-WEB-A-012",
            "category": "Websites",
            "type": "Add-On",
            "name": "CRM Lite",
            "description": "Lead management, client notes, tagging system",
            "price": 4500
        },
        {
            "sku": "DG-WEB-A-013",
            "category": "Websites",
            "type": "Add-On",
            "name": "Customer Portal",
            "description": "Client portal for orders/invoices/files",
            "price": 7500
        },
        {
            "sku": "DG-WEB-A-014",
            "category": "Websites",
            "type": "Add-On",
            "name": "Billing + Payments",
            "description": "Invoices, Stripe checkout, tax logic, subscriptions",
            "price": 10000
        },
        {
            "sku": "DG-WEB-A-015",
            "category": "Websites",
            "type": "Add-On",
            "name": "User Management System",
            "description": "Users, roles, permissions, statuses",
            "price": 4000
        },
        {
            "sku": "DG-WEB-A-016",
            "category": "Websites",
            "type": "Add-On",
            "name": "Advanced Admin Dashboard",
            "description": "KPIs, charts, tables, analytics dashboards",
            "price": 6000
        },
        {
            "sku": "DG-WEB-A-017",
            "category": "Websites",
            "type": "Add-On",
            "name": "AI Assistant",
            "description": "Embedded AI chatbot with RAG or LLM integration",
            "price": 8000
        },
        {
            "sku": "DG-WEB-A-018",
            "category": "Websites",
            "type": "Add-On",
            "name": "Automations Engine",
            "description": "Trigger-based business workflow automations",
            "price": 6000
        },
        {
            "sku": "DG-WEB-A-019",
            "category": "Websites",
            "type": "Add-On",
            "name": "Integrations / APIs",
            "description": "Integrate QuickBooks, Google API, CRMs, or ERPs",
            "price": 7500
        },
        {
            "sku": "DG-WEB-A-020",
            "category": "Websites",
            "type": "Add-On",
            "name": "Analytics Engine",
            "description": "Graphs, dashboards, insights tracking",
            "price": 6500
        },
        {
            "sku": "DG-WEB-A-021",
            "category": "Websites",
            "type": "Add-On",
            "name": "Booking System",
            "description": "Calendar booking with admin controls",
            "price": 4200
        },
        {
            "sku": "DG-WEB-A-022",
            "category": "Websites",
            "type": "Add-On",
            "name": "Popup Builder",
            "description": "Marketing popups with triggers and analytics",
            "price": 1200
        },
        {
            "sku": "DG-WEB-A-023",
            "category": "Websites",
            "type": "Add-On",
            "name": "Service Quote Calculator",
            "description": "Interactive pricing calculator for services",
            "price": 3000
        },
        {
            "sku": "DG-WEB-A-024",
            "category": "Websites",
            "type": "Add-On",
            "name": "Review Importer",
            "description": "Import reviews from Google or Yelp",
            "price": 1800
        },
        {
            "sku": "DG-WEB-A-025",
            "category": "Websites",
            "type": "Add-On",
            "name": "Membership System",
            "description": "Subscriptions, gated content, access tiers",
            "price": 6500
        },
        {
            "sku": "DG-WEB-A-026",
            "category": "Websites",
            "type": "Add-On",
            "name": "Loyalty Points System",
            "description": "Reward points, customer tiers, gamified loyalty",
            "price": 4500
        },
        {
            "sku": "DG-WEB-A-027",
            "category": "Websites",
            "type": "Add-On",
            "name": "A/B Testing System",
            "description": "Split testing for pages and components",
            "price": 2500
        },
        {
            "sku": "DG-WEB-A-028",
            "category": "Websites",
            "type": "Add-On",
            "name": "Social Auto-Puller",
            "description": "Automatically sync Instagram/Facebook feeds",
            "price": 2000
        },
        {
            "sku": "DG-WEB-A-029",
            "category": "Websites",
            "type": "Add-On",
            "name": "Dynamic Sections Pack",
            "description": "Reusable animated UI sections",
            "price": 2200
        },
        {
            "sku": "DG-WEB-A-030",
            "category": "Websites",
            "type": "Add-On",
            "name": "Brand Icons Pack",
            "description": "Custom icon set designed for brand identity",
            "price": 1100
        },
        {
            "sku": "DG-WEB-A-031",
            "category": "Websites",
            "type": "Add-On",
            "name": "Animated SVG Pack",
            "description": "Custom SVG animations",
            "price": 1500
        },
        {
            "sku": "DG-WEB-A-032",
            "category": "Websites",
            "type": "Add-On",
            "name": "Cookie Consent System",
            "description": "GDPR/CCPA-compliant cookie banner system",
            "price": 500
        },
        {
            "sku": "DG-WEB-A-033",
            "category": "Websites",
            "type": "Add-On",
            "name": "Scheduling System",
            "description": "Advanced multi-user scheduling",
            "price": 5200
        },
        {
            "sku": "DG-WEB-A-034",
            "category": "Websites",
            "type": "Add-On",
            "name": "Application Form System",
            "description": "Job/contractor application builder",
            "price": 3500
        },
        {
            "sku": "DG-WEB-A-035",
            "category": "Websites",
            "type": "Add-On",
            "name": "Newsletter System",
            "description": "Email signup + autoresponder",
            "price": 1500
        },
        {
            "sku": "DG-WEB-A-036",
            "category": "Websites",
            "type": "Add-On",
            "name": "Single Page Website",
            "description": "One-page scrolling website",
            "price": 800
        },



    ]
    batch_insert(items)


def seed_games():
    items = [
        # GAME SEEDS GO HERE


        # ============================================================
        # GAME TIERS
        # ============================================================
        {
            "sku": "DG-GAME-T-001",
            "category": "Games",
            "type": "Tier",
            "name": "Game Tier 1 - Basic Web Game",
            "description": "Simple 2D game using Phaser/Canvas; scoring; animations; responsive; sound effects.",
            "price": 6500
        },
        {
            "sku": "DG-GAME-T-002",
            "category": "Games",
            "type": "Tier",
            "name": "Game Tier 2 - Web/Mobile",
            "description": "Everything in Tier 1 + levels, AI, power-ups, save system, UI overhaul, mobile builds.",
            "price": 18000
        },
        {
            "sku": "DG-GAME-T-003",
            "category": "Games",
            "type": "Tier",
            "name": "Game Tier 3 - Full Game (Unity/Godot)",
            "description": "Full cross-platform game; multi-level; inventory; XP; combat; physics; bosses; analytics; Steam/mobile builds.",
            "price": 45000
        },

        # ============================================================
        # GAME ADD-ONS
        # ============================================================
        {
            "sku": "DG-GAME-A-001",
            "category": "Games",
            "type": "Add-On",
            "name": "Extra Game Level",
            "description": "Adds a custom new playable level.",
            "price": 500
        },
        {
            "sku": "DG-GAME-A-002",
            "category": "Games",
            "type": "Add-On",
            "name": "Boss Fight",
            "description": "Unique boss encounter with custom logic and AI.",
            "price": 1200
        },
        {
            "sku": "DG-GAME-A-003",
            "category": "Games",
            "type": "Add-On",
            "name": "Multiplayer",
            "description": "Online co-op or versus mode with matchmaking.",
            "price": 4500
        },
        {
            "sku": "DG-GAME-A-004",
            "category": "Games",
            "type": "Add-On",
            "name": "In-Game Shop",
            "description": "Virtual shop for items, skins, or consumables.",
            "price": 3000
        },
        {
            "sku": "DG-GAME-A-005",
            "category": "Games",
            "type": "Add-On",
            "name": "Ad Integration",
            "description": "AdMob or Unity Ads integration for monetization.",
            "price": 700
        },
        {
            "sku": "DG-GAME-A-006",
            "category": "Games",
            "type": "Add-On",
            "name": "Achievements System",
            "description": "Trophy, medal, and achievement system.",
            "price": 650
        },
        {
            "sku": "DG-GAME-A-007",
            "category": "Games",
            "type": "Add-On",
            "name": "Leaderboards",
            "description": "Online high-score leaderboard integration.",
            "price": 900
        },
        {
            "sku": "DG-GAME-A-008",
            "category": "Games",
            "type": "Add-On",
            "name": "Character Skins",
            "description": "Custom character skin pack.",
            "price": 350
        },
        {
            "sku": "DG-GAME-A-009",
            "category": "Games",
            "type": "Add-On",
            "name": "Soundtrack Pack",
            "description": "Original soundtrack composed for the game.",
            "price": 1500
        },
        {
            "sku": "DG-GAME-A-010",
            "category": "Games",
            "type": "Add-On",
            "name": "Controller Support",
            "description": "Support for Xbox/PS controllers, gamepads, etc.",
            "price": 900
        },
        {
            "sku": "DG-GAME-A-011",
            "category": "Games",
            "type": "Add-On",
            "name": "Game Analytics",
            "description": "Event tracking, metrics, player behavior insights.",
            "price": 2000
        },
        {
            "sku": "DG-GAME-A-012",
            "category": "Games",
            "type": "Add-On",
            "name": "Player Abilities",
            "description": "Adds new skills or abilities for the player.",
            "price": 700
        },
        {
            "sku": "DG-GAME-A-013",
            "category": "Games",
            "type": "Add-On",
            "name": "Crafting System",
            "description": "Material crafting and recipe system.",
            "price": 2500
        },
        {
            "sku": "DG-GAME-A-014",
            "category": "Games",
            "type": "Add-On",
            "name": "Inventory System",
            "description": "Backpack/inventory UI and item handling.",
            "price": 2200
        },
        {
            "sku": "DG-GAME-A-015",
            "category": "Games",
            "type": "Add-On",
            "name": "Quest System",
            "description": "Quests, missions, rewards, tracking.",
            "price": 3500
        },
        {
            "sku": "DG-GAME-A-016",
            "category": "Games",
            "type": "Add-On",
            "name": "Dialogue System",
            "description": "NPC dialogue trees + branching choices.",
            "price": 1800
        },
        {
            "sku": "DG-GAME-A-017",
            "category": "Games",
            "type": "Add-On",
            "name": "Cutscene Pack",
            "description": "Prebuilt cinematic cutscene templates.",
            "price": 1000
        },
        {
            "sku": "DG-GAME-A-018",
            "category": "Games",
            "type": "Add-On",
            "name": "Map Editor",
            "description": "In-game map creation/editing tool.",
            "price": 4500
        },
        {
            "sku": "DG-GAME-A-019",
            "category": "Games",
            "type": "Add-On",
            "name": "Procedural Generation",
            "description": "Random terrain or world generator.",
            "price": 6000
        },
        {
            "sku": "DG-GAME-A-020",
            "category": "Games",
            "type": "Add-On",
            "name": "Seasonal Events System",
            "description": "Holiday events and limited-time content.",
            "price": 3000
        },
        {
            "sku": "DG-GAME-A-021",
            "category": "Games",
            "type": "Add-On",
            "name": "Daily Rewards",
            "description": "Login reward system.",
            "price": 950
        },
        {
            "sku": "DG-GAME-A-022",
            "category": "Games",
            "type": "Add-On",
            "name": "Chest/Key System",
            "description": "Loot chest + key mechanic.",
            "price": 900
        },
        {
            "sku": "DG-GAME-A-023",
            "category": "Games",
            "type": "Add-On",
            "name": "Social Sharing",
            "description": "Share scores to social media.",
            "price": 600
        },
        {
            "sku": "DG-GAME-A-024",
            "category": "Games",
            "type": "Add-On",
            "name": "Replay System",
            "description": "Record and replay gameplay.",
            "price": 1600
        },
        {
            "sku": "DG-GAME-A-025",
            "category": "Games",
            "type": "Add-On",
            "name": "Shader Pack",
            "description": "Custom shaders and visual effects.",
            "price": 2200
        },
        {
            "sku": "DG-GAME-A-026",
            "category": "Games",
            "type": "Add-On",
            "name": "Weather System",
            "description": "Dynamic weather, storms, seasons.",
            "price": 2500
        },
        {
            "sku": "DG-GAME-A-027",
            "category": "Games",
            "type": "Add-On",
            "name": "Physics Upgrade",
            "description": "Improved physics, ragdoll effects.",
            "price": 3500
        },
        {
            "sku": "DG-GAME-A-028",
            "category": "Games",
            "type": "Add-On",
            "name": "Combo Combat System",
            "description": "Combo multipliers, hit chains, advanced fighting.",
            "price": 2800
        },
        {
            "sku": "DG-GAME-A-029",
            "category": "Games",
            "type": "Add-On",
            "name": "Voice Chat",
            "description": "Real-time voice chat for multiplayer.",
            "price": 4500
        },
        {
            "sku": "DG-GAME-A-030",
            "category": "Games",
            "type": "Add-On",
            "name": "Matchmaking System",
            "description": "Skill-based matchmaking, lobbies.",
            "price": 6500
        },
        {
            "sku": "DG-GAME-A-031",
            "category": "Games",
            "type": "Add-On",
            "name": "Analytics Dashboard",
            "description": "Admin dashboard for game metrics and insights.",
            "price": 5300
        },



    ]
    batch_insert(items)


def seed_creative_tools():
    items = [
        # CREATIVE TOOLS GO HERE

        # ============================================================
        # CREATIVE TOOLS — TIERS
        # ============================================================
        {
            "sku": "DG-CRT-T-001",
            "category": "Creative Tools",
            "type": "Tier",
            "name": "Creative Tool Tier 1 - Simple Editor",
            "description": "Basic editor with PNG export, 1–2 layers, undo/redo, basic tools, simple UI.",
            "price": 5000
        },
        {
            "sku": "DG-CRT-T-002",
            "category": "Creative Tools",
            "type": "Tier",
            "name": "Creative Tool Tier 2 - Advanced Editor",
            "description": "Multi-layer editing, brushes, templates, asset uploads, custom themes, advanced UI.",
            "price": 16000
        },
        {
            "sku": "DG-CRT-T-003",
            "category": "Creative Tools",
            "type": "Tier",
            "name": "Creative Tool Tier 3 - SaaS Platform",
            "description": "Full SaaS: user accounts, cloud storage, marketplace, AI features, collaboration.",
            "price": 40000
        },

        # ============================================================
        # CREATIVE TOOLS — ADD-ONS
        # ============================================================
        {
            "sku": "DG-CRT-A-001",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "Brush / Tool",
            "description": "Adds a new brush or design tool to the editor.",
            "price": 350
        },
        {
            "sku": "DG-CRT-A-002",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "Template Pack",
            "description": "10–20 custom design templates.",
            "price": 600
        },
        {
            "sku": "DG-CRT-A-003",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "Asset Library",
            "description": "Icons, shapes, stickers, patterns library.",
            "price": 900
        },
        {
            "sku": "DG-CRT-A-004",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "Cloud Save System",
            "description": "Save projects and assets securely in the cloud.",
            "price": 3500
        },
        {
            "sku": "DG-CRT-A-005",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "Collaboration",
            "description": "Real-time editing with multiple users.",
            "price": 4000
        },
        {
            "sku": "DG-CRT-A-006",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "AI Suggestions",
            "description": "AI auto-enhance, filters, and design suggestions.",
            "price": 5000
        },
        {
            "sku": "DG-CRT-A-007",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "PDF Export",
            "description": "Export designs as print-ready PDFs.",
            "price": 500
        },
        {
            "sku": "DG-CRT-A-008",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "Watermark System",
            "description": "Add/remove brand watermarks from designs.",
            "price": 350
        },
        {
            "sku": "DG-CRT-A-009",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "Theme Builder",
            "description": "Create and save custom UI themes.",
            "price": 800
        },
        {
            "sku": "DG-CRT-A-010",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "Cloud Asset Sync",
            "description": "Shared cloud asset library synced across devices.",
            "price": 2000
        },
        {
            "sku": "DG-CRT-A-011",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "AI Brushes",
            "description": "AI-powered brushes for procedural shapes and textures.",
            "price": 1500
        },
        {
            "sku": "DG-CRT-A-012",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "AI Object Removal",
            "description": "Automatically remove objects/backgrounds from images.",
            "price": 2500
        },
        {
            "sku": "DG-CRT-A-013",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "Layer Effects",
            "description": "Drop shadows, glows, bevels, and filter effects.",
            "price": 1200
        },
        {
            "sku": "DG-CRT-A-014",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "Vector Tools",
            "description": "Bezier curves, vector shapes, and SVG editing.",
            "price": 1800
        },
        {
            "sku": "DG-CRT-A-015",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "Timeline Animation",
            "description": "Motion timeline for frame-by-frame or keyframe animation.",
            "price": 3500
        },
        {
            "sku": "DG-CRT-A-016",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "Color Grading Engine",
            "description": "Advanced color grading controls and sliders.",
            "price": 1800
        },
        {
            "sku": "DG-CRT-A-017",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "LUT Importer",
            "description": "Import LUTs for advanced color profiles.",
            "price": 900
        },
        {
            "sku": "DG-CRT-A-018",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "Social Export Pack",
            "description": "Preset exports for Instagram, TikTok, YouTube, etc.",
            "price": 700
        },
        {
            "sku": "DG-CRT-A-019",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "Auto Background Removal",
            "description": "AI-powered transparent-background extraction.",
            "price": 2500
        },
        {
            "sku": "DG-CRT-A-020",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "RAW Support",
            "description": "Import and edit RAW camera files.",
            "price": 2200
        },
        {
            "sku": "DG-CRT-A-021",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "Batch Exporter",
            "description": "Export multiple files at once with custom rules.",
            "price": 1200
        },
        {
            "sku": "DG-CRT-A-022",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "Template Marketplace",
            "description": "Sell or share templates inside the platform.",
            "price": 5000
        },
        {
            "sku": "DG-CRT-A-023",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "Shared Workspaces",
            "description": "Team collaboration with shared folders.",
            "price": 4000
        },
        {
            "sku": "DG-CRT-A-024",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "Custom Filters Engine",
            "description": "Create and save custom image filters.",
            "price": 3000
        },
        {
            "sku": "DG-CRT-A-025",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "Unlimited Layers Support",
            "description": "Removes layer count limits for advanced designs.",
            "price": 1500
        },
        {
            "sku": "DG-CRT-A-026",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "Offline Mode",
            "description": "Enable full offline editing with local sync.",
            "price": 2800
        },
        {
            "sku": "DG-CRT-A-027",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "Theme Store",
            "description": "Marketplace for downloadable themes.",
            "price": 3500
        },
        {
            "sku": "DG-CRT-A-028",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "Motion Graphics Templates",
            "description": "Premade animation assets and transitions.",
            "price": 2200
        },
        {
            "sku": "DG-CRT-A-029",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "Render Queue",
            "description": "Background queued rendering system.",
            "price": 1700
        },
        {
            "sku": "DG-CRT-A-030",
            "category": "Creative Tools",
            "type": "Add-On",
            "name": "Formula Design Tools",
            "description": "Math-based procedural design tools.",
            "price": 2600
        },


    ]
    batch_insert(items)


def seed_dev_tools():
    items = [

        # ============================================================
        # DEVELOPER TOOLS — TIERS
        # ============================================================
        {
            "sku": "DG-DEV-T-001",
            "category": "Developer Tools",
            "type": "Tier",
            "name": "Dev Tools Tier 1 - Utility Scripts",
            "description": "Small automation scripts, simple processors, API fetchers, file utilities.",
            "price": 4000
        },
        {
            "sku": "DG-DEV-T-002",
            "category": "Developer Tools",
            "type": "Tier",
            "name": "Dev Tools Tier 2 - Automation Pipelines",
            "description": "CRON jobs, report generators, schedulers, auto importers, batch processors.",
            "price": 12000
        },
        {
            "sku": "DG-DEV-T-003",
            "category": "Developer Tools",
            "type": "Tier",
            "name": "Dev Tools Tier 3 - Engineering Systems",
            "description": "Full internal automation systems, ETL pipelines, bots, engineering dashboards.",
            "price": 30000
        },

        # ============================================================
        # DEVELOPER TOOLS — ADD-ONS
        # ============================================================
        {
            "sku": "DG-DEV-A-001",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "Web Scraper",
            "description": "Python/Node-based scraper with structured data extraction.",
            "price": 2500
        },
        {
            "sku": "DG-DEV-A-002",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "Bulk Scraping Pipeline",
            "description": "Multi-source scraping with concurrency and deduplication.",
            "price": 6000
        },
        {
            "sku": "DG-DEV-A-003",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "API Connector",
            "description": "Plugin to integrate with third-party APIs.",
            "price": 1800
        },
        {
            "sku": "DG-DEV-A-004",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "Data Cleaning Script",
            "description": "Normalize, validate, sanitize and format raw data.",
            "price": 1200
        },
        {
            "sku": "DG-DEV-A-005",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "Data Migration Utility",
            "description": "Convert CSV/JSON/XML files into databases.",
            "price": 2000
        },
        {
            "sku": "DG-DEV-A-006",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "ETL Pipeline",
            "description": "Extract-transform-load pipeline with task orchestration.",
            "price": 6000
        },
        {
            "sku": "DG-DEV-A-007",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "Cron Job Scheduler",
            "description": "Automated scheduled tasks with interval logic.",
            "price": 1500
        },
        {
            "sku": "DG-DEV-A-008",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "PDF Automation",
            "description": "PDF extraction, merging, processing, and data parsing.",
            "price": 1800
        },
        {
            "sku": "DG-DEV-A-009",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "Email Parser Bot",
            "description": "Extracts structured data from inbound emails automatically.",
            "price": 2500
        },
        {
            "sku": "DG-DEV-A-010",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "Slack/Discord Bot",
            "description": "Automated bot to run workflows or notify on events.",
            "price": 2000
        },
        {
            "sku": "DG-DEV-A-011",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "File Converter",
            "description": "Convert between CSV, Excel, PDF, JSON, XML formats.",
            "price": 1500
        },
        {
            "sku": "DG-DEV-A-012",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "Database Backup Utility",
            "description": "Automated database backup generator with restore points.",
            "price": 2500
        },
        {
            "sku": "DG-DEV-A-013",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "Monitoring Script",
            "description": "Resource monitoring, error tracking, and alerts.",
            "price": 1800
        },
        {
            "sku": "DG-DEV-A-014",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "AI Classification Pipeline",
            "description": "AI classifier to sort images, text, or datasets.",
            "price": 5500
        },
        {
            "sku": "DG-DEV-A-015",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "Developer Dashboard",
            "description": "Internal dashboard for logs, metrics, dev tools, jobs.",
            "price": 4000
        },

        # EXTRA DEV ADD-ONS (YOU REQUESTED MORE OPTIONS)
        {
            "sku": "DG-DEV-A-016",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "Webhook Engine",
            "description": "Webhook sending/receiving engine for real-time events.",
            "price": 2500
        },
        {
            "sku": "DG-DEV-A-017",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "Encryption Toolkit",
            "description": "AES/RSA encryption utilities for secure data operations.",
            "price": 2000
        },
        {
            "sku": "DG-DEV-A-018",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "API Rate Limiter",
            "description": "IP rate-limiting utility to protect endpoints.",
            "price": 1600
        },
        {
            "sku": "DG-DEV-A-019",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "Session Management Module",
            "description": "Secure, expiring session token handler.",
            "price": 1300
        },
        {
            "sku": "DG-DEV-A-020",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "Error Tracking Dashboard",
            "description": "Centralized place for logs, stack traces, error reports.",
            "price": 3400
        },
        {
            "sku": "DG-DEV-A-021",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "Task Queue Processor",
            "description": "Queue workers using Redis/RQ/Celery.",
            "price": 5000
        },
        {
            "sku": "DG-DEV-A-022",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "SFTP Sync Utility",
            "description": "Sync files via SFTP with automation rules.",
            "price": 1800
        },
        {
            "sku": "DG-DEV-A-023",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "Multi-Database Sync",
            "description": "Sync data between multiple DBs automatically.",
            "price": 5500
        },
        {
            "sku": "DG-DEV-A-024",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "Automated Document Generator",
            "description": "Generate PDFs, reports, receipts using templates.",
            "price": 2400
        },
        {
            "sku": "DG-DEV-A-025",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "Webhook Relay System",
            "description": "Forward events across systems securely.",
            "price": 2000
        },
        {
            "sku": "DG-DEV-A-026",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "Multi-Step Approval Workflow",
            "description": "Approval chains for internal tools.",
            "price": 3200
        },
        {
            "sku": "DG-DEV-A-027",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "Sandbox Environment",
            "description": "Safe environment for testing data imports.",
            "price": 3000
        },
        {
            "sku": "DG-DEV-A-028",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "Admin Command Console",
            "description": "Run admin commands from a panel.",
            "price": 4500
        },
        {
            "sku": "DG-DEV-A-029",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "Internal Package Manager",
            "description": "Private repository for shared internal tools.",
            "price": 6000
        },
        {
            "sku": "DG-DEV-A-030",
            "category": "Developer Tools",
            "type": "Add-On",
            "name": "Auto Data Labeling Pipeline",
            "description": "Auto-label data for ML training.",
            "price": 7000
        },

    ]

    batch_insert(items)


def seed_enterprise():
    items = [

        # ============================================================
        # ENTERPRISE — TIERS
        # ============================================================
        {
            "sku": "DG-ENT-T-001",
            "category": "Enterprise",
            "type": "Tier",
            "name": "Enterprise Tier 1 - Logistics/Fleet System",
            "description": "Fleet tracking, routing, dispatching, GPS integration, driver dashboards, logistics management.",
            "price": 90000
        },
        {
            "sku": "DG-ENT-T-002",
            "category": "Enterprise",
            "type": "Tier",
            "name": "Enterprise Tier 2 - Factory Dashboard System",
            "description": "Factory KPIs, equipment uptime, production metrics, shift reports, IoT sensor integration.",
            "price": 105000
        },
        {
            "sku": "DG-ENT-T-003",
            "category": "Enterprise",
            "type": "Tier",
            "name": "Enterprise Tier 3 - ERP-Lite System",
            "description": "Enterprise resource management with modules for HR, finances, warehouse, inventory, dashboards, permissions.",
            "price": 120000
        },

        # ============================================================
        # ENTERPRISE — ADD-ONS
        # ============================================================
        {
            "sku": "DG-ENT-A-001",
            "category": "Enterprise",
            "type": "Add-On",
            "name": "Manufacturing Flow Tools",
            "description": "Production step tracking, workflow visualizations, bottleneck identification.",
            "price": 15000
        },
        {
            "sku": "DG-ENT-A-002",
            "category": "Enterprise",
            "type": "Add-On",
            "name": "Multi-Warehouse System",
            "description": "Manage multiple warehouse locations, inventory reconciliation, transfers.",
            "price": 10000
        },
        {
            "sku": "DG-ENT-A-003",
            "category": "Enterprise",
            "type": "Add-On",
            "name": "Vendor Bidding System",
            "description": "RFQ creation, vendor bidding logic, approval workflow.",
            "price": 9500
        },
        {
            "sku": "DG-ENT-A-004",
            "category": "Enterprise",
            "type": "Add-On",
            "name": "Corporate BI Dashboard",
            "description": "High-level business intelligence dashboards for executives.",
            "price": 12500
        },
        {
            "sku": "DG-ENT-A-005",
            "category": "Enterprise",
            "type": "Add-On",
            "name": "Supply Chain Dashboard",
            "description": "Logistics metrics, supplier performance tracking, inbound/outbound analytics.",
            "price": 14000
        },

        # ============================================================
        # ENTERPRISE — BONUS ADD-ONS (HIGH VALUE)
        # ============================================================
        {
            "sku": "DG-ENT-A-006",
            "category": "Enterprise",
            "type": "Add-On",
            "name": "IoT Sensor Hub",
            "description": "Connect IoT sensors for factory, logistics, temperature, vibration, or environmental readings.",
            "price": 25000
        },
        {
            "sku": "DG-ENT-A-007",
            "category": "Enterprise",
            "type": "Add-On",
            "name": "Predictive Maintenance Engine",
            "description": "Machine learning system to predict machine failures using sensor & usage data.",
            "price": 35000
        },
        {
            "sku": "DG-ENT-A-008",
            "category": "Enterprise",
            "type": "Add-On",
            "name": "Employee Time & Attendance System",
            "description": "Clock-in/out system, scheduling, compliance rules, payroll export.",
            "price": 16000
        },
        {
            "sku": "DG-ENT-A-009",
            "category": "Enterprise",
            "type": "Add-On",
            "name": "Role-Based Permission System (Advanced)",
            "description": "Multi-layered permissions for enterprise operations.",
            "price": 12000
        },
        {
            "sku": "DG-ENT-A-010",
            "category": "Enterprise",
            "type": "Add-On",
            "name": "Document Control System",
            "description": "ISO-compliant document versioning, approvals, signatures.",
            "price": 18000
        },
        {
            "sku": "DG-ENT-A-011",
            "category": "Enterprise",
            "type": "Add-On",
            "name": "Production Forecasting",
            "description": "ML-based forecasting for inventory, production runs, and staffing.",
            "price": 40000
        },
        {
            "sku": "DG-ENT-A-012",
            "category": "Enterprise",
            "type": "Add-On",
            "name": "Quality Control System",
            "description": "QC inspections, audits, batch tracking, issue reporting.",
            "price": 20000
        },
        {
            "sku": "DG-ENT-A-013",
            "category": "Enterprise",
            "type": "Add-On",
            "name": "Asset Tracking System",
            "description": "Track tools, machinery, and equipment using QR/RFID.",
            "price": 18000
        },
        {
            "sku": "DG-ENT-A-014",
            "category": "Enterprise",
            "type": "Add-On",
            "name": "Custom Enterprise SSO",
            "description": "Login with Azure AD, Okta, Google Workspace, or custom LDAP.",
            "price": 14000
        },
        {
            "sku": "DG-ENT-A-015",
            "category": "Enterprise",
            "type": "Add-On",
            "name": "Multi-Branch Accounting Module",
            "description": "Accounting for multiple facilities with ledger syncing.",
            "price": 30000
        },

    ]

    batch_insert(items)


def seed_scientific():
    items = [

        # ============================================================
        # SCIENCE SOFTWARE — TIERS
        # ============================================================
        {
            "sku": "DG-SCI-T-001",
            "category": "Scientific Software",
            "type": "Tier",
            "name": "Scientific Tier 1 - Research Utility",
            "description": "Basic research tools, lab calculators, data loggers, visualization charts, statistical helpers.",
            "price": 30000
        },
        {
            "sku": "DG-SCI-T-002",
            "category": "Scientific Software",
            "type": "Tier",
            "name": "Scientific Tier 2 - Modeling & Simulation Suite",
            "description": "Physics/chemistry/biology simulation engines, formulas, complex algorithms, experiment modeling.",
            "price": 120000
        },
        {
            "sku": "DG-SCI-T-003",
            "category": "Scientific Software",
            "type": "Tier",
            "name": "Scientific Tier 3 - Enterprise Research Platform",
            "description": "Large-scale scientific platform: datasets, AI models, lab workflow, HPC integration, cloud computing.",
            "price": 350000
        },

        # ============================================================
        # SCIENCE SOFTWARE — ADD-ONS
        # ============================================================
        {
            "sku": "DG-SCI-A-001",
            "category": "Scientific Software",
            "type": "Add-On",
            "name": "Simulation Engine",
            "description": "Physics or chemistry simulation engine with live visualization.",
            "price": 35000
        },
        {
            "sku": "DG-SCI-A-002",
            "category": "Scientific Software",
            "type": "Add-On",
            "name": "Molecular Modeling",
            "description": "3D molecule viewer, interaction forces, bonding predictions.",
            "price": 25000
        },
        {
            "sku": "DG-SCI-A-003",
            "category": "Scientific Software",
            "type": "Add-On",
            "name": "Genome Analysis Tool",
            "description": "DNA/RNA sequence analysis, mutation detection, alignment algorithms.",
            "price": 55000
        },
        {
            "sku": "DG-SCI-A-004",
            "category": "Scientific Software",
            "type": "Add-On",
            "name": "AI Lab Assistant",
            "description": "AI-driven insights, formula predictions, result interpretations.",
            "price": 30000
        },
        {
            "sku": "DG-SCI-A-005",
            "category": "Scientific Software",
            "type": "Add-On",
            "name": "Experiment Modeling UI",
            "description": "Graph-based experiment builder for complex workflows.",
            "price": 18000
        },
        {
            "sku": "DG-SCI-A-006",
            "category": "Scientific Software",
            "type": "Add-On",
            "name": "Clinical Data Manager",
            "description": "HIPAA-compliant clinical data entry, charts, exports.",
            "price": 40000
        },
        {
            "sku": "DG-SCI-A-007",
            "category": "Scientific Software",
            "type": "Add-On",
            "name": "Lab Equipment Integrations",
            "description": "Data ingestion from microscopes, analyzers, sensors, or lab robotics.",
            "price": 30000
        },
        {
            "sku": "DG-SCI-A-008",
            "category": "Scientific Software",
            "type": "Add-On",
            "name": "High-Precision Calculators",
            "description": "Specialized calculators for chemistry, physics, engineering.",
            "price": 7000
        },
        {
            "sku": "DG-SCI-A-009",
            "category": "Scientific Software",
            "type": "Add-On",
            "name": "3D Biology Simulation",
            "description": "Cellular, organ, or biome-level 3D visualization and interactions.",
            "price": 60000
        },
        {
            "sku": "DG-SCI-A-010",
            "category": "Scientific Software",
            "type": "Add-On",
            "name": "AI Data Labeling (Scientific)",
            "description": "Auto-label microscopy images, waveform data, spectrograms, etc.",
            "price": 25000
        },
        {
            "sku": "DG-SCI-A-011",
            "category": "Scientific Software",
            "type": "Add-On",
            "name": "FDA/GxP Compliance Tools",
            "description": "Audit logs, signatures, versioning, validation modules.",
            "price": 45000
        },
        {
            "sku": "DG-SCI-A-012",
            "category": "Scientific Software",
            "type": "Add-On",
            "name": "Spectrometer Data Processor",
            "description": "Parse and visualize spectroscopy files (FTIR/NMR/UV-Vis).",
            "price": 25000
        },
        {
            "sku": "DG-SCI-A-013",
            "category": "Scientific Software",
            "type": "Add-On",
            "name": "Mathematical Solver",
            "description": "ODE/PDE solvers with symbolic & numerical computation.",
            "price": 20000
        },
        {
            "sku": "DG-SCI-A-014",
            "category": "Scientific Software",
            "type": "Add-On",
            "name": "Lab Notebook System",
            "description": "Digital lab notebook with versioning, tagging, and team sharing.",
            "price": 15000
        },
        {
            "sku": "DG-SCI-A-015",
            "category": "Scientific Software",
            "type": "Add-On",
            "name": "Microscopy Image Analyzer",
            "description": "AI cell-counting, segmentation, classification.",
            "price": 55000
        },
        {
            "sku": "DG-SCI-A-016",
            "category": "Scientific Software",
            "type": "Add-On",
            "name": "Greenhouse Automation",
            "description": "Sensors + automation for plant growth experiments.",
            "price": 30000
        },
        {
            "sku": "DG-SCI-A-017",
            "category": "Scientific Software",
            "type": "Add-On",
            "name": "Chemical Reaction Predictor",
            "description": "Predict outcomes, yields, and energy changes using ML.",
            "price": 50000
        },
        {
            "sku": "DG-SCI-A-018",
            "category": "Scientific Software",
            "type": "Add-On",
            "name": "Physics Simulation Pack",
            "description": "Kinematics, electromagnetics, and quantum modules.",
            "price": 35000
        },
        {
            "sku": "DG-SCI-A-019",
            "category": "Scientific Software",
            "type": "Add-On",
            "name": "Bioinformatics Pipeline",
            "description": "FASTQ → alignment → variant calling → reporting.",
            "price": 65000
        },
        {
            "sku": "DG-SCI-A-020",
            "category": "Scientific Software",
            "type": "Add-On",
            "name": "Lab Inventory System",
            "description": "Reagents, samples, freezer tracking, barcode/RFID options.",
            "price": 18000
        },
        {
            "sku": "DG-SCI-A-021",
            "category": "Scientific Software",
            "type": "Add-On",
            "name": "AI Hypothesis Generator",
            "description": "AI model trained on scientific literature to suggest experiments.",
            "price": 45000
        },
        {
            "sku": "DG-SCI-A-022",
            "category": "Scientific Software",
            "type": "Add-On",
            "name": "Climate/Environmental Modeling",
            "description": "Simulations for CO2, soil, weather, climate trends.",
            "price": 40000
        },
        {
            "sku": "DG-SCI-A-023",
            "category": "Scientific Software",
            "type": "Add-On",
            "name": "Statistical Study Analyzer",
            "description": "T-tests, ANOVA, regression, survival analysis, dashboards.",
            "price": 16000
        },
        {
            "sku": "DG-SCI-A-024",
            "category": "Scientific Software",
            "type": "Add-On",
            "name": "Chemical Drawing Toolkit",
            "description": "Structure editor, molecule reconstruction, IUPAC naming.",
            "price": 14000
        },
        {
            "sku": "DG-SCI-A-025",
            "category": "Scientific Software",
            "type": "Add-On",
            "name": "HPC Cluster Integration",
            "description": "Connect to high-performance computing clusters.",
            "price": 30000
        },

    ]

    batch_insert(items)


def seed_ai_engineering():
    items = [

        # ============================================================
        # AI ENGINEERING — TIERS
        # ============================================================
        {
            "sku": "DG-AI-T-001",
            "category": "AI Engineering",
            "type": "Tier",
            "name": "AI Tier 1 - Applied AI Tools",
            "description": "Simple AI tools: text generation, image tagging, summarizers, chatbots, light ML models.",
            "price": 15000
        },
        {
            "sku": "DG-AI-T-002",
            "category": "AI Engineering",
            "type": "Tier",
            "name": "AI Tier 2 - ML Systems & Automation",
            "description": "Automated ML pipelines, embeddings search, RAG systems, vector DBs, classification models, analytics.",
            "price": 60000
        },
        {
            "sku": "DG-AI-T-003",
            "category": "AI Engineering",
            "type": "Tier",
            "name": "AI Tier 3 - Enterprise AI Platform",
            "description": "Full AI ecosystem: custom LLMs, fine-tuning, multi-agent systems, GPU infra, scalable pipelines, dashboards.",
            "price": 250000
        },

        # ============================================================
        # AI ENGINEERING — ADD-ONS
        # ============================================================

        {
            "sku": "DG-AI-A-001",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "Custom LLM Chatbot",
            "description": "Business-trained chatbot with embeddings and vector search.",
            "price": 12000
        },
        {
            "sku": "DG-AI-A-002",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "RAG Pipeline",
            "description": "Retrieval-Augmented Generation pipeline with documents, DBs, PDFs, etc.",
            "price": 18000
        },
        {
            "sku": "DG-AI-A-003",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "Fine-Tuned LLM",
            "description": "Fine-tune a GPT/LLaMA model on client data.",
            "price": 35000
        },
        {
            "sku": "DG-AI-A-004",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "Custom Embeddings Model",
            "description": "Domain-specific embeddings for search, matching, ranking.",
            "price": 25000
        },
        {
            "sku": "DG-AI-A-005",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "Vector Database Setup",
            "description": "Chroma, Pinecone, Weaviate, or Qdrant setup + indexing.",
            "price": 10000
        },
        {
            "sku": "DG-AI-A-006",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "PDF Ingest + AI Extraction",
            "description": "AI pipeline for PDF → text → embeddings → summaries.",
            "price": 9000
        },
        {
            "sku": "DG-AI-A-007",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "Speech-to-Text Engine",
            "description": "ASR engine using Whisper or custom speech pipeline.",
            "price": 15000
        },
        {
            "sku": "DG-AI-A-008",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "Text-to-Speech System",
            "description": "Voice generation, synthetic narration, multi-voice support.",
            "price": 14000
        },
        {
            "sku": "DG-AI-A-009",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "Image Classification Model",
            "description": "Train/test/validate image classifier for products, defects, or objects.",
            "price": 20000
        },
        {
            "sku": "DG-AI-A-010",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "Object Detection System",
            "description": "YOLO/Faster-RCNN detection model pipeline.",
            "price": 30000
        },
        {
            "sku": "DG-AI-A-011",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "AI Document Search",
            "description": "Search through 100k+ documents instantly with AI.",
            "price": 16000
        },
        {
            "sku": "DG-AI-A-012",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "AI Email Classifier",
            "description": "Auto-tag, sort, and prioritize email streams.",
            "price": 8000
        },
        {
            "sku": "DG-AI-A-013",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "AI CRM Assistant",
            "description": "AI auto-summarizes calls, messages, leads, and next steps.",
            "price": 14000
        },
        {
            "sku": "DG-AI-A-014",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "LLM-Powered Support System",
            "description": "Customer support automation with escalation routing.",
            "price": 18000
        },
        {
            "sku": "DG-AI-A-015",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "Recommendation Engine",
            "description": "Product, content, or user-based recommendation AI.",
            "price": 25000
        },
        {
            "sku": "DG-AI-A-016",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "Anomaly Detection",
            "description": "Detect fraud, system errors, or irregular behaviors.",
            "price": 22000
        },
        {
            "sku": "DG-AI-A-017",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "AI Forecasting Model",
            "description": "Time-series forecasting for sales, supply chain, etc.",
            "price": 27000
        },
        {
            "sku": "DG-AI-A-018",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "Multi-Agent AI System",
            "description": "Task agents that coordinate and collaborate.",
            "price": 40000
        },
        {
            "sku": "DG-AI-A-019",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "Vision + OCR Pipeline",
            "description": "Image → text → structured data pipeline.",
            "price": 15000
        },
        {
            "sku": "DG-AI-A-020",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "Custom Training Dataset Builder",
            "description": "Automated dataset cleaning, labeling, and formatting.",
            "price": 20000
        },
        {
            "sku": "DG-AI-A-021",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "AI Evaluation Suite",
            "description": "Benchmarking, hallucination tracking, regression testing.",
            "price": 18000
        },
        {
            "sku": "DG-AI-A-022",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "GPU Server Deployment",
            "description": "Install, configure, and deploy GPU inference servers.",
            "price": 35000
        },
        {
            "sku": "DG-AI-A-023",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "AI Automation Engine",
            "description": "Trigger-based workflows powered by LLMs.",
            "price": 18000
        },
        {
            "sku": "DG-AI-A-024",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "Live AI Monitoring Dashboard",
            "description": "Token usage, latency, success rate, drift detection.",
            "price": 20000
        },
        {
            "sku": "DG-AI-A-025",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "AI Safety Layer",
            "description": "Content filtering, moderation, safe prompting.",
            "price": 10000
        },
        {
            "sku": "DG-AI-A-026",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "Data Pipeline Hardening",
            "description": "Validation, anti-poisoning, anti-corruption protections.",
            "price": 16000
        },
        {
            "sku": "DG-AI-A-027",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "Fine-Tuned Vision Model",
            "description": "Train your own image model for classification or detection.",
            "price": 50000
        },
        {
            "sku": "DG-AI-A-028",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "Synthetic Data Generator",
            "description": "AI generates synthetic training data safely.",
            "price": 30000
        },
        {
            "sku": "DG-AI-A-029",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "LLM Custom Tools API",
            "description": "Custom function calling for business operations.",
            "price": 12000
        },
        {
            "sku": "DG-AI-A-030",
            "category": "AI Engineering",
            "type": "Add-On",
            "name": "AI-Powered Search Engine",
            "description": "Semantic search + keyword hybrid search.",
            "price": 18000
        },

    ]

    batch_insert(items)


def seed_mobile():
    items = [

        # ============================================================
        # MOBILE — TIERS
        # ============================================================
        {
            "sku": "DG-MOB-T-001",
            "category": "Mobile Apps",
            "type": "Tier",
            "name": "Mobile Tier 1 - Starter App",
            "description": "Basic iOS/Android app with 3–5 screens, API integration, auth, navigation, and settings.",
            "price": 20000
        },
        {
            "sku": "DG-MOB-T-002",
            "category": "Mobile Apps",
            "type": "Tier",
            "name": "Mobile Tier 2 - Business App",
            "description": "Everything in Tier 1 + push notifications, offline mode, camera support, advanced UI, dashboards.",
            "price": 60000
        },
        {
            "sku": "DG-MOB-T-003",
            "category": "Mobile Apps",
            "type": "Tier",
            "name": "Mobile Tier 3 - Enterprise Mobile Platform",
            "description": "Full enterprise app: multi-role, databases, AI, payments, chat, real-time sync, cloud storage.",
            "price": 150000
        },

        # ============================================================
        # MOBILE — ADD-ONS
        # ============================================================

        {
            "sku": "DG-MOB-A-001",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "Push Notifications",
            "description": "iOS/Android push notifications with segmentation.",
            "price": 5000
        },
        {
            "sku": "DG-MOB-A-002",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "In-App Purchases",
            "description": "Subscription or one-time purchase flow.",
            "price": 9000
        },
        {
            "sku": "DG-MOB-A-003",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "App Store + Play Store Setup",
            "description": "Publishing, screenshots, listing optimization.",
            "price": 3500
        },
        {
            "sku": "DG-MOB-A-004",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "Offline Mode",
            "description": "Local caching, queueing, background sync.",
            "price": 8000
        },
        {
            "sku": "DG-MOB-A-005",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "Real-Time Chat",
            "description": "WebSockets chat system with typing, images, groups.",
            "price": 12000
        },
        {
            "sku": "DG-MOB-A-006",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "GPS & Mapping",
            "description": "Geolocation, map markers, route tracking.",
            "price": 7000
        },
        {
            "sku": "DG-MOB-A-007",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "Geofencing",
            "description": "Trigger actions when entering/exiting locations.",
            "price": 6500
        },
        {
            "sku": "DG-MOB-A-008",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "Camera Capture & Processing",
            "description": "Camera UI, photo/video capture, compression.",
            "price": 9000
        },
        {
            "sku": "DG-MOB-A-009",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "AI Image Analysis",
            "description": "Mobile-friendly AI for labeling, detection, OCR.",
            "price": 15000
        },
        {
            "sku": "DG-MOB-A-010",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "Social Login",
            "description": "Login with Google, Apple, Facebook.",
            "price": 4500
        },
        {
            "sku": "DG-MOB-A-011",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "User Profile System",
            "description": "Editable profiles, avatars, privacy settings.",
            "price": 6500
        },
        {
            "sku": "DG-MOB-A-012",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "File Upload System",
            "description": "Upload photos, videos, or documents.",
            "price": 8000
        },
        {
            "sku": "DG-MOB-A-013",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "AI Chat Assistant",
            "description": "In-app AI assistant powered by LLMs.",
            "price": 12000
        },
        {
            "sku": "DG-MOB-A-014",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "Multi-Language Support",
            "description": "Localization, translation, language switching.",
            "price": 6000
        },
        {
            "sku": "DG-MOB-A-015",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "Analytics Dashboard",
            "description": "Mobile analytics: retention, funnels, usage.",
            "price": 8500
        },
        {
            "sku": "DG-MOB-A-016",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "Custom Animations",
            "description": "Lottie, GSAP, interactions, page transitions.",
            "price": 7500
        },
        {
            "sku": "DG-MOB-A-017",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "Mobile-Commerce System",
            "description": "Products, cart, checkout, order tracking.",
            "price": 15000
        },
        {
            "sku": "DG-MOB-A-018",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "AR Features",
            "description": "AR overlays using ARCore/ARKit.",
            "price": 20000
        },
        {
            "sku": "DG-MOB-A-019",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "Video Editor",
            "description": "Mobile video trimming, filters, text overlays.",
            "price": 25000
        },
        {
            "sku": "DG-MOB-A-020",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "Voice Commands",
            "description": "Speech-triggered actions.",
            "price": 8000
        },
        {
            "sku": "DG-MOB-A-021",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "Background Services",
            "description": "Background tasks, sensors, sync jobs.",
            "price": 10000
        },
        {
            "sku": "DG-MOB-A-022",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "QR/Barcode Scanner",
            "description": "Scanner integration with parsing.",
            "price": 3500
        },
        {
            "sku": "DG-MOB-A-023",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "Appointment Booking System",
            "description": "Scheduling, availability, cancellations.",
            "price": 9000
        },
        {
            "sku": "DG-MOB-A-024",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "Rewards/Loyalty Program",
            "description": "Points, rewards, app engagement mechanics.",
            "price": 8000
        },
        {
            "sku": "DG-MOB-A-025",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "Push Notification Campaign Engine",
            "description": "Segment users and schedule blasts.",
            "price": 6500
        },
        {
            "sku": "DG-MOB-A-026",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "Mobile AI Vision Kit",
            "description": "Detect labels, faces, objects in the camera live feed.",
            "price": 25000
        },
        {
            "sku": "DG-MOB-A-027",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "Secure Vault Storage",
            "description": "Encrypted storage for documents, keys, secrets.",
            "price": 7000
        },
        {
            "sku": "DG-MOB-A-028",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "Multi-Tenant Mobile Shell",
            "description": "White-labeled version for multiple businesses.",
            "price": 20000
        },
        {
            "sku": "DG-MOB-A-029",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "AI Personalization Engine",
            "description": "Personalized app content using AI predictions.",
            "price": 18000
        },
        {
            "sku": "DG-MOB-A-030",
            "category": "Mobile Apps",
            "type": "Add-On",
            "name": "Advanced App Security",
            "description": "Anti-tampering, encryption, jailbreak/root detection.",
            "price": 15000
        },

    ]

    batch_insert(items)


def seed_design():
    items = [

        # ============================================================
        # DESIGN — TIERED PACKAGES
        # ============================================================
        {
            "sku": "DG-DSN-T-001",
            "category": "Design",
            "type": "Tier",
            "name": "Design Tier 1 - Branding Essentials",
            "description": "Logo, color palette, typography, favicon set, brand basics.",
            "price": 2500
        },
        {
            "sku": "DG-DSN-T-002",
            "category": "Design",
            "type": "Tier",
            "name": "Design Tier 2 - Full Brand Kit",
            "description": "Everything in Tier 1 + full brand system, pattern library, social kit, brand guide PDF.",
            "price": 7000
        },
        {
            "sku": "DG-DSN-T-003",
            "category": "Design",
            "type": "Tier",
            "name": "Design Tier 3 - Product UI/UX System",
            "description": "Full UI/UX system, wireframes, prototypes, components, Figma design system, accessibility guidelines.",
            "price": 20000
        },

        # ============================================================
        # DESIGN — ADD-ONS
        # ============================================================
        {
            "sku": "DG-DSN-A-001",
            "category": "Design",
            "type": "Add-On",
            "name": "Logo Design",
            "description": "3 concept logos + revisions.",
            "price": 600
        },
        {
            "sku": "DG-DSN-A-002",
            "category": "Design",
            "type": "Add-On",
            "name": "Color Palette",
            "description": "Full primary, secondary, accent palette.",
            "price": 300
        },
        {
            "sku": "DG-DSN-A-003",
            "category": "Design",
            "type": "Add-On",
            "name": "Typography Kit",
            "description": "Heading/body font pairings, spacing, hierarchy.",
            "price": 300
        },
        {
            "sku": "DG-DSN-A-004",
            "category": "Design",
            "type": "Add-On",
            "name": "Figma Wireframes",
            "description": "Wireframes for pages or screens.",
            "price": 900
        },
        {
            "sku": "DG-DSN-A-005",
            "category": "Design",
            "type": "Add-On",
            "name": "Figma Prototype",
            "description": "Interactive click-through prototype.",
            "price": 1200
        },
        {
            "sku": "DG-DSN-A-006",
            "category": "Design",
            "type": "Add-On",
            "name": "Design System – Components",
            "description": "Buttons, fields, cards, forms, UI elements.",
            "price": 3500
        },
        {
            "sku": "DG-DSN-A-007",
            "category": "Design",
            "type": "Add-On",
            "name": "Design System – Full Library",
            "description": "Spacing, icons, tokens, grids, interactions.",
            "price": 9000
        },
        {
            "sku": "DG-DSN-A-008",
            "category": "Design",
            "type": "Add-On",
            "name": "UX Research Pack",
            "description": "User flows, heuristics, personas.",
            "price": 2500
        },
        {
            "sku": "DG-DSN-A-009",
            "category": "Design",
            "type": "Add-On",
            "name": "UI Redesign (Per Page)",
            "description": "Modernize visuals for an existing screen or webpage.",
            "price": 500
        },
        {
            "sku": "DG-DSN-A-010",
            "category": "Design",
            "type": "Add-On",
            "name": "Illustration Pack",
            "description": "Custom illustrations or vector scenes.",
            "price": 1500
        },
        {
            "sku": "DG-DSN-A-011",
            "category": "Design",
            "type": "Add-On",
            "name": "3D Render – Basic",
            "description": "Single 3D object model render.",
            "price": 2000
        },
        {
            "sku": "DG-DSN-A-012",
            "category": "Design",
            "type": "Add-On",
            "name": "3D Render – Advanced Scene",
            "description": "Full 3D scene with lighting + animation.",
            "price": 6000
        },
        {
            "sku": "DG-DSN-A-013",
            "category": "Design",
            "type": "Add-On",
            "name": "Custom Icon Set",
            "description": "Set of 20+ icons in brand style.",
            "price": 1200
        },
        {
            "sku": "DG-DSN-A-014",
            "category": "Design",
            "type": "Add-On",
            "name": "Motion Design Pack",
            "description": "Animated elements, transitions, micro-interactions.",
            "price": 3500
        },
        {
            "sku": "DG-DSN-A-015",
            "category": "Design",
            "type": "Add-On",
            "name": "Landing Page Design",
            "description": "Full landing page layout design.",
            "price": 1500
        },
        {
            "sku": "DG-DSN-A-016",
            "category": "Design",
            "type": "Add-On",
            "name": "Mobile App UI Kit",
            "description": "Full UI kit for iOS + Android.",
            "price": 4500
        },
        {
            "sku": "DG-DSN-A-017",
            "category": "Design",
            "type": "Add-On",
            "name": "Web App Dashboard Design",
            "description": "Modern dashboard charts, tables, KPIs.",
            "price": 3800
        },
        {
            "sku": "DG-DSN-A-018",
            "category": "Design",
            "type": "Add-On",
            "name": "Email Template Designs",
            "description": "Branded email layouts for marketing or notifications.",
            "price": 700
        },
        {
            "sku": "DG-DSN-A-019",
            "category": "Design",
            "type": "Add-On",
            "name": "Presentation Deck",
            "description": "Branded pitch deck or investor slides.",
            "price": 1600
        },
        {
            "sku": "DG-DSN-A-020",
            "category": "Design",
            "type": "Add-On",
            "name": "Print Collateral",
            "description": "Flyers, business cards, brochures, menus.",
            "price": 900
        },
        {
            "sku": "DG-DSN-A-021",
            "category": "Design",
            "type": "Add-On",
            "name": "Brand Guide PDF",
            "description": "Brand rules: logo, spacing, color, typography.",
            "price": 1500
        },
        {
            "sku": "DG-DSN-A-022",
            "category": "Design",
            "type": "Add-On",
            "name": "App Icon Pack",
            "description": "iOS/Android icon sets in all sizes.",
            "price": 450
        },
        {
            "sku": "DG-DSN-A-023",
            "category": "Design",
            "type": "Add-On",
            "name": "Social Media Kit",
            "description": "Profile/header images + templates.",
            "price": 750
        },
        {
            "sku": "DG-DSN-A-024",
            "category": "Design",
            "type": "Add-On",
            "name": "UI Animation Library",
            "description": "Reusable interaction animations for dev teams.",
            "price": 3000
        },
        {
            "sku": "DG-DSN-A-025",
            "category": "Design",
            "type": "Add-On",
            "name": "Brand Mascot Illustration",
            "description": "Custom character/mascot in multiple poses.",
            "price": 2000
        },
        {
            "sku": "DG-DSN-A-026",
            "category": "Design",
            "type": "Add-On",
            "name": "UX Testing Report",
            "description": "Usability test + findings + improvement plan.",
            "price": 2500
        },
        {
            "sku": "DG-DSN-A-027",
            "category": "Design",
            "type": "Add-On",
            "name": "Style Tile",
            "description": "Snapshot of brand aesthetic for alignment.",
            "price": 400
        },
        {
            "sku": "DG-DSN-A-028",
            "category": "Design",
            "type": "Add-On",
            "name": "Flow Diagrams",
            "description": "User flows, journeys, system diagrams.",
            "price": 900
        },
        {
            "sku": "DG-DSN-A-029",
            "category": "Design",
            "type": "Add-On",
            "name": "Character Sheets (Games/Apps)",
            "description": "Turnarounds, poses, expressions for characters.",
            "price": 1800
        },
        {
            "sku": "DG-DSN-A-030",
            "category": "Design",
            "type": "Add-On",
            "name": "High-Fidelity Screen",
            "description": "Pixel-perfect UI design per screen.",
            "price": 350
        },

    ]

    batch_insert(items)


def seed_media():
    items = [

        # ============================================================
        # MEDIA — TIERS
        # ============================================================
        {
            "sku": "DG-MED-T-001",
            "category": "Media",
            "type": "Tier",
            "name": "Media Tier 1 - Essential Media Pack",
            "description": "Basic video edits, audio cleanup, image corrections, simple motion graphics.",
            "price": 3000
        },
        {
            "sku": "DG-MED-T-002",
            "category": "Media",
            "type": "Tier",
            "name": "Media Tier 2 - Content Production Suite",
            "description": "Everything in Tier 1 + full video production, multi-camera editing, VFX light, animations.",
            "price": 12000
        },
        {
            "sku": "DG-MED-T-003",
            "category": "Media",
            "type": "Tier",
            "name": "Media Tier 3 - Studio Level Production",
            "description": "High-end film-grade production: 3D animation, heavy VFX, color grading, full audio engineering.",
            "price": 40000
        },

        # ============================================================
        # MEDIA — ADD-ONS
        # ============================================================

        {
            "sku": "DG-MED-A-001",
            "category": "Media",
            "type": "Add-On",
            "name": "Video Editing",
            "description": "Cutting, arranging, trimming, timeline edits.",
            "price": 500
        },
        {
            "sku": "DG-MED-A-002",
            "category": "Media",
            "type": "Add-On",
            "name": "Color Correction",
            "description": "Exposure, contrast, balance adjustments.",
            "price": 400
        },
        {
            "sku": "DG-MED-A-003",
            "category": "Media",
            "type": "Add-On",
            "name": "Color Grading (Cinematic)",
            "description": "Film looks + LUT application.",
            "price": 1200
        },
        {
            "sku": "DG-MED-A-004",
            "category": "Media",
            "type": "Add-On",
            "name": "Motion Graphics",
            "description": "Text animations, lower thirds, transitions.",
            "price": 700
        },
        {
            "sku": "DG-MED-A-005",
            "category": "Media",
            "type": "Add-On",
            "name": "3D Animation (Basic)",
            "description": "Object animation in a simple scene.",
            "price": 2000
        },
        {
            "sku": "DG-MED-A-006",
            "category": "Media",
            "type": "Add-On",
            "name": "3D Animation (Advanced)",
            "description": "Character animation, simulated physics, complex scenes.",
            "price": 6000
        },
        {
            "sku": "DG-MED-A-007",
            "category": "Media",
            "type": "Add-On",
            "name": "VFX Light",
            "description": "Particles, lighting effects, basic compositing.",
            "price": 1500
        },
        {
            "sku": "DG-MED-A-008",
            "category": "Media",
            "type": "Add-On",
            "name": "Heavy VFX",
            "description": "Tracking, masking, simulations, multi-layer effects.",
            "price": 6000
        },
        {
            "sku": "DG-MED-A-009",
            "category": "Media",
            "type": "Add-On",
            "name": "Sound Design",
            "description": "SFX, foley, environmental audio.",
            "price": 1000
        },
        {
            "sku": "DG-MED-A-010",
            "category": "Media",
            "type": "Add-On",
            "name": "Music Scoring",
            "description": "Original music composed for video.",
            "price": 2500
        },
        {
            "sku": "DG-MED-A-011",
            "category": "Media",
            "type": "Add-On",
            "name": "Podcast Editing",
            "description": "Audio cleanup, leveling, intro/outro.",
            "price": 700
        },
        {
            "sku": "DG-MED-A-012",
            "category": "Media",
            "type": "Add-On",
            "name": "Voiceover Recording",
            "description": "Professional voice narration.",
            "price": 800
        },
        {
            "sku": "DG-MED-A-013",
            "category": "Media",
            "type": "Add-On",
            "name": "Scriptwriting",
            "description": "Script for commercial, promo, or explainer.",
            "price": 1200
        },
        {
            "sku": "DG-MED-A-014",
            "category": "Media",
            "type": "Add-On",
            "name": "Image Retouching",
            "description": "Skin cleanup, object removal, enhancements.",
            "price": 300
        },
        {
            "sku": "DG-MED-A-015",
            "category": "Media",
            "type": "Add-On",
            "name": "Photo Manipulation",
            "description": "Composite images, surreal edits, advanced cleanup.",
            "price": 800
        },
        {
            "sku": "DG-MED-A-016",
            "category": "Media",
            "type": "Add-On",
            "name": "360° Video Processing",
            "description": "Stitching + stabilization for VR-ready video.",
            "price": 2500
        },
        {
            "sku": "DG-MED-A-017",
            "category": "Media",
            "type": "Add-On",
            "name": "Drone Footage Editing",
            "description": "Cinematic drone color + stabilization.",
            "price": 1200
        },
        {
            "sku": "DG-MED-A-018",
            "category": "Media",
            "type": "Add-On",
            "name": "Green Screen Remove",
            "description": "Keying, edge cleanup, spill removal.",
            "price": 700
        },
        {
            "sku": "DG-MED-A-019",
            "category": "Media",
            "type": "Add-On",
            "name": "Video Compression Pack",
            "description": "Export for multiple platforms with optimal quality.",
            "price": 300
        },
        {
            "sku": "DG-MED-A-020",
            "category": "Media",
            "type": "Add-On",
            "name": "Cinematic Trailer Edit",
            "description": "Epic, dramatic trailer-style edit.",
            "price": 3500
        },
        {
            "sku": "DG-MED-A-021",
            "category": "Media",
            "type": "Add-On",
            "name": "Short Social Video Pack",
            "description": "10–20 short clips optimized for TikTok/IG.",
            "price": 2000
        },
        {
            "sku": "DG-MED-A-022",
            "category": "Media",
            "type": "Add-On",
            "name": "GIF Animation Pack",
            "description": "Branded GIFs for marketing.",
            "price": 600
        },
        {
            "sku": "DG-MED-A-023",
            "category": "Media",
            "type": "Add-On",
            "name": "Thumbnail Design",
            "description": "High-click-through thumbnails for videos.",
            "price": 200
        },
        {
            "sku": "DG-MED-A-024",
            "category": "Media",
            "type": "Add-On",
            "name": "Narrative Voice Scripting",
            "description": "AI or human voice script writing.",
            "price": 900
        },
        {
            "sku": "DG-MED-A-025",
            "category": "Media",
            "type": "Add-On",
            "name": "Livestream Graphics Pack",
            "description": "Alerts, transitions, screen overlays.",
            "price": 750
        },
        {
            "sku": "DG-MED-A-026",
            "category": "Media",
            "type": "Add-On",
            "name": "Studio Intro Animation",
            "description": "Fully custom YouTube/brand intro.",
            "price": 1500
        },
        {
            "sku": "DG-MED-A-027",
            "category": "Media",
            "type": "Add-On",
            "name": "AI Video Upscaling",
            "description": "Enhance low-quality videos using AI.",
            "price": 700
        },
        {
            "sku": "DG-MED-A-028",
            "category": "Media",
            "type": "Add-On",
            "name": "AI Image Restoration",
            "description": "Repair damaged or low-res images.",
            "price": 900
        },
        {
            "sku": "DG-MED-A-029",
            "category": "Media",
            "type": "Add-On",
            "name": "SFX/Audio Foley Pack",
            "description": "Custom sound effects recorded for scenes.",
            "price": 1400
        },
        {
            "sku": "DG-MED-A-030",
            "category": "Media",
            "type": "Add-On",
            "name": "Multi-Camera Sync & Edit",
            "description": "Sync and edit multi-angle video shoots.",
            "price": 2000
        },

    ]

    batch_insert(items)


def seed_marketing():
    items = [

        # ============================================================
        # MARKETING — TIERS
        # ============================================================
        {
            "sku": "DG-MKT-T-001",
            "category": "Marketing",
            "type": "Tier",
            "name": "Marketing Tier 1 - Local Starter",
            "description": "Google Business optimization, small SEO setup, social branding, local presence improvements.",
            "price": 2500
        },
        {
            "sku": "DG-MKT-T-002",
            "category": "Marketing",
            "type": "Tier",
            "name": "Marketing Tier 2 - Growth Package",
            "description": "Everything in Tier 1 + monthly content, SEO campaigns, ads setup, analytics, email funnels.",
            "price": 9000
        },
        {
            "sku": "DG-MKT-T-003",
            "category": "Marketing",
            "type": "Tier",
            "name": "Marketing Tier 3 - Full Funnel Conversion System",
            "description": "Everything in Tier 1 & 2 + advanced funnels, audience segmentation, retargeting, CRO, multi-channel automations.",
            "price": 25000
        },

        # ============================================================
        # MARKETING — ADD-ONS
        # ============================================================

        {
            "sku": "DG-MKT-A-001",
            "category": "Marketing",
            "type": "Add-On",
            "name": "SEO Audit",
            "description": "Full technical + on-page SEO audit.",
            "price": 800
        },
        {
            "sku": "DG-MKT-A-002",
            "category": "Marketing",
            "type": "Add-On",
            "name": "Keyword Research",
            "description": "Keyword strategy + competition mapping.",
            "price": 600
        },
        {
            "sku": "DG-MKT-A-003",
            "category": "Marketing",
            "type": "Add-On",
            "name": "SEO Optimization (Per Page)",
            "description": "Optimize title, meta, headings, structure.",
            "price": 250
        },
        {
            "sku": "DG-MKT-A-004",
            "category": "Marketing",
            "type": "Add-On",
            "name": "Local SEO Setup",
            "description": "Business listings, citations, local ranking.",
            "price": 1200
        },
        {
            "sku": "DG-MKT-A-005",
            "category": "Marketing",
            "type": "Add-On",
            "name": "Google Business Profile Optimization",
            "description": "Photo uploads, posts, NAP consistency.",
            "price": 500
        },
        {
            "sku": "DG-MKT-A-006",
            "category": "Marketing",
            "type": "Add-On",
            "name": "Social Media Branding Pack",
            "description": "Profile, cover, highlight icons, branding.",
            "price": 700
        },
        {
            "sku": "DG-MKT-A-007",
            "category": "Marketing",
            "type": "Add-On",
            "name": "Social Media Content (10 posts)",
            "description": "Branded static + animated posts.",
            "price": 900
        },
        {
            "sku": "DG-MKT-A-008",
            "category": "Marketing",
            "type": "Add-On",
            "name": "Short Form Video Ads",
            "description": "TikTok/IG/Reels ads pack.",
            "price": 1500
        },
        {
            "sku": "DG-MKT-A-009",
            "category": "Marketing",
            "type": "Add-On",
            "name": "Copywriting (Per Page)",
            "description": "Brand voice + persuasive copy per page.",
            "price": 300
        },
        {
            "sku": "DG-MKT-A-010",
            "category": "Marketing",
            "type": "Add-On",
            "name": "Content Calendar (1 Month)",
            "description": "30-day posting + content strategy.",
            "price": 700
        },
        {
            "sku": "DG-MKT-A-011",
            "category": "Marketing",
            "type": "Add-On",
            "name": "Google Ads Setup",
            "description": "Keyword targeting, ad groups, setup.",
            "price": 1500
        },
        {
            "sku": "DG-MKT-A-012",
            "category": "Marketing",
            "type": "Add-On",
            "name": "Facebook/IG Ads Setup",
            "description": "Audiences, targeting, ad creative.",
            "price": 1200
        },
        {
            "sku": "DG-MKT-A-013",
            "category": "Marketing",
            "type": "Add-On",
            "name": "Remarketing Setup",
            "description": "Pixel installation + audience segmentation.",
            "price": 900
        },
        {
            "sku": "DG-MKT-A-014",
            "category": "Marketing",
            "type": "Add-On",
            "name": "Email Marketing Funnel",
            "description": "3–6 email automation sequences.",
            "price": 2000
        },
        {
            "sku": "DG-MKT-A-015",
            "category": "Marketing",
            "type": "Add-On",
            "name": "Newsletter Writing (1 month)",
            "description": "Weekly newsletters (4 emails).",
            "price": 600
        },
        {
            "sku": "DG-MKT-A-016",
            "category": "Marketing",
            "type": "Add-On",
            "name": "Landing Page CRO Audit",
            "description": "Conversion review + improvements.",
            "price": 700
        },
        {
            "sku": "DG-MKT-A-017",
            "category": "Marketing",
            "type": "Add-On",
            "name": "Full Funnel Setup",
            "description": "Lead magnet → nurture → conversion.",
            "price": 4500
        },
        {
            "sku": "DG-MKT-A-018",
            "category": "Marketing",
            "type": "Add-On",
            "name": "Lead Generation System",
            "description": "Lead capture + scoring + CRM sync.",
            "price": 3000
        },
        {
            "sku": "DG-MKT-A-019",
            "category": "Marketing",
            "type": "Add-On",
            "name": "Brand Voice Guide",
            "description": "Tone, structure, examples, vocabulary.",
            "price": 500
        },
        {
            "sku": "DG-MKT-A-020",
            "category": "Marketing",
            "type": "Add-On",
            "name": "Influencer Outreach Pack",
            "description": "Script templates + prospect list.",
            "price": 600
        },
        {
            "sku": "DG-MKT-A-021",
            "category": "Marketing",
            "type": "Add-On",
            "name": "SEO Blog Posts (x4)",
            "description": "4 fully optimized blog articles.",
            "price": 800
        },
        {
            "sku": "DG-MKT-A-022",
            "category": "Marketing",
            "type": "Add-On",
            "name": "Reputation Management",
            "description": "Review monitoring + response writing.",
            "price": 900
        },
        {
            "sku": "DG-MKT-A-023",
            "category": "Marketing",
            "type": "Add-On",
            "name": "Competitor Analysis",
            "description": "Competitor metrics + strategy document.",
            "price": 750
        },
        {
            "sku": "DG-MKT-A-024",
            "category": "Marketing",
            "type": "Add-On",
            "name": "Sales Script / Pitch Copywriting",
            "description": "Phone/email/DM scripts for conversions.",
            "price": 750
        },
        {
            "sku": "DG-MKT-A-025",
            "category": "Marketing",
            "type": "Add-On",
            "name": "Marketing Automation Setup",
            "description": "HubSpot/MailChimp/Zapier automations.",
            "price": 2000
        },
        {
            "sku": "DG-MKT-A-026",
            "category": "Marketing",
            "type": "Add-On",
            "name": "Analytics Dashboard",
            "description": "Google Analytics 4 + custom dashboard.",
            "price": 1400
        },
        {
            "sku": "DG-MKT-A-027",
            "category": "Marketing",
            "type": "Add-On",
            "name": "Retargeting Creative Pack",
            "description": "Ads optimized for people who visited site.",
            "price": 1200
        },
        {
            "sku": "DG-MKT-A-028",
            "category": "Marketing",
            "type": "Add-On",
            "name": "Funnel A/B Testing",
            "description": "Split-testing pages, ads, offers.",
            "price": 1500
        },
        {
            "sku": "DG-MKT-A-029",
            "category": "Marketing",
            "type": "Add-On",
            "name": "Product Launch Campaign",
            "description": "Full campaign for launching a product.",
            "price": 5000
        },
        {
            "sku": "DG-MKT-A-030",
            "category": "Marketing",
            "type": "Add-On",
            "name": "Monthly Marketing Mgmt (Retainer)",
            "description": "Ongoing monthly management and strategy.",
            "price": 2500
        },

    ]

    batch_insert(items)


def seed_content():
    items = [

        # ============================================================
        # CONTENT — TIERS
        # ============================================================
        {
            "sku": "DG-CNT-T-001",
            "category": "Content",
            "type": "Tier",
            "name": "Content Tier 1 - Starter Writing Pack",
            "description": "Basic business writing: landing page copy, about page, simple descriptions.",
            "price": 1200
        },
        {
            "sku": "DG-CNT-T-002",
            "category": "Content",
            "type": "Tier",
            "name": "Content Tier 2 - Business Content Suite",
            "description": "Everything in Tier 1 + blog posts, email content, SEO writing, product descriptions.",
            "price": 4500
        },
        {
            "sku": "DG-CNT-T-003",
            "category": "Content",
            "type": "Tier",
            "name": "Content Tier 3 - Enterprise Editorial System",
            "description": "Tier 1 & 2 + whitepapers, technical docs, scripts, long-form articles, content strategy.",
            "price": 15000
        },

        # ============================================================
        # CONTENT — ADD-ONS
        # ============================================================

        {
            "sku": "DG-CNT-A-001",
            "category": "Content",
            "type": "Add-On",
            "name": "Landing Page Copywriting",
            "description": "High-converting landing page text.",
            "price": 450
        },
        {
            "sku": "DG-CNT-A-002",
            "category": "Content",
            "type": "Add-On",
            "name": "Home Page Copy",
            "description": "Homepage content optimized for conversions.",
            "price": 400
        },
        {
            "sku": "DG-CNT-A-003",
            "category": "Content",
            "type": "Add-On",
            "name": "About Page Copy",
            "description": "Professional story-driven brand writing.",
            "price": 350
        },
        {
            "sku": "DG-CNT-A-004",
            "category": "Content",
            "type": "Add-On",
            "name": "Services Page Copywriting",
            "description": "Persuasive descriptions of business services.",
            "price": 500
        },
        {
            "sku": "DG-CNT-A-005",
            "category": "Content",
            "type": "Add-On",
            "name": "SEO Blog Post",
            "description": "1000-word SEO blog article.",
            "price": 250
        },
        {
            "sku": "DG-CNT-A-006",
            "category": "Content",
            "type": "Add-On",
            "name": "Long-Form SEO Article",
            "description": "2000–3000 word content-rich article.",
            "price": 600
        },
        {
            "sku": "DG-CNT-A-007",
            "category": "Content",
            "type": "Add-On",
            "name": "Product Descriptions (x5)",
            "description": "SEO product descriptions for eCommerce.",
            "price": 300
        },
        {
            "sku": "DG-CNT-A-008",
            "category": "Content",
            "type": "Add-On",
            "name": "Ad Copy (Google/Facebook)",
            "description": "Short-form ads optimized for CTR.",
            "price": 250
        },
        {
            "sku": "DG-CNT-A-009",
            "category": "Content",
            "type": "Add-On",
            "name": "Email Newsletter",
            "description": "Full brand newsletter email.",
            "price": 150
        },
        {
            "sku": "DG-CNT-A-010",
            "category": "Content",
            "type": "Add-On",
            "name": "Email Funnel (5 emails)",
            "description": "Conversion-oriented email sequence.",
            "price": 900
        },
        {
            "sku": "DG-CNT-A-011",
            "category": "Content",
            "type": "Add-On",
            "name": "Sales Page Copywriting",
            "description": "Long-form sales page or offer page.",
            "price": 1200
        },
        {
            "sku": "DG-CNT-A-012",
            "category": "Content",
            "type": "Add-On",
            "name": "Press Release",
            "description": "Industry-standard press release writing.",
            "price": 600
        },
        {
            "sku": "DG-CNT-A-013",
            "category": "Content",
            "type": "Add-On",
            "name": "Technical Documentation",
            "description": "User guides, API docs, developer docs.",
            "price": 1500
        },
        {
            "sku": "DG-CNT-A-014",
            "category": "Content",
            "type": "Add-On",
            "name": "Whitepaper Writing",
            "description": "Full professional whitepaper.",
            "price": 2500
        },
        {
            "sku": "DG-CNT-A-015",
            "category": "Content",
            "type": "Add-On",
            "name": "Case Study",
            "description": "Customer success case study.",
            "price": 1200
        },
        {
            "sku": "DG-CNT-A-016",
            "category": "Content",
            "type": "Add-On",
            "name": "UX Microcopy",
            "description": "Buttons, tooltips, error messages, flows.",
            "price": 400
        },
        {
            "sku": "DG-CNT-A-017",
            "category": "Content",
            "type": "Add-On",
            "name": "Onboarding Content",
            "description": "Messages + tooltips for new users.",
            "price": 800
        },
        {
            "sku": "DG-CNT-A-018",
            "category": "Content",
            "type": "Add-On",
            "name": "Scriptwriting (Short Video)",
            "description": "Script for promo, ad, explainer.",
            "price": 450
        },
        {
            "sku": "DG-CNT-A-019",
            "category": "Content",
            "type": "Add-On",
            "name": "Scriptwriting (Long Video)",
            "description": "Narrative or educational script.",
            "price": 900
        },
        {
            "sku": "DG-CNT-A-020",
            "category": "Content",
            "type": "Add-On",
            "name": "Brand Story Writing",
            "description": "Full brand origin + story copy.",
            "price": 700
        },
        {
            "sku": "DG-CNT-A-021",
            "category": "Content",
            "type": "Add-On",
            "name": "Product Brochure Content",
            "description": "Brochure or pamphlet writing.",
            "price": 500
        },
        {
            "sku": "DG-CNT-A-022",
            "category": "Content",
            "type": "Add-On",
            "name": "Content Strategy Plan",
            "description": "Full business content plan + roadmap.",
            "price": 1500
        },
        {
            "sku": "DG-CNT-A-023",
            "category": "Content",
            "type": "Add-On",
            "name": "FAQ Writing",
            "description": "Frequently asked questions + answers.",
            "price": 300
        },
        {
            "sku": "DG-CNT-A-024",
            "category": "Content",
            "type": "Add-On",
            "name": "Legal Policy Content",
            "description": "ToS + Privacy Policy + Cookie Policy text.",
            "price": 900
        },
        {
            "sku": "DG-CNT-A-025",
            "category": "Content",
            "type": "Add-On",
            "name": "Product Manual Writing",
            "description": "User instructions + troubleshooting.",
            "price": 800
        },
        {
            "sku": "DG-CNT-A-026",
            "category": "Content",
            "type": "Add-On",
            "name": "Pitch Deck Copy",
            "description": "Investor pitch copywriting.",
            "price": 800
        },
        {
            "sku": "DG-CNT-A-027",
            "category": "Content",
            "type": "Add-On",
            "name": "Webinar Script Pack",
            "description": "Full webinar script + breakdown.",
            "price": 1500
        },
        {
            "sku": "DG-CNT-A-028",
            "category": "Content",
            "type": "Add-On",
            "name": "Podcast Script",
            "description": "Podcast episode structure + dialogue.",
            "price": 600
        },
        {
            "sku": "DG-CNT-A-029",
            "category": "Content",
            "type": "Add-On",
            "name": "eBook Writing",
            "description": "Short eBook or lead magnet writing.",
            "price": 2000
        },
        {
            "sku": "DG-CNT-A-030",
            "category": "Content",
            "type": "Add-On",
            "name": "Monthly Content Writing (Retainer)",
            "description": "Ongoing writing: blogs + emails + updates.",
            "price": 2000
        },

    ]

    batch_insert(items)


def seed_hosting():
    items = [

        # ============================================================
        # HOSTING & MAINTENANCE — TIERS
        # ============================================================
        {
            "sku": "DG-HST-T-001",
            "category": "Hosting",
            "type": "Tier",
            "name": "Hosting Tier 1 - Standard Hosting",
            "description": "Managed hosting; uptime monitoring; SSL; weekly backups; minor updates.",
            "price": 1500
        },
        {
            "sku": "DG-HST-T-002",
            "category": "Hosting",
            "type": "Tier",
            "name": "Hosting Tier 2 - Business Hosting",
            "description": "Everything in Tier 1 + monthly updates; security scans; priority support.",
            "price": 3800
        },
        {
            "sku": "DG-HST-T-003",
            "category": "Hosting",
            "type": "Tier",
            "name": "Hosting Tier 3 - Enterprise Hosting",
            "description": "Everything in Tier 1 & 2 + load balancing; staging environment; dedicated resources.",
            "price": 9000
        },

        # ============================================================
        # HOSTING & MAINTENANCE — ADD-ONS
        # ============================================================

        {
            "sku": "DG-HST-A-001",
            "category": "Hosting",
            "type": "Add-On",
            "name": "Domain Management",
            "description": "DNS, renewals, configuration handled.",
            "price": 200
        },
        {
            "sku": "DG-HST-A-002",
            "category": "Hosting",
            "type": "Add-On",
            "name": "Email Hosting Setup",
            "description": "Microsoft 365 / Google Workspace email setup.",
            "price": 350
        },
        {
            "sku": "DG-HST-A-003",
            "category": "Hosting",
            "type": "Add-On",
            "name": "SSL Installation",
            "description": "Secure HTTPS setup and renewal.",
            "price": 150
        },
        {
            "sku": "DG-HST-A-004",
            "category": "Hosting",
            "type": "Add-On",
            "name": "Daily Backups",
            "description": "Daily snapshots stored and managed.",
            "price": 500
        },
        {
            "sku": "DG-HST-A-005",
            "category": "Hosting",
            "type": "Add-On",
            "name": "Performance Optimization",
            "description": "Speed improvements, caching, compression.",
            "price": 600
        },
        {
            "sku": "DG-HST-A-006",
            "category": "Hosting",
            "type": "Add-On",
            "name": "Security Hardening",
            "description": "Firewall rules, bot protection, patches.",
            "price": 800
        },
        {
            "sku": "DG-HST-A-007",
            "category": "Hosting",
            "type": "Add-On",
            "name": "Monthly Maintenance Pack",
            "description": "30 days of updates and small changes.",
            "price": 300
        },
        {
            "sku": "DG-HST-A-008",
            "category": "Hosting",
            "type": "Add-On",
            "name": "Emergency Fix / Priority Repair",
            "description": "Same-day fix for outages or crashes.",
            "price": 500
        },
        {
            "sku": "DG-HST-A-009",
            "category": "Hosting",
            "type": "Add-On",
            "name": "Platform Migration",
            "description": "Migrate site to a new host or platform.",
            "price": 1200
        },
        {
            "sku": "DG-HST-A-010",
            "category": "Hosting",
            "type": "Add-On",
            "name": "Load Testing",
            "description": "Stress test for traffic spikes.",
            "price": 900
        },
        {
            "sku": "DG-HST-A-011",
            "category": "Hosting",
            "type": "Add-On",
            "name": "Monitoring Dashboard",
            "description": "Real-time system and uptime dashboard.",
            "price": 1800
        },
        {
            "sku": "DG-HST-A-012",
            "category": "Hosting",
            "type": "Add-On",
            "name": "Hourly Dev Support",
            "description": "Development hours for fixes or updates.",
            "price": 150
        },
        {
            "sku": "DG-HST-A-013",
            "category": "Hosting",
            "type": "Add-On",
            "name": "Staging Environment",
            "description": "Full testing environment for changes.",
            "price": 900
        },
        {
            "sku": "DG-HST-A-014",
            "category": "Hosting",
            "type": "Add-On",
            "name": "Dedicated Server Setup",
            "description": "Standalone server provisioning & tuning.",
            "price": 3000
        },
        {
            "sku": "DG-HST-A-015",
            "category": "Hosting",
            "type": "Add-On",
            "name": "CDN Integration",
            "description": "Global content distribution setup.",
            "price": 700
        },
        {
            "sku": "DG-HST-A-016",
            "category": "Hosting",
            "type": "Add-On",
            "name": "Database Tuning",
            "description": "Indexes, queries, performance improvements.",
            "price": 600
        },
        {
            "sku": "DG-HST-A-017",
            "category": "Hosting",
            "type": "Add-On",
            "name": "Automated Error Alerts",
            "description": "Monitoring with error alerting.",
            "price": 500
        },
        {
            "sku": "DG-HST-A-018",
            "category": "Hosting",
            "type": "Add-On",
            "name": "Server Monitoring Bot",
            "description": "AI bot that reports outages and spikes.",
            "price": 1200
        },
        {
            "sku": "DG-HST-A-019",
            "category": "Hosting",
            "type": "Add-On",
            "name": "Weekly Update Pack",
            "description": "Weekly software and dependency updates.",
            "price": 350
        },
        {
            "sku": "DG-HST-A-020",
            "category": "Hosting",
            "type": "Add-On",
            "name": "Enterprise SLA Support",
            "description": "Fastest guaranteed response window.",
            "price": 2500
        },

    ]

    batch_insert(items)


# ===============================================================
# MAIN SEED FUNCTION
# ===============================================================

def seed_products():
    seed_websites()
    seed_games()
    seed_creative_tools()
    seed_dev_tools()
    seed_enterprise()
    seed_scientific()
    seed_ai_engineering()
    seed_mobile()
    seed_design()
    seed_media()
    seed_marketing()
    seed_content()
    seed_hosting()


# ===============================================================
# UNDO
# ===============================================================

def undo_products():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.products RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM products"))
    db.session.commit()

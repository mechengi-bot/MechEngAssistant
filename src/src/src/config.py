# App configuration settings
APP_SETTINGS = {
    "page_title": "MechBot Trilingual",
    "page_icon": "🔧",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# Theme colors
THEME = {
    "primary_color": "#6c5ce7",       # Purple
    "secondary_color": "#f0e6ff",     # Light Purple
    "background_color": "#f5f7ff",    # Light Blue
    "text_color": "#333333"           # Dark Gray
}

# Supported languages
LANGUAGES = {
    "English": {
        "code": "en",
        "icon": "globe2",
        "dir": "ltr"
    },
    "Français": {
        "code": "fr",
        "icon": "globe2",
        "dir": "ltr"
    },
    "العربية": {
        "code": "ar",
        "icon": "globe2",
        "dir": "rtl"
    }
}

# Response categories
CATEGORIES = {
    "prospects": ["career", "job", "prospect", "وظيف", "مهن", "carrière"],
    "lessons": ["lesson", "course", "study", "دراس", "درس", "cours"],
    "admission": ["admission", "require", "قبول", "admission"],
    "fst": ["fst", "tanger", "طنجة"]
}

# Sidebar style
SIDEBAR_STYLE = {
    "container": {
        "padding": "5!important",
        "background-color": "#f0e6ff"
    },
    "icon": {
        "color": "#6c5ce7",
        "font-size": "25px"
    },
    "nav-link": {
        "font-size": "16px",
        "text-align": "left",
        "margin": "0px",
        "--hover-color": "#eee"
    },
    "nav-link-selected": {
        "background-color": "#6c5ce7"
    }
}

# Custom CSS
CUSTOM_CSS = """
    <style>
    .main {
        background: linear-gradient(135deg, #f5f7ff 0%, #f0e6ff 100%);
    }
    .stButton>button {
        background-color: #6c5ce7;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        opacity: 0.9;
        transform: translateY(-1px);
    }
    .chat-message {
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        background-color: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .sidebar .sidebar-content {
        background: #f0e6ff;
    }
    .stTextInput>div>div>input {
        border-color: #6c5ce7;
        border-radius: 8px;
    }
    </style>
"""

# Footer messages
FOOTER_MESSAGES = {
    "en": "*Ask me about: career prospects, courses, admission requirements, or FST Tanger!*",
    "fr": "*Posez-moi des questions sur: les perspectives de carrière, les cours, les conditions d'admission ou la FST Tanger !*",
    "ar": "*اسألني عن: الآفاق المهنية، الدروس، متطلبات القبول، أو كلية العلوم والتقنيات بطنجة!*"
}

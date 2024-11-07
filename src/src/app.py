import streamlit as st
from streamlit_option_menu import option_menu

# Configure page settings
st.set_page_config(
    page_title="MechBot Trilingual",
    page_icon="🔧",
    layout="wide"
)

# Custom CSS
st.markdown("""
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
    }
    .chat-message {
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        background-color: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Responses dictionary
responses = {
    'en': {
        'greeting': 'Welcome to the Mechanical Engineering Information Bot! How can I help you today?',
        'prospects': [
            'Career opportunities in manufacturing industries',
            'Research and development positions',
            'Automotive industry roles',
            'Aerospace engineering',
            'Energy sector positions',
            'Robotics and automation',
            'HVAC systems design'
        ],
        'lessons': [
            'Thermodynamics',
            'Fluid Mechanics',
            'Solid Mechanics',
            'Machine Design',
            'Control Systems',
            'Manufacturing Processes',
            'Materials Science'
        ],
        'admission': [
            'Baccalaureate in Physical Sciences or equivalent',
            'Strong background in mathematics and physics',
            'Minimum GPA requirement: 14/20',
            'Successful completion of entrance exam',
            'Language proficiency in French'
        ],
        'fst': [
            'Located in Tangier, Morocco',
            'Offers Bachelor and Master degrees in Mechanical Engineering',
            'Strong industry partnerships',
            'Modern laboratory facilities',
            'Research opportunities'
        ]
    },
    'fr': {
        'greeting': 'Bienvenue sur le Bot d\'Information en Génie Mécanique ! Comment puis-je vous aider aujourd\'hui ?',
        'prospects': [
            'Opportunités de carrière dans les industries manufacturières',
            'Postes en recherche et développement',
            'Rôles dans l\'industrie automobile',
            'Ingénierie aérospatiale',
            'Postes dans le secteur énergétique',
            'Robotique et automatisation',
            'Conception de systèmes CVC'
        ],
        'lessons': [
            'Thermodynamique',
            'Mécanique des fluides',
            'Mécanique des solides',
            'Conception de machines',
            'Systèmes de contrôle',
            'Procédés de fabrication',
            'Science des matériaux'
        ],
        'admission': [
            'Baccalauréat en Sciences Physiques ou équivalent',
            'Solide formation en mathématiques et physique',
            'Moyenne minimale requise : 14/20',
            'Réussite au concours d\'entrée',
            'Maîtrise de la langue française'
        ],
        'fst': [
            'Située à Tanger, Maroc',
            'Propose des licences et masters en génie mécanique',
            'Partenariats solides avec l\'industrie',
            'Installations de laboratoire modernes',
            'Opportunités de recherche'
        ]
    },
    'ar': {
        'greeting': 'مرحباً بك في روبوت المعلومات الخاص بالهندسة الميكانيكية! كيف يمكنني مساعدتك اليوم؟',
        'prospects': [
            'فرص العمل في الصناعات التحويلية',
            'مناصب في البحث والتطوير',
            'أدوار في صناعة السيارات',
            'هندسة الطيران والفضاء',
            'وظائف في قطاع الطاقة',
            'الروبوتات والأتمتة',
            'تصميم أنظمة التكييف والتهوية'
        ],
        'lessons': [
            'الديناميكا الحرارية',
            'ميكانيكا الموائع',
            'ميكانيكا المواد الصلبة',
            'تصميم الآلات',
            'أنظمة التحكم',
            'عمليات التصنيع',
            'علم المواد'
        ],
        'admission': [
            'بكالوريا في العلوم الفيزيائية أو ما يعادلها',
            'خلفية قوية في الرياضيات والفيزياء',
            'الحد الأدنى للمعدل: 14/20',
            'اجتياز امتحان القبول',
            'إتقان اللغة الفرنسية'
        ],
        'fst': [
            'تقع في طنجة، المغرب',
            'تقدم درجات البكالوريوس والماجستير في الهندسة الميكانيكية',
            'شراكات قوية مع الصناعة',
            'مرافق مختبرات حديثة',
            'فرص البحث العلمي'
        ]
    }
}

def get_response(query, language):
    query = query.lower()
    if 'prospect' in query or 'career' in query or 'job' in query or 'وظيف' in query or 'مهن' in query or 'carrière' in query:
        return responses[language]['prospects']
    elif 'lesson' in query or 'course' in query or 'study' in query or 'دراس' in query or 'درس' in query or 'cours' in query:
        return responses[language]['lessons']
    elif 'admission' in query or 'require' in query or 'قبول' in query or 'admission' in query:
        return responses[language]['admission']
    elif 'fst' in query or 'tanger' in query or 'طنجة' in query:
        return responses[language]['fst']
    else:
        if language == 'en':
            return ["I can help you with information about mechanical engineering prospects, lessons, admission requirements, and FST Tanger. Please ask a specific question."]
        elif language == 'fr':
            return ["Je peux vous aider avec des informations sur les perspectives en génie mécanique, les cours, les conditions d'admission et la FST Tanger. Veuillez poser une question spécifique."]
        else:
            return ["يمكنني مساعدتك بمعلومات عن آفاق الهندسة الميكانيكية، والدروس، ومتطلبات القبول، وكلية العلوم والتقنيات بطنجة. يرجى طرح سؤال محدد."]

def main():
    # Language selector in sidebar
    with st.sidebar:
        selected_language = option_menu(
            "Select Language | Choisir la langue | اختر اللغة",
            ["English", "Français", "العربية"],
            icons=['globe2', 'globe2', 'globe2'],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "5!important", "background-color": "#f0e6ff"},
                "icon": {"color": "#6c5ce7", "font-size": "25px"}, 
                "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#6c5ce7"},
            }
        )
    
    lang_code = 'en' if selected_language == "English" else 'fr' if selected_language == "Français" else 'ar'
    
    # Main title
    st.title("🔧 MechBot Trilingual")
    st.write(responses[lang_code]['greeting'])
    
    # Chat interface
    user_input = st.text_input("Your question:", key="user_input")
    
    if user_input:
        response = get_response(user_input, lang_code)
        
        st.markdown("### Response:")
        for item in response:
            st.markdown(f"- {item}")
    
    # Footer with example questions based on language
    st.markdown("---")
    if lang_code == 'en':
        st.markdown("*Ask me about: career prospects, courses, admission requirements, or FST Tanger!*")
    elif lang_code == 'fr':
        st.markdown("*Posez-moi des questions sur: les perspectives de carrière, les cours, les conditions d'admission ou la FST Tanger !*")
    else:
        st.markdown("*اسألني عن: الآفاق المهنية، الدروس، متطلبات القبول، أو كلية العلوم والتقنيات بطنجة!*")

if __name__ == "__main__":
    main()

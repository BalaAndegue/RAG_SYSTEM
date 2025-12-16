import logging
import streamlit as st
from src.utils import setup_logging
from streamlit_lottie import st_lottie
import json

# Initialize logger
setup_logging()
logger = logging.getLogger(__name__)

# Set page config with expanded layout
st.set_page_config(
    page_title="Jam with AI - Intelligent Document Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern design
def apply_custom_css() -> None:
    """Applies custom CSS styling for a modern, clean interface."""
    st.markdown(
        """
        <style>
        /* Main background with gradient */
        .main {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        
        /* Sidebar styling */
        .sidebar .sidebar-content {
            background: linear-gradient(180deg, #2d3748 0%, #1a202c 100%);
            color: white;
            padding: 1.5rem;
        }
        
        /* Card styling for main content */
        .main-card {
            background: white;
            border-radius: 20px;
            padding: 2.5rem;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            margin: 1rem 0;
        }
        
        /* Feature cards */
        .feature-card {
            background: linear-gradient(135deg, #f6f8ff 0%, #edf2f7 100%);
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1rem 0;
            border-left: 4px solid #667eea;
            transition: transform 0.3s ease;
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.2);
        }
        
        /* Button styling */
        .stButton > button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 12px 32px;
            font-weight: 600;
            font-size: 16px;
            transition: all 0.3s ease;
            width: 100%;
        }
        
        .stButton > button:hover {
            transform: scale(1.05);
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
        }
        
        /* Headings */
        h1, h2, h3 {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 700;
        }
        
        /* Metrics/stats cards */
        .stat-card {
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            border-top: 4px solid #667eea;
        }
        
        /* Custom separator */
        .separator {
            height: 4px;
            width: 80px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 2rem auto;
            border-radius: 2px;
        }
        
        /* Icon styling */
        .feature-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        
        /* Hide default Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #f1f1f1;
            border-radius: 10px;
        }
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    logger.info("Applied modern CSS styling.")

# Create animated placeholder (optional - remove if you don't want animations)
def create_placeholder_animation():
    """Creates a simple JSON animation for visual appeal."""
    animation_json = {
        "v": "5.5.2",
        "fr": 30,
        "ip": 0,
        "op": 60,
        "w": 400,
        "h": 300,
        "nm": "AI Assistant",
        "ddd": 0,
        "assets": [],
        "layers": [
            {
                "ddd": 0,
                "ind": 1,
                "ty": 4,
                "nm": "Brain",
                "sr": 1,
                "ks": {
                    "o": {"a": 0, "k": 100, "ix": 11},
                    "r": {"a": 1, "k": [{"i": {"x": [0.667], "y": [1]}, "o": {"x": [0.333], "y": [0]}, "t": 0, "s": [0]}, {"t": 60, "s": [360]}]},
                    "p": {"a": 0, "k": [200, 150, 0], "ix": 2},
                    "a": {"a": 0, "k": [0, 0, 0], "ix": 1},
                    "s": {"a": 0, "k": [100, 100, 100], "ix": 6}
                },
                "ao": 0,
                "shapes": [
                    {
                        "ty": "gr",
                        "it": [
                            {"ty": "el", "p": {"a": 0, "k": [0, 0]}, "s": {"a": 0, "k": [80, 80]}},
                            {"ty": "fl", "c": {"a": 0, "k": [0.6, 0.2, 0.8, 1]}}
                        ]
                    }
                ]
            }
        ]
    }
    return animation_json

def display_sidebar_content() -> None:
    """Displays a modern sidebar with navigation and info."""
    with st.sidebar:
        # Brand header
        st.markdown(
            """
            <div style="text-align: center; margin-bottom: 2rem;">
                <h1 style="font-size: 2.5rem; margin-bottom: 0.5rem;">🤖</h1>
                <h2 style="margin: 0; font-weight: 800; font-size: 1.8rem;">Jam with AI</h2>
                <p style="color: #a0aec0; font-size: 0.9rem; margin-top: 0.5rem;">
                    Intelligent Document Assistant
                </p>
            </div>
            <div class="separator"></div>
            """,
            unsafe_allow_html=True
        )
        
        # Navigation
        st.markdown("### 🧭 Navigation")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🏠 Home", use_container_width=True):
                st.rerun()
        with col2:
            if st.button("⚙️ Settings", use_container_width=True):
                st.session_state.page = "settings"
        
        # Quick stats
        st.markdown("### 📊 Quick Stats")
        stats_cols = st.columns(2)
        with stats_cols[0]:
            st.markdown(
                """
                <div class="stat-card">
                    <div style="font-size: 2rem;">📄</div>
                    <div style="font-size: 1.2rem; font-weight: bold;">Documents</div>
                    <div style="color: #667eea; font-size: 1.5rem;">24</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with stats_cols[1]:
            st.markdown(
                """
                <div class="stat-card">
                    <div style="font-size: 2rem;">💬</div>
                    <div style="font-size: 1.2rem; font-weight: bold;">Chats</div>
                    <div style="color: #764ba2; font-size: 1.5rem;">156</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        # Footer
        st.markdown(
            """
            <div style="margin-top: 3rem; text-align: center; padding-top: 1.5rem; border-top: 1px solid #4a5568;">
                <p style="color: #a0aec0; font-size: 0.9rem;">
                    © 2024 Jam with AI<br>
                    v2.1.0 • Premium
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

def display_main_content() -> None:
    """Displays the main content with modern design."""
    
    # Hero Section
    st.markdown(
        """
        <div class="main-card">
            <div style="text-align: center;">
                <h1 style="font-size: 3rem; margin-bottom: 1rem;">✨ AI-Powered Document Assistant</h1>
                <p style="font-size: 1.2rem; color: #4a5568; max-width: 800px; margin: 0 auto;">
                    Transform your document workflow with intelligent AI that understands, retrieves, 
                    and converses about your content instantly.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Features Section
    st.markdown("## 🚀 Core Features")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">💬</div>
                <h3 style="margin-top: 0;">Smart Chat Assistant</h3>
                <p style="color: #4a5568;">
                    Engage in natural conversations with AI powered by the latest LLM technology. 
                    Context-aware responses and intelligent follow-ups.
                </p>
                <ul style="color: #4a5568; padding-left: 1.5rem;">
                    <li>Multi-turn conversations</li>
                    <li>Context retention</li>
                    <li>Real-time responses</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">⚡</div>
                <h3 style="margin-top: 0;">Hybrid RAG System</h3>
                <p style="color: #4a5568;">
                    Combines traditional search with semantic understanding for accurate document retrieval.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <h3 style="margin-top: 0;">Document Intelligence</h3>
                <p style="color: #4a5568;">
                    Upload PDFs and extract meaningful insights automatically. 
                    Advanced OCR and text processing capabilities.
                </p>
                <ul style="color: #4a5568; padding-left: 1.5rem;">
                    <li>PDF parsing</li>
                    <li>Smart indexing</li>
                    <li>Content analysis</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">🔒</div>
                <h3 style="margin-top: 0;">Secure & Private</h3>
                <p style="color: #4a5568;">
                    Enterprise-grade security with encrypted storage and private processing.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Quick Actions Section
    st.markdown("## ⚡ Quick Actions")
    
    action_col1, action_col2, action_col3 = st.columns(3)
    
    with action_col1:
        if st.button("💬 Start New Chat", use_container_width=True):
            st.session_state.action = "new_chat"
    
    with action_col2:
        if st.button("📤 Upload Document", use_container_width=True):
            st.session_state.action = "upload"
    
    with action_col3:
        if st.button("🔍 Search Archive", use_container_width=True):
            st.session_state.action = "search"
    
    # Recent Activity
    st.markdown("## 📋 Recent Activity")
    
    with st.container():
        st.markdown(
            """
            <div style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); 
                        border-radius: 15px; padding: 1.5rem;">
                <div style="display: flex; justify-content: space-between; align-items: center; 
                            padding: 0.75rem; border-bottom: 1px solid #dee2e6;">
                    <span style="font-weight: bold;">📄 Quarterly_Report.pdf</span>
                    <span style="color: #667eea;">2 hours ago</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; 
                            padding: 0.75rem; border-bottom: 1px solid #dee2e6;">
                    <span style="font-weight: bold;">💬 Chat with Sales Data</span>
                    <span style="color: #667eea;">Yesterday</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; 
                            padding: 0.75rem;">
                    <span style="font-weight: bold;">📤 Research_Paper.pdf</span>
                    <span style="color: #667eea;">3 days ago</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# Main execution
if __name__ == "__main__":
    apply_custom_css()
    display_sidebar_content()
    display_main_content()
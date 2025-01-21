import streamlit as st


def load_content():
    """Load the content dictionary with all training materials"""
    return {
        "Expert content": """
        Expert content helps establish credibility and trust with potential clients.
        Key points:
        - Industry insights and analysis
        - Best practices and methodologies
        - Case studies and success stories
        - Professional certifications and credentials
        """,

        "Youtube videos": """
        Educational videos on sales techniques and relationship building:
        1. Understanding customer psychology
        2. Active listening techniques
        3. Building trust through video communication
        4. Virtual relationship building strategies
        """,

        "Free webinar": """
        Join our interactive webinar sessions covering:
        - Fundamentals of rapport building
        - Communication skills development
        - Reading and responding to customer signals
        - Creating lasting business relationships
        """,

        "Online form": """
        Comprehensive needs assessment form covering:
        - Current business challenges
        - Goals and objectives
        - Budget considerations
        - Timeline expectations
        - Current solutions in use
        """,

        "Sales meeting": """
        Structured approach to sales meetings:
        1. Introduction and agenda setting
        2. Discovery questions
        3. Solution exploration
        4. Next steps and follow-up
        """,

        "Free consultation": """
        One-on-one consultation session including:
        - Business situation analysis
        - Pain point identification
        - Solution brainstorming
        - Customized recommendations
        """,

        "Free audit": """
        Detailed audit process covering:
        - Current system evaluation
        - Performance analysis
        - Gap identification
        - Improvement recommendations
        """,

        "Zoom demo": """
        Best practices for virtual demonstrations:
        1. Technical setup and preparation
        2. Engagement techniques
        3. Interactive elements
        4. Follow-up procedures
        """,

        "How to present": """
        Effective presentation guidelines:
        - Structure and flow
        - Visual aids usage
        - Storytelling techniques
        - Handling Q&A sessions
        """,

        "What is an objection": """
        Understanding sales objections:
        - Definition and types
        - Psychology behind objections
        - Common triggers
        - Opportunity perspective
        """,

        "Types of objections": """
        Common objection categories:
        1. Price/Budget
        2. Authority/Decision-making
        3. Need/Timing
        4. Competition/Alternative
        5. Trust/Credibility
        """,

        "How to handle objections": """
        Objection handling framework:
        1. Listen actively
        2. Acknowledge concern
        3. Ask clarifying questions
        4. Respond appropriately
        5. Confirm resolution
        """,

        "What is closing": """
        Understanding the sales close:
        - Definition and importance
        - Psychology of closing
        - Timing considerations
        - Signs of readiness
        """,

        "How to close effectively": """
        Effective closing strategies:
        1. Building momentum
        2. Creating urgency
        3. Addressing final concerns
        4. Securing commitment
        """,

        "Closing techniques": """
        Popular closing methods:
        - Assumptive close
        - Alternative close
        - Summary close
        - Trial close
        - Direct close
        """
    }


def show_webpage(selected_key, content):
    """Display the selected content with formatting"""
    st.write("---")
    st.header(selected_key)
    st.markdown(content[selected_key])

    # Add helpful resources section
    st.write("---")
    st.subheader("📚 Additional Resources")
    st.markdown("""
    - Download related materials
    - Schedule a practice session
    - Join our community forum
    """)


def main():
    # Page configuration
    st.set_page_config(
        page_title="Sales Training Agent",
        page_icon="🎯",
        layout="wide"
    )

    # Main title with styling
    st.title("🎯 Interactive Sales Training Agent")
    st.markdown("""
    Welcome to your personal sales training guide! Select a topic below to explore 
    detailed materials and resources for improving your sales skills.
    """)

    # Load content
    content = load_content()

    # Create columns for better layout
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("Training Topics")
        # First-level selection
        first_level = st.radio(
            "What would you like to learn about?",
            [
                "Rapport building",
                "Needs assessment",
                "Presentation",
                "Objections handling",
                "Closing"
            ],
            key="first_level"
        )

        # Define second-level options based on first selection
        second_level_options = {
            "Rapport building": [
                "Expert content",
                "Youtube videos",
                "Free webinar"
            ],
            "Needs assessment": [
                "Online form",
                "Sales meeting",
                "Free consultation",
                "Free audit"
            ],
            "Presentation": [
                "Zoom demo",
                "Sales meeting",
                "How to present"
            ],
            "Objections handling": [
                "What is an objection",
                "Types of objections",
                "How to handle objections"
            ],
            "Closing": [
                "What is closing",
                "How to close effectively",
                "Closing techniques"
            ]
        }

        # Second-level selection
        st.subheader(f"{first_level} Topics")
        second_level = st.radio(
            "Select a specific topic:",
            second_level_options[first_level],
            key="second_level"
        )

    # Display content in the second column
    with col2:
        if second_level:
            show_webpage(second_level, content)


if __name__ == "__main__":
    main()

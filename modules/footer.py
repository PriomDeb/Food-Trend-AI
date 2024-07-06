import streamlit as st


def footer():
    contacts = """
    ---
    
    # 
    
    #### Contact 🌱
    [![Website](https://img.shields.io/badge/priomdeb.com-teal)](https://priomdeb.com)
    [![GitHub](https://img.shields.io/badge/GitHub-black)](https://github.com/PriomDeb)
    [![Mail](https://img.shields.io/badge/priom@priomdeb.com-yellow)](mailto:priom@priomdeb.com)
    
    """
    
    st.markdown(contacts)
    
    
    developer = """
    <style>
    @keyframes typing {
        0% { width: 0; }
        50% { width: 26ch; }
        100% { width: 0; }
    }
        
    @keyframes blink-caret {
        from, to { border-color: transparent; }
        50% { border-color: orange; }
    }
    
    .typewriter {
        text-align: center;
        overflow: hidden;
        border-right: .15em solid orange;
        white-space: nowrap;
        margin: 0 auto;
        animation: typing 4s steps(19, end) infinite, blink-caret .75s step-end infinite;
        width: 19ch; /* Set width to match character count */
        display: inline-block;
    }
    
    .copyright{
        text-align: center;
    }
    
    
    
    a.custom-link {
    color: orange;
    text-decoration: none;
    font-weight: bold;
    
    background-color: #f0f0f0;
    padding: 10px;
    border-radius: 5px;
    }
    
    a.custom-link:hover {
    color: red;
    }
    
    </style>
    
    <div class="copyright">
    <div class="">
    <strong>Food Trend.AI</strong> Made with ❤️ by <a href="https://priomdeb.com/" class="custom-link">Priom Deb</a>
    </div>
    </div>
    """
    
    st.markdown(developer, unsafe_allow_html=True)

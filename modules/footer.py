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
    </style>
    
    <div class="copyright">
    <div class="">
    Made with ❤️ by Priom Deb
    </div>
    </div>
    """
    
    st.markdown(developer, unsafe_allow_html=True)

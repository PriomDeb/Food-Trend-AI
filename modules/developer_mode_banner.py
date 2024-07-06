import streamlit as st


developer_mode_html = """
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
  animation: typing 6s steps(19, end) infinite, blink-caret .75s step-end infinite;
  width: 19ch; /* Set width to match character count */
  display: inline-block;
}

.development{
    text-align: center;
    color: white;
    background-color: red;
    border-radius: 10px;
    height: 26px;
}
</style>

<div class="development">
<div class="typewriter">
  🚀 Development View
</div>
</div>
"""

def developer_mood_banner(mode):
    if mode: st.markdown(developer_mode_html, unsafe_allow_html=True)

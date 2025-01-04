import streamlit as st

# Streamlit app layout
st.title("Sharing the Message from the Seventh Session of Our Year-End Retreat")

# Introduction
st.subheader("Introduction")
st.write(
    """
    In this year-end retreat, I would like to share the insights from the seventh session. 
    Originally, this part was available online as part of the entire conference gathering, 
    but the pastor's personal words, along with his strong requests and warnings concerning the church, 
    were removed. Nevertheless, there were truly important messages conveyed. Ultimately, the pastor spoke about three key points:
    """
)

# Key Question
st.write("**Who are the people that follow the Lord, live in fellowship with Him, and stand before Him as good and faithful servants?**")

# Key Points
st.subheader("Key Points")

# 1. Living According to God’s Will
st.markdown("### 1. Those Who Strive to Live According to God’s Will")
st.write(
    """
    Living according to God’s will is not easy. Even our thoughts cannot be governed by our own desires. 
    It requires unceasing prayer and humility to acknowledge that our thoughts, actions, and emotions differ from the Lord’s. 
    By doing so, we can begin to hear His voice and align ourselves with His will.
    """
)

# 2. Seeking the Face of God
st.markdown("### 2. Seeking the Face of God")
st.write(
    """
    Seeking the face of God means prioritizing knowing and loving Him above all else. 
    When we focus on God, human evaluations and difficulties lose their significance. 
    A life of seeking God's face leads to receiving His vision and following it wholeheartedly.
    """
)

# 3. Embracing God’s Vision
st.markdown("### 3. Embracing God’s Vision")
st.write(
    """
    Embracing God’s vision involves setting aside personal plans and pursuits to follow the vision God provides. 
    This life is not without challenges or misunderstandings, but those who follow God's vision remain steadfast, 
    valuing God's purpose above all else.
    """
)

# Reflection and Conclusion
st.subheader("Reflection and Conclusion")
st.write(
    """
    The pastor concluded by emphasizing the importance of these points for walking with God and living the life described in the Beatitudes. 
    Unexpected events, like the emergence of Muan Airport, remind us that God’s timing is unknown, and His warnings and judgments are inevitable in our lives.
    """
)

# Reflection Questions
st.write("**Reflect on Your Faith Journey Over the Past Year:**")
st.markdown(
    """
    - Has your faith grown?
    - Do you hear God’s voice?
    - Is your heart stirred with excitement and filled with hope because of God?
    - Have you reached the humble state of confessing that the Lord is everything to you, and that you can do nothing of your own goodness?
    """
)

# Interactive Reflection
st.write("Take a moment to reflect and share your thoughts:")
faith_growth = st.radio("Has your faith grown this year?", ["Yes", "No", "Not sure"])
hearing_voice = st.radio("Do you hear God's voice in your life?", ["Yes", "No", "Not sure"])
heart_state = st.radio("Is your heart filled with excitement and hope because of God?", ["Yes", "No", "Not sure"])
humility_confession = st.radio("Have you reached a humble state of fully relying on the Lord?", ["Yes", "No", "Not sure"])

# Closing
st.write("**Thank you for reflecting. May your journey with God continue to deepen and grow.**")

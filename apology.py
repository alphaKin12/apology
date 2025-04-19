import streamlit as st

# Page config
st.set_page_config(
    page_title="I'm So Sorry, Shinu 💛",
    page_icon="🥺",
    layout="centered"
)
st.image("https://github.com/alphaKin12/apology/blob/main/Screenshot_20250328_234910_Chrome.jpg?raw=true", width=300, caption="Forgive me? 🐶💔")

# Main heading
st.markdown("<h1 style='text-align: center; color: #ff6f61;'>I'm So Sorry, My Love</h1>", unsafe_allow_html=True)

# Subheading
st.markdown("<h3 style='text-align: center; color: #555;'>Shinu, you mean the world to me 🌍</h3>", unsafe_allow_html=True)

# Heartfelt message
st.write("""
---

Hey baby,

I know you were hurt because I left the call last night... and I'm really, really sorry. I didn’t mean to make you feel ignored or unloved. I wish I could be there beside you, holding your hand, making it all okay.

You matter more to me than any meeting, any task, any call. Every second without your smile feels incomplete. Please don’t let one small moment steal the joy we’ve built together.

Let this be my little way of saying sorry from 1000 km away. I love you endlessly—and I’ll always keep trying to be better for you.

---
""")

# Poem title
st.markdown("<h4 style='text-align: center; color: #cc6699;'>A Poem for You, My Shinu 💌</h4>", unsafe_allow_html=True)

# Poem
poem = """
To my sunshine with a stormy brow,  
I wish I could hold you, here and now.  
For every tear that found your cheek,  
My silence hurt more than I could speak.

A call I had to take, it stole  
The moments meant to soothe your soul.  
But please believe, it broke me too,  
To not be there, to comfort you.

From miles away, my heart still tries,  
To send you love through silent skies.  
So, Shinu, let this be my plea,  
Forgive your fool, and smile for me. 🌻
"""

st.markdown(f"<pre style='background-color:#fff7f7; color:#444; font-size: 16px; border-left: 4px solid #ffb6b6; padding: 1em; border-radius: 10px;'>{poem}</pre>", unsafe_allow_html=True)

# Puppy face
st.markdown("<h4 style='text-align: center; color: #888;'>Me right now 🥺👇</h4>", unsafe_allow_html=True)
st.image("https://i.imgur.com/8wKQpPb.gif", width=300, caption="Forgive me? 🐶💔", use_column_width=False)

# Closing
st.markdown("<p style='text-align: center; font-size:18px; color: #cc6699;'>Waiting for your smile again... 🌸</p>", unsafe_allow_html=True)

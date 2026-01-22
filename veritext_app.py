import streamlit as st

# -------------------- Page Config --------------------
st.set_page_config(
    page_title="VeriText",
    page_icon="🛡️",
    layout="centered"
)

# -------------------- Title Section --------------------
st.title("🛡️ VeriText")
st.subheader("Explainable Scam & Misinformation Analyzer")
st.write(
    "This prototype analyzes message content and sender context to identify "
    "potential scam or misinformation indicators in a transparent way."
)

# -------------------- User Inputs --------------------
message = st.text_area(
    "📩 Paste the message you received:",
    placeholder="Example: Your bank account will be blocked today. Verify immediately."
)

sender = st.text_input(
    "👤 Sender ID (email / phone number / username):",
    placeholder="Example: bankhelp@gmail.com"
)

# -------------------- Analysis Logic --------------------
if st.button("🔍 Analyze Message"):
    risk_score = 0
    reasons = []

    urgent_words = [
        "urgent", "immediately", "blocked", "last warning",
        "today", "act now", "verify now"
    ]

    authority_words = [
        "bank", "school", "government",
        "delivery", "account", "official"
    ]

    if message:
        for word in urgent_words:
            if word in message.lower():
                risk_score += 1
                reasons.append("Urgency-based language detected")

        for word in authority_words:
            if word in message.lower():
                risk_score += 1
                reasons.append("Possible authority impersonation")

    if sender:
        if "gmail" in sender.lower() or "yahoo" in sender.lower():
            risk_score += 1
            reasons.append("Sender uses a non-official or generic email ID")

    # -------------------- Output --------------------
    if risk_score == 0:
        st.success("🟢 Risk Level: LOW")
    elif risk_score == 1:
        st.warning("🟡 Risk Level: MEDIUM")
    else:
        st.error("🔴 Risk Level: HIGH")

    if reasons:
        st.subheader("📌 Why this message was flagged")
        for reason in set(reasons):
            st.write("•", reason)
    else:
        st.write("No major risk indicators detected.")

# -------------------- Footer --------------------
st.markdown("---")
st.caption("Developed by Akshaj Mishra")
st.caption(
    "⚠️ Prototype for academic and research demonstration only. "
    "This software is not intended for real-world deployment or imitation."
)

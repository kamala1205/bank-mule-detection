import streamlit as st
import streamlit.components.v1 as components
import sqlite3
import pickle
import numpy as np
from datetime import datetime

# ── PAGE CONFIG ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Bank Mule Detection | Kamalakanta Behera",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ── YOUR LINKS — update if needed ─────────────────────────────────────────────
PORTFOLIO_URL = "https://kamala1205.github.io"
DASHBOARD_URL = "https://kamala1205.github.io/bank-mule-detection/dashboard_bank_mule.html"
GITHUB_URL    = "https://github.com/kamala1205/bank-mule-detection"

# ── GLOBAL CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600;700&family=IBM+Plex+Sans:wght@300;400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; }
html, body, [class*="css"], .stApp {
    font-family: 'IBM Plex Sans', sans-serif;
    background-color: #05080f !important;
    color: #c9d4e0;
}
#MainMenu, footer, header { visibility: hidden; }

.hero-eyebrow {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.6rem; letter-spacing: 4px;
    color: #00cfff; text-transform: uppercase; margin-bottom: 10px;
}
.hero-title {
    font-size: 2.4rem; font-weight: 600;
    color: #e8f0f8; line-height: 1.15; margin-bottom: 12px;
}
.hero-sub {
    font-size: 0.92rem; color: #5a7a99;
    line-height: 1.7; margin-bottom: 20px;
}
.badges { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 32px; }
.badge {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.58rem; letter-spacing: 1px;
    padding: 4px 12px; border-radius: 100px;
    border: 1px solid #0d2d44; color: #00cfff;
    background: rgba(0,207,255,0.05);
}
.sec-label {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.58rem; letter-spacing: 4px;
    color: #00cfff; text-transform: uppercase;
    margin-bottom: 14px; padding-bottom: 8px;
    border-bottom: 1px solid #0d2035;
}
.card { border-radius: 10px; padding: 22px 24px; margin: 14px 0; }
.card-mule  { background: rgba(255,65,90,0.07);  border: 1px solid rgba(255,65,90,0.35); }
.card-sus   { background: rgba(255,196,0,0.06);  border: 1px solid rgba(255,196,0,0.35); }
.card-legit { background: rgba(0,210,130,0.06);  border: 1px solid rgba(0,210,130,0.3); }
.card-verdict {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 1.3rem; font-weight: 700; margin-bottom: 6px;
}
.card-score { font-size: 0.85rem; color: #5a7a99; margin-bottom: 10px; }
.card-desc  { font-size: 0.88rem; line-height: 1.75; color: #a0b8cc; }
.feat { margin-bottom: 10px; }
.feat-meta {
    display: flex; justify-content: space-between;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.6rem; color: #5a7a99; margin-bottom: 5px;
}
.feat-track { background: #0d1e2d; border-radius: 3px; height: 4px; }
.feat-fill  { height: 4px; border-radius: 3px; }
.preset-grid { display: flex; gap: 10px; margin-bottom: 16px; flex-wrap: wrap; }
.preset-item {
    flex: 1; min-width: 140px;
    background: #080e18; border: 1px solid #0d2035;
    border-radius: 8px; padding: 12px 14px;
    font-size: 0.8rem; color: #5a7a99; line-height: 1.65;
}
.preset-head {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.6rem; font-weight: 700;
    margin-bottom: 6px; letter-spacing: 1px;
}
</style>
""", unsafe_allow_html=True)

# ── NAV BAR via components.html (target="_blank" = opens in new tab, always works) ──
components.html(f"""
<!DOCTYPE html>
<html>
<head>
<style>
  @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@600;700&display=swap');
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{
    background: #05080f;
    padding: 14px 0 14px;
    border-bottom: 1px solid #0d2035;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    font-family: 'IBM Plex Mono', monospace;
  }}
  .brand {{
    font-size: 0.7rem; font-weight: 700;
    letter-spacing: 3px; color: #00cfff; text-transform: uppercase;
  }}
  .links {{ display: flex; gap: 8px; flex-wrap: wrap; }}
  a {{
    font-size: 0.62rem; letter-spacing: 1.5px;
    padding: 7px 15px; border-radius: 5px;
    border: 1px solid #1a3a55; color: #6b8aaa;
    background: transparent; text-decoration: none;
    display: inline-block; transition: all 0.18s;
  }}
  a:hover {{ color: #00cfff; border-color: #00cfff; background: rgba(0,207,255,0.07); }}
  .active {{
    color: #05080f !important; background: #00cfff !important;
    border-color: #00cfff !important; font-weight: 700; pointer-events: none;
  }}
</style>
</head>
<body>
  <span class="brand">KKB &middot; ML PROJECTS</span>
  <div class="links">
    <a href="{PORTFOLIO_URL}" target="_blank">&#8592; PORTFOLIO</a>
    <a href="{DASHBOARD_URL}" target="_blank">&#128202; DASHBOARD</a>
    <a href="{GITHUB_URL}"    target="_blank">&#9095; GITHUB</a>
    <a class="active">&#128737; LIVE APP</a>
  </div>
</body>
</html>
""", height=58)

st.markdown("<div style='margin-bottom:18px'></div>", unsafe_allow_html=True)

# ── HERO ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-eyebrow">// Machine Learning · Fraud Detection</div>
<div class="hero-title">🛡️ Bank Mule Detection System</div>
<div class="hero-sub">
  Enter account and transaction details below. The trained scikit-learn model classifies
  the account as <strong style="color:#ff415a">Mule</strong>,
  <strong style="color:#ffc400">Suspicious</strong>, or
  <strong style="color:#00d282">Legitimate</strong> in real-time.
</div>
<div class="badges">
  <span class="badge">Random Forest</span>
  <span class="badge">scikit-learn</span>
  <span class="badge">SQLite Logging</span>
  <span class="badge">96.4% Accuracy</span>
</div>
""", unsafe_allow_html=True)

# ── LOAD MODEL ─────────────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    try:
        return pickle.load(open("model.pkl", "rb"))
    except FileNotFoundError:
        st.error("⚠️ model.pkl not found. Please add your trained model file.")
        st.stop()

model = load_model()

# ── DATABASE ───────────────────────────────────────────────────────────────────
def save_to_db(acct_age, phone_changes, txn_count, txn_amount, passthrough, label, score):
    try:
        conn = sqlite3.connect("bank.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            acct_age INTEGER, phone_changes INTEGER,
            txn_count INTEGER, txn_amount REAL,
            passthrough INTEGER, prediction TEXT,
            probability INTEGER, date TEXT)""")
        c.execute("""INSERT INTO transactions
            (acct_age, phone_changes, txn_count, txn_amount,
             passthrough, prediction, probability, date)
            VALUES (?,?,?,?,?,?,?,?)""",
            (acct_age, phone_changes, txn_count, txn_amount,
             passthrough, label, score,
             datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        st.warning(f"DB issue: {e}")
        return False

# ── FEATURE CONFIG ─────────────────────────────────────────────────────────────
FEATS = {
    "Pass-Through Ratio": (0.42, "#ff415a"),
    "Account Age":        (0.24, "#ffc400"),
    "Txn Amount":         (0.16, "#ff8c42"),
    "Txn Count":          (0.11, "#00cfff"),
    "Phone Changes":      (0.07, "#00d282"),
}

# ── SESSION STATE for preset loading ──────────────────────────────────────────
if "preset" not in st.session_state:
    st.session_state.preset = None

PRESETS = {
    "mule":       dict(acct_age=2,  phone_changes=5, txn_count=120, txn_amount=500000, passthrough=85),
    "suspicious": dict(acct_age=8,  phone_changes=2, txn_count=45,  txn_amount=150000, passthrough=55),
    "legit":      dict(acct_age=36, phone_changes=0, txn_count=12,  txn_amount=25000,  passthrough=10),
    None:         dict(acct_age=6,  phone_changes=1, txn_count=20,  txn_amount=50000,  passthrough=20),
}
d = PRESETS[st.session_state.preset]

# ── INPUT FORM ─────────────────────────────────────────────────────────────────
st.markdown('<div class="sec-label">// Account Details</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    acct_age      = st.number_input("Account Age (months)", 0, 60,      d["acct_age"],
                                     help="How old is this account in months?")
    txn_count     = st.number_input("Transaction Count (last 30 days)", 0, 500, d["txn_count"],
                                     help="Total transactions in last 30 days")
with col2:
    phone_changes = st.number_input("Phone Changes (last 6 months)", 0, 10, d["phone_changes"],
                                     help="How many times was the phone number changed?")
    txn_amount    = st.number_input("Transaction Amount (₹)", 0, 1000000, d["txn_amount"],
                                     step=1000, help="Total transaction amount in last 30 days")

st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)
passthrough = st.slider("Pass-Through Ratio (%)", 0, 100, d["passthrough"],
                         help="% of received funds immediately sent out — top mule indicator")
st.caption("⚠️ Pass-Through Ratio is the strongest predictor. Values above 70% are high-risk.")

# ── QUICK PRESETS ──────────────────────────────────────────────────────────────
st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)
st.markdown('<div class="sec-label">// Quick Test Presets</div>', unsafe_allow_html=True)

st.markdown("""
<div class="preset-grid">
  <div class="preset-item" style="border-color:rgba(255,65,90,0.35)">
    <div class="preset-head" style="color:#ff415a">🚨 MULE PROFILE</div>
    Age: 2m · Phone: 5 changes<br>₹5,00,000 · Pass-through: 85%
  </div>
  <div class="preset-item" style="border-color:rgba(255,196,0,0.35)">
    <div class="preset-head" style="color:#ffc400">⚠️ SUSPICIOUS PROFILE</div>
    Age: 8m · Phone: 2 changes<br>₹1,50,000 · Pass-through: 55%
  </div>
  <div class="preset-item" style="border-color:rgba(0,210,130,0.3)">
    <div class="preset-head" style="color:#00d282">✅ LEGIT PROFILE</div>
    Age: 36m · Phone: 0 changes<br>₹25,000 · Pass-through: 10%
  </div>
</div>
""", unsafe_allow_html=True)

pb1, pb2, pb3 = st.columns(3)
with pb1:
    if st.button("🚨 Load Mule",       use_container_width=True):
        st.session_state.preset = "mule";       st.rerun()
with pb2:
    if st.button("⚠️ Load Suspicious", use_container_width=True):
        st.session_state.preset = "suspicious"; st.rerun()
with pb3:
    if st.button("✅ Load Legit",      use_container_width=True):
        st.session_state.preset = "legit";      st.rerun()

# ── ANALYZE BUTTON ─────────────────────────────────────────────────────────────
st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
analyze = st.button("🔍  ANALYZE ACCOUNT", type="primary", use_container_width=True)

if analyze:
    features   = np.array([[acct_age, phone_changes, txn_count, txn_amount, passthrough]])
    prediction = model.predict(features)[0]
    proba      = model.predict_proba(features)[0][1]
    score      = int(proba * 100)

    if score > 60:
        label, card_cls, icon, color, verdict = (
            "Mule", "card-mule", "🚨", "#ff415a", "MULE DETECTED")
        desc = ("This account shows strong money-mule characteristics. "
                "<strong>Immediate account freeze and AML investigation recommended.</strong>")
    elif score > 35:
        label, card_cls, icon, color, verdict = (
            "Suspicious", "card-sus", "⚠️", "#ffc400", "SUSPICIOUS ACCOUNT")
        desc = ("Several suspicious patterns detected. "
                "<strong>Manual review required before approving further transactions.</strong>")
    else:
        label, card_cls, icon, color, verdict = (
            "Legit", "card-legit", "✅", "#00d282", "LEGITIMATE ACCOUNT")
        desc = ("Account behaviour is consistent with normal usage. "
                "<strong>Continue standard monitoring.</strong>")

    # Result card
    st.markdown(f"""
    <div class="card {card_cls}">
      <div class="card-verdict" style="color:{color}">{icon} {verdict}</div>
      <div class="card-score">
        Risk Score: <strong style="color:{color};font-size:1.05rem">{score}%</strong>
        &nbsp;·&nbsp; Classification: <strong style="color:{color}">{label}</strong>
      </div>
      <div class="card-desc">{desc}</div>
    </div>
    """, unsafe_allow_html=True)

    # Progress meter
    st.markdown("**Risk Score Meter**")
    st.progress(score / 100)
    m1, m2, m3 = st.columns(3)
    m1.caption("🟢  0–35%  Safe")
    m2.caption("🟡  35–60%  Suspicious")
    m3.caption("🔴  60–100%  Mule")

    st.divider()

    # Feature contributions
    st.markdown('<div class="sec-label">// Feature Contributions</div>', unsafe_allow_html=True)
    feat_inputs = {
        "Pass-Through Ratio": min(100, passthrough * 1.2),
        "Account Age":        max(5,   100 - acct_age * 1.5),
        "Txn Amount":         min(100, txn_amount / 10000),
        "Txn Count":          min(100, txn_count * 0.8),
        "Phone Changes":      min(100, phone_changes * 22),
    }
    bars = ""
    for feat, (weight, col) in FEATS.items():
        w  = int(weight * 100)
        iv = round(feat_inputs[feat], 1)
        bars += f"""
        <div class="feat">
          <div class="feat-meta">
            <span style="color:#c9d4e0">{feat}</span>
            <span style="color:{col}">{w}% model weight &nbsp;·&nbsp; input signal: {iv}%</span>
          </div>
          <div class="feat-track">
            <div class="feat-fill" style="width:{w}%;background:{col}"></div>
          </div>
        </div>"""
    st.markdown(bars, unsafe_allow_html=True)

    st.divider()

    # Input summary metrics
    st.markdown('<div class="sec-label">// Input Summary</div>', unsafe_allow_html=True)
    s1, s2, s3 = st.columns(3)
    s1.metric("Account Age",   f"{acct_age} months")
    s2.metric("Phone Changes", phone_changes)
    s3.metric("Pass-Through",  f"{passthrough}%")
    s4, s5, _ = st.columns(3)
    s4.metric("Txn Count",  txn_count)
    s5.metric("Txn Amount", f"₹{txn_amount:,}")

    # Save to DB
    if save_to_db(acct_age, phone_changes, txn_count, txn_amount, passthrough, label, score):
        st.success("✅ Record saved to database (bank.db)")

    # ── EXPLORE MORE — links via components.html with target="_blank" ─────────
    st.divider()
    st.markdown('<div class="sec-label">// Explore More</div>', unsafe_allow_html=True)
    st.markdown(
        '<p style="color:#5a7a99;font-size:0.87rem;margin-bottom:12px">'
        'View full analytics, confusion matrix and detection trends in the dashboard.</p>',
        unsafe_allow_html=True)

    components.html(f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@600&display=swap');
      * {{ margin:0; padding:0; box-sizing:border-box; }}
      body {{ background:transparent; display:flex; gap:10px; flex-wrap:wrap; padding:4px 0; }}
      a {{
        font-family:'IBM Plex Mono',monospace; font-size:0.62rem;
        letter-spacing:1px; padding:9px 20px; border-radius:5px;
        text-decoration:none; display:inline-block; transition:all 0.15s;
      }}
      .primary {{ background:rgba(0,207,255,0.12); border:1px solid #00cfff; color:#00cfff; }}
      .primary:hover {{ background:rgba(0,207,255,0.22); }}
      .ghost {{ background:transparent; border:1px solid #1a3a55; color:#5a7a99; }}
      .ghost:hover {{ border-color:#00cfff; color:#00cfff; }}
    </style>
    </head>
    <body>
      <a class="primary" href="{DASHBOARD_URL}" target="_blank">&#128202; View Dashboard</a>
      <a class="ghost"   href="{PORTFOLIO_URL}" target="_blank">&#8592; Portfolio</a>
      <a class="ghost"   href="{GITHUB_URL}"    target="_blank">&#9095; GitHub Repo</a>
    </body>
    </html>
    """, height=52)

# ── FOOTER via components.html with target="_blank" ───────────────────────────
st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
components.html(f"""
<!DOCTYPE html>
<html>
<head>
<style>
  @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&display=swap');
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{
    background: #05080f;
    border-top: 1px solid #0d2035;
    padding: 14px 0;
    font-family: 'IBM Plex Mono', monospace;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 10px;
  }}
  .left  {{ font-size: 0.6rem; color: #2a4a66; }}
  .left span {{ color: #00cfff; }}
  .right {{ display: flex; gap: 16px; }}
  a {{
    font-size: 0.6rem; color: #00cfff;
    text-decoration: none; letter-spacing: 1px;
  }}
  a:hover {{ text-decoration: underline; }}
</style>
</head>
<body>
  <div class="left">Built by <span>Kamalakanta Behera</span> &middot; MCA Final Year &middot; Data Analyst</div>
  <div class="right">
    <a href="{PORTFOLIO_URL}" target="_blank">Portfolio</a>
    <a href="{DASHBOARD_URL}" target="_blank">Dashboard</a>
    <a href="{GITHUB_URL}"    target="_blank">GitHub</a>
  </div>
</body>
</html>
""", height=50)

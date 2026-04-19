"""
FertiliQ — AI Advisor
DM Serif Display + DM Sans. Premium health-tech. All pipeline logic unchanged.
Run: streamlit run app.py
"""

import os, sys, time
from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="FertiliQ",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))

# ─────────────────────────────────────────────────────────────────────────────
#  CSS
# ─────────────────────────────────────────────────────────────────────────────

CSS = """
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600&display=swap" rel="stylesheet">

<style>
/* ── variables ─────────────────────────────────────────────────────── */
:root {
  --serif:  'DM Serif Display', Georgia, serif;
  --sans:   'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  --teal:   #1B4D4D;
  --teal2:  #245f5f;
  --teal-bg:rgba(27,77,77,0.06);
  --gold:   #C9A84C;
  --amber:  #8A5C00;
  --bg:     #FFFFFF;
  --bg-soft:#FDFAF6;
  --bg-sb:  #F8F6F2;
  --border: #E8E2D9;
  --border2:#CFC9BF;
  --text:   #1A1A1A;
  --text2:  #374151;
  --muted:  #6B7280;
  --xmuted: #9CA3AF;
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.06), 0 1px 8px rgba(0,0,0,0.04);
  --shadow-md: 0 4px 16px rgba(0,0,0,0.08), 0 1px 4px rgba(0,0,0,0.04);
}

/* ── reset ─────────────────────────────────────────────────────────── */
*, *::before, *::after { box-sizing: border-box; }
html { font-size: 16px; }
html, body, [class*="css"] {
  font-family: var(--sans);
  font-weight: 300;
  -webkit-font-smoothing: antialiased;
  color: var(--text);
}

/* ── hide streamlit chrome ──────────────────────────────────────────── */
#MainMenu, footer, header,
.stDeployButton,
[data-testid="stDecoration"],
[data-testid="stToolbar"],
[data-testid="stStatusWidget"] { display: none !important; }

/* ── app shell ──────────────────────────────────────────────────────── */
.stApp { background: var(--bg) !important; }

/* ── main content block ─────────────────────────────────────────────── */
.main .block-container {
  max-width: 800px !important;
  padding: 2rem 2.5rem 6rem 2.5rem !important;
  margin: 0 auto !important;
}

/* ── sidebar ────────────────────────────────────────────────────────── */
section[data-testid="stSidebar"] {
  width: 272px !important;
  min-width: 272px !important;
  background: var(--bg-sb) !important;
  border-right: 1px solid var(--border) !important;
}
section[data-testid="stSidebar"] > div:first-child {
  width: 272px !important;
  padding: 0 !important;
  overflow-x: hidden !important;
  overflow-y: auto !important;
}

/* ── style ALL streamlit markdown output ────────────────────────────── */
/* This is the correct way — resp-body div across st.markdown calls fails */
[data-testid="stMarkdownContainer"] p {
  font-family: var(--sans) !important;
  font-size: 15px !important;
  font-weight: 300 !important;
  color: var(--text2) !important;
  line-height: 1.85 !important;
  margin-bottom: .8rem !important;
}
[data-testid="stMarkdownContainer"] p:last-child { margin-bottom: 0 !important; }
[data-testid="stMarkdownContainer"] strong {
  color: var(--text) !important;
  font-weight: 500 !important;
}
[data-testid="stMarkdownContainer"] em { font-style: italic !important; }
[data-testid="stMarkdownContainer"] ul,
[data-testid="stMarkdownContainer"] ol {
  font-family: var(--sans) !important;
  font-size: 15px !important;
  font-weight: 300 !important;
  color: var(--text2) !important;
  line-height: 1.85 !important;
  padding-left: 1.3rem !important;
  margin-bottom: .8rem !important;
}
[data-testid="stMarkdownContainer"] li {
  margin-bottom: .45rem !important;
  line-height: 1.85 !important;
}
[data-testid="stMarkdownContainer"] h3,
[data-testid="stMarkdownContainer"] h4 {
  font-family: var(--sans) !important;
  font-size: 11px !important;
  font-weight: 600 !important;
  letter-spacing: 0.09em !important;
  text-transform: uppercase !important;
  color: var(--teal) !important;
  margin: 1.4rem 0 .45rem !important;
}
[data-testid="stMarkdownContainer"] code {
  font-size: 13px !important;
  background: var(--teal-bg) !important;
  color: var(--teal) !important;
  padding: .1em .35em !important;
  border-radius: 4px !important;
}

/* ── text input — pill search bar ──────────────────────────────────── */
.stTextInput { width: 100% !important; }
.stTextInput > div { width: 100% !important; }
.stTextInput > div > div {
  display: flex !important;
  align-items: center !important;
  width: 100% !important;
  background: #FAFAF9 !important;
  border: 1.5px solid var(--border2) !important;
  border-radius: 24px !important;
  padding: .65rem 1.3rem !important;
  min-height: 50px !important;
  height: auto !important;
  transition: border-color .2s, box-shadow .2s !important;
  overflow: visible !important;
}
.stTextInput > div > div:focus-within {
  border-color: var(--teal) !important;
  box-shadow: 0 0 0 3px rgba(27,77,77,0.1) !important;
  background: #FFFFFF !important;
}
.stTextInput input {
  font-family: var(--sans) !important;
  font-size: 15px !important;
  font-weight: 300 !important;
  color: var(--text) !important;
  padding: 0 !important;
  margin: 0 !important;
  height: auto !important;
  line-height: 1.4 !important;
  background: transparent !important;
  caret-color: var(--teal) !important;
  border: none !important;
  outline: none !important;
  width: 100% !important;
  min-width: 0 !important;
  flex: 1 !important;
}
.stTextInput input::placeholder {
  color: var(--xmuted) !important;
  font-weight: 300 !important;
}
.stTextInput label { display: none !important; }

/* ── fix: vertically align search columns without breaking layout ───── */
[data-testid="stHorizontalBlock"] > [data-testid="column"] > div {
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 100%;
}

/* ── primary button (pill, teal) ────────────────────────────────────── */
.stButton > button[kind="primary"] {
  font-family: var(--sans) !important;
  font-size: 14px !important;
  font-weight: 500 !important;
  letter-spacing: 0.025em !important;
  color: #FFFFFF !important;
  background: var(--teal) !important;
  border: none !important;
  border-radius: 24px !important;
  height: 50px !important;
  padding: 0 1.4rem !important;
  width: 100% !important;
  transition: background .15s, box-shadow .15s, transform .1s !important;
  box-shadow: 0 2px 10px rgba(27,77,77,0.22) !important;
  white-space: nowrap !important;
}
.stButton > button[kind="primary"]:hover {
  background: var(--teal2) !important;
  box-shadow: 0 4px 16px rgba(27,77,77,0.3) !important;
  transform: translateY(-1px) !important;
}
.stButton > button[kind="primary"]:active {
  transform: translateY(0) !important;
  box-shadow: 0 1px 6px rgba(27,77,77,0.2) !important;
}

/* ── secondary buttons (suggestion pills) ───────────────────────────── */
.stButton > button:not([kind="primary"]) {
  font-family: var(--sans) !important;
  font-size: 14px !important;
  font-weight: 300 !important;
  color: var(--teal) !important;
  background: #FFFFFF !important;
  border: 1.5px solid var(--border) !important;
  border-radius: 24px !important;
  padding: .55rem 1.15rem !important;
  transition: border-color .15s, box-shadow .15s, background .15s !important;
  text-align: left !important;
  width: 100% !important;
  line-height: 1.5 !important;
  height: auto !important;
  white-space: normal !important;
}
.stButton > button:not([kind="primary"]):hover {
  border-color: var(--teal) !important;
  box-shadow: 0 2px 8px rgba(27,77,77,0.1) !important;
  background: #FAFDF8 !important;
}

/* ── expander ───────────────────────────────────────────────────────── */
.stExpander {
  border: 1.5px solid var(--border) !important;
  border-radius: 10px !important;
  background: #FFFFFF !important;
  overflow: hidden !important;
  box-shadow: var(--shadow-sm) !important;
  margin-bottom: .5rem !important;
}
.stExpander > details > summary {
  font-family: var(--sans) !important;
  font-size: 13px !important;
  font-weight: 400 !important;
  /* intentionally NOT uppercase — source titles would look wrong in caps */
  color: var(--muted) !important;
  padding: .8rem 1.1rem !important;
  background: var(--bg-soft) !important;
  border-bottom: 1px solid var(--border) !important;
  transition: color .15s, background .15s !important;
  user-select: none !important;
}
.stExpander > details > summary:hover {
  color: var(--teal) !important;
  background: #FAF7F2 !important;
}
.stExpander > details[open] > summary {
  color: var(--teal) !important;
  background: #FAF7F2 !important;
}
.stExpander [data-testid="stExpanderDetails"] {
  padding: 1.1rem 1.2rem !important;
  background: #FFFFFF !important;
}

/* ── spinner ────────────────────────────────────────────────────────── */
.stSpinner > div { border-top-color: var(--teal) !important; }
[data-testid="stSpinnerContainer"] p {
  font-family: var(--sans) !important;
  font-size: 14px !important;
  font-weight: 300 !important;
  color: var(--muted) !important;
}

/* ── alerts ─────────────────────────────────────────────────────────── */
[data-testid="stAlert"] {
  font-family: var(--sans) !important;
  font-size: 14px !important;
  font-weight: 300 !important;
  border-radius: 10px !important;
}

/* ══════════════════════════════════════════════════════════════════════
   SIDEBAR COMPONENTS
   ══════════════════════════════════════════════════════════════════════ */

.sb-top {
  padding: 1.6rem 1.35rem 1.35rem;
  border-bottom: 1px solid var(--border);
}
.sb-wordmark {
  font-family: var(--sans);
  font-size: 13px;
  font-weight: 600;
  color: var(--teal);
  letter-spacing: 0.07em;
  text-transform: uppercase;
  display: flex;
  align-items: center;
  gap: 7px;
}
.sb-wordmark-dot {
  width: 7px; height: 7px;
  border-radius: 50%;
  background: var(--gold);
  flex-shrink: 0;
}
.sb-version {
  font-size: 11px;
  font-weight: 300;
  color: var(--xmuted);
  margin-top: 4px;
  letter-spacing: 0.03em;
}

.sb-section {
  padding: 1.1rem 1.35rem .4rem;
}
.sb-section-label {
  font-size: 9px;
  font-weight: 500;
  letter-spacing: 0.13em;
  text-transform: uppercase;
  color: var(--xmuted);
  display: block;
  margin-bottom: .5rem;
}

.sb-item {
  padding: .55rem 1.35rem;
  transition: background .12s;
  border-radius: 0;
}
.sb-item:hover { background: rgba(27,77,77,0.04); }
.sb-item-q {
  font-size: 12.5px;
  font-weight: 300;
  color: var(--text2);
  line-height: 1.5;
  word-break: break-word;
  white-space: normal;
  display: block;
}
.sb-item-meta {
  font-size: 11px;
  font-weight: 300;
  color: var(--xmuted);
  margin-top: 3px;
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 4px;
  letter-spacing: 0.02em;
}
.sb-cf-dot {
  display: inline-block;
  width: 5px; height: 5px;
  border-radius: 50%;
  background: var(--gold);
  flex-shrink: 0;
}

.sb-divider {
  height: 1px;
  background: var(--border);
  margin: .5rem 1.35rem;
}

.sb-stats {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 1px;
  margin: .25rem 1.35rem .75rem;
  border: 1.5px solid var(--border);
  border-radius: 9px;
  overflow: hidden;
  background: var(--border);
}
.sb-stat {
  padding: .65rem .4rem;
  background: #FFFFFF;
  text-align: center;
}
.sb-stat-n {
  font-size: 17px;
  font-weight: 600;
  color: var(--teal);
  display: block;
  line-height: 1;
  font-feature-settings: 'tnum';
}
.sb-stat-l {
  font-size: 9px;
  font-weight: 400;
  letter-spacing: 0.09em;
  text-transform: uppercase;
  color: var(--xmuted);
  display: block;
  margin-top: 4px;
}

.sb-footer {
  padding: 1.2rem 1.35rem;
  border-top: 1px solid var(--border);
  margin-top: .5rem;
}
.sb-footer-text {
  font-size: 10.5px;
  font-weight: 300;
  color: var(--xmuted);
  line-height: 1.6;
}
.sb-footer-text strong {
  font-weight: 500;
  color: var(--muted);
}

/* ══════════════════════════════════════════════════════════════════════
   MAIN CONTENT COMPONENTS
   ══════════════════════════════════════════════════════════════════════ */

/* ── hero ───────────────────────────────────────────────────────────── */
.hero {
  padding: 3.75rem 0 2.5rem;
}
.hero-eyebrow {
  font-size: 10.5px;
  font-weight: 400;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--gold);
  margin-bottom: .95rem;
  display: flex;
  align-items: center;
  gap: 8px;
}
.hero-eyebrow-bar {
  display: inline-block;
  width: 20px; height: 1.5px;
  background: var(--gold);
  border-radius: 2px;
  flex-shrink: 0;
}
.hero-title {
  font-family: var(--serif);
  font-size: 2.9rem;
  font-weight: 400;
  color: var(--teal);
  letter-spacing: -0.02em;
  line-height: 1.14;
  margin-bottom: .8rem;
}
.hero-title em {
  font-style: italic;
  color: #2A7272;
}
.hero-sub {
  font-size: 14.5px;
  font-weight: 300;
  color: var(--muted);
  line-height: 1.75;
  white-space: nowrap;
}

/* ── suggestion pills label ─────────────────────────────────────────── */
.suggest-label {
  font-size: 9.5px;
  font-weight: 500;
  letter-spacing: 0.13em;
  text-transform: uppercase;
  color: var(--xmuted);
  display: block;
  margin: 2rem 0 .7rem;
}

/* ── search row bottom margin ───────────────────────────────────────── */
.search-gap { margin-bottom: .5rem; }

/* ── query echo ─────────────────────────────────────────────────────── */
.q-echo {
  margin: 2rem 0 0;
  padding: 1.25rem 1.5rem;
  background: var(--bg-soft);
  border: 1.5px solid var(--border);
  border-radius: 12px;
}
.q-echo-label {
  font-size: 9.5px;
  font-weight: 500;
  letter-spacing: 0.13em;
  text-transform: uppercase;
  color: var(--xmuted);
  display: block;
  margin-bottom: .45rem;
}
.q-echo-text {
  font-size: 15.5px;
  font-weight: 400;
  color: var(--teal);
  line-height: 1.55;
}

/* ── response section header ────────────────────────────────────────── */
.resp-header {
  display: flex;
  align-items: center;
  gap: .6rem;
  padding: 1.5rem 0 1.1rem;
  border-bottom: 1.5px solid var(--border);
  margin-bottom: 1.2rem;
}
.resp-dot {
  width: 6px; height: 6px;
  border-radius: 50%;
  background: var(--gold);
  flex-shrink: 0;
}
.resp-label {
  font-size: 9.5px;
  font-weight: 600;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--teal);
}
.resp-spacer { flex: 1; }
.resp-latency {
  font-size: 11px;
  font-weight: 400;
  color: var(--xmuted);
  letter-spacing: 0.03em;
  background: var(--bg-soft);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: .15rem .6rem;
}
.resp-cf-badge {
  font-size: 10px;
  font-weight: 500;
  letter-spacing: 0.07em;
  color: var(--amber);
  background: rgba(201,168,76,0.1);
  border: 1px solid rgba(201,168,76,0.3);
  border-radius: 20px;
  padding: .15rem .65rem;
}

/* ── source row ─────────────────────────────────────────────────────── */
.source-row {
  margin-top: 1.4rem;
  padding-top: 1.1rem;
  border-top: 1.5px solid var(--border);
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .4rem;
}
.source-row-label {
  font-size: 9.5px;
  font-weight: 500;
  letter-spacing: 0.13em;
  text-transform: uppercase;
  color: var(--xmuted);
  margin-right: .15rem;
  flex-shrink: 0;
}
/* pill chips */
.stag {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-family: var(--sans);
  font-size: 12px;
  font-weight: 400;
  letter-spacing: 0.02em;
  border-radius: 20px;
  padding: .22rem .75rem;
  white-space: nowrap;
  max-width: 230px;
  overflow: hidden;
  text-overflow: ellipsis;
  border: 1.5px solid transparent;
  transition: box-shadow .15s;
}
.stag.doc   { color: var(--teal);  background: rgba(27,77,77,0.06);   border-color: rgba(27,77,77,0.15); }
.stag.blog  { color: var(--amber); background: rgba(201,168,76,0.08); border-color: rgba(201,168,76,0.2); }
.stag.forum { color: var(--muted); background: #F3F4F6; border-color: #DDE0E5; }
.stag.cf    { box-shadow: 0 0 0 2px rgba(201,168,76,0.4); }
.stag-pip   { width: 5px; height: 5px; border-radius: 50%; flex-shrink: 0; }
.stag.doc  .stag-pip { background: var(--teal); }
.stag.blog .stag-pip { background: var(--gold); }
.stag.forum .stag-pip{ background: var(--xmuted); }

/* ── source expanders section header ────────────────────────────────── */
.src-exp-label {
  font-size: 9.5px;
  font-weight: 500;
  letter-spacing: 0.13em;
  text-transform: uppercase;
  color: var(--xmuted);
  display: block;
  margin: 1.25rem 0 .55rem;
}

/* ── conflict banner ────────────────────────────────────────────────── */
.cp {
  margin: 1.5rem 0 .5rem;
  border: 1.5px solid #ECD87A;
  border-left: 4px solid var(--gold);
  border-radius: 12px;
  padding: 1.35rem 1.4rem 1.2rem;
  background: #FFFCF0;
}
.cp-top {
  display: flex;
  align-items: center;
  gap: .6rem;
  margin-bottom: .7rem;
}
.cp-title {
  font-size: 13.5px;
  font-weight: 500;
  color: var(--amber);
}
.cp-badge {
  margin-left: auto;
  font-size: 10px;
  font-weight: 500;
  letter-spacing: 0.09em;
  text-transform: uppercase;
  color: var(--amber);
  background: rgba(201,168,76,0.1);
  border: 1px solid rgba(201,168,76,0.28);
  border-radius: 20px;
  padding: .18rem .6rem;
}
.cp-desc {
  font-size: 13.5px;
  font-weight: 300;
  color: var(--muted);
  line-height: 1.8;
  margin-bottom: .9rem;
}
.cp-bar-row {
  display: flex;
  align-items: center;
  gap: .7rem;
  margin-bottom: 1rem;
}
.cp-bar-label {
  font-size: 10.5px;
  font-weight: 400;
  color: var(--xmuted);
  white-space: nowrap;
  letter-spacing: 0.05em;
}
.cp-bar-track {
  flex: 1; height: 3px;
  background: #EDE8D4;
  border-radius: 3px; overflow: hidden;
}
.cp-bar-fill {
  height: 100%; border-radius: 3px;
  background: var(--gold);
  transition: width .7s cubic-bezier(.4,0,.2,1);
}
.cp-bar-pct {
  font-size: 11px;
  color: var(--amber);
  font-weight: 500;
  white-space: nowrap;
}
.cp-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: .8rem;
}
.cp-side {
  border: 1.5px solid #EDE8D4;
  border-radius: 9px;
  padding: .95rem 1.05rem;
  background: #FFFFFF;
}
.cp-side-lbl {
  font-size: 9.5px;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 4px;
}
.cp-side.newer .cp-side-lbl { color: var(--teal); }
.cp-side.older .cp-side-lbl { color: var(--xmuted); }
.cp-side-src {
  font-size: 11px;
  font-weight: 300;
  color: var(--xmuted);
  margin-bottom: 5px;
  letter-spacing: 0.02em;
}
.cp-side-text {
  font-size: 12.5px;
  font-weight: 300;
  color: #4B5563;
  line-height: 1.7;
}

/* ── retrieval detail stat cells ────────────────────────────────────── */
.rd-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: .6rem;
  margin-bottom: 1.2rem;
}
.rd-cell {
  border: 1.5px solid var(--border);
  border-radius: 9px;
  padding: .85rem .75rem;
  text-align: center;
  background: var(--bg-soft);
}
.rd-val {
  display: block;
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--teal);
  line-height: 1;
  font-feature-settings: 'tnum';
}
.rd-lbl {
  display: block;
  font-size: 9px;
  font-weight: 400;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--xmuted);
  margin-top: 5px;
}

/* ── chunk cards in retrieval expander ──────────────────────────────── */
.ck {
  border: 1.5px solid var(--border);
  border-radius: 9px;
  overflow: hidden;
  margin-bottom: .6rem;
  background: #FFFFFF;
}
.ck.ck-cf { border-color: #ECD87A; }
.ck-head {
  display: flex;
  align-items: center;
  gap: .5rem;
  padding: .55rem .9rem;
  background: var(--bg-soft);
  border-bottom: 1px solid var(--border);
}
.ck.ck-cf .ck-head { background: #FFFCF0; border-bottom-color: #ECD87A; }
.ck-src {
  font-size: 9.5px;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: .18rem .5rem;
  border-radius: 20px;
  flex-shrink: 0;
}
.ck-src.doc   { color: var(--teal);  background: rgba(27,77,77,0.08); }
.ck-src.blog  { color: var(--amber); background: rgba(201,168,76,0.12); }
.ck-src.forum { color: var(--muted); background: #F3F4F6; }
.ck-title {
  font-size: 12.5px;
  font-weight: 400;
  color: var(--text2);
  flex: 1;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.ck-date {
  font-size: 11px;
  font-weight: 300;
  color: var(--xmuted);
  margin-left: auto;
  white-space: nowrap;
  flex-shrink: 0;
}
.ck-body {
  padding: .75rem .9rem;
  font-size: 12.5px;
  font-weight: 300;
  line-height: 1.72;
  color: var(--muted);
  max-height: 108px;
  overflow: hidden;
  position: relative;
}
.ck-body::after {
  content: '';
  position: absolute;
  bottom: 0; left: 0; right: 0;
  height: 32px;
  background: linear-gradient(transparent, #FFFFFF);
  pointer-events: none;
}

/* ── thin rule ──────────────────────────────────────────────────────── */
.thin-rule {
  height: 1.5px;
  background: var(--border);
  margin: 1.5rem 0;
  border: none;
  border-radius: 2px;
}

/* ── responsive ─────────────────────────────────────────────────────── */
@media (max-width: 960px) {
  .main .block-container { padding: 1.5rem 1.25rem 5rem !important; }
  .hero-title  { font-size: 2.2rem; }
  .hero-sub    { white-space: normal; }
  .cp-grid     { grid-template-columns: 1fr; }
  .rd-row      { grid-template-columns: repeat(2, 1fr); }
}
</style>
"""


# ─────────────────────────────────────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────────────────────────────────────

EXAMPLE_QUERIES = [
    "I have MTHFR C677T — what should I take?",
    "What does a low AMH mean for fertility?",
    "What CoQ10 dose is right for egg quality at 38?",
    "When is the best time to try to conceive?",
    "My vitamin D is 18 ng/mL — what do I do?",
]

def _esc(t: str) -> str:
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def _src_css(src: str) -> str:
    return {"documentation": "doc", "blog": "blog", "forum": "forum"}.get(src, "forum")

def _year(chunk) -> int:
    try:
        return int(str(chunk.metadata.get("date", "2020"))[:4])
    except Exception:
        return 2020

def _stag_html(src: str, title: str, conflict: bool = False) -> str:
    css = _src_css(src)
    short = (title[:38] + "…") if len(title) > 38 else title
    cf = " cf" if conflict else ""
    return (f'<span class="stag {css}{cf}" title="{_esc(title)}">'
            f'<span class="stag-pip"></span>{_esc(short)}</span>')

def _fmt_latency(ms: int) -> str:
    if ms < 1000:
        return f"{ms} ms"
    return f"{ms / 1000:.1f}s"


# ─────────────────────────────────────────────────────────────────────────────
#  SIDEBAR
# ─────────────────────────────────────────────────────────────────────────────

def render_sidebar(log_entries, doc_col, forum_col, blog_col):
    with st.sidebar:
        # Brand
        st.markdown("""
        <div class="sb-top">
          <div class="sb-wordmark">
            <span class="sb-wordmark-dot"></span>FertiliQ
          </div>
          <div class="sb-version">AI Health Advisor · v2.1</div>
        </div>
        """, unsafe_allow_html=True)

        # Recent queries
        st.markdown("""
        <div class="sb-section">
          <span class="sb-section-label">Recent queries</span>
        </div>
        """, unsafe_allow_html=True)

        if log_entries:
            for e in reversed(log_entries[-5:]):
                q   = e.get("query", "")
                ts  = e.get("timestamp", "")[:10]
                lat = _fmt_latency(e.get("latency_ms", 0))
                cf  = '<span class="sb-cf-dot"></span>' if e.get("contradictions_detected") else ""
                st.markdown(f"""
                <div class="sb-item">
                  <div class="sb-item-q">{_esc(q)}</div>
                  <div class="sb-item-meta">{cf}<span>{ts}</span>
                  <span style="color:var(--border)">·</span>
                  <span>{lat}</span></div>
                </div>""", unsafe_allow_html=True)
        else:
            st.markdown(
                '<div class="sb-item">'
                '<div class="sb-item-q" style="font-style:italic;color:var(--xmuted)">'
                'No queries yet</div></div>',
                unsafe_allow_html=True)

        st.markdown('<div class="sb-divider"></div>', unsafe_allow_html=True)

        # Knowledge base
        st.markdown("""
        <div class="sb-section">
          <span class="sb-section-label">Knowledge base</span>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(f"""
        <div class="sb-stats">
          <div class="sb-stat">
            <span class="sb-stat-n">{doc_col.count()}</span>
            <span class="sb-stat-l">Docs</span>
          </div>
          <div class="sb-stat">
            <span class="sb-stat-n">{forum_col.count()}</span>
            <span class="sb-stat-l">Forum</span>
          </div>
          <div class="sb-stat">
            <span class="sb-stat-n">{blog_col.count()}</span>
            <span class="sb-stat-l">Blog</span>
          </div>
        </div>""", unsafe_allow_html=True)

        # Performance
        if log_entries:
            n        = len(log_entries)
            n_cf     = sum(1 for e in log_entries if e.get("contradictions_detected"))
            cf_pct   = f"{n_cf / n * 100:.0f}%"
            avg_lat  = f"{sum(e.get('latency_ms', 0) for e in log_entries) / n / 1000:.0f}s"
            st.markdown('<div class="sb-divider"></div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="sb-section">
              <span class="sb-section-label">Session performance</span>
            </div>
            """, unsafe_allow_html=True)
            st.markdown(f"""
            <div class="sb-stats">
              <div class="sb-stat">
                <span class="sb-stat-n">{n}</span>
                <span class="sb-stat-l">Queries</span>
              </div>
              <div class="sb-stat">
                <span class="sb-stat-n">{cf_pct}</span>
                <span class="sb-stat-l">Conflict</span>
              </div>
              <div class="sb-stat">
                <span class="sb-stat-n">{avg_lat}</span>
                <span class="sb-stat-l">Avg time</span>
              </div>
            </div>""", unsafe_allow_html=True)

        # Footer
        st.markdown("""
        <div class="sb-footer">
          <div class="sb-footer-text">
            <strong>FertiliQ RAG</strong> · Hybrid retrieval with
            contradiction detection. Sources ranked by credibility,
            recency, and relevance.
          </div>
        </div>
        """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
#  HERO
# ─────────────────────────────────────────────────────────────────────────────

def render_hero():
    st.markdown("""
    <div class="hero">
      <div class="hero-eyebrow">
        <span class="hero-eyebrow-bar"></span>
        Preconception intelligence
      </div>
      <h1 class="hero-title">Your fertility,<br><em>answered clearly.</em></h1>
      <p class="hero-sub">Ask about your genetics, biomarkers, nutrition, supplements, or conception timing.</p>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
#  EMPTY STATE
# ─────────────────────────────────────────────────────────────────────────────

def render_suggestions() -> str | None:
    st.markdown('<span class="suggest-label">Common questions</span>',
                unsafe_allow_html=True)
    for i, q in enumerate(EXAMPLE_QUERIES):
        if st.button(q, key=f"sq_{i}", type="secondary"):
            return q
    return None


# ─────────────────────────────────────────────────────────────────────────────
#  CONFLICT PANEL
# ─────────────────────────────────────────────────────────────────────────────

def render_conflict(result, top3, ContradictionUnit):
    units = [i for i in top3 if isinstance(i, ContradictionUnit)]
    if not units:
        return
    u    = units[0]
    conf = result["contradiction_confidence"]
    pct  = int(conf * 100)
    lvl  = "High confidence" if conf > .7 else "Moderate confidence" if conf > .4 else "Low confidence"
    ctype = u.contradiction_type.capitalize()

    newer, older = ((u.chunk_a, u.chunk_b) if _year(u.chunk_a) >= _year(u.chunk_b)
                    else (u.chunk_b, u.chunk_a))

    def _side(chunk, cls, lbl):
        src   = chunk.metadata.get("source_type", "").capitalize()
        ver   = chunk.metadata.get("version", "")
        date  = chunk.metadata.get("date", "")[:7]
        src_s = (f"{src} {ver}".strip() + f" · {date}").strip(" ·")
        text  = _esc(chunk.content[:200])
        return (f'<div class="cp-side {cls}">'
                f'<div class="cp-side-lbl">{lbl}</div>'
                f'<div class="cp-side-src">{src_s}</div>'
                f'<div class="cp-side-text">{text}…</div>'
                f'</div>')

    st.markdown(f"""
    <div class="cp">
      <div class="cp-top">
        <span style="font-size:14px">⚠</span>
        <span class="cp-title">Conflicting information detected</span>
        <span class="cp-badge">{ctype}</span>
      </div>
      <div class="cp-desc">{_esc(u.description or "Two sources disagree on this topic.")}</div>
      <div class="cp-bar-row">
        <span class="cp-bar-label">Confidence</span>
        <div class="cp-bar-track">
          <div class="cp-bar-fill" style="width:{pct}%"></div>
        </div>
        <span class="cp-bar-pct">{pct}% · {lvl}</span>
      </div>
      <div class="cp-grid">
        {_side(newer, "newer", "Current guidance")}
        {_side(older, "older", "Superseded")}
      </div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
#  RESPONSE
# ─────────────────────────────────────────────────────────────────────────────

def render_response(query, result, top3, ContradictionUnit, Chunk):
    # ── Query echo ──────────────────────────────────────────────────────────
    st.markdown(f"""
    <div class="q-echo">
      <span class="q-echo-label">Your question</span>
      <div class="q-echo-text">{_esc(query)}</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Response header ─────────────────────────────────────────────────────
    # Correctly rendered as a single self-contained block
    lat_badge  = f'<span class="resp-latency">{_fmt_latency(result["latency_ms"])}</span>'
    cf_badge   = ('<span class="resp-cf-badge">⚠ Conflict detected</span>'
                  if result["contradictions_present"] else "")
    st.markdown(f"""
    <div class="resp-header">
      <span class="resp-dot"></span>
      <span class="resp-label">FertiliQ Answer</span>
      <span class="resp-spacer"></span>
      {cf_badge}
      {lat_badge}
    </div>
    """, unsafe_allow_html=True)

    # ── Response body ───────────────────────────────────────────────────────
    # st.markdown renders into [data-testid="stMarkdownContainer"] — styled
    # globally via CSS. Do NOT wrap across multiple st.markdown calls.
    raw  = result["response"]
    body = raw[:raw.index("**Sources:**")].strip() if "**Sources:**" in raw else raw.strip()
    st.markdown(body)

    # ── Source chips — one per top3 slot (max 3) ────────────────────────────
    # ContradictionUnit counts as ONE slot, shown with conflict marker.
    tags = ""
    for item in top3:
        if isinstance(item, ContradictionUnit):
            # Use newer chunk's metadata for the chip label
            newer = (item.chunk_a if _year(item.chunk_a) >= _year(item.chunk_b)
                     else item.chunk_b)
            tags += _stag_html(newer.metadata.get("source_type", "forum"),
                               newer.metadata.get("title", ""), conflict=True)
        elif isinstance(item, Chunk):
            tags += _stag_html(item.metadata.get("source_type", "forum"),
                               item.metadata.get("title", ""))

    st.markdown(f"""
    <div class="source-row">
      <span class="source-row-label">Sources</span>
      {tags}
    </div>
    """, unsafe_allow_html=True)

    # ── Source expanders — one per top3 slot (max 3) ─────────────────────────
    st.markdown('<span class="src-exp-label">Read source excerpts</span>',
                unsafe_allow_html=True)
    src_icon = {"doc": "📄", "blog": "✍️", "forum": "💬"}

    for item in top3:
        if isinstance(item, ContradictionUnit):
            # Single expander showing both conflicting sides
            newer = (item.chunk_a if _year(item.chunk_a) >= _year(item.chunk_b)
                     else item.chunk_b)
            older = item.chunk_b if newer is item.chunk_a else item.chunk_a
            n_title = newer.metadata.get("title", "")
            n_date  = newer.metadata.get("date", "")
            n_css   = _src_css(newer.metadata.get("source_type", "forum"))
            short   = (n_title[:46] + "…") if len(n_title) > 46 else n_title
            label   = f"{src_icon.get(n_css, '📎')}  {short}  ·  {n_date}  ·  ⚠ Conflict"
            with st.expander(label):
                st.markdown(f"**Current guidance** ({newer.metadata.get('date','')[:7]})")
                st.markdown(newer.content)
                st.markdown("---")
                st.markdown(f"**Superseded** ({older.metadata.get('date','')[:7]})")
                st.markdown(older.content)
        elif isinstance(item, Chunk):
            css   = _src_css(item.metadata.get("source_type", "forum"))
            icon  = src_icon.get(css, "📎")
            title = item.metadata.get("title", "")
            date  = item.metadata.get("date", "")
            short = (title[:50] + "…") if len(title) > 50 else title
            with st.expander(f"{icon}  {short}  ·  {date}"):
                st.markdown(item.content)


# ─────────────────────────────────────────────────────────────────────────────
#  RETRIEVAL DETAILS EXPANDER
# ─────────────────────────────────────────────────────────────────────────────

def render_details(result, top3, ContradictionUnit, Chunk):
    conf_s = (f"{result['contradiction_confidence']:.2f}"
              if result["contradictions_present"] else "—")
    with st.expander("🔍  Retrieval details", expanded=False):
        st.markdown(f"""
        <div class="rd-row">
          <div class="rd-cell">
            <span class="rd-val">30</span>
            <span class="rd-lbl">Retrieved</span>
          </div>
          <div class="rd-cell">
            <span class="rd-val">{result['after_dedup']}</span>
            <span class="rd-lbl">After dedup</span>
          </div>
          <div class="rd-cell">
            <span class="rd-val">{_fmt_latency(result['latency_ms'])}</span>
            <span class="rd-lbl">Latency</span>
          </div>
          <div class="rd-cell">
            <span class="rd-val">{conf_s}</span>
            <span class="rd-lbl">Conflict conf.</span>
          </div>
        </div>
        """, unsafe_allow_html=True)

        for item in top3:
            pairs = ([(item.chunk_a, True), (item.chunk_b, True)]
                     if isinstance(item, ContradictionUnit) else [(item, False)])
            for ch, is_cf in pairs:
                src    = ch.metadata.get("source_type", "forum")
                css    = _src_css(src)
                title  = ch.metadata.get("title", "")
                date   = ch.metadata.get("date", "")
                body   = _esc(ch.content[:350])
                cf_cls = " ck-cf" if is_cf else ""
                st.markdown(f"""
                <div class="ck{cf_cls}">
                  <div class="ck-head">
                    <span class="ck-src {css}">{src}</span>
                    <span class="ck-title">{_esc(title)}</span>
                    <span class="ck-date">{date}</span>
                  </div>
                  <div class="ck-body">{body}…</div>
                </div>
                """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
#  PIPELINE  (logic unchanged)
# ─────────────────────────────────────────────────────────────────────────────

@st.cache_resource(show_spinner="Loading knowledge base…")
def load_system():
    from src.ingest import GeminiEmbeddingFunction, get_chroma_client, get_collections
    from src.gemini_client import get_client
    api_key = os.environ.get("GEMINI_API_KEY", "")
    if not api_key:
        st.error("GEMINI_API_KEY not set.")
        st.stop()
    get_client()
    ef = GeminiEmbeddingFunction()
    cl = get_chroma_client()
    dc, fc, bc = get_collections(cl, ef)
    if dc.count() == 0:
        st.error("ChromaDB empty — run generate_data.py then src/ingest.py.")
        st.stop()
    return dc, fc, bc


def run_query(query, dc, fc, bc):
    from src.retrieval import hybrid_search
    from src.reranking import (Chunk, deduplicate, detect_contradictions,
                               embed_chunks, llm_rerank)
    from src.generation import generate_response, get_top3_source_metadata
    from src.logger import log_query
    t0  = time.time()
    raw = hybrid_search(query, dc, fc, bc, top_k_per_col=10)
    chunks = [Chunk(id=r["id"],
                    content=r.get("metadata", {}).get("parent_content") or r["content"],
                    metadata=r["metadata"],
                    rrf_score=r.get("rrf_score", 0.))
              for r in raw]
    embed_chunks(chunks)
    deduped         = deduplicate(chunks, threshold=0.85)
    units, clean    = detect_contradictions(deduped)
    top3, _         = llm_rerank(units, clean, query)
    response, conf, conflicts = generate_response(query, top3)
    latency_ms      = int((time.time() - t0) * 1000)
    log_query(query=query,
              candidates_retrieved=len(raw),
              after_dedup=len(deduped),
              contradictions_detected=conflicts,
              contradiction_types=[u.contradiction_type for u in units],
              contradiction_confidence=conf if conflicts else 0.,
              top3_sources=get_top3_source_metadata(top3),
              response_generated=True,
              latency_ms=latency_ms)
    return dict(response=response,
                contradiction_confidence=conf,
                contradictions_present=conflicts,
                contradiction_types=[u.contradiction_type for u in units],
                top3=top3,
                after_dedup=len(deduped),
                latency_ms=latency_ms)


# ─────────────────────────────────────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    from src.logger import read_log
    from src.reranking import Chunk, ContradictionUnit

    st.markdown(CSS, unsafe_allow_html=True)

    dc, fc, bc  = load_system()
    log_entries = read_log()

    render_sidebar(log_entries, dc, fc, bc)

    if "active_q" not in st.session_state:
        st.session_state.active_q = ""

    # ── Hero ─────────────────────────────────────────────────────────────────
    render_hero()

    # ── Search bar ───────────────────────────────────────────────────────────
    c_in, c_btn = st.columns([5, 1])
    with c_in:
        typed = st.text_input(
            "q",
            placeholder="Ask anything about your genetics or fertility…",
            label_visibility="collapsed",
            key="qi",
        )
    with c_btn:
        go = st.button("Ask →", type="primary", use_container_width=True)

    # ── Empty state ───────────────────────────────────────────────────────────
    if not typed and not go and not st.session_state.active_q:
        pick = render_suggestions()
        if pick:
            st.session_state.active_q = pick
            st.rerun()
        return

    if go and not typed.strip():
        st.warning("Please enter a question.")
        return

    final_q = typed.strip() if (go and typed.strip()) else st.session_state.active_q
    if not final_q:
        return
    st.session_state.active_q = ""

    # ── Run pipeline ──────────────────────────────────────────────────────────
    with st.spinner("Searching knowledge base and generating answer…"):
        try:
            result = run_query(final_q, dc, fc, bc)
        except Exception as e:
            st.error(f"Pipeline error: {e}")
            st.exception(e)
            return

    # ── Conflict panel (before answer) ────────────────────────────────────────
    if result["contradictions_present"]:
        render_conflict(result, result["top3"], ContradictionUnit)

    # ── Answer + sources ──────────────────────────────────────────────────────
    render_response(final_q, result, result["top3"], ContradictionUnit, Chunk)

    # ── Retrieval details ─────────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    render_details(result, result["top3"], ContradictionUnit, Chunk)


if __name__ == "__main__":
    main()

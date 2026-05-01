import matplotlib.pyplot as plt

# ---------- TRIGGERS ----------
def generate_triggers(confidence):
    triggers = []
    if confidence < 40:
        triggers.append("Low confidence score detected")
    if confidence < 60:
        triggers.append("Possible inconsistencies found")
    if confidence > 80:
        triggers.append("High consistency detected")
    return triggers

# ---------- TRUST SCORE ----------
def calculate_trust_score(confidence, triggers):
    return max(0, min(confidence - len(triggers)*5, 100))

# ---------- LABEL ----------
def get_risk_label(score):
    if score > 80:
        return "SAFE"
    elif score > 50:
        return "SUSPICIOUS"
    else:
        return "FRAUD"

# ---------- REASONS ----------
def get_reasons(triggers):
    return triggers if triggers else ["No major issues detected"]

# ---------- PLOTS (CREATIVE + SMALL) ----------

def plot_trust_gauge(score):
    fig, ax = plt.subplots(figsize=(4,3))
    ax.barh(['Score'], [score])
    ax.set_xlim(0,100)
    ax.set_title("Trust Score", fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.5)
    return fig


def plot_score_breakdown(score):
    fig, ax = plt.subplots(figsize=(4,3))
    ax.pie([score, 100-score], labels=['Trust','Risk'], autopct='%1.1f%%')
    ax.set_title("Score Breakdown", fontsize=12)
    return fig


def plot_risk_factors(confidence, triggers):
    fig, ax = plt.subplots(figsize=(4,3))
    ax.bar(['Confidence','Risk'], [confidence, len(triggers)*10])
    ax.set_title("Risk Factors", fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.5)
    return fig


def plot_ml_probability(confidence, triggers):
    fig, ax = plt.subplots(figsize=(4,3))
    ax.bar(['Safe','Fraud'], [confidence, 100-confidence])
    ax.set_title("ML Prediction", fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.5)
    return fig
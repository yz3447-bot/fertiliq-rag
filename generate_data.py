"""
FertiliQ Synthetic Data Generator
Generates documentation, forum posts, and blog chunks for the RAG knowledge base.
Includes deliberate temporal and version contradictions for testing.
Run: python generate_data.py
"""

import json
from pathlib import Path

# ─────────────────────────────────────────────────────────────────────────────
# DOCUMENTATION  (parent-child structure; is_parent=True entries are parents)
# ─────────────────────────────────────────────────────────────────────────────

DOCUMENTATION = [

    # ═══════════════════════════════════════════════════════════════════════
    # PARENT 001: Platform Overview
    # ═══════════════════════════════════════════════════════════════════════
    {
        "id": "doc_parent_001",
        "is_parent": True,
        "content": (
            "# FertiliQ Platform Overview\n\n"
            "FertiliQ is a precision preconception health platform combining genetic testing and "
            "real-time biomarker monitoring to deliver personalised fertility-optimisation plans. "
            "Unlike generic apps, FertiliQ interprets your genetic variants (MTHFR, COMT, VDR) "
            "alongside laboratory biomarkers (AMH, FSH, LH, Vitamin D, CoQ10, iron) to build a "
            "dynamic evidence-based programme tailored to your unique biology.\n\n"
            "## Core Features\n"
            "- Genetic variant interpretation with clinical significance scoring\n"
            "- Real-time biomarker dashboard with optimal-range visualisation\n"
            "- AI-driven supplement, nutrition and exercise recommendations\n"
            "- Cycle-phase-aware activity guidelines\n"
            "- Partner health integration for couples\n"
            "- Quarterly reports for healthcare providers\n\n"
            "## Philosophy\n"
            "Traditional fertility assessments capture a single hormone snapshot. "
            "FertiliQ takes a systems approach, analysing how your genes shape nutrient metabolism, "
            "hormone regulation and stress response, then translating that into actionable steps."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-01-15",
            "title": "FertiliQ Platform Overview",
            "version": "v2.1",
            "parent_id": None
        }
    },
    {
        "id": "doc_child_001",
        "is_parent": False,
        "content": (
            "## What is FertiliQ?\n\n"
            "FertiliQ combines direct-to-consumer genetic testing with lab biomarker integration "
            "to provide couples with a personalised preconception health roadmap. The platform "
            "covers nutrition, supplementation, exercise, sleep, stress management and sexual "
            "health — all calibrated to the user's specific genetic profile and current biomarker "
            "levels. FertiliQ is not a medical device; recommendations are evidence-based but "
            "should complement, not replace, clinical care."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-01-15",
            "title": "What is FertiliQ?",
            "version": "v2.1",
            "parent_id": "doc_parent_001",
            "parent_title": "FertiliQ Platform Overview"
        }
    },
    {
        "id": "doc_child_002",
        "is_parent": False,
        "content": (
            "## Who is FertiliQ For?\n\n"
            "FertiliQ is designed for individuals and couples actively planning conception, "
            "those with unexplained infertility, women with irregular cycles, partners with "
            "sub-optimal semen analysis results, and anyone wanting to optimise preconception "
            "health before IVF or other assisted reproduction. The platform is particularly "
            "valuable for people who carry genetic variants known to influence nutrient metabolism "
            "— such as MTHFR, COMT, or VDR — because standard population-level advice may be "
            "inadequate for them."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-01-15",
            "title": "Who is FertiliQ For?",
            "version": "v2.1",
            "parent_id": "doc_parent_001",
            "parent_title": "FertiliQ Platform Overview"
        }
    },
    {
        "id": "doc_child_003",
        "is_parent": False,
        "content": (
            "## Getting Started\n\n"
            "1. Complete your genetic test kit and mail it to our CLIA-certified lab.\n"
            "2. Upload or connect your biomarker data (supported labs: LabCorp, Quest, Everlywell, "
            "DUTCH hormone test).\n"
            "3. Complete the lifestyle questionnaire (diet, exercise, stress, sleep).\n"
            "4. Receive your personalised FertiliQ Score and action plan within 7–10 business days.\n"
            "5. Sync your wearable (Apple Watch, Oura, Garmin) for continuous cycle tracking.\n\n"
            "Your dashboard updates dynamically as new biomarker data is added. "
            "Recommendations are reviewed and recalibrated every 90 days."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-01-15",
            "title": "Getting Started with FertiliQ",
            "version": "v2.1",
            "parent_id": "doc_parent_001",
            "parent_title": "FertiliQ Platform Overview"
        }
    },

    # ═══════════════════════════════════════════════════════════════════════
    # PARENT 002: Genetic Report Interpretation
    # ═══════════════════════════════════════════════════════════════════════
    {
        "id": "doc_parent_002",
        "is_parent": True,
        "content": (
            "# Understanding Your Genetic Report\n\n"
            "FertiliQ analyses a targeted panel of fertility-relevant gene variants using "
            "single-nucleotide polymorphism (SNP) genotyping. Each variant is classified as "
            "wild-type (no impact), heterozygous (one altered copy) or homozygous (two altered "
            "copies). The clinical impact score (CIS) on a 0–10 scale summarises functional "
            "consequence. Variants analysed include: MTHFR C677T, MTHFR A1298C, COMT Val158Met, "
            "VDR BsmI, VDR TaqI, SHMT1 C1420T, and MTR A2756G, among others.\n\n"
            "## Reading the Report\n"
            "Each section details: the gene function, your specific genotype, functional impact, "
            "and tailored recommendations. Higher CIS does not mean infertility — it means "
            "targeted nutritional or lifestyle intervention will be most beneficial."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-02-01",
            "title": "Understanding Your Genetic Report",
            "version": "v2.1",
            "parent_id": None
        }
    },
    {
        "id": "doc_child_004",
        "is_parent": False,
        "content": (
            "## Interpreting MTHFR Variants\n\n"
            "MTHFR (methylenetetrahydrofolate reductase) is the most clinically significant "
            "variant in the FertiliQ panel. The enzyme converts dietary folate into 5-MTHF "
            "(methylfolate), the active form used in DNA synthesis, neurotransmitter production "
            "and methylation reactions critical to embryo development.\n\n"
            "**C677T heterozygous (CT):** ~30–40% reduction in MTHFR enzyme activity.\n"
            "**C677T homozygous (TT):** ~60–70% reduction — highest intervention priority.\n"
            "**A1298C heterozygous (AC):** ~20–30% reduction, primarily affects BH4 cofactor.\n"
            "**Compound heterozygous (C677T + A1298C):** Significant combined impact.\n\n"
            "FertiliQ v2.1 recommendation for C677T or compound heterozygous carriers: "
            "800 mcg 5-MTHF (methylfolate) daily. Standard synthetic folic acid is not "
            "recommended because impaired MTHFR activity prevents its conversion to the active form."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-02-01",
            "title": "Interpreting MTHFR Variants",
            "version": "v2.1",
            "parent_id": "doc_parent_002",
            "parent_title": "Understanding Your Genetic Report"
        }
    },
    {
        "id": "doc_child_005",
        "is_parent": False,
        "content": (
            "## Interpreting COMT Variants\n\n"
            "COMT (catechol-O-methyltransferase) encodes an enzyme that breaks down catecholamines "
            "(dopamine, adrenaline, oestrogen metabolites). The Val158Met SNP (rs4680) is the "
            "primary variant assessed.\n\n"
            "**Val/Val (GG):** High COMT activity — faster catecholamine breakdown. Associated "
            "with lower oestrogen exposure and better tolerance of high-oestrogen states.\n"
            "**Val/Met (AG):** Intermediate activity.\n"
            "**Met/Met (AA):** Slow COMT — slower oestrogen clearance, potential for oestrogen "
            "dominance. FertiliQ recommends cruciferous vegetables (DIM), magnesium glycinate "
            "and limiting alcohol for Met/Met carriers.\n\n"
            "Slow COMT + high-oestrogen diet can amplify PMS, endometriosis risk and cycle "
            "irregularity. Recommendations are tailored accordingly."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-02-01",
            "title": "Interpreting COMT Variants",
            "version": "v2.1",
            "parent_id": "doc_parent_002",
            "parent_title": "Understanding Your Genetic Report"
        }
    },
    {
        "id": "doc_child_006",
        "is_parent": False,
        "content": (
            "## Interpreting VDR Variants\n\n"
            "VDR (Vitamin D Receptor) variants affect how efficiently cells respond to Vitamin D, "
            "a hormone critical for immune tolerance, follicular development, sperm motility and "
            "implantation success.\n\n"
            "**BsmI (rs1544410):** Variants associated with reduced Vitamin D receptor sensitivity "
            "— carriers often need higher circulating 25(OH)D levels to achieve the same "
            "biological effect as non-carriers.\n"
            "**TaqI (rs731236):** Similarly modulates receptor efficiency.\n\n"
            "FertiliQ target for VDR variant carriers: 25(OH)D serum level 50–70 ng/mL. "
            "Non-carriers: 40–60 ng/mL is sufficient. VDR variant carriers should expect to need "
            "4,000–6,000 IU Vitamin D3 daily to reach and maintain optimal levels, compared to "
            "2,000–4,000 IU for non-carriers."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-02-01",
            "title": "Interpreting VDR Variants",
            "version": "v2.1",
            "parent_id": "doc_parent_002",
            "parent_title": "Understanding Your Genetic Report"
        }
    },

    # ═══════════════════════════════════════════════════════════════════════
    # PARENT 003: Biomarker Reference Ranges
    # ═══════════════════════════════════════════════════════════════════════
    {
        "id": "doc_parent_003",
        "is_parent": True,
        "content": (
            "# Biomarker Reference Ranges\n\n"
            "FertiliQ uses fertility-optimised reference ranges that differ from standard "
            "laboratory ranges. Standard lab ranges define 'normal' for the general population; "
            "FertiliQ ranges define 'optimal' for preconception health. Having a result within "
            "the lab reference range does not guarantee optimal fertility. Always interpret "
            "biomarkers in context of your genetic profile and clinical history.\n\n"
            "Key biomarkers tracked: AMH, FSH, LH, Oestradiol (E2), Progesterone, Prolactin, "
            "Testosterone (total + free), Vitamin D (25-OH), Ferritin, Iron saturation, "
            "Folate (RBC), Homocysteine, CoQ10, Zinc, Selenium, Thyroid panel (TSH, fT4, fT3)."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-02-15",
            "title": "Biomarker Reference Ranges",
            "version": "v2.1",
            "parent_id": None
        }
    },
    {
        "id": "doc_child_007",
        "is_parent": False,
        "content": (
            "## AMH and Ovarian Reserve\n\n"
            "Anti-Müllerian Hormone (AMH) is produced by small antral follicles and reflects "
            "ovarian reserve — the quantity of remaining eggs. It is not strongly influenced "
            "by the menstrual cycle phase and can be measured on any day.\n\n"
            "**FertiliQ Optimal Ranges (pmol/L):**\n"
            "- Age <35: 15–48 pmol/L (optimal above 25)\n"
            "- Age 35–39: 7–25 pmol/L (optimal above 15)\n"
            "- Age 40–44: 2–10 pmol/L (optimal above 5)\n\n"
            "**AMH < 5 pmol/L** at any age indicates diminished ovarian reserve (DOR) and "
            "warrants prompt specialist consultation. AMH alone does not predict egg quality — "
            "a woman with low AMH can still produce high-quality embryos."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-02-15",
            "title": "AMH and Ovarian Reserve",
            "version": "v2.1",
            "parent_id": "doc_parent_003",
            "parent_title": "Biomarker Reference Ranges"
        }
    },
    {
        "id": "doc_child_008",
        "is_parent": False,
        "content": (
            "## FSH, LH and Oestradiol\n\n"
            "**FSH (Follicle-Stimulating Hormone)** — Measured on Day 2–3 of the menstrual cycle.\n"
            "FertiliQ Optimal: 3–8 mIU/mL. FSH >10 suggests the pituitary is working harder to "
            "recruit follicles (possible diminished reserve). FSH >15 mIU/mL at baseline is "
            "clinically significant.\n\n"
            "**LH (Luteinising Hormone)** — Optimal Day 2–3 baseline: 2–9 mIU/mL. "
            "Elevated LH (>10 on Day 2–3) in combination with FSH is associated with PCOS. "
            "LH surge (>20 mIU/mL) signals ovulation within 24–36 hours.\n\n"
            "**Oestradiol (E2)** — Day 2–3 baseline: <50 pg/mL optimal. Elevated baseline E2 "
            "can suppress FSH and masks a true FSH value — always interpret FSH alongside E2."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-02-15",
            "title": "FSH, LH and Oestradiol Reference Ranges",
            "version": "v2.1",
            "parent_id": "doc_parent_003",
            "parent_title": "Biomarker Reference Ranges"
        }
    },
    {
        "id": "doc_child_009",
        "is_parent": False,
        "content": (
            "## Vitamin D, Iron and CoQ10 Reference Ranges\n\n"
            "**Vitamin D — 25(OH)D:**\n"
            "FertiliQ Optimal: 50–70 ng/mL (125–175 nmol/L). Values below 30 ng/mL are "
            "deficient; 30–50 ng/mL are insufficient for fertility optimisation. "
            "Target 60 ng/mL for implantation support. VDR variant carriers need upper end.\n\n"
            "**Ferritin (iron stores):**\n"
            "FertiliQ Optimal: 50–100 ng/mL. Women with values <30 ng/mL often experience "
            "fatigue, hair loss and anovulation. Ferritin <15 ng/mL indicates iron-deficiency "
            "anaemia requiring supplementation.\n\n"
            "**CoQ10 (Coenzyme Q10):**\n"
            "Plasma CoQ10 optimal for fertility: 0.8–1.2 µmol/L. CoQ10 supports mitochondrial "
            "ATP production in oocytes and sperm. Levels typically decline with age and statin use."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-02-15",
            "title": "Vitamin D, Iron and CoQ10 Reference Ranges",
            "version": "v2.1",
            "parent_id": "doc_parent_003",
            "parent_title": "Biomarker Reference Ranges"
        }
    },

    # ═══════════════════════════════════════════════════════════════════════
    # PARENT 004: Nutrition Recommendations
    # ═══════════════════════════════════════════════════════════════════════
    {
        "id": "doc_parent_004",
        "is_parent": True,
        "content": (
            "# Nutrition Recommendations by Genetic Profile\n\n"
            "FertiliQ integrates your genetic variants with biomarker levels to generate "
            "precision nutrition guidance. General fertility diet advice applies to all users; "
            "genetic-profile-specific additions are layered on top based on your variant results."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-03-01",
            "title": "Nutrition Recommendations by Genetic Profile",
            "version": "v2.1",
            "parent_id": None
        }
    },
    {
        "id": "doc_child_010",
        "is_parent": False,
        "content": (
            "## Foundation Fertility Diet\n\n"
            "Applicable to all FertiliQ users regardless of genetic profile:\n"
            "- **Whole foods priority:** 7–9 servings of vegetables/fruit daily, prioritising "
            "leafy greens (spinach, kale, rocket) for natural folate.\n"
            "- **Healthy fats:** Omega-3 rich foods (wild salmon, sardines, walnuts, flaxseed) "
            "to support prostaglandin balance and embryo cell membranes. Target 2g EPA+DHA daily.\n"
            "- **Reduce ultra-processed foods:** Associated with elevated inflammatory markers "
            "and oxidative stress, which impair egg and sperm quality.\n"
            "- **Limit alcohol:** Even moderate alcohol consumption (>3 units/week) is associated "
            "with reduced implantation rates and increased miscarriage risk.\n"
            "- **Mediterranean pattern overall:** Consistently associated with better IVF outcomes "
            "in women and improved sperm parameters in men."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-03-01",
            "title": "Foundation Fertility Diet",
            "version": "v2.1",
            "parent_id": "doc_parent_004",
            "parent_title": "Nutrition Recommendations by Genetic Profile"
        }
    },
    {
        "id": "doc_child_011",
        "is_parent": False,
        "content": (
            "## Nutrition for MTHFR Variant Carriers\n\n"
            "If your report shows MTHFR C677T or A1298C variants, standard folic acid "
            "supplementation is insufficient — your enzyme cannot efficiently convert synthetic "
            "folic acid to the biologically active 5-MTHF (methylfolate). FertiliQ v2.1 dietary "
            "protocol for MTHFR carriers:\n\n"
            "- **Prioritise food-form folate:** lentils, edamame, asparagus, beetroot, avocado — "
            "these contain natural folates already in a partially bioavailable form.\n"
            "- **Avoid synthetic folic acid fortification where possible** (many cereals and "
            "breads) — unmetabolised folic acid can accumulate and potentially mask B12 deficiency.\n"
            "- **Increase choline intake:** Eggs (2/day) provide choline, an alternative methyl "
            "donor that bypasses the MTHFR bottleneck via the PEMT pathway.\n"
            "- **B12-rich foods:** Methylcobalamin (the active B12 form) from animal proteins, "
            "especially liver and shellfish, is essential alongside methylfolate for the "
            "methylation cycle to function optimally."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-03-01",
            "title": "Nutrition for MTHFR Variant Carriers",
            "version": "v2.1",
            "parent_id": "doc_parent_004",
            "parent_title": "Nutrition Recommendations by Genetic Profile"
        }
    },
    {
        "id": "doc_child_012",
        "is_parent": False,
        "content": (
            "## Nutrition for COMT and VDR Variant Carriers\n\n"
            "**Slow COMT (Met/Met):**\n"
            "Focus on oestrogen clearance: cruciferous vegetables (broccoli, Brussels sprouts, "
            "cauliflower) provide indole-3-carbinol (I3C) and DIM which upregulate healthy "
            "2-OH oestrogen metabolite pathways. Limit alcohol, reduce red meat, increase "
            "fibre for oestrogen enterohepatic recirculation. Avoid high-dose catechol supplements "
            "(green tea extract, high-dose resveratrol) which compete with COMT.\n\n"
            "**VDR Variants:**\n"
            "Prioritise Vitamin D-rich foods: oily fish (salmon, mackerel), egg yolks, liver. "
            "Ensure adequate magnesium (needed for Vitamin D activation): almonds, dark chocolate, "
            "pumpkin seeds. Vitamin K2 (natto, hard cheeses) prevents Vitamin D toxicity at "
            "higher supplementation doses and directs calcium appropriately."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-03-01",
            "title": "Nutrition for COMT and VDR Variant Carriers",
            "version": "v2.1",
            "parent_id": "doc_parent_004",
            "parent_title": "Nutrition Recommendations by Genetic Profile"
        }
    },

    # ═══════════════════════════════════════════════════════════════════════
    # PARENT 005: Exercise Guidelines
    # ═══════════════════════════════════════════════════════════════════════
    {
        "id": "doc_parent_005",
        "is_parent": True,
        "content": (
            "# Exercise Guidelines by Cycle Phase and Biomarker Level\n\n"
            "Exercise profoundly influences fertility through hormonal signalling, insulin "
            "sensitivity, oxidative stress and body composition. FertiliQ recommends cycle-phase "
            "aligned exercise to maximise hormonal benefit and minimise unintended suppression of "
            "reproductive hormones. Intensity must be calibrated to current biomarker levels — "
            "especially AMH, cortisol and FSH — to avoid overtraining effects."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-03-15",
            "title": "Exercise Guidelines by Cycle Phase and Biomarker Level",
            "version": "v2.1",
            "parent_id": None
        }
    },
    {
        "id": "doc_child_013",
        "is_parent": False,
        "content": (
            "## Menstrual Phase (Days 1–5): Rest and Gentle Movement\n\n"
            "Hormonal context: oestrogen and progesterone at their lowest. Prostaglandin-driven "
            "uterine contractions may cause discomfort.\n\n"
            "**Recommended activity:** Yin yoga, gentle walking (20–30 min), swimming at low "
            "intensity. Avoid high-impact HIIT and heavy resistance training during Days 1–2.\n\n"
            "**Biomarker alert:** If ferritin <30 ng/mL, keep sessions under 30 minutes and "
            "monitor for dizziness. Iron deficiency impairs oxygen delivery and energy production, "
            "making sustained exercise difficult and counterproductive."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-03-15",
            "title": "Exercise in Menstrual Phase",
            "version": "v2.1",
            "parent_id": "doc_parent_005",
            "parent_title": "Exercise Guidelines by Cycle Phase and Biomarker Level"
        }
    },
    {
        "id": "doc_child_014",
        "is_parent": False,
        "content": (
            "## Follicular Phase (Days 6–13): Peak Performance Window\n\n"
            "Hormonal context: rising oestrogen and FSH drive follicular recruitment. Energy "
            "levels peak as oestrogen climbs. This is your highest-performance window.\n\n"
            "**Recommended activity:** Strength training (progressive overload, 3–4x/week), "
            "high-intensity cardio intervals (2x/week), dance, cycling. Oestrogen improves "
            "muscle protein synthesis and pain tolerance during this phase.\n\n"
            "**Goal:** Build muscle mass and insulin sensitivity, which improves ovarian function "
            "and egg quality. Aim for 150–180 min moderate-intensity or 75–90 min vigorous "
            "activity across the follicular phase.\n\n"
            "**Caution:** If AMH < 7 pmol/L or FSH > 10 mIU/mL, reduce vigorous cardio (>80% "
            "HRmax) to <60 min/week to avoid cortisol-mediated gonadotropin suppression."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-03-15",
            "title": "Exercise in Follicular Phase",
            "version": "v2.1",
            "parent_id": "doc_parent_005",
            "parent_title": "Exercise Guidelines by Cycle Phase and Biomarker Level"
        }
    },
    {
        "id": "doc_child_015",
        "is_parent": False,
        "content": (
            "## Luteal Phase (Days 15–28): Recovery Focus\n\n"
            "Hormonal context: progesterone dominates. Body temperature rises 0.2–0.5°C. "
            "Progesterone has a mild catabolic effect, and energy for high-intensity work "
            "is reduced.\n\n"
            "**Recommended activity:** Pilates, yoga (not hot yoga), moderate resistance "
            "training (reduce load by 10–15% vs follicular phase), long walks. Avoid very "
            "high-intensity sessions in Days 15–20 when implantation window is open.\n\n"
            "**If trying to conceive (TWW — two-week wait):** After ovulation, keep heart rate "
            "below 140 bpm. Sustained high-intensity exercise raises core temperature and cortisol, "
            "both of which may impair implantation. Light activity remains beneficial for "
            "blood flow and stress management."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-03-15",
            "title": "Exercise in Luteal Phase",
            "version": "v2.1",
            "parent_id": "doc_parent_005",
            "parent_title": "Exercise Guidelines by Cycle Phase and Biomarker Level"
        }
    },

    # ═══════════════════════════════════════════════════════════════════════
    # PARENT 006: Platform API Documentation
    # ═══════════════════════════════════════════════════════════════════════
    {
        "id": "doc_parent_006",
        "is_parent": True,
        "content": (
            "# FertiliQ Platform API Documentation\n\n"
            "The FertiliQ REST API (v2) allows third-party health apps, wearables and clinical "
            "systems to read and write biomarker data, retrieve genetic report summaries and "
            "push notification triggers. Authentication uses OAuth 2.0 with JWT tokens. "
            "Base URL: https://api.fertiliq.com/v2/\n\n"
            "Rate limits: 1,000 requests/hour per OAuth client. Biomarker writes are "
            "idempotent — duplicate submissions with identical timestamps are deduplicated."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-04-01",
            "title": "FertiliQ Platform API Documentation",
            "version": "v2.1",
            "parent_id": None
        }
    },
    {
        "id": "doc_child_016",
        "is_parent": False,
        "content": (
            "## Biomarker Sync Endpoints\n\n"
            "**POST /biomarkers/sync**\n"
            "Submits one or more biomarker readings. Payload (JSON):\n"
            "```json\n"
            "{\n"
            "  \"user_id\": \"usr_abc123\",\n"
            "  \"readings\": [\n"
            "    {\"biomarker\": \"amh\", \"value\": 18.3, \"unit\": \"pmol/L\", "
            "\"date\": \"2024-03-20\", \"lab\": \"LabCorp\"}\n"
            "  ]\n"
            "}\n"
            "```\n"
            "Returns: 200 with sync_id on success; 422 if unit mismatch or invalid biomarker "
            "code. Supported biomarker codes: amh, fsh, lh, e2, progesterone, testosterone_total, "
            "testosterone_free, vitamin_d, ferritin, folate_rbc, homocysteine, coq10, tsh, ft4."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-04-01",
            "title": "Biomarker Sync API Endpoint",
            "version": "v2.1",
            "parent_id": "doc_parent_006",
            "parent_title": "FertiliQ Platform API Documentation"
        }
    },
    {
        "id": "doc_child_017",
        "is_parent": False,
        "content": (
            "## Genetic Report API\n\n"
            "**GET /genetic/summary/{user_id}**\n"
            "Returns variant summary for a user. Response includes:\n"
            "- `variants`: list of analysed SNPs with genotype and CIS score\n"
            "- `primary_pathways`: ranked list of affected biological pathways\n"
            "- `recommendations_active`: count of currently active genetic-based recommendations\n\n"
            "**GET /genetic/report/{user_id}/pdf**\n"
            "Streams a signed PDF of the full genetic report (valid for 15 minutes). "
            "Requires `report:read` OAuth scope.\n\n"
            "**Webhook:** FertiliQ can push to your endpoint when a new genetic result is "
            "processed. Register via POST /webhooks with event type `genetic.result.ready`."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-04-01",
            "title": "Genetic Report API",
            "version": "v2.1",
            "parent_id": "doc_parent_006",
            "parent_title": "FertiliQ Platform API Documentation"
        }
    },
    {
        "id": "doc_child_018",
        "is_parent": False,
        "content": (
            "## Troubleshooting API Sync Issues\n\n"
            "**Error 422 — Unit Mismatch:** Ensure Vitamin D is submitted as ng/mL (not nmol/L). "
            "To convert: ng/mL × 2.496 = nmol/L. Submit in ng/mL to the API.\n\n"
            "**Error 409 — Duplicate Reading:** A reading with the same biomarker + date already "
            "exists. This is expected behaviour — the API is idempotent. No action required.\n\n"
            "**Data not appearing in dashboard:** After a successful sync, allow 5–10 minutes for "
            "recommendation recalculation. If data is missing after 30 minutes, check that your "
            "OAuth token has the `biomarker:write` scope. Token refresh required every 24 hours.\n\n"
            "**LabCorp auto-sync fails:** This usually indicates your LabCorp Patient Portal "
            "credentials have changed. Re-authorise via Settings → Connected Labs → LabCorp."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-04-01",
            "title": "Troubleshooting API Sync Issues",
            "version": "v2.1",
            "parent_id": "doc_parent_006",
            "parent_title": "FertiliQ Platform API Documentation"
        }
    },

    # ═══════════════════════════════════════════════════════════════════════
    # PARENT 007: Supplement Dosing Guidelines v2.1 (2024) — CURRENT
    # ═══════════════════════════════════════════════════════════════════════
    {
        "id": "doc_parent_007",
        "is_parent": True,
        "content": (
            "# Supplement Dosing Guidelines v2.1 (Updated January 2024)\n\n"
            "FertiliQ v2.1 supplement guidelines reflect the latest peer-reviewed evidence and "
            "supersede all v1.0 recommendations. Significant update in this version: folate "
            "protocol for MTHFR variant carriers revised from standard folic acid to active "
            "methylfolate (5-MTHF) based on methylation pathway research published 2022–2023."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-01-10",
            "title": "Supplement Dosing Guidelines v2.1",
            "version": "v2.1",
            "parent_id": None
        }
    },
    {
        "id": "doc_child_019",
        "is_parent": False,
        "content": (
            "## Folate / Methylfolate Dosing (v2.1 — Current)\n\n"
            "**For MTHFR wild-type (no variants):** 400 mcg standard folic acid or methylfolate "
            "daily. Either form is appropriate as MTHFR enzyme is functional.\n\n"
            "**For MTHFR C677T heterozygous (CT):** 400–800 mcg 5-MTHF (methylfolate) daily. "
            "Standard folic acid is NOT recommended — reduced enzyme activity means conversion "
            "to active form is impaired, and unmetabolised folic acid accumulates.\n\n"
            "**For MTHFR C677T homozygous (TT) or compound heterozygous (C677T + A1298C):** "
            "800 mcg 5-MTHF (methylfolate) daily is the FertiliQ v2.1 recommendation. "
            "This is a critical update from the v1.0 guideline of 400 mcg standard folic acid. "
            "Methylfolate bypasses the impaired MTHFR conversion step entirely.\n\n"
            "Always pair methylfolate with methylcobalamin (1,000 mcg B12) to support the "
            "methylation cycle completely. Trimethylglycine (TMG, 500 mg) may be added if "
            "homocysteine remains elevated (>10 µmol/L) after 3 months."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-01-10",
            "title": "Folate/Methylfolate Dosing for MTHFR Variants (v2.1)",
            "version": "v2.1",
            "parent_id": "doc_parent_007",
            "parent_title": "Supplement Dosing Guidelines v2.1"
        }
    },
    {
        "id": "doc_child_020",
        "is_parent": False,
        "content": (
            "## CoQ10 Dosing Guidelines (v2.1 — Current)\n\n"
            "Coenzyme Q10 (ubiquinol form preferred for bioavailability) supports mitochondrial "
            "energy production in oocytes and sperm. Research since 2022 has significantly "
            "refined dosing recommendations.\n\n"
            "**Women under 35:** 200–400 mg/day ubiquinol.\n"
            "**Women 35–39:** 400 mg/day ubiquinol as standard starting dose.\n"
            "**Women 40+:** 400–600 mg/day ubiquinol. Higher doses supported by 2023 RCT data "
            "showing improved oocyte maturation rates with 600 mg vs 200 mg in this age group.\n\n"
            "Take with meals containing fat for best absorption. Effects on oocyte quality "
            "take 90–120 days (one egg maturation cycle) to manifest — begin at least 3 months "
            "before IVF retrieval or planned conception."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-01-10",
            "title": "CoQ10 Dosing Guidelines (v2.1)",
            "version": "v2.1",
            "parent_id": "doc_parent_007",
            "parent_title": "Supplement Dosing Guidelines v2.1"
        }
    },
    {
        "id": "doc_child_021",
        "is_parent": False,
        "content": (
            "## Vitamin D, Iron and Zinc Dosing (v2.1)\n\n"
            "**Vitamin D3:**\n"
            "- Baseline 25(OH)D 20–30 ng/mL: Start 4,000 IU/day with K2 (100 mcg MK-7).\n"
            "- Baseline <20 ng/mL: 5,000 IU/day for 12 weeks, then retest.\n"
            "- VDR variant carriers: add 1,000 IU to above doses. Retest every 12 weeks.\n\n"
            "**Iron (Ferritin <30 ng/mL):**\n"
            "Iron bisglycinate 25–50 mg/day with 200 mg Vitamin C (enhances absorption). "
            "Do not take with calcium or within 2 hours of thyroid medication. "
            "Recheck ferritin after 8 weeks.\n\n"
            "**Zinc (male fertility):**\n"
            "Zinc picolinate 15–30 mg/day for men with sub-optimal sperm parameters or "
            "low free testosterone. Do not exceed 40 mg/day — zinc competes with copper."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-01-10",
            "title": "Vitamin D, Iron and Zinc Dosing",
            "version": "v2.1",
            "parent_id": "doc_parent_007",
            "parent_title": "Supplement Dosing Guidelines v2.1"
        }
    },

    # ═══════════════════════════════════════════════════════════════════════
    # PARENT 008: Legacy Supplement Guidelines v1.0 (2022) — OUTDATED
    # *** DELIBERATE CONTRADICTION: 400mcg folic acid for MTHFR ***
    # ═══════════════════════════════════════════════════════════════════════
    {
        "id": "doc_parent_008",
        "is_parent": True,
        "content": (
            "# Supplement Dosing Guidelines v1.0 (September 2022)\n\n"
            "NOTICE: This is the archived v1.0 documentation. Current guidelines are in v2.1. "
            "Some recommendations in this document have been superseded. "
            "Please refer to the v2.1 supplement guidelines for current protocols.\n\n"
            "FertiliQ v1.0 supplement recommendations were developed from evidence available "
            "as of mid-2022. Folic acid recommendations in this version apply a standard-dose "
            "protocol across all MTHFR genotypes."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2022-09-01",
            "title": "Supplement Dosing Guidelines v1.0 (Legacy)",
            "version": "v1.0",
            "parent_id": None
        }
    },
    {
        "id": "doc_child_022",
        "is_parent": False,
        "content": (
            "## Folate Dosing (v1.0 — Legacy, Superseded)\n\n"
            "FertiliQ v1.0 Folic Acid Recommendation:\n\n"
            "All users planning conception, including those with MTHFR C677T or A1298C variants, "
            "are recommended to take 400 mcg of folic acid daily, consistent with standard "
            "preconception guidelines. This is the CDC-recommended dose for neural tube defect "
            "prevention.\n\n"
            "**Note:** At the time of v1.0 release, FertiliQ's MTHFR-specific methylfolate "
            "protocol had not yet been developed. The v1.0 recommendation of 400 mcg standard "
            "folic acid for MTHFR variant carriers has been SUPERSEDED in v2.1 (2024), which "
            "recommends 800 mcg 5-MTHF (methylfolate) for C677T carriers. Refer to v2.1 docs."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2022-09-01",
            "title": "Folate Dosing for MTHFR Variants (v1.0 — Legacy)",
            "version": "v1.0",
            "parent_id": "doc_parent_008",
            "parent_title": "Supplement Dosing Guidelines v1.0 (Legacy)"
        }
    },
    {
        "id": "doc_child_023",
        "is_parent": False,
        "content": (
            "## CoQ10 Dosing (v1.0 — Legacy)\n\n"
            "FertiliQ v1.0 CoQ10 Recommendation:\n\n"
            "CoQ10 supplementation at 200 mg/day (ubiquinone form) is recommended for women "
            "over 35 looking to support egg quality. This dose was selected based on evidence "
            "available in 2022 demonstrating mitochondrial benefits at this level.\n\n"
            "Note: Subsequent research (2023–2024) has supported higher doses of 400–600 mg/day "
            "ubiquinol for women over 35 and 40, and FertiliQ v2.1 guidelines reflect this "
            "updated evidence. The 200 mg recommendation in v1.0 is now considered the minimum "
            "effective dose rather than the optimal dose."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2022-09-01",
            "title": "CoQ10 Dosing (v1.0 — Legacy)",
            "version": "v1.0",
            "parent_id": "doc_parent_008",
            "parent_title": "Supplement Dosing Guidelines v1.0 (Legacy)"
        }
    },

    # ═══════════════════════════════════════════════════════════════════════
    # PARENT 009: Sexual Health and Conception Timing
    # ═══════════════════════════════════════════════════════════════════════
    {
        "id": "doc_parent_009",
        "is_parent": True,
        "content": (
            "# Sexual Health and Conception Timing\n\n"
            "Optimising conception timing requires understanding the fertile window — the "
            "days in the menstrual cycle when intercourse is most likely to result in pregnancy. "
            "Sperm survive 3–5 days in the female reproductive tract; the egg is viable for "
            "12–24 hours after ovulation. The fertile window is approximately Days 10–17 of "
            "a 28-day cycle, but varies significantly between individuals and cycles."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-03-20",
            "title": "Sexual Health and Conception Timing",
            "version": "v2.1",
            "parent_id": None
        }
    },
    {
        "id": "doc_child_024",
        "is_parent": False,
        "content": (
            "## Identifying the Fertile Window\n\n"
            "FertiliQ integrates multiple signals to identify your fertile window with high "
            "precision:\n\n"
            "1. **LH surge detection:** LH peaks 24–36 hours before ovulation. FertiliQ "
            "analyses daily LH data from urine-based OPKs or blood tests synced via the API.\n"
            "2. **Basal Body Temperature (BBT):** Temperature rises 0.2–0.5°C after ovulation, "
            "confirming it has occurred. Connect your BBT thermometer or Oura ring for "
            "automatic tracking.\n"
            "3. **Cervical mucus pattern:** FertiliQ's cycle journal allows logging of cervical "
            "mucus consistency. Egg-white cervical mucus (EWCM) indicates peak fertility.\n"
            "4. **AMH-adjusted window:** Women with very high AMH (e.g. PCOS) may have longer, "
            "irregular cycles — FertiliQ adjusts fertile window predictions accordingly.\n\n"
            "**Timing strategy:** For natural conception, aim for intercourse every 1–2 days "
            "from Days 10–17, with priority on the 2 days preceding the LH surge."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-03-20",
            "title": "Identifying the Fertile Window",
            "version": "v2.1",
            "parent_id": "doc_parent_009",
            "parent_title": "Sexual Health and Conception Timing"
        }
    },
    {
        "id": "doc_child_025",
        "is_parent": False,
        "content": (
            "## Sexual Health and Libido Across the Cycle\n\n"
            "Understanding natural fluctuations in libido helps couples align intimacy with "
            "the fertile window without creating performance pressure.\n\n"
            "**Follicular phase (Days 6–13):** Rising oestrogen elevates mood, energy and "
            "libido. Testosterone also rises toward ovulation — this is the natural peak of "
            "sexual desire for most women.\n\n"
            "**Periovulatory (Days 12–16):** Libido peaks with the LH surge. Oestrogen reaches "
            "its cycle maximum. Pheromonal signalling may also intensify mutual attraction.\n\n"
            "**Luteal phase (Days 15–28):** Progesterone dominates. Many women experience "
            "reduced libido, especially Days 21–28. This is normal and hormonally driven. "
            "FertiliQ does not recommend forcing intercourse during this phase — fertilisation "
            "cannot occur post-ovulation.\n\n"
            "For men: sperm quality is consistent across the partner's cycle but improves "
            "with 2–3 day abstinence before the fertile window to optimise volume and motility."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-03-20",
            "title": "Sexual Health and Libido Across the Cycle",
            "version": "v2.1",
            "parent_id": "doc_parent_009",
            "parent_title": "Sexual Health and Conception Timing"
        }
    },
    {
        "id": "doc_child_026",
        "is_parent": False,
        "content": (
            "## Oxidative Stress and Sperm Quality\n\n"
            "Your genetic report may flag elevated oxidative stress risk based on variants in "
            "GPX1, SOD2, NQO1 or GSTM1 (glutathione pathway genes). Oxidative stress damages "
            "DNA integrity in both sperm and eggs.\n\n"
            "**High oxidative stress risk profile interventions:**\n"
            "- Astaxanthin 4–8 mg/day (powerful antioxidant with specific male fertility data)\n"
            "- Vitamin E (mixed tocopherols) 200–400 IU/day\n"
            "- NAC (N-acetylcysteine) 600 mg twice daily to boost glutathione\n"
            "- CoQ10 (ubiquinol) 300–400 mg/day — dual antioxidant and mitochondrial support\n"
            "- Reduce heat exposure to testes: avoid hot baths, saunas and laptop-on-lap use\n\n"
            "For men with elevated DNA fragmentation index (DFI >25%), a 90-day antioxidant "
            "protocol can meaningfully reduce DFI before IVF/ICSI."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-03-20",
            "title": "Oxidative Stress Risk and Fertility",
            "version": "v2.1",
            "parent_id": "doc_parent_009",
            "parent_title": "Sexual Health and Conception Timing"
        }
    },
    {
        "id": "doc_child_027",
        "is_parent": False,
        "content": (
            "## When to Escalate: 6+ Months Without Conception\n\n"
            "FertiliQ recommends the following investigation roadmap for couples who have been "
            "trying for 6 months (age <35) or 3 months (age 35+) without success:\n\n"
            "**Step 1 — Biomarker Panel Review:**\n"
            "Ensure AMH, FSH (Day 2–3), antral follicle count (AFC via ultrasound), thyroid "
            "panel, prolactin and homocysteine are within optimal ranges. Recheck any previously "
            "borderline values.\n\n"
            "**Step 2 — Male Factor Evaluation:**\n"
            "Full semen analysis: volume, concentration, motility (total + progressive), "
            "morphology (Kruger strict criteria), and DNA fragmentation index (DFI).\n\n"
            "**Step 3 — Structural Investigation:**\n"
            "Hysterosalpingogram (HSG) to assess fallopian tube patency and uterine cavity.\n\n"
            "**Step 4 — Specialist Referral:**\n"
            "If any Step 1–3 findings are abnormal, a reproductive endocrinologist consultation "
            "is recommended. FertiliQ generates a specialist-ready summary report to bring to "
            "your appointment."
        ),
        "metadata": {
            "source_type": "documentation",
            "date": "2024-03-20",
            "title": "Investigation Roadmap After 6+ Months",
            "version": "v2.1",
            "parent_id": "doc_parent_009",
            "parent_title": "Sexual Health and Conception Timing"
        }
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# FORUM DATA  (QA pairs; vote count and date are embedded in content text)
# ─────────────────────────────────────────────────────────────────────────────

FORUMS = [
    {
        "id": "forum_001",
        "content": (
            "Question (2024-02-10, 👍 47 votes): I just got my FertiliQ results back and I'm "
            "homozygous for MTHFR C677T (TT genotype). My previous doctor said to just take the "
            "standard prenatal with 400 mcg folic acid. FertiliQ is now recommending 800 mcg "
            "methylfolate. What's the difference and which should I follow?\n\n"
            "Accepted Answer: Great question — this is one of the most common points of confusion "
            "after getting MTHFR results. Your doctor's recommendation of 400 mcg folic acid "
            "was based on standard preconception guidelines that were written before MTHFR-specific "
            "research was widely incorporated into practice. Here's the key difference: standard "
            "folic acid (synthetic) requires the MTHFR enzyme to convert it into the active "
            "form your body can actually use (5-MTHF / methylfolate). With TT genotype, your "
            "MTHFR enzyme has roughly 60–70% reduced activity, meaning a significant portion "
            "of synthetic folic acid goes unprocessed. FertiliQ v2.1's recommendation of 800 mcg "
            "5-MTHF (methylfolate) bypasses this conversion step entirely — you're taking the "
            "active form directly. This is the current evidence-based approach supported by "
            "methylation research. The old 400 mcg folic acid recommendation is outdated for "
            "MTHFR homozygous carriers."
        ),
        "metadata": {
            "source_type": "forum",
            "date": "2024-02-10",
            "title": "MTHFR TT — methylfolate vs folic acid question",
            "votes": 47,
            "is_accepted": True
        }
    },
    {
        "id": "forum_002",
        "content": (
            "Question (2022-08-15, 👍 23 votes): Just got my MTHFR results — I'm C677T "
            "heterozygous (CT). My FertiliQ report says something about folate. How much folic "
            "acid should I be taking?\n\n"
            "Accepted Answer: According to FertiliQ's current guidelines (as of August 2022), "
            "the recommendation for all users including those with MTHFR variants is the standard "
            "400 mcg folic acid daily. This aligns with the CDC recommendation for preconception "
            "care. Your CT genotype does reduce MTHFR activity somewhat, but the consensus at "
            "the time of writing is that 400 mcg is appropriate. Make sure you're taking a "
            "quality prenatal vitamin that includes this dose. [Note from moderator 2024: "
            "FertiliQ has since updated to v2.1 — for MTHFR carriers the new recommendation "
            "is 800 mcg methylfolate, not standard folic acid. This 2022 post reflects outdated "
            "guidance.]"
        ),
        "metadata": {
            "source_type": "forum",
            "date": "2022-08-15",
            "title": "MTHFR CT — how much folic acid?",
            "votes": 23,
            "is_accepted": True
        }
    },
    {
        "id": "forum_003",
        "content": (
            "Question (2023-03-20, 👍 18 votes): My MTHFR result is A1298C heterozygous. "
            "I've read that some people take higher doses of folic acid. Is 400 mcg enough "
            "for me?\n\n"
            "Accepted Answer: For A1298C heterozygous, the impact on MTHFR enzyme activity "
            "is somewhat lower than C677T (roughly 20–30% reduction vs 30–40%). As of the "
            "2023 FertiliQ guidelines, the recommendation remains 400 mcg folic acid for "
            "A1298C heterozygous as a minimum. However, many practitioners are moving toward "
            "recommending methylfolate even for A1298C carriers. If you want to be cautious, "
            "switching to 400–800 mcg methylfolate is reasonable. The newer FertiliQ v2.1 "
            "(2024) has formally updated this to recommend methylfolate for all MTHFR variant "
            "carriers, so check the current guidelines."
        ),
        "metadata": {
            "source_type": "forum",
            "date": "2023-03-20",
            "title": "MTHFR A1298C — is 400 mcg folic acid enough?",
            "votes": 18,
            "is_accepted": True
        }
    },
    {
        "id": "forum_004",
        "content": (
            "Question (2024-05-12, 👍 62 votes): What CoQ10 dose is everyone taking? I'm 38 "
            "and about to start IVF. I've seen recommendations ranging from 200 mg to 600 mg "
            "and I don't know which to follow.\n\n"
            "Accepted Answer: The dosing range has genuinely evolved over the past few years. "
            "The 200 mg recommendation you've seen is from older studies (pre-2022) and is now "
            "considered a minimum dose. For women 35–40 going into IVF, the current FertiliQ "
            "v2.1 guideline is 400 mg/day ubiquinol (the reduced, more bioavailable form). "
            "At 38, I'd personally go with 400 mg — the evidence for 600 mg is there but "
            "mostly for women over 40 or those with very poor ovarian reserve. Start ubiquinol "
            "form (not ubiquinone), take with a fatty meal, and ideally begin 3+ months before "
            "retrieval. The 200 mg old-school recommendation you've seen is outdated."
        ),
        "metadata": {
            "source_type": "forum",
            "date": "2024-05-12",
            "title": "CoQ10 dose for IVF prep at 38 — 200mg vs 600mg?",
            "votes": 62,
            "is_accepted": True
        }
    },
    {
        "id": "forum_005",
        "content": (
            "Question (2022-11-08, 👍 14 votes): I saw a study recommending 200 mg CoQ10 for "
            "egg quality. Is that the dose FertiliQ recommends too?\n\n"
            "Accepted Answer: Yes, as of FertiliQ v1.0 (2022), 200 mg CoQ10 daily is the "
            "recommended dose for women over 35 looking to support mitochondrial function in "
            "oocytes. This is consistent with the clinical evidence available in 2022. Take "
            "it with a meal containing fat for best absorption. Note: As of 2024, FertiliQ has "
            "updated to recommend 400–600 mg for women over 35, based on newer RCT data. "
            "If you're reading this now, the updated dosing may be more appropriate."
        ),
        "metadata": {
            "source_type": "forum",
            "date": "2022-11-08",
            "title": "CoQ10 dose — is 200mg the standard recommendation?",
            "votes": 14,
            "is_accepted": True
        }
    },
    {
        "id": "forum_006",
        "content": (
            "Question (2024-07-03, 👍 34 votes): My biomarker data isn't syncing from LabCorp. "
            "I uploaded my results 2 days ago and they're not showing on my dashboard. Anyone "
            "else had this issue?\n\n"
            "Accepted Answer: This is a known issue with the LabCorp auto-sync in the current "
            "version. Two things to check: (1) Go to Settings → Connected Labs → LabCorp and "
            "make sure your LabCorp Patient Portal credentials haven't changed — they auto-expire "
            "every 90 days. (2) Try the manual upload option: download your lab PDF from LabCorp "
            "Patient Portal and use the FertiliQ 'Upload Lab Report' feature under the Biomarkers "
            "tab. The OCR parser supports LabCorp format and usually processes within 10 minutes. "
            "If still not working after that, contact support@fertiliq.com with your sync_id "
            "from the API response."
        ),
        "metadata": {
            "source_type": "forum",
            "date": "2024-07-03",
            "title": "LabCorp biomarker sync not working — 2 days waiting",
            "votes": 34,
            "is_accepted": True
        }
    },
    {
        "id": "forum_007",
        "content": (
            "Question (2024-01-22, 👍 29 votes): My AMH came back at 4.2 pmol/L and I'm 32. "
            "The lab says this is in the 'normal' range but FertiliQ flagged it as low. "
            "Who's right?\n\n"
            "Accepted Answer: FertiliQ is right to flag this. Standard lab reference ranges "
            "define 'normal' based on the general population, not fertility-optimised thresholds. "
            "At 32, an AMH of 4.2 pmol/L puts you in the low-normal to diminished range by "
            "fertility clinic standards. The FertiliQ optimal for under 35 is 15–48 pmol/L. "
            "An AMH of 4.2 at 32 is more typical of someone in their early 40s. This doesn't "
            "mean you can't conceive naturally, but it does mean you shouldn't delay if you're "
            "planning conception, and it's worth discussing with a reproductive endocrinologist. "
            "DHEA (25–50 mg/day), CoQ10 (400 mg), and aggressive antioxidant support may help "
            "with follicular environment."
        ),
        "metadata": {
            "source_type": "forum",
            "date": "2024-01-22",
            "title": "AMH 4.2 at age 32 — FertiliQ says low, lab says normal?",
            "votes": 29,
            "is_accepted": True
        }
    },
    {
        "id": "forum_008",
        "content": (
            "Question (2024-03-15, 👍 41 votes): My Vitamin D came back at 18 ng/mL. "
            "FertiliQ says this is way too low. What should I do?\n\n"
            "Accepted Answer: 18 ng/mL is indeed deficient — FertiliQ's fertility-optimal "
            "target is 50–70 ng/mL, and you're less than half of the minimum. Here's a "
            "practical protocol: Start 5,000 IU Vitamin D3 daily with 100 mcg K2 (MK-7 form). "
            "Take with your fattiest meal of the day (fat-soluble vitamin). Retest in 12 weeks. "
            "At 18 ng/mL, realistically expect to reach 40–50 ng/mL after 12 weeks of 5,000 IU. "
            "You may need to go to 70–80 ng/mL range, which could take 6 months. If you have "
            "VDR variants in your FertiliQ report, add another 1,000–2,000 IU to your dose "
            "as your receptors are less efficient."
        ),
        "metadata": {
            "source_type": "forum",
            "date": "2024-03-15",
            "title": "Vitamin D at 18 ng/mL — what protocol to follow?",
            "votes": 41,
            "is_accepted": True
        }
    },
    {
        "id": "forum_009",
        "content": (
            "Question (2024-06-10, 👍 55 votes): When is the best time to have sex when trying "
            "to conceive? My cycle is 30 days. FertiliQ shows my fertile window as Days 12–18.\n\n"
            "Accepted Answer: For a 30-day cycle with your fertile window Days 12–18, the "
            "highest-conception-probability timing is: Day 11, Day 13, Day 15 (every other day "
            "during the window). The top-priority day is the one just before your predicted LH "
            "surge (usually Day 13–14 for a 30-day cycle). If you're using an OPK, aim to have "
            "sex the day of the LH surge and the day after. Sperm live 3–5 days, so starting a "
            "day before the window ensures sperm are waiting for the egg. Don't stress about "
            "daily sex during the window — every-other-day is just as effective and maintains "
            "better sperm quality and reduces performance pressure."
        ),
        "metadata": {
            "source_type": "forum",
            "date": "2024-06-10",
            "title": "Best timing for sex — 30-day cycle, fertile window Days 12-18",
            "votes": 55,
            "is_accepted": True
        }
    },
    {
        "id": "forum_010",
        "content": (
            "Question (2024-04-02, 👍 38 votes): My partner was told he has low sperm motility "
            "(total motility 25%). What supplements should he take?\n\n"
            "Accepted Answer: 25% total motility is significantly below the WHO reference of "
            ">40%. Good news — sperm regenerate over approximately 72 days (one spermatogenesis "
            "cycle), so a targeted 3-month supplement protocol can meaningfully improve results. "
            "Evidence-based protocol for low motility: (1) CoQ10 ubiquinol 300–400 mg/day — "
            "sperm mitochondria in the mid-piece drive motility, and CoQ10 directly fuels this. "
            "(2) Zinc picolinate 25–30 mg/day — essential for sperm maturation. (3) Selenium "
            "100–200 mcg/day — selenoprotein P is concentrated in testes and required for "
            "flagellar structure. (4) Vitamin C 1,000 mg/day + Vitamin E 400 IU/day — "
            "antioxidant protection against DNA damage. (5) L-carnitine 1–2 g/day — "
            "supports sperm energy metabolism. Retest after 3 months."
        ),
        "metadata": {
            "source_type": "forum",
            "date": "2024-04-02",
            "title": "Low sperm motility 25% — what supplements help?",
            "votes": 38,
            "is_accepted": True
        }
    },
    {
        "id": "forum_011",
        "content": (
            "Question (2024-08-20, 👍 44 votes): I've been trying to conceive for 8 months "
            "with no success. I'm 34. FertiliQ shows everything seems 'in range'. What "
            "should I check next?\n\n"
            "Accepted Answer: 8 months at 34 with in-range results — time to dig deeper. "
            "FertiliQ's escalation protocol for this scenario: (1) Check homocysteine — even "
            "with genetic and folate data, an elevated homocysteine (>10 µmol/L) is a red flag "
            "for methylation pathway dysfunction and is associated with recurrent implantation "
            "failure. (2) Get a full thyroid panel including TPO antibodies — subclinical "
            "hypothyroidism (TSH 2.5–4.5) and Hashimoto's are significantly associated with "
            "infertility even with 'normal' TSH. (3) Male factor: full semen analysis plus "
            "DNA fragmentation index (DFI) — if DFI >25%, this is a hidden cause of unexplained "
            "infertility not visible on standard SA. (4) Consider ERA (Endometrial Receptivity "
            "Analysis) if pursuing IVF. (5) At 34 after 8 months, specialist referral is "
            "appropriate — don't wait for the 12-month 'standard' guideline."
        ),
        "metadata": {
            "source_type": "forum",
            "date": "2024-08-20",
            "title": "8 months TTC with in-range results — what to check next?",
            "votes": 44,
            "is_accepted": True
        }
    },
    {
        "id": "forum_012",
        "content": (
            "Question (2024-09-05, 👍 28 votes): The FertiliQ app crashed when I tried to "
            "sync my Oura ring data. Error message says 'Wearable sync failed — invalid token'. "
            "How do I fix this?\n\n"
            "Accepted Answer: 'Invalid token' on Oura sync typically means your Oura API access "
            "token has expired (they expire every 7 days by default). Fix: Go to FertiliQ → "
            "Settings → Connected Wearables → Oura Ring → 'Reconnect'. This will prompt you "
            "to re-authorise FertiliQ in the Oura app. If the error persists after reconnecting: "
            "on your phone, uninstall and reinstall the FertiliQ app (data is cloud-saved), "
            "then reconnect Oura. Known issue in iOS 17+ — the Oura SDK has a token refresh bug "
            "that FertiliQ is working with Oura to resolve. Fix expected in next app update."
        ),
        "metadata": {
            "source_type": "forum",
            "date": "2024-09-05",
            "title": "Oura ring sync error — invalid token fix",
            "votes": 28,
            "is_accepted": True
        }
    },
    {
        "id": "forum_013",
        "content": (
            "Question (2024-02-28, 👍 33 votes): What foods should I eat during the follicular "
            "phase to support egg development?\n\n"
            "Accepted Answer: Follicular phase is when your eggs are being recruited and one "
            "dominant follicle is maturing — this is prime time to support that process "
            "nutritionally. Key foods: (1) Leafy greens daily (spinach, kale, rocket) — "
            "natural folate for DNA synthesis in developing follicles. (2) Eggs (2/day) — "
            "choline for methylation, plus all B vitamins and fat-soluble vitamins in the yolk. "
            "(3) Wild salmon 2–3x/week — EPA/DHA for granulosa cell membranes and "
            "anti-inflammatory prostaglandins. (4) Colourful vegetables (bell peppers, "
            "carrots, berries) — antioxidants to neutralise follicular oxidative stress. "
            "(5) Fermented foods (kimchi, kefir, yoghurt) — gut microbiome supports oestrogen "
            "metabolism. (6) Brazil nuts (1–2/day) — selenium. Avoid: heavy alcohol, processed "
            "foods, excessive caffeine (>200 mg/day associated with reduced follicular response)."
        ),
        "metadata": {
            "source_type": "forum",
            "date": "2024-02-28",
            "title": "Follicular phase foods for egg development",
            "votes": 33,
            "is_accepted": True
        }
    },
    {
        "id": "forum_014",
        "content": (
            "Question (2023-07-14, 👍 19 votes): What does it mean if my FertiliQ genetic "
            "report says I have 'high oxidative stress risk'? Is that bad?\n\n"
            "Accepted Answer: High oxidative stress risk in FertiliQ means you have variants "
            "in one or more genes involved in antioxidant defence — typically GPX1 (glutathione "
            "peroxidase), SOD2 (superoxide dismutase), or GSTM1 (glutathione S-transferase). "
            "These genes normally neutralise reactive oxygen species (ROS) that are produced as "
            "byproducts of normal metabolism. With reduced antioxidant gene efficiency, you're "
            "more susceptible to oxidative damage — particularly in metabolically demanding "
            "cells like eggs and sperm. This isn't catastrophic — it means antioxidant "
            "supplementation and diet become more important for you than for someone without "
            "these variants. Practical action: increase CoQ10 (400 mg), add NAC 600 mg twice "
            "daily, ensure Vitamin C and E through food and supplements, reduce alcohol, "
            "processed food and environmental toxin exposure."
        ),
        "metadata": {
            "source_type": "forum",
            "date": "2023-07-14",
            "title": "High oxidative stress risk in genetic report — what does it mean?",
            "votes": 19,
            "is_accepted": True
        }
    },
    {
        "id": "forum_015",
        "content": (
            "Question (2024-11-01, 👍 51 votes): I've heard conflicting things about how much "
            "folic acid vs methylfolate MTHFR carriers should take. Some old posts here say "
            "400 mcg is fine, some say 800 mcg methylfolate. What's the actual current "
            "recommendation?\n\n"
            "Accepted Answer: I understand the confusion — FertiliQ actually changed this "
            "recommendation between versions! The 400 mcg folic acid advice in older posts (2022) "
            "was from FertiliQ v1.0 and reflected the standard preconception recommendation at "
            "the time. FertiliQ v2.1 (released January 2024) updated this specifically for "
            "MTHFR carriers: the current recommendation is 800 mcg 5-MTHF (methylfolate) for "
            "C677T homozygous carriers, and 400–800 mcg methylfolate for heterozygous carriers. "
            "Standard folic acid is no longer recommended for MTHFR variant carriers in the "
            "current guidelines. Always check the version tag on documentation — if it says "
            "v1.0 or is dated pre-2024, the folate recommendation may be the old 400 mcg one."
        ),
        "metadata": {
            "source_type": "forum",
            "date": "2024-11-01",
            "title": "MTHFR folic acid vs methylfolate — current recommendation clarified",
            "votes": 51,
            "is_accepted": True
        }
    },
    {
        "id": "forum_016",
        "content": (
            "Question (2024-10-15, 👍 37 votes): Should I be having sex every day during my "
            "fertile window to maximise chances?\n\n"
            "Accepted Answer: Counter-intuitively, every other day is generally as effective "
            "as daily and sometimes better. The reason: sperm require 48–72 hours to replenish "
            "in adequate numbers after ejaculation. Daily sex can reduce total sperm count and "
            "motility per ejaculate, especially if the baseline count is already borderline. "
            "Exception: if your partner has been assessed with a high sperm count and excellent "
            "motility (>60 million/mL, >50% progressive motility), daily sex during peak "
            "fertile days (the 48 hours before and including ovulation) is fine. The "
            "every-other-day approach also reduces performance pressure and fatigue, which can "
            "be a meaningful quality-of-life factor over months of trying."
        ),
        "metadata": {
            "source_type": "forum",
            "date": "2024-10-15",
            "title": "Sex every day vs every other day during fertile window",
            "votes": 37,
            "is_accepted": True
        }
    },
    {
        "id": "forum_017",
        "content": (
            "Question (2024-12-03, 👍 43 votes): My FertiliQ dashboard shows a 'methylation "
            "pathway concern' flag. What does this mean and what should I do?\n\n"
            "Accepted Answer: The methylation pathway concern flag is triggered when FertiliQ's "
            "algorithm detects a combination of factors: MTHFR variant present + homocysteine "
            "above 9 µmol/L + folate (RBC) below 800 nmol/L. This combination suggests your "
            "methylation cycle is running suboptimally. Methylation drives hundreds of reactions "
            "critical for fertility: DNA repair, gene expression, neurotransmitter synthesis, "
            "and detoxification. Priority actions: (1) Switch to methylfolate 800 mcg if not "
            "already (never standard folic acid with MTHFR). (2) Add methylcobalamin 1,000 mcg "
            "B12. (3) Add TMG (trimethylglycine) 500–1,000 mg/day — a methyl donor that helps "
            "reduce homocysteine independently. (4) Retest homocysteine after 8 weeks."
        ),
        "metadata": {
            "source_type": "forum",
            "date": "2024-12-03",
            "title": "Methylation pathway concern flag — what to do?",
            "votes": 43,
            "is_accepted": True
        }
    },
    {
        "id": "forum_018",
        "content": (
            "Question (2024-08-07, 👍 26 votes): I'm in the two-week wait (TWW). Is it OK "
            "to exercise?\n\n"
            "Accepted Answer: Yes, but keep it moderate. The luteal phase (which is what the "
            "TWW is) naturally calls for reduced intensity anyway due to progesterone's effects "
            "on energy. FertiliQ guidelines for the TWW: keep heart rate below 140 bpm, "
            "avoid sustained HIIT or heavy lifting, no hot yoga or saunas (elevated core "
            "temperature may affect implantation). Good TWW activities: walking, gentle yoga, "
            "Pilates, swimming at easy pace. There's no evidence that normal moderate exercise "
            "prevents implantation, so don't feel you need to be on bedrest. In fact, "
            "gentle movement supports blood flow to the uterus. Just avoid the kind of "
            "all-out sessions that significantly spike cortisol."
        ),
        "metadata": {
            "source_type": "forum",
            "date": "2024-08-07",
            "title": "Exercise during the two-week wait — is it safe?",
            "votes": 26,
            "is_accepted": True
        }
    },
    {
        "id": "forum_019",
        "content": (
            "Question (2023-05-22, 👍 15 votes): How do I read my genetic report — what does "
            "'Clinical Impact Score 7' mean for my MTHFR result?\n\n"
            "Accepted Answer: The Clinical Impact Score (CIS) in FertiliQ runs from 0–10. "
            "A CIS of 7 for MTHFR means this variant is having a significant functional "
            "impact on your methylation pathway — it's near the high end of the scale. "
            "CIS 0–3: low functional impact, lifestyle support recommended. "
            "CIS 4–6: moderate impact, targeted supplementation recommended. "
            "CIS 7–9: high impact, specific therapeutic supplementation essential. "
            "CIS 10: severe impact, may warrant clinical methylation assessment. "
            "At CIS 7, the FertiliQ recommendation is that methylfolate 800 mcg + "
            "methylcobalamin B12 are non-optional for you, not just 'nice to have'. "
            "The scoring also factors in your biomarker context — if your homocysteine "
            "is elevated or RBC folate is low, the CIS will be on the higher end."
        ),
        "metadata": {
            "source_type": "forum",
            "date": "2023-05-22",
            "title": "What does Clinical Impact Score 7 mean for MTHFR?",
            "votes": 15,
            "is_accepted": True
        }
    },
    {
        "id": "forum_020",
        "content": (
            "Question (2024-06-25, 👍 48 votes): Is there a bug with the FSH chart on the "
            "dashboard? My Day 3 FSH shows as 9.2 mIU/mL but it's graphed outside the green "
            "zone even though 9 is supposed to be normal.\n\n"
            "Accepted Answer: This is a known display bug in FertiliQ app version 3.1.0 "
            "(iOS and Android). The FSH chart is using a hardcoded population reference range "
            "(3–10 mIU/mL) for the green zone, but FertiliQ's fertility-optimised optimal "
            "range is 3–8 mIU/mL. So 9.2 is technically above the FertiliQ optimal range "
            "even though it's within the lab reference. Your result is not alarming — 9.2 "
            "is borderline but not pathological. The chart rendering bug is confirmed and will "
            "be corrected in v3.1.1. In the meantime, refer to the numeric value and the "
            "colour-coded bar in the Biomarker Details view, which uses the correct "
            "fertility-optimised thresholds."
        ),
        "metadata": {
            "source_type": "forum",
            "date": "2024-06-25",
            "title": "FSH chart display bug — outside green zone at 9.2?",
            "votes": 48,
            "is_accepted": True
        }
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# BLOG DATA  (semantic paragraphs; title and date embedded in each chunk)
# ─────────────────────────────────────────────────────────────────────────────

BLOGS = [

    # ───── Article 1: MTHFR and Folate Metabolism (2024-03-15) ─────
    {
        "id": "blog_001",
        "content": (
            "[Article: The Science of MTHFR and Folate Metabolism | Date: 2024-03-15]\n\n"
            "MTHFR (methylenetetrahydrofolate reductase) is arguably the most clinically "
            "relevant gene variant for preconception health. This enzyme catalyses the final "
            "step in converting dietary folate into 5-methyltetrahydrofolate (5-MTHF) — the "
            "only form that can donate a methyl group to convert homocysteine back to "
            "methionine. This methylation reaction sits at the hub of a network of hundreds "
            "of biochemical processes including DNA synthesis, gene expression regulation, "
            "neurotransmitter production, and detoxification. When MTHFR activity is impaired, "
            "the downstream consequences ripple across nearly every system in the body."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2024-03-15",
            "title": "The Science of MTHFR and Folate Metabolism"
        }
    },
    {
        "id": "blog_002",
        "content": (
            "[Article: The Science of MTHFR and Folate Metabolism | Date: 2024-03-15]\n\n"
            "The two most studied MTHFR polymorphisms are C677T (rs1801133) and A1298C "
            "(rs1801131). The C677T variant involves a cytosine-to-thymine substitution at "
            "position 677, resulting in an alanine-to-valine amino acid change. This structural "
            "alteration reduces enzyme thermostability and activity. Heterozygous carriers (CT) "
            "have approximately 35–40% reduced enzyme activity; homozygous carriers (TT) have "
            "60–70% reduced activity. The A1298C variant has a more complex mechanism, affecting "
            "the enzyme's interaction with the BH4 cofactor rather than directly reducing "
            "thermostability. Compound heterozygosity (one of each variant) produces an "
            "intermediate-to-significant functional impact."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2024-03-15",
            "title": "The Science of MTHFR and Folate Metabolism"
        }
    },
    {
        "id": "blog_003",
        "content": (
            "[Article: The Science of MTHFR and Folate Metabolism | Date: 2024-03-15]\n\n"
            "For MTHFR C677T homozygous individuals, standard synthetic folic acid "
            "supplementation is now understood to be insufficient and potentially counterproductive. "
            "Synthetic folic acid requires the MTHFR enzyme itself to convert to 5-MTHF — "
            "precisely the step that is impaired. Research from 2022–2024 demonstrates that "
            "unmetabolised folic acid (UMFA) accumulates in the bloodstream of MTHFR TT "
            "carriers taking standard folic acid supplements. UMFA may competitively inhibit "
            "natural folate receptor uptake and has been associated with impaired NK cell "
            "function and disrupted immune tolerance at the implantation site. The clinical "
            "consensus supported by current evidence: MTHFR C677T carriers should take 800 mcg "
            "5-MTHF (methylfolate) directly, bypassing the impaired conversion step entirely."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2024-03-15",
            "title": "The Science of MTHFR and Folate Metabolism"
        }
    },
    {
        "id": "blog_004",
        "content": (
            "[Article: The Science of MTHFR and Folate Metabolism | Date: 2024-03-15]\n\n"
            "Methylfolate supplementation bypasses the MTHFR bottleneck by providing 5-MTHF "
            "directly to the methylation cycle. The recommended form is L-methylfolate calcium "
            "(also sold as Metafolin, Quatrefolic), which is chemically identical to the "
            "predominant form of folate in human plasma. For C677T TT carriers, 800 mcg daily "
            "is the evidence-supported target dose. Importantly, methylfolate must be accompanied "
            "by adequate methylcobalamin (B12) — the two are co-factors in the homocysteine "
            "remethylation reaction. Taking methylfolate without B12 can drive a functional B12 "
            "deficiency by 'using up' available B12 in methylation reactions without replenishing "
            "it. Always take 1,000 mcg methylcobalamin alongside your methylfolate."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2024-03-15",
            "title": "The Science of MTHFR and Folate Metabolism"
        }
    },

    # ───── Article 2: AMH and Ovarian Reserve (2024-05-20) ─────
    {
        "id": "blog_005",
        "content": (
            "[Article: AMH Levels and Ovarian Reserve: A Complete Interpretation Guide | Date: 2024-05-20]\n\n"
            "Anti-Müllerian hormone (AMH) is produced by granulosa cells of small antral and "
            "preantral follicles (2–6 mm diameter). Because these early-stage follicles are "
            "present throughout the cycle, AMH levels are remarkably stable regardless of the "
            "cycle day on which blood is drawn. This makes AMH the most reliable single marker "
            "of ovarian reserve currently available. However, AMH measures follicle quantity, "
            "not quality — a critical distinction that is often misunderstood by patients."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2024-05-20",
            "title": "AMH Levels and Ovarian Reserve: A Complete Interpretation Guide"
        }
    },
    {
        "id": "blog_006",
        "content": (
            "[Article: AMH Levels and Ovarian Reserve: A Complete Interpretation Guide | Date: 2024-05-20]\n\n"
            "A low AMH does not mean infertility. This point cannot be overstated. Women with "
            "AMH levels as low as 1–3 pmol/L have conceived naturally and with IVF. What low "
            "AMH means is: (1) lower quantity of recruitable follicles per cycle, (2) potentially "
            "shorter reproductive window before reaching menopause, (3) reduced response to "
            "ovarian stimulation in IVF (fewer eggs retrieved per cycle). Women with low AMH "
            "who are trying to conceive naturally should not interpret their results as futile. "
            "However, they should avoid delaying — ovarian reserve naturally declines with age, "
            "and time spent waiting reduces options. For IVF candidates with low AMH, a natural "
            "cycle IVF or mini-IVF approach often performs proportionally as well as conventional "
            "stimulation."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2024-05-20",
            "title": "AMH Levels and Ovarian Reserve: A Complete Interpretation Guide"
        }
    },
    {
        "id": "blog_007",
        "content": (
            "[Article: AMH Levels and Ovarian Reserve: A Complete Interpretation Guide | Date: 2024-05-20]\n\n"
            "Can AMH be improved? This is a nuanced question. AMH cannot be raised to levels "
            "that exceed your genetic follicular endowment — you cannot create new primordial "
            "follicles after birth. However, the measured AMH value can be influenced by "
            "modifiable factors: (1) Vitamin D deficiency is consistently associated with lower "
            "AMH; correcting a deficiency (to 50–70 ng/mL 25-OH-D) has been shown to improve "
            "AMH values in several studies. (2) DHEA supplementation (25–75 mg/day) in women "
            "with diminished ovarian reserve may improve follicular environment and, in some "
            "studies, AMH values — though evidence is mixed. (3) Reducing chronic inflammation "
            "and oxidative stress through diet and CoQ10 supplementation may support follicular "
            "health. (4) Smoking dramatically suppresses AMH — cessation can partially restore it."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2024-05-20",
            "title": "AMH Levels and Ovarian Reserve: A Complete Interpretation Guide"
        }
    },

    # ───── Article 3: CoQ10 — 2022 article (200mg recommendation) ─────
    # *** DELIBERATE CONTRADICTION: 200mg vs 400-600mg ***
    {
        "id": "blog_008",
        "content": (
            "[Article: CoQ10 and Egg Quality: The Mitochondrial Connection | Date: 2022-06-10]\n\n"
            "Coenzyme Q10 (CoQ10) is a fat-soluble antioxidant present in every cell membrane, "
            "with particularly high concentrations in tissues with high energy demand: heart, "
            "liver, kidney — and reproductive cells. In oocytes (eggs), mitochondria are "
            "responsible for generating the ATP required for meiotic spindle assembly, "
            "fertilisation and early embryonic cell divisions. With ageing, mitochondrial "
            "efficiency declines and CoQ10 levels fall, contributing to the age-related decline "
            "in egg quality. Supplemental CoQ10 aims to replenish this deficit."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2022-06-10",
            "title": "CoQ10 and Egg Quality: The Mitochondrial Connection"
        }
    },
    {
        "id": "blog_009",
        "content": (
            "[Article: CoQ10 and Egg Quality: The Mitochondrial Connection | Date: 2022-06-10]\n\n"
            "Based on the clinical research available in 2022, the evidence supports CoQ10 "
            "supplementation at 200 mg per day for women over 35 seeking to improve egg quality. "
            "The pivotal study by Bentov et al. (2014) and subsequent human data showed "
            "improvements in oocyte quality metrics with CoQ10 supplementation at this dose. "
            "The ubiquinone form (the oxidised form) has been used in most fertility research "
            "to date. Ubiquinol (the reduced form) offers better bioavailability and may be "
            "preferred, with an equivalent effect at a slightly lower dose. At 200 mg/day, "
            "plasma CoQ10 levels typically increase from a baseline of 0.5–0.8 µmol/L to "
            "0.8–1.2 µmol/L — within the FertiliQ optimal range."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2022-06-10",
            "title": "CoQ10 and Egg Quality: The Mitochondrial Connection"
        }
    },
    {
        "id": "blog_010",
        "content": (
            "[Article: CoQ10 and Egg Quality: The Mitochondrial Connection | Date: 2022-06-10]\n\n"
            "Practical recommendations for CoQ10 supplementation as of mid-2022: Start with "
            "200 mg/day of CoQ10 (ubiquinone or ubiquinol form). Take with your fattiest meal "
            "of the day for maximum absorption — CoQ10 is lipophilic. Allow at least 90 days "
            "for full benefit, as eggs require approximately one full maturation cycle (90 days) "
            "to benefit from improved mitochondrial support. Side effects are rare at 200 mg; "
            "very high doses (>600 mg) may occasionally cause GI discomfort. For IVF cycles, "
            "begin CoQ10 at least 3 months before planned egg retrieval."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2022-06-10",
            "title": "CoQ10 and Egg Quality: The Mitochondrial Connection"
        }
    },

    # ───── Article 4: CoQ10 Updated — 2024 article (400-600mg) ─────
    {
        "id": "blog_011",
        "content": (
            "[Article: CoQ10 and Egg Quality: Updated Evidence 2024 | Date: 2024-02-28]\n\n"
            "New meta-analytic data published in 2023 has substantially reshaped the CoQ10 "
            "dosing discussion for fertility. A systematic review of six RCTs and four "
            "observational studies (Becker et al., Reproductive Biology and Endocrinology, 2023) "
            "found that fertility-related outcomes — including oocyte maturation rate, blastocyst "
            "development rate, and clinical pregnancy rate — demonstrated a clear dose-response "
            "relationship: women randomised to 400–600 mg CoQ10 (ubiquinol) showed significantly "
            "better outcomes than those at 200 mg, particularly in women aged 35–42. The 200 mg "
            "dose that was considered standard in earlier literature appears to represent a "
            "minimum threshold rather than an optimal dose for fertility indication specifically."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2024-02-28",
            "title": "CoQ10 and Egg Quality: Updated Evidence 2024"
        }
    },
    {
        "id": "blog_012",
        "content": (
            "[Article: CoQ10 and Egg Quality: Updated Evidence 2024 | Date: 2024-02-28]\n\n"
            "Revised dosing recommendations based on 2023–2024 evidence:\n\n"
            "Women under 35 with good ovarian reserve: 200–300 mg ubiquinol/day is adequate.\n"
            "Women 35–39: 400 mg ubiquinol/day is the new evidence-based standard. The previous "
            "recommendation of 200 mg was based on studies that did not stratify by age group.\n"
            "Women 40+: 400–600 mg ubiquinol/day. The 2023 RCT specifically found that at 40+, "
            "the 600 mg group had a 23% higher blastocyst rate than the 200 mg group — a "
            "clinically meaningful difference. This should be the new standard of care for "
            "women in this age bracket pursuing fertility optimisation.\n\n"
            "The older 200 mg recommendation from pre-2023 sources is now considered "
            "suboptimal for fertility purposes, though still appropriate as a general "
            "cardiovascular and antioxidant maintenance dose."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2024-02-28",
            "title": "CoQ10 and Egg Quality: Updated Evidence 2024"
        }
    },
    {
        "id": "blog_013",
        "content": (
            "[Article: CoQ10 and Egg Quality: Updated Evidence 2024 | Date: 2024-02-28]\n\n"
            "For maximum CoQ10 bioavailability: choose ubiquinol (reduced form) over ubiquinone "
            "(oxidised form). Plasma ubiquinol levels after 400 mg ubiquinol supplementation "
            "are approximately 2-fold higher than after 400 mg ubiquinone, because the body "
            "must convert ubiquinone to ubiquinol before it can be used. This conversion step "
            "is itself energy-dependent and may be compromised in older cells. Liposomal CoQ10 "
            "formulations show 3–5x better absorption than standard softgels at equivalent "
            "doses and are worth considering for women 40+ who want to maximise tissue levels. "
            "Target: plasma CoQ10 ≥1.5 µmol/L for fertility optimisation; this typically "
            "requires 400–600 mg ubiquinol daily in the 40+ age group."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2024-02-28",
            "title": "CoQ10 and Egg Quality: Updated Evidence 2024"
        }
    },

    # ───── Article 5: Exercise and Hormone Optimisation (2024-04-10) ─────
    {
        "id": "blog_014",
        "content": (
            "[Article: Exercise and Hormone Optimisation for Fertility | Date: 2024-04-10]\n\n"
            "Exercise is one of the most powerful modulators of reproductive hormone balance — "
            "for better or worse, depending on the type, intensity and timing. In the right "
            "dose, exercise improves insulin sensitivity (critical for ovarian function), "
            "reduces androgens in PCOS, supports healthy body composition, reduces cortisol "
            "chronically (while acutely raising it), and improves sperm parameters in men. "
            "In the wrong dose — particularly chronic high-intensity endurance training — "
            "exercise suppresses the hypothalamic-pituitary-ovarian (HPO) axis through "
            "energy availability and cortisol pathways, leading to anovulation, luteal phase "
            "defects, and reduced oestrogen."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2024-04-10",
            "title": "Exercise and Hormone Optimisation for Fertility"
        }
    },
    {
        "id": "blog_015",
        "content": (
            "[Article: Exercise and Hormone Optimisation for Fertility | Date: 2024-04-10]\n\n"
            "Resistance training stands out as the most fertility-beneficial form of exercise. "
            "Muscle tissue is an endocrine organ: it secretes myokines (including irisin and "
            "IL-6) that directly influence ovarian function, insulin signalling and "
            "anti-inflammatory pathways. For women with PCOS — where insulin resistance and "
            "hyperandrogenism disrupt follicular development — resistance training 3–4x/week "
            "is among the most evidence-backed non-pharmacological interventions. Aim for "
            "progressive overload: gradually increasing weight/resistance over weeks to "
            "drive continued hormonal adaptation."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2024-04-10",
            "title": "Exercise and Hormone Optimisation for Fertility"
        }
    },
    {
        "id": "blog_016",
        "content": (
            "[Article: Exercise and Hormone Optimisation for Fertility | Date: 2024-04-10]\n\n"
            "For women with diminished ovarian reserve (low AMH, high FSH), the exercise "
            "prescription requires additional caution. Vigorous cardio (>80% HRmax for >45 "
            "minutes) acutely raises cortisol significantly. Chronically elevated cortisol "
            "competes with progesterone at the receptor level and suppresses LH pulsatility. "
            "The FertiliQ recommendation for DOR: limit vigorous cardio to 30–45 minutes max "
            "twice weekly; prioritise Zone 2 cardio (60–70% HRmax) and resistance training. "
            "Yoga and mindfulness-based movement have the added benefit of HPA axis regulation, "
            "directly addressing the cortisol component."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2024-04-10",
            "title": "Exercise and Hormone Optimisation for Fertility"
        }
    },

    # ───── Article 6: Male Fertility (2024-07-15) ─────
    {
        "id": "blog_017",
        "content": (
            "[Article: Male Fertility: Optimising Sperm Quality Through Nutrition and Supplements | Date: 2024-07-15]\n\n"
            "Male factor infertility contributes to approximately 40–50% of all infertility "
            "cases, yet it remains significantly under-assessed relative to female factors. "
            "The most commonly assessed parameters — sperm concentration, motility and "
            "morphology — represent only part of the picture. Sperm DNA fragmentation, "
            "oxidative stress markers, and mitochondrial function in the sperm mid-piece "
            "are increasingly recognised as critical determinants of fertilisation success, "
            "embryo quality, and miscarriage risk. These parameters are all modifiable through "
            "targeted nutritional intervention."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2024-07-15",
            "title": "Male Fertility: Optimising Sperm Quality Through Nutrition and Supplements"
        }
    },
    {
        "id": "blog_018",
        "content": (
            "[Article: Male Fertility: Optimising Sperm Quality Through Nutrition and Supplements | Date: 2024-07-15]\n\n"
            "Zinc is perhaps the most critical mineral for male reproductive health. The testes "
            "contain the highest zinc concentration of any organ in the body. Zinc is required "
            "for: testosterone biosynthesis, sperm cell maturation (spermatogenesis), DNA "
            "integrity maintenance in sperm, and the activity of antioxidant enzymes including "
            "superoxide dismutase (SOD). Sub-optimal zinc (serum zinc <70 µg/dL) is associated "
            "with reduced testosterone, impaired sperm morphology and elevated DNA fragmentation. "
            "Supplementation: zinc picolinate 25–30 mg/day is the preferred form for absorption. "
            "Do not exceed 40 mg/day without copper supplementation (zinc competes with copper "
            "for intestinal absorption)."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2024-07-15",
            "title": "Male Fertility: Optimising Sperm Quality Through Nutrition and Supplements"
        }
    },
    {
        "id": "blog_019",
        "content": (
            "[Article: Male Fertility: Optimising Sperm Quality Through Nutrition and Supplements | Date: 2024-07-15]\n\n"
            "Selenium plays an indispensable role in male fertility through its incorporation "
            "into selenoproteins. Selenoprotein P is the primary selenium transport protein in "
            "blood; phospholipid glutathione peroxidase (PHGPx/GPX5) is expressed specifically "
            "in sperm and is essential for the structural integrity of the flagellum (the sperm "
            "tail that drives motility). Selenium deficiency is directly linked to impaired "
            "sperm motility and abnormal sperm morphology. Recommended dose: 100–200 mcg/day. "
            "Food sources: 1–2 Brazil nuts daily provides approximately 70–90 mcg selenium. "
            "Do not exceed 400 mcg/day (upper tolerable limit) — selenosis causes hair loss, "
            "nerve damage and GI distress."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2024-07-15",
            "title": "Male Fertility: Optimising Sperm Quality Through Nutrition and Supplements"
        }
    },
    {
        "id": "blog_020",
        "content": (
            "[Article: Male Fertility: Optimising Sperm Quality Through Nutrition and Supplements | Date: 2024-07-15]\n\n"
            "L-carnitine and acetyl-L-carnitine merit particular attention for men with low "
            "sperm motility. Carnitine is highly concentrated in the epididymis, where it "
            "supports sperm maturation and the fatty acid oxidation that powers sperm flagellar "
            "movement. Multiple RCTs have demonstrated that 2–3 g/day L-carnitine (or 1 g "
            "acetyl-L-carnitine + 1 g L-carnitine) improves total and progressive motility "
            "significantly over 3–6 months. For men with oligoasthenoteratozoospermia (OAT), "
            "the combination of L-carnitine + CoQ10 ubiquinol (400 mg) + selenium produces "
            "additive improvement in semen parameters. This combination should be taken for a "
            "minimum of one full spermatogenesis cycle (90 days) before reassessment."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2024-07-15",
            "title": "Male Fertility: Optimising Sperm Quality Through Nutrition and Supplements"
        }
    },

    # ───── Article 7: Conception Timing Strategies (2024-09-01) ─────
    {
        "id": "blog_021",
        "content": (
            "[Article: Precision Conception Timing: Beyond the OPK | Date: 2024-09-01]\n\n"
            "Ovulation predictor kits (OPKs) detect the LH surge that precedes ovulation by "
            "24–36 hours, giving couples a reliable signal for timing intercourse. But the "
            "fertile window is wider than many realise: sperm can survive in the female "
            "reproductive tract for 3–5 days in the presence of oestrogen-rich cervical mucus. "
            "This means that intercourse 3–4 days before ovulation can still result in "
            "fertilisation. The egg itself has a viability window of 12–24 hours post-ovulation. "
            "This asymmetry (long sperm survival, short egg viability) means that the optimal "
            "strategy is to have sperm in the fallopian tube waiting for the egg — not chasing "
            "the egg after ovulation."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2024-09-01",
            "title": "Precision Conception Timing: Beyond the OPK"
        }
    },
    {
        "id": "blog_022",
        "content": (
            "[Article: Precision Conception Timing: Beyond the OPK | Date: 2024-09-01]\n\n"
            "Cycle length variability significantly affects conception timing accuracy. A woman "
            "who believes she has a regular 28-day cycle may actually ovulate anywhere from Day "
            "11 to Day 21 across different cycles. Tracking multiple biomarkers simultaneously "
            "— LH, BBT, cervical mucus, and oestrogen (via urine or blood) — dramatically "
            "increases the precision of ovulation identification. FertiliQ's cycle model uses "
            "a Bayesian framework that updates the ovulation probability in real time as new "
            "daily data comes in. The more cycles tracked, the more personalised and accurate "
            "the prediction becomes — typically reaching high precision by cycle 3–4."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2024-09-01",
            "title": "Precision Conception Timing: Beyond the OPK"
        }
    },

    # ───── Article 8: Vitamin D and Fertility (2024-06-05) ─────
    {
        "id": "blog_023",
        "content": (
            "[Article: Vitamin D and Fertility: Why 'Sufficient' Isn't Enough | Date: 2024-06-05]\n\n"
            "Vitamin D receptors (VDR) are expressed in granulosa cells of ovarian follicles, "
            "endometrial cells, and immune cells at the implantation site. This ubiquitous "
            "expression signals the breadth of Vitamin D's influence on reproductive biology: "
            "follicular development, endometrial receptivity, immune tolerance of the embryo "
            "(preventing NK cell over-activation), and placental development. Studies consistently "
            "show that women with serum 25(OH)D >40 ng/mL have significantly higher IVF success "
            "rates than those with levels below 30 ng/mL. The association is dose-dependent "
            "up to approximately 60–70 ng/mL."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2024-06-05",
            "title": "Vitamin D and Fertility: Why 'Sufficient' Isn't Enough"
        }
    },
    {
        "id": "blog_024",
        "content": (
            "[Article: Vitamin D and Fertility: Why 'Sufficient' Isn't Enough | Date: 2024-06-05]\n\n"
            "Standard laboratory 'sufficient' threshold (30 ng/mL) is inadequate for fertility "
            "optimisation. This threshold was established for bone health endpoints, not "
            "reproductive outcomes. FertiliQ's fertility-specific target of 50–70 ng/mL is "
            "supported by the reproductive endocrinology literature. A 2023 systematic review "
            "of 14 IVF cohort studies found that the odds ratio for live birth was 1.46 for "
            "women with 25(OH)D >50 ng/mL compared to those below 30 ng/mL. For women with "
            "a level of 18 ng/mL (severely deficient), aggressive repletion with 5,000 IU/day "
            "D3 is justified, with retesting at 12 weeks. At 18 ng/mL, it typically takes "
            "4–6 months to reach the 50–70 ng/mL target with 5,000 IU daily."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2024-06-05",
            "title": "Vitamin D and Fertility: Why 'Sufficient' Isn't Enough"
        }
    },

    # ───── Article 9: Oxidative Stress (2023-11-20) ─────
    {
        "id": "blog_025",
        "content": (
            "[Article: Oxidative Stress, Genetic Variants, and Fertility | Date: 2023-11-20]\n\n"
            "Reactive oxygen species (ROS) are generated as byproducts of normal cellular "
            "metabolism, particularly in mitochondria. In reproductive cells — oocytes and sperm "
            "— ROS at low levels serve signalling functions (acrosome reaction, fertilisation). "
            "At excessive levels, however, ROS cause oxidative damage to lipid membranes, "
            "proteins, and critically, DNA. In sperm, oxidative DNA damage elevates the DNA "
            "fragmentation index (DFI), impairing embryo development and implantation. In oocytes, "
            "mitochondrial oxidative damage impairs ATP production critical for meiosis and early "
            "embryonic division."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2023-11-20",
            "title": "Oxidative Stress, Genetic Variants, and Fertility"
        }
    },
    {
        "id": "blog_026",
        "content": (
            "[Article: Oxidative Stress, Genetic Variants, and Fertility | Date: 2023-11-20]\n\n"
            "FertiliQ analyses oxidative stress risk through several gene pathways. The GPX1 "
            "(glutathione peroxidase 1) Pro198Leu polymorphism (rs1050450) reduces GPX enzyme "
            "activity, impairing hydrogen peroxide neutralisation. SOD2 Ala16Val (rs4880) — "
            "the most studied oxidative stress variant — is found in approximately 40% of "
            "the population in heterozygous form and affects mitochondrial superoxide "
            "dismutase targeting, reducing its transit to the mitochondrial matrix where it "
            "is needed most. GSTM1 null genotype (deletion polymorphism) eliminates a class "
            "of glutathione transferase enzymes that conjugate and neutralise oxidative toxins. "
            "Having two or more of these variants in combination significantly elevates baseline "
            "oxidative stress risk."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2023-11-20",
            "title": "Oxidative Stress, Genetic Variants, and Fertility"
        }
    },
    {
        "id": "blog_027",
        "content": (
            "[Article: Oxidative Stress, Genetic Variants, and Fertility | Date: 2023-11-20]\n\n"
            "For individuals with high oxidative stress risk profiles (multiple antioxidant gene "
            "variants), the supplementation priority is significantly elevated. The evidence-based "
            "antioxidant stack for fertility: CoQ10 ubiquinol 400 mg/day (simultaneous "
            "antioxidant and ATP production support), NAC 600 mg twice daily (glutathione "
            "precursor, directly addresses GPX pathway weakness), Vitamin E mixed tocopherols "
            "200–400 IU (lipid-soluble antioxidant, protects cell membranes), Vitamin C 1,000 mg "
            "(water-soluble, regenerates Vitamin E), Astaxanthin 4 mg/day (the most potent "
            "known antioxidant carotenoid, with specific benefits for sperm quality). Diet "
            "should emphasise polyphenol-rich foods: blueberries, pomegranate, dark chocolate, "
            "green tea (not extract — whole tea is safer for COMT slow metabolisers)."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2023-11-20",
            "title": "Oxidative Stress, Genetic Variants, and Fertility"
        }
    },

    # ───── Article 10: Follicular Phase Nutrition (2024-08-12) ─────
    {
        "id": "blog_028",
        "content": (
            "[Article: Eating for Each Phase: Follicular Phase Nutrition Guide | Date: 2024-08-12]\n\n"
            "The follicular phase is the active growth phase of the menstrual cycle, driven by "
            "FSH recruiting a cohort of follicles, with one dominant follicle emerging to "
            "maturity. Nutritional support during this phase directly influences the quality "
            "of the developing follicle and its oocyte. The follicular phase is also when "
            "oestrogen builds toward its pre-ovulatory peak, and nutrition can support healthy "
            "oestrogen metabolism as levels rise — particularly important for COMT slow-"
            "metaboliser variants."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2024-08-12",
            "title": "Eating for Each Phase: Follicular Phase Nutrition Guide"
        }
    },
    {
        "id": "blog_029",
        "content": (
            "[Article: Eating for Each Phase: Follicular Phase Nutrition Guide | Date: 2024-08-12]\n\n"
            "Key nutrients for follicular phase support: (1) Folate (or methylfolate for MTHFR "
            "carriers): spinach, lentils, asparagus, edamame — DNA synthesis in rapidly "
            "dividing follicular cells requires sustained folate supply. (2) Iron: The endometrium "
            "is rebuilding after menstruation and follicular cells require iron for oxidative "
            "phosphorylation. Red lentils, pumpkin seeds, dark leafy greens + Vitamin C for "
            "absorption. (3) Zinc: Follicular fluid zinc concentration is a predictor of oocyte "
            "quality. Foods: oysters, pumpkin seeds, beef. (4) Vitamin E: Protects follicular "
            "membranes from lipid peroxidation as follicles enlarge. Sunflower seeds, almonds, "
            "avocado."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2024-08-12",
            "title": "Eating for Each Phase: Follicular Phase Nutrition Guide"
        }
    },
    {
        "id": "blog_030",
        "content": (
            "[Article: Eating for Each Phase: Follicular Phase Nutrition Guide | Date: 2024-08-12]\n\n"
            "The follicular phase is the optimal time for fermented foods and probiotic-rich "
            "foods because the gut microbiome significantly influences oestrogen metabolism. "
            "The 'estrobolome' — the subset of gut bacteria that metabolise oestrogens — "
            "determines how efficiently used oestrogens are excreted vs reabsorbed. An "
            "imbalanced estrobolome can lead to oestrogen recirculation (raising total oestrogen "
            "burden) or insufficient oestrogen (reducing the pre-ovulatory surge). Fermented "
            "foods to prioritise during follicular phase: plain kefir, kimchi, sauerkraut, "
            "miso, tempeh. Fibre (25–35g/day) from vegetables and legumes supports oestrogen "
            "excretion by binding to oestrogen-glucuronide conjugates in the intestine."
        ),
        "metadata": {
            "source_type": "blog",
            "date": "2024-08-12",
            "title": "Eating for Each Phase: Follicular Phase Nutrition Guide"
        }
    },
]


def generate_data():
    """Write all synthetic knowledge base data to JSON files in the data/ directory."""
    data_dir = Path(__file__).parent / "data"
    data_dir.mkdir(exist_ok=True)

    with open(data_dir / "documentation.json", "w", encoding="utf-8") as f:
        json.dump(DOCUMENTATION, f, indent=2, ensure_ascii=False)
    print(f"[OK] documentation.json — {len(DOCUMENTATION)} entries "
          f"({sum(1 for d in DOCUMENTATION if not d['is_parent'])} child chunks, "
          f"{sum(1 for d in DOCUMENTATION if d['is_parent'])} parent sections)")

    with open(data_dir / "forums.json", "w", encoding="utf-8") as f:
        json.dump(FORUMS, f, indent=2, ensure_ascii=False)
    print(f"[OK] forums.json — {len(FORUMS)} QA-pair chunks")

    with open(data_dir / "blogs.json", "w", encoding="utf-8") as f:
        json.dump(BLOGS, f, indent=2, ensure_ascii=False)
    print(f"[OK] blogs.json — {len(BLOGS)} paragraph chunks")


if __name__ == "__main__":
    generate_data()

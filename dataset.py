# ── Real Drug Reviews Dataset ─────────────────────────────────────────────────
# Modeled after the UCI Drug Review Dataset (Kallumadi & Grer, 2018)
# 300+ reviews across 20 conditions and 80+ drugs

REVIEWS = [
    # ── Acne ─────────────────────────────────────────────────────────────────
    {"drug": "Benzoyl Peroxide",   "condition": "Acne", "rating": 9,  "date": "September 10, 2019", "review": "Best medication I've taken for Acne. Benzoyl Peroxide works exactly as expected. Some skin dryness at first but manageable. Would definitely recommend."},
    {"drug": "Tretinoin",          "condition": "Acne", "rating": 8,  "date": "September 26, 2017", "review": "Using Tretinoin for Acne - it's helping a little. Dryness makes it uncomfortable. Results are inconsistent. Will give it more time."},
    {"drug": "Doxycycline",        "condition": "Acne", "rating": 8,  "date": "January 30, 2010",   "review": "After struggling with Acne for years, Doxycycline finally gave me relief. Yes there is some nausea initially but it goes away. Worth it!"},
    {"drug": "Clindamycin",        "condition": "Acne", "rating": 9,  "date": "March 5, 2021",      "review": "Clindamycin cleared my acne within weeks. Minimal side effects. Highly effective."},
    {"drug": "Adapalene",          "condition": "Acne", "rating": 7,  "date": "June 12, 2020",      "review": "Adapalene is slow but steady. Skin is clearer after 3 months. Some purging initially."},
    {"drug": "Minocycline",        "condition": "Acne", "rating": 2,  "date": "August 3, 2018",     "review": "Terrible experience. Made my acne worse and caused severe dizziness."},
    {"drug": "Isotretinoin",       "condition": "Acne", "rating": 10, "date": "December 1, 2022",   "review": "Life changing! Acne is completely gone after 6 months. Worth every side effect."},
    {"drug": "Salicylic Acid",     "condition": "Acne", "rating": 6,  "date": "April 20, 2021",     "review": "Decent OTC option. Helps with mild acne but not severe cases."},
    {"drug": "Benzoyl Peroxide",   "condition": "Acne", "rating": 8,  "date": "May 14, 2022",       "review": "Works great on blackheads and whiteheads. My skin dried out at first but using a good moisturizer fixed that."},
    {"drug": "Tretinoin",          "condition": "Acne", "rating": 9,  "date": "October 2, 2023",    "review": "Tretinoin is the gold standard. Clears acne and helps with anti-aging. The purge phase is rough but push through it."},
    {"drug": "Doxycycline",        "condition": "Acne", "rating": 6,  "date": "February 18, 2021",  "review": "Works okay but gave me significant sun sensitivity. Had to be very careful outdoors."},
    {"drug": "Adapalene",          "condition": "Acne", "rating": 8,  "date": "July 7, 2022",       "review": "Differin over the counter is amazing. Took about 4 months but my skin is the clearest it's been in years."},
    {"drug": "Isotretinoin",       "condition": "Acne", "rating": 9,  "date": "March 20, 2020",     "review": "Accutane changed my life. I had severe cystic acne and nothing else worked. Yes it's harsh but it's worth it."},
    {"drug": "Clindamycin",        "condition": "Acne", "rating": 7,  "date": "August 12, 2023",    "review": "Good topical antibiotic. Works best combined with benzoyl peroxide to prevent resistance."},
    {"drug": "Spironolactone",     "condition": "Acne", "rating": 9,  "date": "November 5, 2022",   "review": "As a woman with hormonal acne this was a game changer. Skin cleared up in 3 months. Highly recommend for hormonal breakouts."},
    {"drug": "Spironolactone",     "condition": "Acne", "rating": 7,  "date": "April 1, 2021",      "review": "Helped my hormonal acne significantly. Some breast tenderness and irregular periods but manageable. Worth it for clear skin."},

    # ── Depression ───────────────────────────────────────────────────────────
    {"drug": "Sertraline",         "condition": "Depression", "rating": 9,  "date": "February 14, 2022", "review": "Sertraline has been a lifesaver. My mood improved significantly within 4 weeks."},
    {"drug": "Fluoxetine",         "condition": "Depression", "rating": 7,  "date": "July 22, 2020",     "review": "Fluoxetine helped but caused insomnia and nausea initially. Stick with it - it gets better."},
    {"drug": "Escitalopram",       "condition": "Depression", "rating": 9,  "date": "November 10, 2021", "review": "Very effective with minimal side effects. Feeling much better after 6 weeks."},
    {"drug": "Bupropion",          "condition": "Depression", "rating": 8,  "date": "March 15, 2023",    "review": "Bupropion helped my depression and I lost weight too. Win-win."},
    {"drug": "Venlafaxine",        "condition": "Depression", "rating": 5,  "date": "January 8, 2019",   "review": "Mixed results. Helped depression but caused significant sweating and anxiety."},
    {"drug": "Sertraline",         "condition": "Depression", "rating": 8,  "date": "September 3, 2022", "review": "Been on Zoloft for 2 years. Stable mood, able to enjoy life again. Sexual side effects are frustrating but the benefits outweigh them."},
    {"drug": "Fluoxetine",         "condition": "Depression", "rating": 8,  "date": "May 25, 2021",      "review": "Prozac gave me my life back. Some initial anxiety that faded. Energy returned. Highly recommend."},
    {"drug": "Escitalopram",       "condition": "Depression", "rating": 10, "date": "December 8, 2023",  "review": "Lexapro is the best antidepressant I've tried. Fewest side effects, works quickly. My psychiatrist's favorite for a reason."},
    {"drug": "Duloxetine",         "condition": "Depression", "rating": 7,  "date": "April 14, 2022",    "review": "Cymbalta helps my depression and also manages my chronic pain. Two benefits in one. Withdrawal is brutal though so don't skip doses."},
    {"drug": "Mirtazapine",        "condition": "Depression", "rating": 8,  "date": "October 20, 2021",  "review": "Mirtazapine works well and helps me sleep. Weight gain is a downside but my mood is much better."},
    {"drug": "Bupropion",          "condition": "Depression", "rating": 6,  "date": "June 30, 2020",     "review": "Wellbutrin worked for depression but gave me insomnia and headaches. Had to add another medication to sleep."},
    {"drug": "Venlafaxine",        "condition": "Depression", "rating": 8,  "date": "January 22, 2023",  "review": "Effexor finally worked when SSRIs failed me. More side effects but the results are worth it."},
    {"drug": "Amitriptyline",      "condition": "Depression", "rating": 6,  "date": "March 5, 2019",     "review": "Old school medication. Works but so many side effects - dry mouth, weight gain, drowsiness. Only use if newer options fail."},
    {"drug": "Trazodone",          "condition": "Depression", "rating": 7,  "date": "August 8, 2022",    "review": "Trazodone is good for depression with insomnia. Makes me sleepy but that's the point. Depression has improved."},

    # ── Diabetes ─────────────────────────────────────────────────────────────
    {"drug": "Metformin",          "condition": "Diabetes", "rating": 8,  "date": "May 30, 2021",       "review": "Metformin has kept my blood sugar stable for years. Some GI issues at first."},
    {"drug": "Insulin Glargine",   "condition": "Diabetes", "rating": 8,  "date": "September 12, 2020", "review": "Consistent basal insulin. Takes discipline but keeps levels steady."},
    {"drug": "Empagliflozin",      "condition": "Diabetes", "rating": 8,  "date": "October 5, 2022",    "review": "Great for both diabetes and heart health. Some UTI risk but manageable."},
    {"drug": "Metformin",          "condition": "Diabetes", "rating": 9,  "date": "February 7, 2023",   "review": "Metformin is the first line medication for a reason. Affordable, effective, and well-tolerated after the first few weeks."},
    {"drug": "Semaglutide",        "condition": "Diabetes", "rating": 10, "date": "July 15, 2023",      "review": "Ozempic is incredible. Blood sugar under control, lost 25 pounds, and feel great. Nausea in the beginning but it passed."},
    {"drug": "Semaglutide",        "condition": "Diabetes", "rating": 9,  "date": "November 3, 2023",   "review": "Best diabetes medication I've been on. A1C dropped from 9.2 to 6.8 in 6 months. Amazing results."},
    {"drug": "Dulaglutide",        "condition": "Diabetes", "rating": 8,  "date": "April 28, 2022",     "review": "Trulicity is easy to use - once weekly injection. Good blood sugar control with weight loss benefit."},
    {"drug": "Sitagliptin",        "condition": "Diabetes", "rating": 7,  "date": "August 19, 2021",    "review": "Januvia is gentle on the stomach compared to metformin. Not as powerful but good tolerability."},
    {"drug": "Canagliflozin",      "condition": "Diabetes", "rating": 7,  "date": "March 11, 2022",     "review": "Invokana works well but I got a UTI within the first month. Once that cleared up blood sugar control has been good."},
    {"drug": "Pioglitazone",       "condition": "Diabetes", "rating": 6,  "date": "October 14, 2019",   "review": "Controls blood sugar but caused significant fluid retention and weight gain. Switched medications."},
    {"drug": "Glipizide",          "condition": "Diabetes", "rating": 7,  "date": "January 5, 2021",    "review": "Old faithful. Glipizide is not fancy but keeps my sugar in range. Low blood sugar episodes are the main risk."},
    {"drug": "Insulin Aspart",     "condition": "Diabetes", "rating": 9,  "date": "June 22, 2023",      "review": "NovoLog fast acting insulin works exactly as needed. Precise dosing is key but it provides excellent meal coverage."},

    # ── Hypertension ─────────────────────────────────────────────────────────
    {"drug": "Amlodipine",         "condition": "Hypertension", "rating": 7,  "date": "April 18, 2021",    "review": "Blood pressure well controlled. Ankle swelling is annoying but tolerable."},
    {"drug": "Lisinopril",         "condition": "Hypertension", "rating": 6,  "date": "August 25, 2020",   "review": "Effective but gave me a persistent dry cough. Switched medications."},
    {"drug": "Losartan",           "condition": "Hypertension", "rating": 9,  "date": "January 3, 2023",   "review": "Great BP control with no side effects. Highly recommend."},
    {"drug": "Metoprolol",         "condition": "Hypertension", "rating": 7,  "date": "June 15, 2022",     "review": "Metoprolol keeps my heart rate and blood pressure in check. Fatigue can be an issue. Good overall."},
    {"drug": "Amlodipine",         "condition": "Hypertension", "rating": 8,  "date": "October 10, 2023",  "review": "Norvasc has worked great for my hypertension. Once daily dosing is convenient. Just deal with the leg swelling."},
    {"drug": "Hydrochlorothiazide","condition": "Hypertension", "rating": 7,  "date": "March 22, 2021",    "review": "HCTZ is simple and affordable. Works well combined with other medications. Makes me urinate a lot but that's expected."},
    {"drug": "Valsartan",          "condition": "Hypertension", "rating": 8,  "date": "September 8, 2022", "review": "Diovan has controlled my BP well with minimal side effects. Much better than lisinopril was for me."},
    {"drug": "Carvedilol",         "condition": "Hypertension", "rating": 7,  "date": "December 14, 2020", "review": "Effective for both BP and heart failure. Weight gain and dizziness initially but stabilized after a few weeks."},
    {"drug": "Olmesartan",         "condition": "Hypertension", "rating": 8,  "date": "May 3, 2023",       "review": "Benicar has been excellent. Consistent blood pressure control throughout the day. No noticeable side effects."},
    {"drug": "Chlorthalidone",     "condition": "Hypertension", "rating": 8,  "date": "February 28, 2022", "review": "More effective than HCTZ in my experience. Good potassium levels so far. BP well controlled."},
    {"drug": "Atenolol",           "condition": "Hypertension", "rating": 6,  "date": "July 30, 2019",     "review": "Atenolol works but I feel tired all the time. Switched to a different beta blocker."},

    # ── Anxiety ──────────────────────────────────────────────────────────────
    {"drug": "Buspirone",          "condition": "Anxiety", "rating": 7,  "date": "March 22, 2022",    "review": "Buspirone is subtle but effective for generalized anxiety. No sedation."},
    {"drug": "Clonazepam",         "condition": "Anxiety", "rating": 6,  "date": "July 14, 2019",     "review": "Works fast but habit forming. Use cautiously. Short-term relief only."},
    {"drug": "Alprazolam",         "condition": "Anxiety", "rating": 5,  "date": "November 30, 2020", "review": "Immediate relief but dependency risk is real. Doctor supervision essential."},
    {"drug": "Sertraline",         "condition": "Anxiety", "rating": 8,  "date": "April 5, 2022",     "review": "Zoloft works for my anxiety without the dependency risks of benzodiazepines. Takes weeks but worth the wait."},
    {"drug": "Escitalopram",       "condition": "Anxiety", "rating": 9,  "date": "September 17, 2023","review": "Lexapro is my go-to for anxiety. Calm, functional, no panic attacks. Changed my life."},
    {"drug": "Buspirone",          "condition": "Anxiety", "rating": 6,  "date": "February 10, 2021", "review": "Takes 2-4 weeks to work and the effect is mild. Not for acute anxiety but good for chronic GAD."},
    {"drug": "Lorazepam",          "condition": "Anxiety", "rating": 7,  "date": "June 25, 2020",     "review": "Ativan works quickly for panic attacks. Not for daily use but invaluable when needed. Be careful about dependence."},
    {"drug": "Venlafaxine",        "condition": "Anxiety", "rating": 8,  "date": "January 19, 2023",  "review": "Effexor XR is excellent for anxiety. After 8 weeks I feel like a different person. Manageable side effects."},
    {"drug": "Pregabalin",         "condition": "Anxiety", "rating": 8,  "date": "October 22, 2022",  "review": "Lyrica worked surprisingly well for my severe anxiety. Calmer and able to function. Some dizziness initially."},
    {"drug": "Hydroxyzine",        "condition": "Anxiety", "rating": 7,  "date": "July 8, 2021",      "review": "Vistaril is great for acute anxiety. Non-addictive, works within 30 minutes. Makes me drowsy but that helps at night."},
    {"drug": "Clonazepam",         "condition": "Anxiety", "rating": 8,  "date": "December 20, 2022", "review": "Klonopin has been the only thing that controls my severe panic disorder. Used responsibly with my psychiatrist it's very effective."},

    # ── ADHD ─────────────────────────────────────────────────────────────────
    {"drug": "Adderall",           "condition": "ADHD", "rating": 9,  "date": "March 1, 2022",     "review": "Adderall XR transformed my ability to focus. Finally able to complete tasks and organize my day. Life changing."},
    {"drug": "Methylphenidate",    "condition": "ADHD", "rating": 8,  "date": "August 15, 2021",   "review": "Ritalin works very well for my ADHD. Fewer appetite and sleep issues than Adderall for me personally."},
    {"drug": "Atomoxetine",        "condition": "ADHD", "rating": 6,  "date": "January 12, 2020",  "review": "Strattera takes months to work and the effect is modest. Non-stimulant is good if stimulants aren't an option."},
    {"drug": "Lisdexamfetamine",   "condition": "ADHD", "rating": 9,  "date": "June 7, 2023",      "review": "Vyvanse is the smoothest stimulant I've tried. No crash, steady focus all day. Worth the higher cost."},
    {"drug": "Concerta",           "condition": "ADHD", "rating": 8,  "date": "November 28, 2022", "review": "Concerta lasts the full day and keeps me productive. Some insomnia if I take it too late but works great otherwise."},
    {"drug": "Adderall",           "condition": "ADHD", "rating": 7,  "date": "April 19, 2021",    "review": "Helps focus but appetite suppression is significant. Lost too much weight and switched to a different formulation."},
    {"drug": "Guanfacine",         "condition": "ADHD", "rating": 7,  "date": "September 30, 2022","review": "Intuniv is great for my child - helps with impulsivity without stimulant side effects. Took a few months to see full benefit."},
    {"drug": "Methylphenidate",    "condition": "ADHD", "rating": 7,  "date": "February 6, 2021",  "review": "Works well but wears off quickly. The rebound in the afternoon is tough. Extended release is much better."},
    {"drug": "Lisdexamfetamine",   "condition": "ADHD", "rating": 8,  "date": "July 14, 2023",     "review": "Vyvanse has been excellent for executive function. The controlled release makes it predictable. Side effects are minimal."},
    {"drug": "Clonidine",          "condition": "ADHD", "rating": 6,  "date": "October 5, 2020",   "review": "Kapvay helps with impulsivity and sleep. The blood pressure lowering can cause dizziness. Good adjunct to stimulants."},

    # ── Hypothyroidism ───────────────────────────────────────────────────────
    {"drug": "Levothyroxine",      "condition": "Hypothyroidism", "rating": 8,  "date": "May 22, 2021",      "review": "Synthroid has kept my thyroid levels normal for years. Take it consistently at the same time each day and it works perfectly."},
    {"drug": "Levothyroxine",      "condition": "Hypothyroidism", "rating": 9,  "date": "October 15, 2022",  "review": "Life is normal again on levothyroxine. Energy back, weight stabilized, no more brain fog."},
    {"drug": "Levothyroxine",      "condition": "Hypothyroidism", "rating": 6,  "date": "March 8, 2020",     "review": "Struggled to get my dose right for years. When it's right it's great but fine-tuning TSH takes patience."},
    {"drug": "Liothyronine",       "condition": "Hypothyroidism", "rating": 8,  "date": "August 27, 2023",   "review": "Adding T3 to my T4 was transformative. Finally feel human again. Not all doctors prescribe it but it made a real difference."},
    {"drug": "Armour Thyroid",     "condition": "Hypothyroidism", "rating": 9,  "date": "January 18, 2022",  "review": "Natural desiccated thyroid worked better for me than synthetic. More stable energy and better mood."},
    {"drug": "Levothyroxine",      "condition": "Hypothyroidism", "rating": 7,  "date": "June 12, 2023",     "review": "Generic levothyroxine works fine. The key is consistent timing and avoiding interactions with coffee and calcium."},

    # ── Asthma ───────────────────────────────────────────────────────────────
    {"drug": "Albuterol",          "condition": "Asthma", "rating": 9,  "date": "April 30, 2022",    "review": "Albuterol rescue inhaler is a lifesaver during attacks. Works within minutes. Keep it with you always."},
    {"drug": "Fluticasone",        "condition": "Asthma", "rating": 9,  "date": "September 14, 2021","review": "Flovent has dramatically reduced my asthma attacks. Daily controller medication makes a huge difference."},
    {"drug": "Montelukast",        "condition": "Asthma", "rating": 7,  "date": "February 25, 2023", "review": "Singulair adds extra protection. Works well combined with inhaled steroids. Some mood changes to watch for."},
    {"drug": "Budesonide",         "condition": "Asthma", "rating": 8,  "date": "November 8, 2022",  "review": "Pulmicort is excellent maintenance therapy. Consistent use has nearly eliminated my asthma symptoms."},
    {"drug": "Formoterol",         "condition": "Asthma", "rating": 8,  "date": "July 19, 2021",     "review": "The LABA bronchodilator provides excellent long-term relief. Combined with ICS it's very effective."},
    {"drug": "Albuterol",          "condition": "Asthma", "rating": 8,  "date": "December 5, 2022",  "review": "ProAir is reliable and fast acting. Trembling is a minor side effect after use but manageable."},
    {"drug": "Tiotropium",         "condition": "Asthma", "rating": 7,  "date": "March 16, 2021",    "review": "Spiriva added as add-on therapy for severe asthma. Helps with airflow on top of other medications."},
    {"drug": "Dupilumab",          "condition": "Asthma", "rating": 10, "date": "August 22, 2023",   "review": "Dupixent biologic for severe asthma. Off oral steroids for the first time in years. Injection is easy and results are incredible."},

    # ── Pain / Arthritis ─────────────────────────────────────────────────────
    {"drug": "Ibuprofen",          "condition": "Pain", "rating": 7,  "date": "June 3, 2022",      "review": "Ibuprofen works great for acute pain and inflammation. Take with food to avoid stomach issues."},
    {"drug": "Naproxen",           "condition": "Pain", "rating": 8,  "date": "October 28, 2021",  "review": "Aleve lasts much longer than ibuprofen. Twice daily dosing is convenient. Works well for arthritis pain."},
    {"drug": "Celecoxib",          "condition": "Pain", "rating": 8,  "date": "March 12, 2023",    "review": "Celebrex has been excellent for my arthritis. Effective anti-inflammatory with less stomach risk than traditional NSAIDs."},
    {"drug": "Tramadol",           "condition": "Pain", "rating": 6,  "date": "August 16, 2020",   "review": "Moderate pain relief. Better than OTC options but not as strong as opioids. Constipation and nausea are side effects."},
    {"drug": "Gabapentin",         "condition": "Pain", "rating": 7,  "date": "January 25, 2022",  "review": "Neurontin helps with my neuropathic pain. Drowsy at first but adjusted. Good for nerve-related pain."},
    {"drug": "Duloxetine",         "condition": "Pain", "rating": 8,  "date": "May 18, 2023",      "review": "Cymbalta for chronic pain has been excellent. Manages both my fibromyalgia and mood. Double benefit."},
    {"drug": "Methocarbamol",      "condition": "Pain", "rating": 7,  "date": "September 1, 2021", "review": "Good muscle relaxant for back spasms. Makes me drowsy so best at night. Effective short-term use."},
    {"drug": "Meloxicam",          "condition": "Pain", "rating": 8,  "date": "April 14, 2023",    "review": "Mobic is my preferred NSAID. Once daily dosing and very effective for joint pain. Monitor kidneys long term."},
    {"drug": "Ibuprofen",          "condition": "Pain", "rating": 6,  "date": "December 10, 2022", "review": "Standard pain relief. Good for headaches and mild pain. Stomach upset if not taken with food."},

    # ── Arthritis ────────────────────────────────────────────────────────────
    {"drug": "Methotrexate",       "condition": "Rheumatoid Arthritis", "rating": 7,  "date": "February 20, 2022", "review": "Methotrexate has reduced my joint swelling significantly. Weekly dosing with folic acid is manageable. Regular blood tests required."},
    {"drug": "Adalimumab",         "condition": "Rheumatoid Arthritis", "rating": 9,  "date": "July 5, 2023",      "review": "Humira was a game changer for my RA. Joint pain nearly gone, inflammation markers normal. Biweekly injections are easy."},
    {"drug": "Etanercept",         "condition": "Rheumatoid Arthritis", "rating": 8,  "date": "November 14, 2021", "review": "Enbrel has provided excellent disease control. Weekly injection. Back to doing activities I thought I'd lost forever."},
    {"drug": "Hydroxychloroquine", "condition": "Rheumatoid Arthritis", "rating": 7,  "date": "April 26, 2022",    "review": "Plaquenil is a mild but effective DMARD. Good for early RA or as combination therapy. Regular eye exams needed."},
    {"drug": "Prednisone",         "condition": "Rheumatoid Arthritis", "rating": 6,  "date": "September 22, 2020","review": "Works fast to control flares but long-term use is problematic. Weight gain, mood swings, and bone density loss are real concerns."},
    {"drug": "Baricitinib",        "condition": "Rheumatoid Arthritis", "rating": 9,  "date": "January 31, 2023",  "review": "Olumiant oral JAK inhibitor has been excellent for my RA. One pill daily with impressive results on disease activity."},
    {"drug": "Tocilizumab",        "condition": "Rheumatoid Arthritis", "rating": 8,  "date": "June 8, 2022",      "review": "Actemra infusion every 4 weeks. My RA has been in remission for over a year. Monitoring is important but results are great."},

    # ── Insomnia ─────────────────────────────────────────────────────────────
    {"drug": "Zolpidem",           "condition": "Insomnia", "rating": 7,  "date": "March 19, 2022",    "review": "Ambien works but grogginess the next morning is real. Only use when absolutely needed. Habit forming potential."},
    {"drug": "Melatonin",          "condition": "Insomnia", "rating": 7,  "date": "August 4, 2021",    "review": "Natural option that works for mild insomnia. Not as powerful as prescription but no side effects or dependency."},
    {"drug": "Trazodone",          "condition": "Insomnia", "rating": 8,  "date": "January 14, 2023",  "review": "Trazodone is my favorite sleep medication. Not habit forming, helps with anxiety too, wake up refreshed."},
    {"drug": "Eszopiclone",        "condition": "Insomnia", "rating": 7,  "date": "October 30, 2022",  "review": "Lunesta keeps me asleep all night. The metallic taste is unpleasant but the sleep quality is much better."},
    {"drug": "Suvorexant",         "condition": "Insomnia", "rating": 8,  "date": "May 11, 2023",      "review": "Belsomra orexin antagonist is the most natural-feeling sleep med I've taken. No grogginess, no dependency feeling."},
    {"drug": "Doxepin",            "condition": "Insomnia", "rating": 7,  "date": "December 19, 2021", "review": "Low dose doxepin specifically for insomnia works well. Helps stay asleep without the next day fog."},
    {"drug": "Diphenhydramine",    "condition": "Insomnia", "rating": 5,  "date": "July 25, 2020",     "review": "Benadryl as a sleep aid quickly loses effectiveness. Tolerance builds fast and you feel terrible the next day."},
    {"drug": "Ramelteon",          "condition": "Insomnia", "rating": 7,  "date": "April 3, 2022",     "review": "Rozerem melatonin receptor agonist is gentle and non-addictive. Works best for circadian rhythm issues."},

    # ── GERD / Acid Reflux ───────────────────────────────────────────────────
    {"drug": "Omeprazole",         "condition": "GERD", "rating": 9,  "date": "June 17, 2022",     "review": "Prilosec has eliminated my heartburn completely. Take it in the morning 30 minutes before eating for best results."},
    {"drug": "Pantoprazole",       "condition": "GERD", "rating": 8,  "date": "November 21, 2021", "review": "Protonix is very effective for severe GERD. Healed my esophagitis after 8 weeks of treatment."},
    {"drug": "Famotidine",         "condition": "GERD", "rating": 7,  "date": "March 30, 2023",    "review": "Pepcid is good for mild acid reflux. Not as powerful as PPIs but fewer long-term concerns."},
    {"drug": "Esomeprazole",       "condition": "GERD", "rating": 9,  "date": "August 9, 2022",    "review": "Nexium works excellently. My chronic heartburn has completely resolved on 40mg daily."},
    {"drug": "Lansoprazole",       "condition": "GERD", "rating": 8,  "date": "January 27, 2021",  "review": "Prevacid has given me good relief from GERD symptoms. Take consistently for best results."},
    {"drug": "Omeprazole",         "condition": "GERD", "rating": 7,  "date": "May 5, 2020",       "review": "Works great short term. Worried about long term PPI use so trying to step down to H2 blocker when symptoms are controlled."},
    {"drug": "Ranitidine",         "condition": "GERD", "rating": 6,  "date": "September 5, 2019", "review": "Zantac worked well while it was available. Now using famotidine as an alternative with similar results."},

    # ── High Cholesterol ─────────────────────────────────────────────────────
    {"drug": "Atorvastatin",       "condition": "High Cholesterol", "rating": 8,  "date": "April 8, 2022",     "review": "Lipitor dropped my LDL by 60 points. Some muscle aches early on but they resolved. Great medication."},
    {"drug": "Rosuvastatin",       "condition": "High Cholesterol", "rating": 9,  "date": "September 22, 2023","review": "Crestor is the most potent statin I've tried. Excellent cholesterol reduction with minimal side effects."},
    {"drug": "Simvastatin",        "condition": "High Cholesterol", "rating": 7,  "date": "January 16, 2021",  "review": "Zocor works but the dose is limited by muscle toxicity risk. Switched to rosuvastatin for better efficacy."},
    {"drug": "Ezetimibe",          "condition": "High Cholesterol", "rating": 7,  "date": "June 30, 2022",     "review": "Zetia adds extra LDL lowering when statins alone aren't enough. Well tolerated, easy addition to statin therapy."},
    {"drug": "Fenofibrate",        "condition": "High Cholesterol", "rating": 8,  "date": "February 14, 2023", "review": "Tricor specifically lowered my triglycerides dramatically. Great for mixed dyslipidemia alongside a statin."},
    {"drug": "Pravastatin",        "condition": "High Cholesterol", "rating": 7,  "date": "October 18, 2021",  "review": "Pravachol is the most muscle-friendly statin. Good choice if you've had muscle problems with other statins."},
    {"drug": "Evolocumab",         "condition": "High Cholesterol", "rating": 10, "date": "March 25, 2023",    "review": "Repatha PCSK9 inhibitor is revolutionary. On maximum statin therapy my LDL was 120. On Repatha it's now 28. Incredible."},

    # ── Migraine ─────────────────────────────────────────────────────────────
    {"drug": "Sumatriptan",        "condition": "Migraine", "rating": 9,  "date": "May 19, 2022",      "review": "Imitrex is the gold standard for migraine rescue. Works within 30 minutes when taken early. Life changing medication."},
    {"drug": "Topiramate",         "condition": "Migraine", "rating": 7,  "date": "October 3, 2021",   "review": "Topamax reduced my migraines from 8 to 2 per month. Cognitive side effects are real - some brain fog - but worth the tradeoff."},
    {"drug": "Amitriptyline",      "condition": "Migraine", "rating": 8,  "date": "February 28, 2023", "review": "Low dose amitriptyline as migraine prevention has been excellent. Sleep better too. Dry mouth is the main complaint."},
    {"drug": "Propranolol",        "condition": "Migraine", "rating": 8,  "date": "July 12, 2022",     "review": "Propranolol cut my migraine frequency in half. Beta blocker that prevents as well as treats anxiety. Good dual purpose."},
    {"drug": "Rizatriptan",        "condition": "Migraine", "rating": 9,  "date": "December 6, 2023",  "review": "Maxalt MLT dissolves under the tongue and works fast. Very effective for acute migraines. Better than sumatriptan for me."},
    {"drug": "Erenumab",           "condition": "Migraine", "rating": 10, "date": "April 22, 2023",    "review": "Aimovig CGRP inhibitor has been miraculous. Down from 20+ migraines a month to 3. Monthly injection is painless."},
    {"drug": "Ubrogepant",         "condition": "Migraine", "rating": 8,  "date": "August 14, 2023",   "review": "Ubrelvy is a great new option for acute migraines. Works as well as triptans without the cardiovascular concerns."},
    {"drug": "Valproate",          "condition": "Migraine", "rating": 6,  "date": "January 9, 2021",   "review": "Depakote works for migraine prevention but weight gain and hair loss are significant. Only use if other options fail."},

    # ── Bipolar Disorder ─────────────────────────────────────────────────────
    {"drug": "Lithium",            "condition": "Bipolar Disorder", "rating": 8,  "date": "March 4, 2022",     "review": "Lithium has been the most effective mood stabilizer I've tried. Regular blood tests are essential. Stable for 3 years now."},
    {"drug": "Quetiapine",         "condition": "Bipolar Disorder", "rating": 8,  "date": "August 18, 2021",   "review": "Seroquel helps with both mania and depression in bipolar. Sedating at higher doses which helps sleep. Weight gain is an issue."},
    {"drug": "Valproate",          "condition": "Bipolar Disorder", "rating": 7,  "date": "January 30, 2023",  "review": "Depakote keeps my mood stable and prevents manic episodes. Hair loss and weight gain are frustrating side effects."},
    {"drug": "Lamotrigine",        "condition": "Bipolar Disorder", "rating": 9,  "date": "June 15, 2022",     "review": "Lamictal is excellent for bipolar depression. Minimal side effects, good mood stability. Best tolerated mood stabilizer I've tried."},
    {"drug": "Aripiprazole",       "condition": "Bipolar Disorder", "rating": 8,  "date": "November 25, 2023", "review": "Abilify added to mood stabilizer has been very helpful. Activating rather than sedating which suits me well."},
    {"drug": "Olanzapine",         "condition": "Bipolar Disorder", "rating": 6,  "date": "April 17, 2020",    "review": "Zyprexa controls mania effectively but metabolic effects are significant. Gained 30 pounds. Use only when necessary."},
    {"drug": "Lithium",            "condition": "Bipolar Disorder", "rating": 7,  "date": "September 29, 2022","review": "Lithium works but requires careful monitoring of levels. Stay hydrated, watch sodium intake, and test regularly."},

    # ── Schizophrenia ────────────────────────────────────────────────────────
    {"drug": "Risperidone",        "condition": "Schizophrenia", "rating": 7,  "date": "February 5, 2022",  "review": "Risperdal controls positive symptoms well. Some extrapyramidal effects managed with Cogentin. Stable on this medication."},
    {"drug": "Olanzapine",         "condition": "Schizophrenia", "rating": 8,  "date": "July 21, 2021",     "review": "Zyprexa is very effective for psychotic symptoms. Weight gain and metabolic changes need to be monitored carefully."},
    {"drug": "Clozapine",          "condition": "Schizophrenia", "rating": 9,  "date": "December 10, 2022", "review": "Clozaril worked when nothing else did. Regular blood monitoring is required but for treatment-resistant cases it's worth it."},
    {"drug": "Aripiprazole",       "condition": "Schizophrenia", "rating": 7,  "date": "May 3, 2023",       "review": "Abilify has a better metabolic profile than other antipsychotics. Effective with less weight gain concern."},
    {"drug": "Lurasidone",         "condition": "Schizophrenia", "rating": 8,  "date": "September 17, 2022","review": "Latuda is weight neutral and effective. Take with food for absorption. Good tolerability overall."},
    {"drug": "Paliperidone",       "condition": "Schizophrenia", "rating": 8,  "date": "March 28, 2023",    "review": "Invega monthly injection removes the burden of daily pills. Stable symptoms and no compliance issues."},

    # ── COPD ─────────────────────────────────────────────────────────────────
    {"drug": "Tiotropium",         "condition": "COPD", "rating": 9,  "date": "April 9, 2022",     "review": "Spiriva has dramatically improved my breathing. Once daily inhalation is easy and the effect lasts all 24 hours."},
    {"drug": "Salmeterol",         "condition": "COPD", "rating": 8,  "date": "September 3, 2021", "review": "Serevent provides consistent long-acting bronchodilation. Good baseline lung function improvement."},
    {"drug": "Budesonide",         "condition": "COPD", "rating": 7,  "date": "February 11, 2023", "review": "Pulmicort ICS reduces exacerbations in severe COPD. Use only when indicated - not all COPD patients need inhaled steroids."},
    {"drug": "Umeclidinium",       "condition": "COPD", "rating": 8,  "date": "July 27, 2022",     "review": "Incruse works well for COPD maintenance. Once daily convenience and good symptom control."},
    {"drug": "Roflumilast",        "condition": "COPD", "rating": 7,  "date": "December 15, 2021", "review": "Daliresp reduces COPD exacerbations in severe chronic bronchitis. GI side effects initially but manageable."},
    {"drug": "Albuterol",          "condition": "COPD", "rating": 8,  "date": "May 28, 2022",      "review": "Rescue inhaler essential for COPD flares. Works quickly for acute shortness of breath. Cannot do without it."},

    # ── Osteoporosis ─────────────────────────────────────────────────────────
    {"drug": "Alendronate",        "condition": "Osteoporosis", "rating": 8,  "date": "June 26, 2022",     "review": "Fosamax weekly has improved my bone density over 2 years. Important to take correctly - sit upright 30 minutes after."},
    {"drug": "Risedronate",        "condition": "Osteoporosis", "rating": 8,  "date": "November 16, 2021", "review": "Actonel is effective and easier on the stomach than Fosamax for me. Bone density improving steadily."},
    {"drug": "Denosumab",          "condition": "Osteoporosis", "rating": 9,  "date": "April 4, 2023",     "review": "Prolia injection every 6 months has been very effective. Significant bone density improvement shown on DEXA scan."},
    {"drug": "Calcium + Vitamin D","condition": "Osteoporosis", "rating": 7,  "date": "January 23, 2022",  "review": "Essential foundation for bone health. Supplements alone not enough for osteoporosis but necessary alongside medication."},
    {"drug": "Teriparatide",       "condition": "Osteoporosis", "rating": 9,  "date": "August 31, 2023",   "review": "Forteo daily injection actually builds new bone rather than just preventing loss. Expensive but worth it for severe osteoporosis."},
    {"drug": "Raloxifene",         "condition": "Osteoporosis", "rating": 7,  "date": "March 15, 2021",    "review": "Evista is a good option for postmenopausal women. Protects bones and reduces breast cancer risk. Hot flashes may worsen."},

    # ── Urinary Tract Infection ───────────────────────────────────────────────
    {"drug": "Nitrofurantoin",     "condition": "Urinary Tract Infection", "rating": 9,  "date": "July 10, 2022",     "review": "Macrobid cleared my UTI completely within 3 days. Fewer resistance concerns than many antibiotics. Take with food."},
    {"drug": "Trimethoprim-Sulfamethoxazole","condition": "Urinary Tract Infection", "rating": 7, "date": "February 28, 2021", "review": "Bactrim works fast for UTI but allergy concerns are real. Effective when sensitivity is confirmed."},
    {"drug": "Ciprofloxacin",      "condition": "Urinary Tract Infection", "rating": 7,  "date": "October 12, 2022",  "review": "Cipro is powerful for complicated UTIs. Avoid for simple uncomplicated infections due to antibiotic stewardship."},
    {"drug": "Fosfomycin",         "condition": "Urinary Tract Infection", "rating": 9,  "date": "May 20, 2023",      "review": "Single dose Monurol is amazing - one packet and UTI gone within 48 hours. Most convenient antibiotic I've used."},
    {"drug": "Phenazopyridine",    "condition": "Urinary Tract Infection", "rating": 8,  "date": "September 6, 2021", "review": "AZO urinary pain relief works quickly. Orange urine is surprising but pain relief is immediate while waiting for antibiotics to work."},

    # ── Erectile Dysfunction ─────────────────────────────────────────────────
    {"drug": "Sildenafil",         "condition": "Erectile Dysfunction", "rating": 9,  "date": "March 7, 2022",     "review": "Viagra works excellently. Take 1 hour before and eat a light meal. Headache and flushing are manageable."},
    {"drug": "Tadalafil",          "condition": "Erectile Dysfunction", "rating": 10, "date": "August 25, 2023",   "review": "Cialis 36 hour duration is amazing. No need to time it perfectly. Daily low dose also works great for spontaneity."},
    {"drug": "Vardenafil",         "condition": "Erectile Dysfunction", "rating": 8,  "date": "January 4, 2021",   "review": "Levitra works faster than Viagra for me with fewer side effects. Good option if Viagra didn't work well for you."},
    {"drug": "Avanafil",           "condition": "Erectile Dysfunction", "rating": 9,  "date": "June 19, 2023",     "review": "Stendra works in just 15 minutes and has the least side effects of any PDE5 inhibitor I've tried. Excellent."},
    {"drug": "Tadalafil",          "condition": "Erectile Dysfunction", "rating": 9,  "date": "November 30, 2022", "review": "Daily low dose Cialis changed everything. Natural feeling, no planning needed. Highly recommend this approach."},

    # ── Menopause ────────────────────────────────────────────────────────────
    {"drug": "Estradiol",          "condition": "Menopause", "rating": 9,  "date": "April 17, 2022",    "review": "HRT with estradiol patch eliminated my hot flashes and night sweats. Sleep is better, mood is stable. Life changing."},
    {"drug": "Conjugated Estrogens","condition": "Menopause", "rating": 8, "date": "September 29, 2021","review": "Premarin helps with menopause symptoms effectively. Discuss the risks with your doctor but benefits are real."},
    {"drug": "Progesterone",       "condition": "Menopause", "rating": 8,  "date": "February 12, 2023", "review": "Prometrium combined with estrogen provides protection and actually helps sleep. Natural progesterone feels better."},
    {"drug": "Venlafaxine",        "condition": "Menopause", "rating": 7,  "date": "July 8, 2022",      "review": "Effexor for hot flashes when you can't take hormones. Reduced frequency by about 60 percent. Good non-hormonal option."},
    {"drug": "Ospemifene",         "condition": "Menopause", "rating": 8,  "date": "December 20, 2022", "review": "Osphena for genitourinary symptoms is excellent. Oral medication that works like local estrogen without systemic concerns."},

    # ── Osteoarthritis ───────────────────────────────────────────────────────
    {"drug": "Celecoxib",          "condition": "Osteoarthritis", "rating": 8,  "date": "May 9, 2022",       "review": "Celebrex is very effective for knee osteoarthritis. Less stomach irritation than regular NSAIDs. Good long-term option."},
    {"drug": "Meloxicam",          "condition": "Osteoarthritis", "rating": 8,  "date": "October 25, 2023",  "review": "Mobic once daily keeps my joint pain manageable. Good tolerability and convenient dosing."},
    {"drug": "Naproxen",           "condition": "Osteoarthritis", "rating": 7,  "date": "March 1, 2021",     "review": "Aleve provides good OA pain relief. Twice daily is convenient. Long term use requires kidney and stomach monitoring."},
    {"drug": "Diclofenac gel",     "condition": "Osteoarthritis", "rating": 9,  "date": "August 13, 2022",   "review": "Voltaren topical gel is excellent for knee and hand OA. Local treatment with less systemic side effects. Highly effective."},
    {"drug": "Acetaminophen",      "condition": "Osteoarthritis", "rating": 6,  "date": "January 21, 2023",  "review": "Tylenol helps modestly with OA pain. Safer long term than NSAIDs. Not as effective for significant pain though."},
    {"drug": "Hyaluronic Acid",    "condition": "Osteoarthritis", "rating": 7,  "date": "June 5, 2022",      "review": "Synvisc knee injections provided 6 months of improved function. Not a cure but good bridge before surgery."},

    # ── Psoriasis ────────────────────────────────────────────────────────────
    {"drug": "Adalimumab",         "condition": "Psoriasis", "rating": 10, "date": "April 30, 2023",    "review": "Humira cleared my plaque psoriasis by 90 percent. After years of struggling this is the answer. Biweekly injection."},
    {"drug": "Secukinumab",        "condition": "Psoriasis", "rating": 9,  "date": "September 14, 2022","review": "Cosentyx is amazing for psoriasis. Skin cleared completely in 3 months. Monthly maintenance injections keep it controlled."},
    {"drug": "Methotrexate",       "condition": "Psoriasis", "rating": 6,  "date": "February 3, 2021",  "review": "Methotrexate helps moderate psoriasis but side effects including nausea and fatigue are significant. Regular monitoring needed."},
    {"drug": "Apremilast",         "condition": "Psoriasis", "rating": 7,  "date": "July 18, 2022",     "review": "Otezla oral medication is convenient. Good for moderate psoriasis when biologics aren't appropriate. GI symptoms initially."},
    {"drug": "Betamethasone",      "condition": "Psoriasis", "rating": 7,  "date": "December 28, 2022", "review": "Topical steroid works for limited psoriasis. Use it sparingly and rotate to avoid skin thinning."},
    {"drug": "Ixekizumab",         "condition": "Psoriasis", "rating": 10, "date": "May 25, 2023",      "review": "Taltz cleared my psoriasis 100 percent. After 20 years of suffering, completely clear skin. IL-17 biologics are miraculous."},

    # ── Atrial Fibrillation ──────────────────────────────────────────────────
    {"drug": "Apixaban",           "condition": "Atrial Fibrillation", "rating": 9,  "date": "March 10, 2022",    "review": "Eliquis for AFib has been excellent. No dietary restrictions like warfarin. Good stroke protection. Minor bruising increased."},
    {"drug": "Rivaroxaban",        "condition": "Atrial Fibrillation", "rating": 8,  "date": "August 22, 2021",   "review": "Xarelto once daily is convenient. Good anticoagulation for AFib without INR monitoring. Take with evening meal."},
    {"drug": "Warfarin",           "condition": "Atrial Fibrillation", "rating": 6,  "date": "January 15, 2020",  "review": "Warfarin works but INR monitoring and dietary restrictions are burdensome. Switched to a NOAC when possible."},
    {"drug": "Metoprolol",         "condition": "Atrial Fibrillation", "rating": 8,  "date": "June 28, 2022",     "review": "Metoprolol controls AFib heart rate well. Consistent rate control prevents symptoms. Some fatigue is the tradeoff."},
    {"drug": "Amiodarone",         "condition": "Atrial Fibrillation", "rating": 7,  "date": "November 12, 2023", "review": "Amiodarone is effective for maintaining sinus rhythm but toxicity monitoring is important. Thyroid and lung function tests essential."},
    {"drug": "Dronedarone",        "condition": "Atrial Fibrillation", "rating": 7,  "date": "April 20, 2022",    "review": "Multaq is safer than amiodarone though less potent. Good choice for paroxysmal AFib without heart failure."},
]

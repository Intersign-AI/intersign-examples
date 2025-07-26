# ASL Prosody Data Requirements: Detailed Specifications

To effectively test and validate the prosody extraction and translation modules, two complementary datasets are described below. As our focus has shifted more toward sentence-level prosody, the **phrase-based dataset is prioritized** as the primary requirement. The atomic gesture dataset remains an **optional** and future-facing component for gesture-level experimentation.

---

## **E.1 - Phrase-Based Dataset (Primary)**

### **Overview**

This dataset explores sentence-level prosody variation and translation, structured similarly to the [**EmoSign**](https://huggingface.co/datasets/catfang/emosign) dataset. Please refer to this [arXiv paper](https://arxiv.org/pdf/2505.17090) for more details.

### **Core Requirements**

- Target of **200 ASL video phrases**
  - **100 phrases** can serve as a **minimum** baseline if budget or resources are limited
- Each sentence should include:
  - A **non-prosody version** (neutral emotion, neutral facial cues, normal speed, sentiment = 0)
  - Multiple **prosodic variations** of the same sentence (different emotions, different delivery)

### **How many samples per sentence?**
- This is **flexible**
- Example: For the sentence *"Why is the teacher upset?"*, there could be:
  - One version where the teacher is **angry**
  - Another where the teacher is **sad**
- These differences are crucial to capture the **expressiveness and adjective-level prosody** in the English translation of ASL phrases
- **Example structure**: If each sentence has 5 samples, we would need approximately 40 unique sentences

---

### **Annotations Required**

#### **Emotion & Sentiment Labels**

- **Emotion categories** (7 total):
  - happy, sad, fear, disgust, surprise, anger, **neutral**
- Each emotion must be rated on a **0–3 scale**:
  - `0` – not present
  - `3` – strongly present throughout the sentence
- **Overall sentiment label**:
  - Integer scale from **-3 to +3**
    - `+3`: strongly positive
    - `0`: neutral
    - `-3`: strongly negative

#### **Prosodic Features**

- **Speed**: slow, normal, fast

> ℹ️ **Note**: We are no longer requiring a separate *intensity* label, as emotional intensity is already captured through emotion scores and sentiment.

#### **Translation & Reference**

- Accurate **ASL-to-English** phrase translation
- **Sign label** array
- **Optional** *Sign count

#### **Reasoning Annotations**

- Three **brief observational phrases** (2–3 words) describing visible expressive behaviors (e.g. "furrowed brows", "open mouth", etc.)

---

### **Sample Data Table Structure**

| Field                   | Description                                | Example Values                      |
|-------------------------|--------------------------------------------|-------------------------------------|
| `video_id`              | Unique identifier                          | Cory_2013-6-27_sc107                |
| `English_translation`   | English equivalent                         | "Why is the teacher upset?"         |
| `sign_count`            | Number of signs                            | 5                                   |
| `sign_labels_array`     | Optional sign sequence                     | ['TEACH+AGENT', 'UPSET', 'WHY++']   |
| `Sentiment`             | Overall sentiment (-3 to +3)               | -2                                  |
| `Emotion scores`        | Per-emotion scores (0–3)                   | happy: 0, anger: 3, sadness: 2       |
| `Speed`                 | Speech speed                               | normal                              |
| `Reasoning`             | 3 short explanations                       | furrowed brows, rhetorical tone, scrunched face |

---

### **Sample Annotation Table**

| video_id               | English_translation         | sign_count | sign_labels_array                                               | Sentiment | happy | sad | fear | disgust | surprise | anger | neutral | Speed  | Reasoning_1                            | Reasoning_2                  | Reasoning_3                       |
|------------------------|-----------------------------|------------|------------------------------------------------------------------|-----------|--------|-----|------|---------|----------|--------|---------|--------|----------------------------------------|-----------------------------|----------------------------------|
| Cory_2013-6-27_sc107   | Why is the teacher upset?   | 5          | ['TEACH+AGENT', 'UPSET', 'WHY++', '(1h)part']                     | -2        | 0      | 2   | 0    | 1       | 1        | 3      | 0       | normal | furrowed brows with 'upset' emphasis | rhetorical tone at end     | scrunched face                   |
| Cory_2013-6-27_sc108   | Boston is a great city.     | 4          | ['ns-BOSTON', 'WOW+', 'WONDERFUL', 'CITY']                        | 3         | 3      | 0   | 0    | 0       | 2        | 0      | 0       | normal | widened eyes, emphasis on 'wow'      | eye wide on "wow"          | hand spread                      |
| Cory_2013-6-27_sc109   | I love my new car.          | 7          | ['POSS-1p+', 'NEW+', '#CAR', 'IX-1p', 'KISS-FIST', 'IX-1p']       | 3         | 3      | 0   | 0    | 0       | 2        | 0      | 0       | normal | pause before kiss-fist               | open mouth expression       | lips pout                        |




### **Recommended Dataset Creation Workflow**

1. **Base Model Training**: First, collect 80 samples for each individual gesture/sign that will be used across all phrases to train a foundational detection model
2. **Neutral Sentence Creation**: Create sentences using the base gestures WITHOUT prosody features (neutral facial expressions, normal speed, sentiment = 0)
3. **Prosodic Enhancement**: Create prosodic-rich variations of the same sentences by adding emotional expressions, varying speed, and intensity while keeping the core manual gestures identical

#### **Gesture/Sign Sourcing for Phrases**

- Each phrase/sentence will contain multiple gestures/signs
- **Gesture sources**: Signs used in phrases should come from either:
    1. Gestures from **already existing datasets**,  AND/OR
    2. [optional] The **20 distinct gestures** provided in the Atomic Gesture Dataset (E.1)
- **Critical requirement**: For each individual sign/gesture used across all phrases, we need **80 samples minimum**
- **Purpose**: These samples will train a base detection model for gesture recognition (accuracy optimization is not the focus, just foundational detection capability)



> ### **Annotation Responsibility Notes:**
>
> The **signer who is recording the video** should be the one to annotate the **Speed** value. Since baseline signing speed can vary from person to person, it’s most accurate if the signer self-identifies whether a sentence was delivered at a *slow*, *normal*, or *fast* pace relative to their natural style.
>
> Additionally, the **person assigning emotion scores and overall sentiment** should also be the one writing the **Reasoning\_1, Reasoning\_2, and Reasoning\_3** fields. These short textual notes explain *why* a particular emotion is marked as present or absent, and why the overall sentence feels positive, negative, or neutral. This ensures consistency between the quantitative annotations and their qualitative justification.
> 

> Furthermore, if a sentence has **multiple variations** (e.g. five samples with different emotions or prosodic features), **all those variations should be recorded by the same signer**. For example, if a sentence like *"Why is the teacher upset?"* is performed in five different ways, all five should be performed by a **single signer**. It should not be split between different signers (e.g., three samples by one signer, two by another).
>
> If multiple signers are to perform the same sentence, then **each signer must complete the full set of variations independently**. In this case, there would be two complete sets of the same sentence, one set per signer, each containing all intended variations.
>
> This consistency is important because prosodic features like emotion, sentiment, and expression style can vary significantly between individuals. Keeping all variations of a sentence within a single signer ensures that the **variation is due to intentional prosodic change** rather than individual signing habits or facial tendencies. It allows for cleaner, more controlled analysis and model training.




--
---


## **E.2 - Atomic Gesture Dataset (Optional)**
> **Note:** The Atomic Gesture Dataset is considered **optional** for this phase. While both datasets explore prosodic variation, they are not fully correlated:
> 
> - Mouth movements in atomic gestures may change the *gesture’s meaning* rather than express prosody.
> - Thus, this dataset is more relevant for gesture classification than pure prosody extraction.
> - It is useful for building more nuanced base models but is not essential for achieving our current prosody modeling goals.


**

### **Overview**

This dataset is designed to evaluate how **facial and mouth morphemes** affect the interpretation of otherwise similar hand gestures. These distinctions are useful for analyzing gesture disambiguation, particularly in non-verbal prosodic expressions.

### **Core Requirements**

- **20 distinct gestures**, each with a **minimum of 80 video samples**
- Gestures should specifically capture variations based on facial expressions and mouth morphemes
- Please refer to the **"[ASL: Mouth Morphemes Change Sign Definitions](https://www.youtube.com/watch?v=KiF86lzBtoc)"** video for reference
- The following set of examples provides a good starting point for dataset creation:
    - **Set 1** - sick, hilarious, disappointed, funny stop that, LOL
    - **Set 2** - finish, hands off, mind boggling, that's all
    - **Set 3** - awful, impossible, believe it or not
    - **Set 4** - wrong, accidentally, unexpectedly, what matters
    - **Set 5** - good, see you later, best

### **Technical Specifications**

- **Video Quality**: High-quality frontal videos (≥ 30fps), consistent lighting, and diverse signers
- **Signer Diversity**: Videos can come from a single signer or multiple signers (e.g., 20 samples × 4 signers). Greater signer diversity is preferred but not required
- **Same baseline quality** as previously recorded gestures

### **Required Annotations**

- **Gesture label**
- **Associated facial expression/mouth morpheme**
- **Signer identity metadata** (optional)

### **Prosody Parameter Definitions**

This is in regards to the Associated facial expression/mouth morpheme.
We require verification from ASL expert (Adrian) whether the following parameter/value definitions are valid and sufficient to differentiate gestures, specifically for the 5 sets of gestures earlier mentioned:

|Parameter|Possible Values|
|---|---|
|**Cheeks**|puff right, puffed, tensed, tensed left, tensed right|
|**Eye Aperture**|blink, closed, further lowered, further squinted, lowered lid, slightly lowered, slightly squinted, slightly wide, squint, wide, wider|
|**Eyebrows**|further lowered, further raised, left raised/right furrowed, lowered, raised, raised-furrowed, right raised/left furrowed, slightly lowered, slightly raised|
|**Eye Gaze**|down, down/left, down/right, into space, left, other, to addressee, up, up/left, up/right, watch hands|
|**Mouth**|bite lower lip, blow, brr, cs, intense, left tense, lips pursed corners down, lips pursed: mm, lips pursed: oo, lips pursed: oo-tight, lips spread, lips spread & corners down, lips spread & corners up, open, open & corners down, open & round, open & tense, open & tongue visible, pow, raised upper lip, right tense, sh, smile mouth open, tongue on lower lip, tongue out, tongue sucked in quickly|
|**Nose**|slightly tensed, slightly wrinkle, slightly wrinkled, tensed, wrinkle|



---

## **Preferred Data Formats**

- **Video**: `.mp4` format, 30fps or higher
- **Annotations**: `.csv` format for all labels and metadata
- **Documentation** (optional): Include parameter explanations, annotation schemas, and metadata descriptions

---


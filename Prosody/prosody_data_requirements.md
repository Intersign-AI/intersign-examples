

# ASL Prosody Data Requirements: Detailed Specifications

To effectively test and validate the initial prosody extraction and translation modules, two complementary datasets are required for this phase. The videos should be carefully selected and annotated by ASL experts to ensure each video features meaningful ASL expressions incorporating distinct prosody elements.

---

## **E.1 - Atomic Gesture Dataset**

### **Overview**

This dataset is designed to evaluate how different mouth morphemes and facial expressions affect the interpretation of similar manual gestures. These distinctions will guide the tuning of our prosody detection system to determine whether gestures can be differentiated solely based on prosodic cues.

### **Core Requirements**

- **20 distinct gestures**, each with a **minimum of 80 video samples**
- Gestures should specifically capture variations based on facial expressions and mouth morphemes
- Please refer to the **"[ASL: Mouth Morphemes Change Sign Definitions](https://www.youtube.com/watch?v=KiF86lzBtoc)"** video for reference
- The following set of examples provides a good starting point for dataset creation:
    - **Set 1** - sick, hilarious, disappointed, funny, stop that, LOL
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

<div style="page-break-after: always;"></div>

## **E.2 - Phrase-based Dataset**

### **Overview**

This dataset explores sentence-level prosody variation and translation, structured similarly to the [**EmoSign**](https://huggingface.co/datasets/catfang/emosign) dataset. Please refer to this [arXiv paper](https://arxiv.org/pdf/2505.17090) for more details.

### **Core Requirements**

- We had earlier mentioned approximately 200 ASL video phrases but 100 ASL video phrases would suffice to limit the scope.
- Each sentence should include:
    - A **non-prosody version** (neutral facial cues, normal speed, sentiment = 0)
    - Multiple **prosodic variations** of the same sentence (different emotion, speed, intensity)
- **Example structure**: If each sentence has 5 samples, we would need approximately 20 unique sentences

### **Dataset Creation Workflow**

1. **Base Model Training**: First, collect 80 samples for each individual gesture/sign that will be used across all phrases to train a foundational detection model
2. **Neutral Sentence Creation**: Create sentences using the base gestures WITHOUT prosody features (neutral facial expressions, normal speed, sentiment = 0)
3. **Prosodic Enhancement**: Create prosodic-rich variations of the same sentences by adding emotional expressions, varying speed, and intensity while keeping the core manual gestures identical

### **Gesture/Sign Sourcing for Phrases**

- Each phrase/sentence will contain multiple gestures/signs
- **Gesture sources**: Signs used in phrases should come from either:
    1. The **20 distinct gestures** provided in the Atomic Gesture Dataset (E.1), AND/OR
    2. Gestures from **already existing datasets**
- **Critical requirement**: For each individual sign/gesture used across all phrases, we need **80 samples minimum**
- **Purpose**: These samples will train a base detection model for gesture recognition (accuracy optimization is not the focus, just foundational detection capability)

### **Detailed Annotations Required**

#### **Emotion & Sentiment Labels**

- **Complete emotion set**: happy, excited, surprise, worry, sadness, fear, disgust, frustration, anger, plus neutral
- **Overall sentiment label**: Integer scale from **-3 to +3**
    - (+3: strongly positive, -3: strongly negative, 0: neutral)
- **Short reasoning annotations** (2-3 words each): Brief observations explaining the sentiment or emotion

#### **Prosodic Features**

- **Speed categories**: slow, normal, fast
- **Intensity categories**: low, medium, high

#### **Translation & Reference**

- **Accurate ASL-to-English phrase translations**
- **Sign count** (optional, for reference and alignment)

<div style="page-break-after: always;"></div>

### **Sample Data Structure**

| Field                   | Description                                | Example Values                      |
| ----------------------- | ------------------------------------------ | ----------------------------------- |
| **video_id**            | Unique identifier                          | Cory_2013-6-27_sc107                |
| **English_translation** | Accurate English equivalent                | "Why is the teacher upset?"         |
| **sign_count**          | Number of signs in phrase                  | 5                                   |
| **sign_labels_array**   | Optional sign sequence                     | ['TEACH+AGENT', 'UPSET', 'WHY++']   |
| **Sentiment**           | Overall sentiment of the phrase (-3 to +3) | -2                                  |
| **Emotion_scores**      | Individual emotion ratings (1-4 scale)     | joy: 1, worry: 4, anger: 4          |
| **Speed**               | Delivery speed                             | normal, fast, slow                  |
| **Intensity**           | Expression intensity                       | low, medium, high                   |
| **Reasoning**           | 2-3 brief observations                     | "furrowed brows", "rhetorical tone" |

### **Complete Sample Annotation Example**

|video_id|English_translation|sign_count|sign_labels_array|Sentiment|joy|excited|surprise_pos|surprise_neg|worry|sadness|fear|disgust|frustration|anger|Speed|Intensity|Reasoning_1|Reasoning_2|Reasoning_3|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Cory_2013-6-27_sc107|Why is the teacher upset?|5|['TEACH+AGENT', 'UPSET', 'WHY++', '(1h)part']|-2|1|1|1|1|4|1|4|1|4|4|normal|high|furrowed brows with 'upset' emphasis|rhetorical tone at end|bared teeth, scrunched face|
|Cory_2013-6-27_sc108|Boston is a great city.|4|['ns-BOSTON', 'WOW+', 'WONDERFUL', 'CITY']|3|4|4|3|1|1|1|1|1|1|1|normal|medium|widened eyes, emphasis on 'wow'|eye wide on "wow"|exaggerated hand spread|
|Cory_2013-6-27_sc109|I love my new car.|7|['POSS-1p+', 'NEW+', '#CAR', 'IX-1p', 'KISS-FIST']|3|4|4|4|1|1|1|1|1|1|1|normal|high|pause before kiss-fist|open mouth expression|lips pout for excitement|

---

## **Dataset Deliverables**

These datasets will be essential for:

1. **Tuning prosody mappings** between facial expressions and semantic meaning
2. **Validating system performance** end-to-end
3. **Training translation models** to account for prosodic variations
4. **Benchmarking** against existing ASL recognition systems

### **Preferred Data Formats**

- **Video files**: MP4 format, minimum 30fps
- **Annotations**: CSV format for easy integration
- **Documentation**: Detailed annotation guidelines and prosody parameter definitions

---

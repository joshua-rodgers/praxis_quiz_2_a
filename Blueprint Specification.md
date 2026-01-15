# **PRAXIS 5652 Exam Prep: Self-Contained Flask Blueprint Specification**

## **1\. Project Overview**

This document serves as a master specification for an LLM to generate a self-contained Flask Blueprint named praxis\_quiz\_2. The blueprint implements a study platform for the PRAXIS 5652 Computer Science certification.

**Key Architectural Decisions:**

1. **Database Strategy**: **Raw sqlite3** only. No ORM (SQLAlchemy) is permitted. Database interactions are handled via helper functions using Python's built-in sqlite3 module.  
2. **Asset Namespacing**: To prevent conflicts with the parent Flask application, all static assets and templates must be strictly namespaced under praxis\_quiz\_2.  
3. **Modular Quiz Engine**: The quiz delivery logic (rendering, parsing, state) is isolated in a **Sub-Blueprint** named quiz\_delivery.  
4. **Strict Syntax Enforcement**: The system relies on a custom pseudocode language (defined in pseudocode\_def.md). The AI prompts and UI highlighting must strictly adhere to this specific syntax.  
5. **Primary Constraint:** The blueprint must be runnable simply by importing it and calling `app.register_blueprint(praxis_bp)` in the main application. All initialization and configuration must happen within the blueprint itself. [app.py](http://app.py) should be clean and simple.  
6. 

## **2\. Directory Structure**

The implementation must follow this exact structure. Note the sub-blueprint (quiz\_delivery) and namespaced asset folders.

praxis\_blueprint/  
├── \_\_init\_\_.py                 \# Main Blueprint registration, DB connection factory  
├── schema.sql                  \# Raw SQL DDL for table creation  
├── db.py                       \# Raw sqlite3 wrapper (get\_db, query\_db, init\_db)  
├── main\_routes.py              \# Dashboard, Settings, Quiz Builder routes  
├── utils\_ai.py                 \# Gemini SDK interactions (Context Caching, Generation)  
├── praxis\_data/  
│   ├── praxis.db               \# SQLite database file (auto-created)  
│   ├── 5652\_objectives.md      \# Reference file  
│   ├── MCQs.md                 \# Reference file  
│   └── pseudocode\_def.md       \# Reference file  
├── quiz\_delivery/              \# \[SUB-BLUEPRINT\]  
│   ├── \_\_init\_\_.py             \# Sub-blueprint definition & registration  
│   ├── delivery\_routes.py      \# Active quiz routes, AJAX answer handling  
│   └── content\_parser.py       \# JSON Sanitization & Markdown/Code formatter  
├── static/  
│   └── praxis\_quiz\_2/            \# \[NAMESPACED\]  
│       ├── css/  
│       │   └── style.css       \# Tailwind directives & Custom overrides  
│       └── js/  
│           ├── quiz\_engine.js  \# Timer, State management, AJAX  
│           └── syntax\_highlighter.js \# Custom Lexer for Exam Pseudocode  
└── templates/  
    └── praxis\_quiz\_2/            \# \[NAMESPACED\]  
        ├── layout.html         \# Base template (Sharp corners, light theme)  
        ├── dashboard.html      \# User stats & history  
        ├── builder.html        \# Quiz generation configuration  
        ├── quiz/               \# \[Quiz Delivery Specifics\]  
        │   ├── active\_quiz.html  
        │   └── results.html  
        └── components/  
            └── code\_block.html \# Macro for consistent \<pre\> rendering

## **3\. Database Schema (Raw SQLite)**

The database schema is defined in schema.sql. The db.py module manages connections using g (Flask global) to ensure thread safety.

**Tables:**

1. **users**  
   * id (INTEGER PRIMARY KEY AUTOINCREMENT)  
   * username (TEXT UNIQUE NOT NULL)  
   * created\_at (TIMESTAMP DEFAULT CURRENT\_TIMESTAMP)  
2. **questions**  
   * id (INTEGER PRIMARY KEY AUTOINCREMENT)  
   * content\_json (TEXT NOT NULL): A JSON string containing the question stem, code snippet, and options dictionary.  
   * correct\_answer (TEXT NOT NULL): Single character (e.g., "A").  
   * explanation\_md (TEXT): Markdown text explaining the solution.  
   * category (TEXT NOT NULL): Mapped from 5652\_objectives.md.  
   * difficulty (TEXT): "Easy", "Medium", "Hard".  
   * source (TEXT): "original" (seeded) or "ai\_generated".  
3. **quizzes**  
   * id (INTEGER PRIMARY KEY AUTOINCREMENT)  
   * user\_id (INTEGER, Foreign Key to users)  
   * score (INTEGER)  
   * total\_questions (INTEGER)  
   * settings\_json (TEXT): Stores config (e.g., {"timer": true, "categories": \["Algorithms"\]}).  
   * created\_at (TIMESTAMP DEFAULT CURRENT\_TIMESTAMP)  
4. **quiz\_attempts**  
   * id (INTEGER PRIMARY KEY AUTOINCREMENT)  
   * quiz\_id (INTEGER, Foreign Key to quizzes)  
   * question\_id (INTEGER, Foreign Key to questions)  
   * user\_answer (TEXT)  
   * is\_correct (INTEGER): 0 for false, 1 for true.

## **4\. Sub-Blueprint: Quiz Delivery System (quiz\_delivery)**

This module is designed to be pluggable. It handles the raw output from the AI and transforms it into a safe, reliable user interface.

### **A. content\_parser.py (The Formatter)**

This module contains static methods to process data before rendering:

1. **JSON Validation**: Strict schema validation ensures the AI response contains required fields (question\_text, options, correct\_option).  
2. **Markdown Rendering**: Converts explanation text to safe HTML.  
3. **Code Block Extraction**: If the JSON contains a code\_snippet field, this parser wraps it in a specific HTML structure:  
   \<div class="praxis-code-container"\>  
       \<pre class="praxis-code-block" data-language="praxis-pseudo"\>{raw\_code}\</pre\>  
   \</div\>

### **B. syntax\_highlighter.js (The Custom Lexer)**

Standard syntax highlighters do not support the specific tokens used in the Praxis 5652 exam. A custom Javascript tokenizer is required.

* **Target Syntax**: Must strictly parse tokens defined in pseudocode\_def.md.  
* **Token Rules**:  
  * **Operators**: ← (Assignment), ≠ (Not Equal), ≤, ≥.  
  * **Keywords**: procedure, end procedure, if, end if, repeat, until, for, end for, while, end while, return.  
  * **Types**: int, boolean, String, double, void.  
  * **Comments**: Single line //, Multi-line /\* ... \*/.  
  * **Literals**: Strings in "...", Numbers.  
* **Logic**: On page load, scan all .praxis-code-block elements, regex-replace tokens with \<span class="token keyword"\>...\</span\>, and apply CSS colors.

## **5\. Google Gemini AI Integration**

**Target Model:** Google Gemini 2.5 Pro (via Google Gen AI SDK, `google-genai`)

### **A. Context Caching**

On initialization (\_\_init\_\_.py), the system checks for a cache named praxis-context-cache. If missing, it uploads MCQs.md, 5652\_objectives.md, and pseudocode\_def.md to Gemini and creates the cache with a 1-hour TTL (refreshed on use).

### **B. Prompt Engineering (Strict Enforcement)**

The utils\_ai.py module must generate prompts that enforce the schema and syntax rules.

**1\. Question Generation Prompt:**

"You are an exam author for the PRAXIS 5652 Computer Science test.  
Context: Use the 5652\_objectives.md and pseudocode\_def.md files from the cache.  
Task: Generate {n} multiple-choice questions on '{category}'.  
**STRICT CODE RULES (Zero Tolerance):**

1. You **MUST** use the ← arrow for assignment. NEVER use \= for assignment.  
2. You **MUST** use specific block terminators: end if, end while, end procedure. Do NOT use braces {}.  
3. Arrays are 0-indexed.  
4. **Do not** output Python, Java, or C++ syntax. Use ONLY the provided pseudocode definition.

Output Format:  
Return a JSON LIST of objects. Do not wrap in markdown code fences. Structure:  
\[{ "question\_text": "...", "code\_snippet": "...", "options": {"A": "...", "B": "..."}, "correct\_option": "A", "explanation": "..." }\]"

**2\. Explanation Prompt:**

"Analyze this student's error.  
Question: {question\_json}  
Student Answer: {user\_answer}  
Task:

1. Explain the correct logic (referencing specific lines in the code snippet if present).  
2. Explain the misconception in the student's answer.  
3. Generate a *follow-up practice question* (JSON format) that tests the same concept but with different values or logic."

## **6\. UI/UX Design System**

* **Design Language**: "Blueprint Technical".  
* **Theme**: Light mode only. White (\#ffffff) and Cool Gray (\#f3f4f6).  
* **Geometry**: **0px Border Radius** on ALL elements (Inputs, Buttons, Cards, Modals).  
* **Typography**:  
  * Headings/Body: Inter or system-ui.  
  * Code: JetBrains Mono or Fira Code.  
* **Components**:  
  * **Buttons**: 2px solid border. Hover: Black background, White text. Active: Translate 1px down.  
  * **Quiz Card**: Sharp borders, minimal padding. Code blocks appear in a distinct, high-contrast box (Light Yellow/Beige background \#fffbeb to simulate paper, or standard Gray \#f8f9fa).


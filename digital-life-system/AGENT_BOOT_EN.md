# AGENT_BOOT.md

> This file is the AI initialization guide. AI should follow this script to help users initialize the system on first use.
>
> **Core principle: Guide, don't replace. Let users fill in their own core content.**

---

## Initialization Flow

### Step 1: Introduce the System

Greet the user:

```
Hello! This is a Personal Digital Life System — it helps you organize everything about yourself into a structured archive that AI can understand and remember.

The system has 16 modules. Today we'll start with the 6 core ones.

I'll guide you through each step, about 5-10 minutes each. You can skip any question at any time.
```

### Step 2: Fill in Soul Anchor (Most Important)

> The Soul Anchor is the core of the entire system. Complete this first.

Read `memory/L5-soul/ANCHOR.md`, then ask the user:

1. **What is your deepest belief?** (Something you will never compromise on)
2. **Why are you alive?** (Your life mission)
3. **What do you care about most?** (5 or fewer)
4. **How do you want to be remembered?**
5. **If you died tomorrow, what would you regret?**

Organize the user's answers and write to `memory/L5-soul/ANCHOR.md`.

### Step 3: Define Identity

Read `memory/L4-persona/IDENTITY.md`, then ask:

1. **Who are you?** (Describe yourself in 3 sentences)
2. **How do others usually see you?**
3. **What is your sense of identity?**

### Step 4: Personality & Behavior

Read `memory/L4-persona/PERSONA.md`, then ask:

1. **What are your core personality traits?** (3-5 keywords)
2. **What do you do under pressure?**
3. **What is your communication style?**

### Step 5: Life Narrative

Read `memory/L5-soul/NARRATIVE.md`, then ask:

1. **Describe your life story in a metaphor** (e.g. "always climbing a mountain I can't see")
2. **What is the most important turning point in your life?**
3. **What stage of life are you in now?**

### Step 6: Cognitive Framework

Read `memory/L3-cognitive/COGNITION.md`, then ask:

1. **What do you rely on most when making decisions?** (logic / intuition / emotion / experience)
2. **What are the characteristics of how you think?**
3. **What fixed thinking patterns do you have?**

### Step 7: Vision

Read `memory/V-vision/VISION.md`, then ask:

1. **What does your ideal life look like in 3 years?**
2. **If you had unlimited time and resources, what would you do?**
3. **What do you most want to leave behind?**

### Step 8: Summary & Next Steps

After initialization, tell the user:

```
✅ Core modules initialized!

Your Soul Anchor and Identity Profile have been saved to memory/L5-soul/ and memory/L4-persona/.

In every future conversation, I will remember these.

If you want to go further, you can continue with:
- L-SUCCESS: Your success patterns and lessons from failures
- L-relations: The people you care about
- L-PROJECTS: What you're working on
```

---

## Initialization Rules

1. **Ask only 3 core questions per step** — don't overwhelm users
2. **Users can skip any question** — never force
3. **AI organizes, user confirms** — don't decide for the user
4. **Keep conversation natural** — don't read files mechanically
5. **When answers are vague, ask for specific examples**
6. **Confirm after each save** — let users verify

---

## File Writing Rules

- Read the template file first, preserve all `[Instructions]`
- User content goes after the template structure, separated by `---`
- Never delete or overwrite `[Instructions]` comments
- After writing, confirm content with the user

---
name: design-meaningful-interfaces
description: Design, redesign, critique, and implement expressive product interfaces whose visual structure communicates purpose before explanatory text is needed. Use for mobile apps, web apps, dashboards, onboarding, settings, forms, detail screens, design mockups, Compose, SwiftUI, Flutter, React, HTML/CSS, or Figma work when Codex needs to improve hierarchy, reduce text-heavy layouts, make a UI feel premium, translate product logic into visible interface states, or build a real screen with intentional visual meaning.
---

# Design Meaningful Interfaces

Create interfaces that explain themselves through hierarchy, grouping, contrast, rhythm, state, and interaction. Treat copy as support for the design, not the design itself.

## Core Principle

Make each screen answer one primary user question within three seconds.

Examples:

- Dashboard: "What matters right now?"
- Routine: "What should I do today, and why?"
- Memory: "What has my day looked like, and what changes next?"
- Checkout: "What am I getting, and what will happen if I continue?"

If the screen cannot be summarized as one question, clarify the product logic before composing the UI.

## Workflow

### 1. Read the product context

Inspect the existing product requirements, screen code, design system, navigation, nearby screens, and available data before changing the UI. Reuse established components and tokens when implementing.

### 2. Define the screen contract

Write a private design brief with:

- **Primary question:** the one question the screen must answer.
- **Primary object:** the plan, score, item, status, or action users came to see.
- **Evidence:** the minimum data that makes the primary object credible.
- **State:** what changes visually when the situation changes.
- **Action:** the single next action to emphasize.
- **Secondary paths:** details that may remain available without competing for attention.

Do not present this brief to the user unless an explanation is requested.

### 3. Convert meaning into visual roles

Assign every element a role:

- **Hero:** the primary answer.
- **Signal:** compact metric, status, or comparison.
- **Evidence:** timeline, chart, progress, preview, or grouped facts.
- **Control:** action that changes state.
- **Insight:** consequence, recommendation, or next-step preview.
- **Safety/support:** necessary context that stays visually quiet.

Remove elements that merely repeat another role in paragraph form.

### 4. Compose the screen narrative

Order sections so the eye learns the screen naturally:

1. Answer
2. Evidence
3. Active status or available control
4. User input, if needed
5. Consequence or next step

Use visual grammar from [references/visual-grammar.md](references/visual-grammar.md). Read it when creating or substantially redesigning a screen.

### 5. Choose the output path

#### For a mockup

Generate a high-fidelity visual when the user asks to see the concept. Include realistic content, platform-appropriate spacing, clear states, and concise legible copy. Avoid generic placeholder dashboards.

#### For production implementation

Inspect the codebase first. Implement with the existing framework, components, navigation, and data model. Keep business logic outside UI functions. Add or adjust tests when presentation depends on computed state. Build and visually verify the result when possible.

#### For Figma

Use the available Figma workflow and reuse the design system first. Build editable frames, components, and tokens rather than a flattened imitation.

## Design Rules

- Prefer one dominant visual anchor per viewport.
- Use cards only when they create a meaningful group. Do not wrap every text block in a card.
- Replace prose lists with visual evidence when the data has shape: timeline, comparison, progress ring, chart, segmented status, or metric tiles.
- Make active processes visually distinct from historical information.
- Use color semantically and sparingly: status, emphasis, selection, warning, or category.
- Show change when adaptation is the value: previous vs current, trend, delta, reason, or next recommendation.
- Keep secondary actions quieter than the primary action.
- Preserve breathing room. Density should come from structure, not cramped text.
- Avoid decorative charts, meaningless gradients, and icon clutter.
- Keep safety language visible but subordinate unless the state is urgent.
- Make empty, loading, error, blocked, and success states feel intentionally designed.

## Copy Discipline

Use text for precision, not compensation.

- Prefer labels, values, and one-line consequences.
- Explain only what the visual structure cannot communicate.
- Replace repeated instructions with visible state and clear action labels.
- Use progressive disclosure for deeper explanations.
- Never hide uncertainty in a polished design. Mark estimates and previews honestly.

## Implementation Audit

Before finishing, verify:

1. Can a user identify the screen's purpose in three seconds?
2. Is the most important state visible without reading a paragraph?
3. Does the primary action look primary?
4. Does each card or section have a distinct job?
5. Can any explanatory copy be replaced by hierarchy or a visual pattern?
6. Are active, warning, recovery, empty, and premium states visibly different?
7. Does the screen still feel coherent on a small phone and a wide web viewport?
8. For production work, does the implementation preserve accessibility, platform conventions, and existing architecture?

If the answer to any important question is no, iterate before presenting the result.

## Explain the Design

When the user asks for design logic, explain the interface in this order:

1. The primary question.
2. The role of each major section.
3. Why the hierarchy reduces user effort.
4. How state changes alter the design.
5. What was intentionally left quiet or deferred.

Do not describe colors and rounded corners as the main logic. Explain the product meaning they support.

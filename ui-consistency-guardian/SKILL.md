---
name: ui-consistency-guardian
description: Use when creating, editing, reviewing, or refactoring frontend UI, screens, components, CSS, Tailwind classes, design tokens, typography, fonts, font sizes, spacing, colors, icons, or visual design. Ensures UI elements and design language stay consistent across the project. Do not use for backend-only, data-only, or infrastructure-only tasks unless they affect user-facing UI.
---

# UI Consistency Guardian

## Purpose

Protect the product’s visual and interaction consistency whenever Codex works on user-facing UI. Treat design consistency as a first-class requirement, not a polish step.

This skill ensures that UI elements, design language, fonts, font sizes, spacing, colors, component variants, accessibility states, and responsive behavior remain aligned with the project’s existing design system.

## Core principle

Before adding or changing UI, identify the project’s existing source of truth and reuse it. Prefer existing design tokens, components, utilities, variants, patterns, and layout conventions over introducing new visual decisions.

## When to use this skill

Use this skill for work involving:

- Frontend components, pages, screens, forms, modals, navigation, dashboards, marketing pages, or app shells.
- CSS, SCSS, Tailwind, CSS variables, design tokens, themes, component libraries, or UI kits.
- Typography, font family, font weight, font size, line height, letter spacing, color, spacing, border radius, shadows, icons, motion, or responsive layout.
- UI reviews, visual bug fixes, UX polish, refactors, or design-system cleanup.

Do not use it for backend-only changes unless they directly alter user-facing UI behavior or presentation.

## Required workflow

### 1. Discover the design system before editing

Inspect the repository for the current visual source of truth. Prioritize these files and folders when present:

- `AGENTS.md`, `README.md`, `docs/`, `design/`, `styleguide/`, `storybook/`
- `tailwind.config.*`, `theme.*`, `tokens.*`, `design-tokens.*`
- global CSS files such as `globals.css`, `app.css`, `index.css`, `variables.css`
- component library folders such as `components/ui`, `ui`, `shared/components`, `design-system`
- package choices such as shadcn/ui, Radix, Material UI, Chakra, Mantine, Bootstrap, Ant Design, or custom primitives
- Figma/design export references if present in the repo

If the source of truth is unclear, infer it from repeated usage patterns and document the inference in the final response.

### 2. Create a short consistency contract for the task

Before implementing substantial UI changes, summarize the relevant contract in your working notes or final response:

- Color system: primary, secondary, surface, background, border, muted, danger, success, warning, info.
- Typography: approved font families, scale, weights, line heights, heading/body/caption styles.
- Spacing: spacing scale and layout rhythm.
- Shape: radius scale, borders, elevation/shadows.
- Component rules: existing button, input, card, modal, badge, alert, table, navigation, and form variants.
- States: hover, focus-visible, active, disabled, selected, loading, error, empty.
- Responsive rules: breakpoints, container widths, layout changes.

Keep the contract concise. Use it to guide implementation and review.

### 3. Reuse before creating

When building or changing UI:

- Reuse existing components and variants before creating new ones.
- Use semantic design tokens instead of raw visual values.
- Use existing typography utilities or text variants before adding new font sizes.
- Use existing spacing, radius, shadow, and color scales.
- Match existing interaction patterns for hover, focus, disabled, loading, and validation states.
- Keep naming consistent with existing component, prop, class, and variant conventions.

### 4. Typography rules

Typography consistency is mandatory.

- Do not introduce a new font family unless the task explicitly requires it and the project design system is updated.
- Do not add new font imports casually.
- Use project-approved font tokens, CSS variables, Tailwind theme values, or component text variants.
- Avoid one-off font sizes such as `13px`, `15px`, `text-[13px]`, or inline `style={{ fontSize: ... }}` unless tokenized or justified.
- Preserve hierarchy: page title, section title, subsection title, body, muted body, caption, label, helper text, and error text should map to existing styles.
- Verify line height and font weight, not just font size.

### 5. Color and spacing rules

- Do not hard-code colors in component code when tokens exist.
- Avoid raw hex, RGB, HSL, or arbitrary Tailwind colors outside token/theme files.
- Do not introduce visually similar near-duplicates such as two almost-identical grays, blues, shadows, or radii.
- Use the project spacing scale. Avoid arbitrary pixel margins and padding unless required for precise alignment and documented.
- Ensure visual grouping and hierarchy are clear through consistent spacing, not ad hoc values.

### 6. Component consistency rules

When changing components:

- Check existing component variants before adding new props or classes.
- Keep button styles consistent across primary, secondary, destructive, ghost, link, disabled, loading, and icon-only variants.
- Keep form fields consistent across label, helper text, placeholder, focus, error, disabled, and validation states.
- Keep cards, panels, dialogs, popovers, dropdowns, tabs, and tables consistent with existing structure.
- Keep icon size, stroke width, alignment, and color usage consistent.
- Avoid building duplicate UI primitives if an equivalent already exists.

### 7. Accessibility and UX consistency

Every UI change must preserve or improve usability:

- Use semantic HTML where possible.
- Preserve keyboard navigation and visible focus states.
- Check color contrast for text, icons, borders, and state indicators.
- Keep touch/click targets large enough for comfortable use.
- Provide accessible labels for icon-only controls.
- Ensure loading, error, empty, and success states are visually and textually clear.
- Respect reduced-motion preferences when adding animation.

### 8. Responsive consistency

- Use the project’s existing breakpoint system.
- Match existing container widths and grid patterns.
- Avoid fixing layout issues with magic pixel widths.
- Verify small, medium, and large viewport behavior when touching layout.

### 9. Design drift audit

For UI-heavy tasks, run or simulate a drift audit before finishing:

- Search for newly introduced raw colors, arbitrary font sizes, arbitrary spacing, inline visual styles, duplicate components, and inconsistent variants.
- If scripts are available, use `scripts/audit_design_consistency.py` from this skill.
- Review the diff for one-off design decisions that should be tokens or variants.

### 10. Final response requirements

When reporting completion, include:

- Design-system sources used.
- Existing components/tokens reused.
- Any new component, variant, or token added and why it was necessary.
- Any intentional exception to the design system.
- Validation performed: lint, tests, typecheck, storybook, screenshots, or manual audit.

If no validation could be run, say so clearly and explain the reason.

## Strict do-not rules

Do not:

- Add raw hex/RGB/HSL colors in components when tokens exist.
- Add arbitrary Tailwind values like `text-[13px]`, `p-[17px]`, `bg-[#123456]`, or `rounded-[10px]` without justification.
- Add inline visual styles for static styling when classes/tokens can express the design.
- Add new font families or font imports without updating the design system source of truth.
- Create duplicate buttons, inputs, cards, modals, or typography components instead of extending existing primitives.
- Mix multiple visual languages in one screen.
- Ignore focus, disabled, error, empty, loading, and responsive states.

## Useful references in this skill

- `references/design-system-audit-checklist.md` — manual review checklist.
- `references/design-token-contract.md` — template for documenting project tokens.
- `scripts/audit_design_consistency.py` — optional scanner for common design drift patterns.

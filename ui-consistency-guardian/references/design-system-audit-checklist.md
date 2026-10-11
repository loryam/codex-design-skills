# Design System Audit Checklist

Use this checklist when reviewing UI changes for consistency.

## Source of truth

- [ ] Identified the design system source of truth: tokens, theme config, component library, CSS variables, docs, or repeated project conventions.
- [ ] Reused existing components before creating new components.
- [ ] Reused existing component variants before creating new variants.
- [ ] Documented any intentional deviation.

## Typography

- [ ] Font family comes from the approved project source.
- [ ] Font sizes use the existing type scale or semantic text variants.
- [ ] Font weights match project hierarchy.
- [ ] Line heights are consistent and readable.
- [ ] Labels, helper text, captions, and error text follow existing patterns.

## Color

- [ ] Colors use semantic tokens or theme variables.
- [ ] No one-off hex/RGB/HSL colors were added to component code.
- [ ] Text contrast is sufficient.
- [ ] State colors for error, warning, success, disabled, selected, and focus are consistent.

## Spacing and layout

- [ ] Margins, padding, gaps, and container widths use the project scale.
- [ ] Layout rhythm matches nearby screens/components.
- [ ] No magic pixel values were introduced without justification.
- [ ] Responsive behavior matches existing breakpoint conventions.

## Components and states

- [ ] Buttons match existing size, radius, typography, icon spacing, and variants.
- [ ] Inputs match existing label, placeholder, helper, error, focus, and disabled states.
- [ ] Cards/modals/dropdowns/tables/navigation match existing structure.
- [ ] Icons use consistent size, stroke, alignment, and color.
- [ ] Loading, empty, success, and error states are covered.

## Accessibility

- [ ] Interactive elements are keyboard reachable.
- [ ] Focus-visible state is clear.
- [ ] Icon-only buttons have accessible names.
- [ ] Semantics are appropriate: headings, buttons, links, labels, lists, tables.
- [ ] Motion respects reduced-motion preferences where applicable.

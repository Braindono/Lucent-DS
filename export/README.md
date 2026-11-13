# Lucent — token export

A portable export of the design tokens and typographic rules from the **Lucent** design system (a glass + neumorphic hybrid — cool tones, Bauhaus/Teenage Engineering/retro-futurism lineage, three concept directions plus an Aurora Console dashboard). This package carries only the *foundations* — color, type, spacing, radius, shadow, blur, opacity — not the components, assets or brand narrative; pair it with the components and README under `project/` for the fuller picture.

## What's here

| File | Format | Use it when… |
|---|---|---|
| `tokens.css` | Plain CSS custom properties + type-scale utility classes | …the target is a web project and you want a zero-tooling drop-in. No build step, no parser needed. |
| `tokens.light.json`, `tokens.dark.json` | [W3C Design Tokens (DTCG)](https://design-tokens.github.io/community-group/format/) draft format | …the target has (or expects) a token pipeline — Style Dictionary, Tokens Studio, a custom codegen step, or another agent that reads structured tokens rather than CSS. |
| `typography.json` | DTCG `fontFamily` + `typography` composite tokens, theme-independent | …importing the type scale specifically. Font sizes and line-heights are `rem`, not `px` — they scale with the root font-size. |
| `motion.json` | DTCG `duration` + `cubicBezier` tokens, theme-independent | …importing the motion system: one easing curve, two durations, nothing else. |

All four describe the *same* values — pick the shape that fits the target project rather than importing more than one.

## This export is generated — do not hand-edit it

Every file in this folder (including `tokens.css`) is produced by `project/scripts/regen_tokens.py` from `project/tokens.json`, the single source of truth. A hand edit here will be silently overwritten the next time the script runs, and in the meantime it drifts from the source without anything flagging it. To change a value: edit `project/tokens.json`, then from the `Design_System` folder run:

```
python3 project/scripts/regen_tokens.py
```

This regenerates `tokens.css`, `tokens.light.json`, `tokens.dark.json`, `typography.json`, `motion.json`, and `lucent-tokens-export.zip` together, so they can't drift out of sync with each other or with the source. `tokens.css`'s header comment records which source file hash and timestamp produced it, so staleness is checkable at a glance.

## Using `tokens.css`

Link or inline the file, then set `data-theme="light"` or `data-theme="dark"` on `<html>` (or leave it unset — `:root` alone already resolves to light). Every custom property is theme-aware via the `[data-theme="…"]` attribute selector; nothing else needs to change when the user toggles themes.

Also load the two typefaces — both are hosted on Google Fonts, no font files to ship:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap">
```

The stylesheet also defines one CSS class per type style (`.heading-md`, `.body`, `.data-mono`, …) — see Typographic rules below.

## Using the DTCG JSON files

Each color/shadow token carries:
- `$value` — a literal value, or a DTCG alias reference (`"{color.surface.base}"`) to another token in the *same* theme file. Resolve aliases before use, or run the file through any DTCG-aware tool.
- `$description` — the usage note: where the token is meant to be used, and any contrast number it was validated against.
- `$extensions["lucent.sourceName"]` — the token's original flat name in Lucent (e.g. `accent-a`), for tracing a value back to the source system.

`tokens.light.json` and `tokens.dark.json` are structurally identical (same paths); only the leaf `$value`s differ. A consuming project typically either picks one at build time, or generates two token sets (a common Style Dictionary / Tokens Studio pattern) keyed the same way `tokens.css` keys them, by `data-theme`.

Shadows are exported as DTCG `shadow` composite tokens — an **array** of layers (`{color, offsetX, offsetY, blur, spread, inset}`), since several of these (the neumorphic ones) are two-layer shadows (a highlight + a shadow). Rebuild the CSS `box-shadow` value by joining the layers with commas.

## Typographic rules

Two type families, both loaded from Google Fonts — no serif or display face anywhere:

- **`Space Grotesk`** (`font.sans`) — a geometric, Bauhaus-adjacent grotesk. Everything except data.
- **`Space Mono`** (`font.mono`) — every number, timestamp, coordinate, and instrument-panel label. This is a deliberate identity choice, not a fallback: Lucent treats monospaced figures as part of its "measuring instrument" visual language, so hero numbers and stat values use `data-mono`/`display-*` in the mono face rather than the more conventional proportional-sans hero figure.

| Style | Family | Size / line-height / weight | Use it for |
|---|---|---|---|
| `display-xl` | sans | 4rem / 4.25rem / 700 | The system name on a cover or a full-bleed hero moment. One per view, ever. |
| `display-lg` | sans | 2.5rem / 2.875rem / 700 | Section-opening numerals, large dashboard readouts. |
| `heading-lg` | sans | 1.75rem / 2.125rem / 600 | Page and panel titles. |
| `heading-md` | sans | 1.25rem / 1.625rem / 600 | Card and section titles. |
| `heading-sm` | sans | 1rem / 1.375rem / 600 | Control-cluster labels, list-row titles. |
| `body` | sans | 0.9375rem / 1.375rem / 400 | Default body copy. |
| `body-sm` | sans | 0.8125rem / 1.125rem / 400 | Captions, helper text, secondary list content. |
| `label-mono` | mono | 0.6875rem / 0.875rem / 500, tracking +0.04em | Tick labels and tags. Set uppercase in CSS — the token itself stores mixed case. |
| `data-mono` | mono | 0.8125rem / 1.125rem / 400 | Numeric readouts, coordinates, version stamps, stat-tile values. |

Sizes are `rem` (root-relative), not `px` — the whole scale moves together if the root font-size changes, which is what makes a user text-scale control possible.

Rules that don't live in the token values themselves, carried over from the source brand book:

- Write UI labels short and declarative, Title Case for controls and nav ("Save Layout"); body and helper copy in sentence case, no exclamation points.
- Large standalone numbers (a hero figure, a stat-tile value) use the font's normal proportional figures; reserve `font-variant-numeric: tabular-nums` for columns of numbers that must align vertically (table rows, axis ticks) — moot for `Space Mono` itself, since a true monospace face has no proportional/tabular distinction, but relevant if a receiving project substitutes a proportional sans for the mono role.

## Motion rules worth carrying over, not just the values

One easing curve (`ease-out`, `cubic-bezier(0.22,1,0.36,1)`) and two durations (`dur-fast`, 120ms, press/tap feedback only; `dur-base`, 180ms, everything else). No springs, no bounces, no slower duration — motion here confirms an interaction, it never performs one. `status-pulse` is the one named exception, reserved for an "active/in-progress" status dot. Wrap every use of these in `@media (prefers-reduced-motion: reduce)`.

## Color rules worth carrying over, not just the values

- **Elevation is shadow, not a second fill color.** `color.surface.raised` and `color.surface.sunken` both alias straight back to `color.surface.base` — depth comes only from pairing a surface with `shadow.neu-raised` or `shadow.neu-inset`, never from a lighter/darker background.
- **`color.viz.series-b` (cyan) sits below 3:1 contrast in the light theme by design** — it passed the categorical color-blindness/lightness checks but not the light-surface contrast check. Ship it with a legend or direct labels, never as an unlabeled fill alone.
- **`color.accent.c-glow` (violet-500) is decorative-only** — glow effects, large icons, borders. It clears 3:1 but not 4.5:1, so it never carries small text or a solid icon meant to be read as text.
- **Status colors (`color.status.*`) always pair with an icon or shape, never color alone** — `good`/`warning`/`serious`/`critical` are reserved and distinct from the categorical `viz.series-*` slots on purpose, so a status color never gets mistaken for "just another series."
- Every color/shadow token's `$description` states which surface it was checked against and, where relevant, the exact contrast ratio — that's copied straight from the source system's own validation notes, not re-derived.

## Source

Exported from the **Lucent** design system.

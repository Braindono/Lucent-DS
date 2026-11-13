# Structural

Site-level chrome that every page needs and none of the concept/dashboard previews
demonstrate on their own: a header/nav bar, a project card, and a footer, composed
together in one scene on Primary Direction tokens.

**This is also the first component to use the Lucent icon set** (`project/icons/`) —
search, menu, external-link, arrow, and the four social marks are the shipped
`icon-sprite.svg` symbols, inlined here (not fetched) to keep this preview
self-contained the way every other `preview.html` in this folder is.

## What's here

- **Header** — logo mark (a placeholder dot + wordmark; Lucent doesn't have its own
  brand mark yet, see TODO.md), a capped primary nav, a search icon button, a mobile
  menu-toggle icon button, and one `accent-primary` CTA. Collapses at 640px: the nav
  hides, the hamburger button appears (wiring the actual open/close menu is left to
  whoever builds this into a real page — this preview shows the collapsed state, not
  a functioning drawer).
- **Project card** — the whole card is the link (not a small "read more" inside it),
  neumorphic raised with a glass-elevation lift on hover/focus, a status-style tag,
  and an `arrow-up-right` external-link icon on the CTA.
- **Footer** — a brand column with the social row, three link columns, and a legal
  bar. Link columns stay short on purpose (see below).

## UX laws this bakes in, not just documents

Rather than keep usability laws as a parallel document, this component makes several of them literal CSS
rules instead of prose:

- **Fitts's Law (44×44px minimum target).** Every clickable control here —
  nav links, icon buttons, the CTA, footer social icons — has `min-height: 44px`
  (`min-width` too, where the control is icon-only) even where the visible label or
  icon is much smaller. The hit area, not the glyph, is sized to the rule.
- **Jakob's Law.** Logo left, primary nav center-left, utility actions right; footer
  link columns beneath a brand column. No novel chrome layout — visitors spend zero
  learning cost on where things are.
- **Hick's Law.** The primary nav is capped at four items. More choices in the top
  bar is a tax on every visitor, every page load.
- **Miller's Law.** Each footer column stays at or under five links — small enough to
  read as one chunk, not a list to scan-and-count.
- **Von Restorff Effect.** Exactly one nav item carries weight (the active page) and
  exactly one action in the header is a solid `accent-primary` fill (the CTA) —
  everything else stays neutral so those two things are what actually stand out.
- **Fitts's Law again, at the card level.** The entire card is the anchor, not a
  small "Read case study →" link inside it — the obvious click target is the large
  one, not the small one that happens to say "click me."

## Token usage

Nothing new was added to `tokens.json` for this — it's built entirely from existing
tokens (`accent-primary/secondary/tertiary`, `glass-surface(-strong)`, `neu-raised`,
`glass-elevation-2`, `radius-xs/sm/full`, `focus-ring`) plus the typography utility
classes (`label-mono`, `heading-sm`, `body-sm`, `data-mono`) from `export/tokens.css`.
Verified in both themes and at a 420px mobile width via Playwright — no overflow, no
contrast regressions, hover/focus states visible in both themes.

## Left for later

- A real mobile nav drawer (this preview shows the collapsed trigger, not the open
  drawer's transition/overlay/focus-trap behavior).
- Lucent's own brand mark, to replace the placeholder dot+wordmark once one exists.
- Breadcrumbs, pagination, tooltip, modal, table — still on TODO.md's list, not
  attempted here.

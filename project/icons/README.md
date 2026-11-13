# Lucent icon set

1,383 single-ink outline icons — `viewBox="0 0 24 24"`, `stroke-width="1.5"` (normalized; the
source file had ~11 stray path-level values drifted to things like `1.2195` from a vector-export
round-trip — all forced back to `1.5`), `fill="none"`, `stroke="currentColor"`. `currentColor`
means every icon inherits its color from CSS — set `color` on the `<svg>`/`<use>` wrapper to one
ink token, per the design system's own "single-ink SVG icon, one ink token per icon" rule
(`project/README.md`, Iconography). This satisfies that TODO item as a real, usable asset, not a
placeholder.

**Provenance note:** the set is an original asset of this project, not a named third-party icon
library (not Tabler/Feather/Phosphor/etc.), so it carries no outside licensing terms. Embedded
file metadata from the source export has been stripped from `icon-sprite.svg`.

## Files

| File | What it's for |
|---|---|
| `icon-sprite.svg` | The actual asset. One `<svg style="display:none">` wrapper holding all 1,383 `<symbol id="…">` defs. Include it once per page (inline or fetched), then reference any icon with `<svg class="icon"><use href="icon-sprite.svg#arrow-left"/></svg>`. |
| `manifest.json` | Structured lookup: `{id, family, viewBox}` for all 1,383 icons, `family` = the id's first hyphen-segment (e.g. `arrow-up-right` → family `arrow`). For tooling that wants to query rather than grep. |
| `index.txt` | Flat, one-icon-per-line (`id<TAB>family:X`), alphabetically sorted. This is the fast lookup path — `grep -i keyword index.txt` beats scanning 1,383 lines of manifest JSON or opening the sprite. |

## Looking up an icon

```
grep -i "arrow" index.txt        # every arrow-* icon
grep -i "calendar" index.txt     # calendar family + anything else mentioning it
grep -iE "close|xmark|^x\b" index.txt   # close/dismiss candidates
```

**Be honest about what "family" buys you.** This set spans UI chrome, brand marks (Adobe, Apple,
Google…), objects, sports, nature — far broader than a curated interface icon pack. Grouping by
first-hyphen-segment gives 637 families, but 383 of those are singletons (no real cluster) and only
59 have 5+ icons (`arrow` 32, `emoji` 23, `database` 16, `home`/`shield` 14, `page` 13…). Family
grouping is a bonus for the icons that do cluster, not a universal taxonomy — the names themselves
are the real index; grep them directly rather than trusting the family field to be exhaustive.

## Core-UI shortlist (covers the TODO.md ask directly)

The near-term need was nav/menu, close, external-link, arrow/chevron, search, and social — all
present in the set without needing new icons drawn:

| Need | Icon id |
|---|---|
| Menu / hamburger | `menu` |
| Close / dismiss | `x` (or `xmark` if a heavier glyph reads better at small size) |
| External link | `arrow-up-right` |
| Chevron / directional (no dedicated "chevron" or "caret" id exists in this set — the plain `arrow-*` directionals fill the same role) | `arrow-left`, `arrow-right`, `arrow-up`, `arrow-down` |
| Search | `search` |
| Social — LinkedIn, GitHub, Twitter, Facebook, Instagram, YouTube | `linkedin`, `github`, `twitter`, `facebook`, `instagram`, `youtube` |
| Email | `mail` |

If a genuine chevron (distinct from a full arrow) turns out to matter visually once the nav bar is
built, that's a small, cheap addition rather than a blocker — flag it and it can be drawn to match.

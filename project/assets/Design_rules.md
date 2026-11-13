# UX Design Rules — Agent Reference

purpose: Canonical, condensed rule set for a design agent to apply when producing or reviewing UI/UX work.
usage: Treat each rule as a checkable constraint. When a design decision conflicts with a rule, prefer the rule unless the user has stated an explicit override.
format: Each rule = id, name, category, rule (the constraint), why (rationale), apply (concrete trigger/check).

---

## 01 — Visibility of System Status
category: Feedback
rule: Always show the user what state the system is in, within ~1 second of any action.
why: Uncertainty about whether an action registered erodes trust and causes repeat actions.
apply: Loading spinners, progress bars, saved/sent confirmations, active-state highlighting on nav/buttons.

## 02 — Match Between System and Real World
category: Mental Model
rule: Use language, icons, and concepts familiar to the user's domain, not internal system jargon.
why: Users map new interfaces onto real-world or prior-tool experience; mismatches force translation effort.
apply: Label actions with verbs users already use (e.g., "Send," not "Submit Payload"); order fields the way users think about a task.

## 03 — User Control and Freedom
category: Trust
rule: Provide clearly marked exits: undo, cancel, back, and "emergency exit" from any flow.
why: Users take wrong actions by mistake; forcing them through extra steps to recover breeds frustration.
apply: Every destructive action gets an undo or confirm step; every multi-step flow gets a visible exit/back.

## 04 — Consistency and Standards
category: Learnability
rule: Same word, icon, and interaction pattern must always mean the same thing across the product.
why: Reduces cognitive load; leverages platform conventions users already know.
apply: One component library; reuse existing patterns before inventing new ones; follow platform HIG/Material conventions unless there's a strong reason not to.

## 05 — Error Prevention
category: Reliability
rule: Prefer design that prevents errors over messaging that explains them after the fact.
why: A prevented error costs nothing; a caught-and-explained error still costs user time and trust.
apply: Disable invalid submits, constrain input formats, confirm before irreversible/high-cost actions.

## 06 — Recognition Rather Than Recall
category: Cognitive Load
rule: Make objects, actions, and options visible; don't require users to remember information across screens.
why: Recognition is cognitively cheaper than recall.
apply: Show recently used items, autofill, visible menus over memorized shortcuts/commands.

## 07 — Flexibility and Efficiency of Use
category: Scalability
rule: Provide accelerators (shortcuts, defaults, bulk actions) for expert users without cluttering the interface for novices.
why: Novices and power users have different needs; a single fixed path underserves one or both.
apply: Keyboard shortcuts, saved presets, batch operations — hidden by default, discoverable on demand.

## 08 — Aesthetic and Minimalist Design
category: Visual Design
rule: Every unit of information competes with relevant information; remove anything not earning its place.
why: Extraneous elements dilute attention and slow comprehension.
apply: Cut decorative-only elements; challenge every label, icon, and border to justify its presence.

## 09 — Help Users Recognize, Diagnose, and Recover From Errors
category: Error Handling
rule: Error messages must be in plain language, state the problem precisely, and suggest a fix.
why: Vague or technical errors (e.g., "Error 500") leave users stuck.
apply: No raw codes/stack traces in user-facing copy; always pair error with next action.

## 10 — Help and Documentation
category: Support
rule: If help is needed, it must be searchable, task-focused, and available in context — not just in a separate manual.
why: Users look for help at the point of confusion, not before.
apply: Inline tooltips/empty-state guidance over long onboarding docs; contextual help links near complex controls.

## 11 — Fitts's Law
category: Interaction
rule: Target size and distance determine speed/accuracy of selection — make frequent/important targets large and close.
why: Smaller and farther targets take longer and are more error-prone to hit, especially on touch/mobile.
apply: Primary CTAs ≥44x44px on touch; place frequent actions near the user's current focus, not across the screen.

## 12 — Hick's Law
category: Decision Load
rule: Time to decide increases with the number and complexity of choices — reduce or group options.
why: Overloaded choice sets slow decisions and increase abandonment.
apply: Cap primary nav/menu items (~5–7); progressively disclose secondary options; provide smart defaults.

## 13 — Progressive Disclosure
category: Information Architecture
rule: Show only what's needed for the current step; defer advanced/rare options to a secondary view.
why: Prevents overwhelming first-time or majority-case users with edge-case complexity.
apply: "Advanced settings" behind a toggle; wizards/steppers for complex multi-field forms.

## 14 — Visual Hierarchy
category: Visual Design
rule: Size, weight, contrast, and whitespace must communicate importance and reading order without relying on labels alone.
why: Users scan before they read; hierarchy guides that scan path.
apply: One dominant primary action per screen; body text and headings differentiated by scale, not color alone.

## 15 — Gestalt Principles (Proximity, Similarity, Closure)
category: Perception
rule: Group related elements spatially and stylistically; unrelated elements must be visibly separated.
why: Users perceive groups before individual elements; misleading grouping causes misreads.
apply: Related form fields/labels sit closer together than to unrelated fields; consistent styling = implied relationship.

## 16 — Accessibility (WCAG AA Minimum)
category: Inclusive Design
rule: Meet WCAG 2.1 AA: 4.5:1 text contrast (3:1 for large text), full keyboard navigation, alt text for meaningful images, visible focus states.
why: Legal requirement in many jurisdictions and removes barriers for users with disabilities — benefits all users under poor conditions (glare, small screens).
apply: Run contrast checks on all text/background pairs; tab through every flow with no mouse; never convey meaning by color alone.

## 17 — Response Time Thresholds
category: Performance/Feedback
rule: <0.1s feels instant (no feedback needed); <1s keeps flow uninterrupted (subtle feedback); >1s requires a progress indicator; >10s risks abandonment and needs explicit status + escape.
why: Perceived performance is as important as actual performance to user satisfaction.
apply: Add spinners/skeletons past 1s; add progress bars + cancel option past 10s.

## 18 — Mobile-First / Responsive Constraints
category: Layout
rule: Design for the smallest, most constrained viewport and touch input first, then scale up.
why: Constraints force prioritization; expanding from mobile to desktop is easier than compressing the reverse.
apply: Single-column base layout, touch-sized targets, then add multi-column/hover states at larger breakpoints.

## 19 — Content-First / Plain Language
category: Content
rule: Use the simplest language that accurately conveys meaning; avoid jargon, marketing tone, or ambiguity in UI copy.
why: Clarity reduces support burden and cognitive load; cleverness often reduces comprehension speed.
apply: Prefer "Delete" over "Remove permanently from your account"; write copy at roughly an 8th-grade reading level unless domain-expert audience justifies otherwise.

## 20 — Match Confirmation Cost to Action Cost
category: Trust/Safety
rule: The friction of confirming an action should scale with how costly/irreversible that action is.
why: Over-confirming trivial actions trains users to click through warnings; under-confirming costly ones causes accidental data loss.
apply: One-click for reversible/low-cost actions; explicit modal + typed confirmation for destructive/irreversible/high-cost actions.

---

## Application Notes for the Design Agent
- When rules conflict (e.g., minimalism vs. accessibility), accessibility and error-prevention rules take precedence over aesthetic ones.
- Cite the rule ID (e.g., "Rule 11 — Fitts's Law") when justifying a design decision so rationale stays traceable.
- These rules are defaults, not absolutes — deviate only with an explicit, stated reason tied to user research or platform convention.

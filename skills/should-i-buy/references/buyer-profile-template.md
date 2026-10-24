# Buyer Profile Template & Maintenance Rules

Reference for reading, creating, and updating an optional persistent buyer profile so [`should-i-buy`](../SKILL.md) remembers the user's baseline context across sessions without re-asking settled questions.

## Discovery order

1. **Project-scoped profile**: `.agents/buyer-profile.md` in the current workspace (useful for team/B2B procurement or project-specific budgets).
2. **User-global profile**: `~/.agents/buyer-profile.md` (default home for personal buying decisions across CLI and IDE agents).
3. **Chat environment fallback**: in Claude Desktop or web chat where local dotfiles are unavailable, read built-in platform memory or project instructions, and offer a copyable Markdown block when the user asks to save their profile.

## Maintenance rules

1. **Zero-config by default**: Never block an evaluation because no profile file exists. Gather only the context needed for the current purchase via Step 1.
2. **Opt-in writes only**: Create or update `.agents/buyer-profile.md` or `~/.agents/buyer-profile.md` only after delivering the verdict and confirming the user wants to save the newly established preferences or decision log entry.
3. **Keep entries compact and durable**: Store only facts that affect future purchase evaluations (currency, tax/shipping region, financial guardrails, owned ecosystem/gear, active subscriptions, and past decision outcomes). Never store raw account numbers, credentials, or sensitive personal identifiers.

## Recommended schema (`buyer-profile.md`)

```markdown
# Buyer Profile

## Baseline & Region
- **Currency**: USD ($)
- **Region & Tax Baseline**: [Country / State / VAT or sales tax %]
- **Net Hourly Time Valuation**: $[X]/hr (used for Cost per Net Hour Saved calculations)

## Financial Guardrails
- **Default Opportunity-Cost Benchmark**: [e.g., 4.5% HYSA / 7% real index return / 22% APR debt payoff]
- **Cooling-Off Rules**:
  - $100 to $500 discretionary: 72-hour wait
  - Over $500 discretionary: 30-day wait
- **Hard Guardrails**:
  - Cash-only for discretionary wants (no revolving credit or fee-bearing BNPL)
  - Preserve [X]-month emergency fund floor

## Owned Ecosystem & Inventory
- **Computing & Mobile**: [e.g., macOS / iOS / USB-C + Thunderbolt 4 monitor]
- **Smart Home / Local Standards**: [e.g., Matter / Home Assistant / local-only preference]
- **Tool / Battery Platforms**: [e.g., Makita 18V LXT]
- **Key Existing Gear**: [notable appliances, audio, camera, vehicles, or fitness gear to prevent redundant purchases]

## Active Subscriptions
| Service | Billing Cost | Renewal Cadence | Primary Use / Audit Notes |
| :--- | :--- | :--- | :--- |
| [Example Service] | $[X]/mo | Monthly | [Active daily / candidate for rotation] |

## Purchase Decision Log & Post-Mortems
| Date | Item Evaluated | Verdict Assigned | Action Taken | 6-Month Post-Mortem / Lesson |
| :--- | :--- | :--- | :--- | :--- |
| YYYY-MM-DD | [Item Name] | `Buy` / `Do Not Buy` / etc. | Bought / Skipped / Returned | [Used daily vs. shelf-ware; what worked or failed] |
```

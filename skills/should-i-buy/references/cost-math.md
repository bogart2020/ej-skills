# Cost Math for Step 4

Formulas and definitions behind Step 4 of [`SKILL.md`](../SKILL.md). Read it before computing costs; scale depth to the rigor tier.

## 1. Total Cost of Ownership over holding horizon T

$$\text{TCO}(T) = C_{\text{acquisition}} + C_{\text{onboarding}} + C_{\text{financing}} + C_{\text{operating}}(T) + C_{\text{maintenance}}(T) + C_{\text{exit}} - V_{\text{salvage}}(T)$$

- $C_{\text{acquisition}}$: street price + sales/VAT tax + shipping/customs + mandatory day-one accessories.
- $C_{\text{onboarding}}$: installation, setup, migration, or learning-curve cost.
- $C_{\text{financing}}$: total interest and fees over any loan, credit, or BNPL term.
- $C_{\text{operating}}(T)$: electricity/fuel, consumables (filters, ink, pods, blades), insurance, and recurring subscriptions over $T$.
- $C_{\text{maintenance}}(T)$: scheduled servicing, battery replacements, and expected out-of-warranty repairs.
- $C_{\text{exit}} - V_{\text{salvage}}(T)$: realistic resale or trade-in value at $T$ from completed secondary-market sales, minus marketplace selling fees (typically 10% to 15%) or termination penalties.

## 2. Deflated cost per use and per hour

Cost-Per-Use = $\text{TCO}(T) / \text{total uses}$; Cost-Per-Hour = $\text{TCO}(T) / \text{total active hours}$. Compute both at stated usage and at **50% of stated usage**, to guard against optimism bias.

## 3. Break-even uses and time value

- When a rent, lease, or pay-per-use option costs $R$ per use and ownership has variable cost $v$ per use:
  $$N^* = \frac{C_{\text{acquisition}} + C_{\text{onboarding}} + C_{\text{financing}} + C_{\text{exit}} - V_{\text{salvage}}(T)}{R - v}$$
- When the purchase saves time, compute **cost per net hour saved** ($\Delta \text{TCO}(T) / \Delta H_{\text{net saved}}$, subtracting setup, cleaning, and maintenance time) and compare it with the user's net hourly rate.

## 4. Opportunity cost

Frame $\text{TCO}(T)$ against concrete competing uses of the same money: paying off high-APR debt (a 20% to 29% guaranteed return), keeping emergency-fund liquidity, compounding at a conservative real return over $T$ and over 10 years, or funding a higher-priority goal.

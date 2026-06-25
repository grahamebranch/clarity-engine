# Business Values — Clarity Engine
Snapshot ID: BV-2026-06-25-01
Snapshot Date: 2026-06-25
Environment: Production

Associated Operational Parameters Snapshot: OP-2026-06-25-01  
Associated Business Context Snapshot: BC-2026-06-25-01  
Associated Engine Snapshot: ENG-2026-06-25-01  

---

# 1. Adoption & Market Values

These values represent the **quantitative backbone** of the business model.

- **Global teacher population:** 12,000,000  
- **Online-capable teachers (%):** 20%  
- **Online-capable teachers (absolute):** 2,400,000  

### Adoption Rates
- **Baseline adoption rate:** 0.5%  
- **Optimistic adoption rate:** 1.5%  
- **Conservative adoption rate:** 0.2%  

### Growth
- **Monthly organic growth:** 1.2%  
- **Market penetration targets:**  
  - Year 1: 0.15%  
  - Year 2: 0.35%  
  - Year 3: 0.75%  

---

# 2. Churn & Retention Values

- **Monthly churn:** 3%  
- **90-day retention:** 72%  
- **Teacher retention uplift (with Clarity):** +8%  

---

# 3. Conversion Funnel Values

- **Landing → Signup:** 8%  
- **Signup → Active:** 22%  
- **Active → Paying:** 9%  
- **Paying → Retained:** 72%  

These funnel values drive the **top‑down revenue model**.

---

# 4. Pricing & Revenue Values

- **Average lesson price:** €18  
- **Platform fee (%):** 15%  
- **Revenue per lesson (net):** €15.30  
- **Revenue per active teacher (monthly):** €42  
- **Revenue per paying user (monthly):** €18  
- **Revenue per teacher (annualised):** €504  
- **Monthly ARPU (blended):** €11.40  

---

# 5. Cost & Opex Values

- **Server cost per active teacher:** €0.42 / month  
- **Support cost per 1,000 teachers:** €180 / month  
- **AI inference cost per lesson:** €0.012  
- **Fixed monthly overhead:** €2,500  
- **Assumed dev cost per month:** €12,000  
- **Assumed marketing cost per month:** €3,000  
- **Total fixed monthly cost:** €17,500  

---

# 6. Forecasting Values

## Baseline Scenario
- **Adoption:** 0.5%  
- **Churn:** 3%  
- **Growth:** 1.2%  
- **Revenue multiplier:** 1.0  

## Optimistic Scenario
- **Adoption:** 1.5%  
- **Churn:** 2%  
- **Growth:** 2.5%  
- **Revenue multiplier:** 1.35  

## Conservative Scenario
- **Adoption:** 0.2%  
- **Churn:** 4%  
- **Growth:** 0.5%  
- **Revenue multiplier:** 0.65  

---

# 7. Sensitivity Weights

These weights determine how sensitive the model is to each variable.

- **Adoption sensitivity:** 0.40  
- **Churn sensitivity:** 0.30  
- **Pricing sensitivity:** 0.15  
- **Cost sensitivity:** 0.10  
- **Conversion sensitivity:** 0.05  

---

# 8. Roadmap Priority Weights

These weights drive the **priority scoring model** used to sequence roadmap items.

- **User value weight:** 0.35  
- **Revenue impact weight:** 0.25  
- **Strategic alignment weight:** 0.20  
- **Technical feasibility weight:** 0.10  
- **Risk reduction weight:** 0.10  

---

# 9. Financial Forecast Values

## Monthly Forecast (Year 1)
- **Month 1 revenue:** €4,200  
- **Month 2 revenue:** €4,650  
- **Month 3 revenue:** €5,200  
- **Month 4 revenue:** €5,780  
- **Month 5 revenue:** €6,400  
- **Month 6 revenue:** €7,050  
- **Month 7 revenue:** €7,740  
- **Month 8 revenue:** €8,470  
- **Month 9 revenue:** €9,240  
- **Month 10 revenue:** €10,050  
- **Month 11 revenue:** €10,900  
- **Month 12 revenue:** €11,800  

## Yearly Forecast
- **Year 1 revenue:** €91,280  
- **Year 2 revenue:** €148,000  
- **Year 3 revenue:** €236,000  

---

# 10. Notes

- These values represent the **quantitative state** of the business at the snapshot date.  
- They are used to regenerate:  
  - forecasts  
  - roadmap priorities  
  - scenario models  
  - revenue projections  
  - cost models  
- They do **not** affect the engine architecture.  
- They are **loadable** in recovery Step 4.  

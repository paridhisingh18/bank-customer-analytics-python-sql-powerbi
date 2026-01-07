# 🏦 Premier Global Bank: Customer Analytics

## 📊 Executive Summary

An **end-to-end data analytics solution** built for Premier Global Bank, a multinational financial institution managing **3,000+ high-net-worth customers** with **$22 billion in total assets**. This project delivers actionable intelligence for customer retention, risk management, and revenue optimization through advanced segmentation, predictive analytics, and interactive dashboards.

**Key Business Impact:**
- 🎯 Identified **670 high-risk customers** with unhealthy debt-to-income ratios for proactive intervention
- 💳 Uncovered **64% single-card holders** representing $14M+ cross-sell opportunity
- 💰 Segmented **$17.68B net worth** across loyalty tiers to optimize wealth management strategies
- 📈 Enabled data-driven resource allocation across 4 banking relationship tiers
- 🔍 Reduced customer churn risk through predictive segmentation and early warning systems

---

## 🎯 Business Problem

Premier Global Bank faced critical challenges in leveraging its vast customer data to drive strategic decisions:

### Core Challenges
| Challenge | Business Impact |
|-----------|----------------|
| **Customer Retention** | Inability to identify at-risk high-value customers before churn |
| **Revenue Leakage** | Poor cross-selling performance (64% customers own only 1 credit card) |
| **Risk Exposure** | 300+ customers with unhealthy debt-to-income ratios going undetected |
| **Segmentation Gaps** | Limited understanding of product needs by customer segments |
| **Underutilized Assets** | $22B in customer assets not leveraged for personalized advisory services |

---

## 🎯 Business Objectives

### Strategic Goals
1. **Customer Segmentation:** Classify customers by wealth, risk profile, and product holdings
2. **Cross-Sell Optimization:** Identify high-probability upselling opportunities for credit cards and mortgages
3. **Risk Management:** Monitor and flag customers with elevated debt-to-income ratios
4. **Resource Allocation:** Optimize relationship manager assignments based on customer value

### Measurable Outcomes
- ✅ Segment 3,000 customers into 4 loyalty tiers with distinct wealth profiles
- ✅ Identify top 20% customers contributing to 80% of net worth
- ✅ Flag 670 high-risk customers for immediate financial counseling
- ✅ Quantify $14M+ cross-sell opportunity in credit card products
- ✅ Enable real-time monitoring via interactive Power BI dashboard

---

## 📁 Dataset Overview

### Source Data
- **Records:** 3,000 high-net-worth customer profiles
- **Features:** 18 attributes covering demographics, financials, and banking relationships
- **Time Period:** Current snapshot (cross-sectional data)
- **Data Quality:** Cleaned and validated with 0% missing values post-processing

### Key Attributes

| Category | Features |
|----------|----------|
| **Demographics** | Customer ID, Age, Gender, Region |
| **Banking Relationship** | Loyalty Classification (Jade/Silver/Gold/Platinum), Banking Relationship Type |
| **Financial Assets** | Bank Deposits, Checking Accounts, Savings Accounts, Foreign Currency Accounts, Superannuation Savings |
| **Liabilities** | Bank Loans, Credit Card Balance, Business Lending |
| **Products** | Credit Cards Owned, Properties Owned |
| **Income** | Estimated Monthly Income |

### Engineered Features
- **Net Worth:** Total Assets - Total Liabilities
- **Debt-to-Income Ratio:** Total Liabilities / Annual Income
- **Property Value:** Properties Owned × Average Property Value ($4M)
- **Total Assets:** Sum of all deposit accounts + Property Value
- **Income Band:** Low (<$100K) | Mid ($100K-$300K) | High (>$300K)
- **Age Groups:** 17-21, 22-34, 35-44, 45-54, 55-64, 65+

---

## 🏗️ Architecture & Workflow

```
┌─────────────────────────────────────────────────────────────────────┐
│                         DATA PIPELINE ARCHITECTURE                   │
└─────────────────────────────────────────────────────────────────────┘

📥 DATA INGESTION
   │
   ├─► Raw CSV Data
   │      │
   │      └─► Python Ingestion Script (SQLAlchemy)
   │             │
   │             └─► PostgreSQL Database (Raw Layer)
   │
   ▼
🧹 DATA PROCESSING
   │
   ├─► Python + Pandas
   │      │
   │      ├─► Data Cleaning
   │      │      • Handle missing values
   │      │      • Remove duplicates
   │      │      • Standardize formats
   │      │
   │      ├─► Feature Engineering
   │      │      • Calculate Net Worth
   │      │      • Derive Debt-to-Income Ratio
   │      │      • Create Age Groups & Income Bands
   │      │      • Compute Property Values
   │      │
   │      └─► Exploratory Data Analysis
   │             • Univariate/Bivariate Analysis
   │             • Correlation Analysis
   │             • Distribution Analysis
   │             • Outlier Detection
   │
   ├─► PostgreSQL (Cleaned Layer)
   │      │
   │      └─► Structured Tables Ready for BI
   │
   ▼
📊 VISUALIZATION & INSIGHTS
   │
   └─► Power BI Dashboard
```

---

## 🛠️ Tools & Technologies

### Data Engineering Stack
| Tool | Purpose | Version |
|------|---------|---------|
| **Python** | Data processing, ETL, analysis | 3.9+ |
| **PostgreSQL** | Relational database for structured storage | 13+ |
| **SQLAlchemy** | Python-PostgreSQL ORM connector | 1.4+ |
| **Pandas** | Data manipulation and transformation | 1.5+ |
| **NumPy** | Numerical computations | 1.23+ |

### Analytics & Visualization
| Tool | Purpose |
|------|---------|
| **Jupyter Notebook** | Interactive EDA and documentation |
| **Matplotlib/Seaborn** | Statistical visualizations |
| **Power BI** | Interactive business intelligence dashboard |

### Development Environment
- **IDE:** Jupyter Lab
- **Version Control:** Git/GitHub
- **Database Client:** pgAdmin 4

---

## 🔬 EDA & Feature Engineering

### Data Cleaning Operations
1. **Missing Value Treatment**
   - Identified and imputed missing values using domain-appropriate strategies
   - Validated data completeness across all 18 features

2. **Data Type Standardization**
   - Converted financial columns to appropriate numeric types
   - Standardized date formats and categorical encodings

3. **Outlier Detection**
   - Identified 408 customers with **negative net worth** (debt-heavy profiles)
   - Flagged extreme debt-to-income ratios for risk management

### Feature Engineering Highlights

#### 1. **Net Worth Calculation**
```python
Net Worth = (Bank Deposits + Checking + Savings + Foreign Currency + 
             Superannuation + Property Value) - 
            (Bank Loans + Credit Card Balance + Business Lending)
```
**Business Value:** Enables wealth-based customer segmentation and personalized advisory services

#### 2. **Debt-to-Income Ratio**
```python
DTI Ratio = Total Liabilities / (Estimated Monthly Income × 12)
```
**Business Value:** Identifies high-risk customers requiring financial counseling (670 flagged)

#### 3. **Property Valuation**
```python
Property Value = Properties Owned × 4,000,000 (avg market value)
```
**Business Value:** Quantifies real estate wealth for mortgage and investment product targeting

#### 4. **Income Segmentation**
- **Low:** < $100,000 annual income
- **Mid:** $100,000 - $300,000
- **High:** > $300,000

**Business Value:** Tailors product offerings and communication strategies by income tier

### Key EDA Insights

#### 📈 Distribution Analysis
- **Right-Skewed Wealth Distribution:** Small segment of high-value clients drives disproportionate share of total assets
- **Middle-Income Dominance:** Majority of customers fall in mid-income band, indicating mass-affluent target market
- **Age-Agnostic Patterns:** Minimal correlation between age and financial metrics (synthetic data characteristic)

#### 🔗 Correlation Insights
| Relationship | Correlation | Business Implication |
|--------------|-------------|---------------------|
| **Net Worth ↔ Properties Owned** | 0.99 | Property ownership is primary wealth driver |
| **Bank Deposits ↔ Checking Accounts** | 0.84 | Strong liquidity management behavior |
| **Income ↔ Debt-to-Income Ratio** | -0.45 | Higher earners manage debt more efficiently |
| **Income ↔ Superannuation** | 0.37 | Wealthy customers prioritize retirement savings |

#### 💡 Behavioral Patterns
- **Loyal Customers:** Maintain lower DTI ratios, indicating financial stability
- **Cross-Sell Gap:** 64% of customers own only 1 credit card despite multi-product relationships
- **Risk Concentration:** 300+ customers exceed healthy DTI thresholds (>40%)

---

## 📊 Dashboard & KPIs

### Power BI Dashboard Components

#### 1. **Executive KPI Scorecard**
| Metric | Value | Business Context |
|--------|-------|-----------------|
| **Total Customers** | 3,000 | Complete customer base coverage |
| **Total Assets** | $22.07B | Total managed wealth |
| **Total Net Worth** | $17.68B | Customer equity after liabilities |
| **Average Net Worth** | $5.89M | Per-customer wealth indicator |
| **High-Risk Customers** | 670 | Require immediate intervention |
| **Avg Products/Customer** | 7.42 | Product penetration rate |

#### 2. **Customer Segmentation Views**

**By Loyalty Tier (Net Worth)**
- 🥇 **Jade:** $7.9B average (ultra-high-net-worth)
- 🥈 **Silver:** $4.5B average (high-net-worth)
- 🥉 **Gold:** $3.3B average (affluent)
- 💎 **Platinum:** $1.9B average (mass-affluent)

**By Banking Relationship**
- **Private Bank:** 33% High | 33% Mid | 34% Low income distribution
- **Retail:** 34% High | 30% Mid | 35% Low
- **Commercial:** 33% High | 36% Mid | 31% Low
- **Institutional:** 32% High | 35% Mid | 33% Low

#### 3. **Risk Management Dashboard**
- **Risk Matrix:** Debt-to-Income vs. Net Worth scatter plot
- **High-Risk Flagging:** 670 customers with DTI > 2.0
- **Risk Distribution:** Color-coded by severity (Low/Mid/High)

#### 4. **Cross-Sell Opportunity Analysis**
- **Credit Card Penetration:**
  - 1 Card: 64.07% (1,922 customers) → **Primary target**
  - 2 Cards: 25.5% (765 customers)
  - 3 Cards: 10.43% (313 customers)
- **Estimated Revenue Opportunity:** $14M+ from upgrading single-card holders

#### 5. **Wealth Distribution Analysis**
- **Net Worth by Property Ownership:**
  - 0 Properties: -$0.1M (renters/debt-heavy)
  - 1 Property: $3.8M
  - 2 Properties: $7.9M
  - 3 Properties: $11.7M (ultra-wealthy segment)

### Interactive Filters
- Gender (Male/Female)
- Age Groups (17-21, 22-34, 35-44, 45-54, 55-64, 65+)
- Bank Type (Commercial, Institutional, Private Bank, Retail)
- Loyalty Classification (Jade, Silver, Gold, Platinum)

---

## 💼 Key Insights & Business Impact

### Strategic Insights

#### 1. **Customer Retention Priority**
**Finding:** Jade tier customers are only 26% of customers but hold about 45% of total assets.

**Action:** These customers should be treated as high priority with better relationship management.

**Impact:** Focusing on this group can help the bank protect a large portion of its total wealth.

---

#### 2. **Cross-Sell Revenue Opportunity**
**Finding:** 64% of customers have only one credit card.

**Action:** These customers can be targeted for additional credit card and banking products.

**Impact:** This shows a strong opportunity to increase revenue from existing customers.

---

#### 3. **Risk Mitigation Strategy**
**Finding:** Identified high-risk customers based on negative net worth and debt-to-income ratio > 2 for proactive financial intervention.

**Action:** These customers should be monitored and supported with better financial planning and risk controls.

**Impact:** Early identification can help reduce future financial risk.
---

#### 4. **Wealth Management Optimization**
**Finding:** Customers owning more properties generally have higher net worth.

**Action:** Property ownership can be used to target customers for wealth management and investment products.

**Impact:** This helps the bank offer more relevant financial services.

---

#### 5. **Resource Allocation Efficiency**
**Finding:** Net worth varies significantly across customers even when revenue is similar.

**Action:** Banking services can be better aligned based on customer value.

**Impact:** This can improve customer experience and service efficiency.

---

## 📂 Project Structure

```
premier-global-bank-analytics/
│
├── data/
│   ├── raw/                          # Original CSV files
│   ├── processed/                    # Cleaned datasets
│   └── schema/                       # Database schema definitions
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb       # PostgreSQL data loading
│   ├── 02_data_cleaning and feature_engineering.ipynb        # Data quality & preprocessing
│   └── 03_exploratory_analysis.ipynb # EDA & insights
│
├── scripts/
│   ├── ingestion_db.py               # Database connection & ETL
│   
│
├── dashboards/
│   ├── bank_customers_analytics.pbix # Power BI dashboard file
│   └── dashboard_screenshot.png      # Dashboard preview
│
│
├── requirements.txt                  # Python dependencies
├── README.md                         # Project documentation
└── LICENSE                           # MIT License

```
## 📜 License

This project is licensed under the MIT License.

---

## 👤 Author

**Paridhi Singh**  

---

## 🙏 Acknowledgments

- Premier Global Bank (fictional case study)
- Open-source community for Python, PostgreSQL, and Power BI tools

---

**⭐ If you found this project valuable, please consider starring the repository!**


# 🛍️ Amazon Sales Data Analysis

A complete exploratory data analysis (EDA) and visualization project built with Python and Pandas, based on a publicly available Amazon Sales dataset. This project simulates a real-world analytics request: surfacing revenue drivers, discount effectiveness, and customer sentiment trends, visual storytelling — designed for business owners, e-commerce analysts, and early-stage founders seeking better data-driven decision-making. 

---

## 📌 Objective

To extract, analyze, and visualize insights from Amazon product sales data, focusing on pricing strategies, discount structures, and customer sentiment — providing clear, data-driven insights that can guide e-commerce strategy.
---

## 📊 Dataset Overview

- **Source:** [Amazon Sales Dataset on Kaggle](https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset)
- **Size:** ~17,000 records
- **Features include:** 
- Product details: product_name, category, about_product, img_linK
- Pricing & discounts: actual_price, discounted_price, discount_percentage, price_difference, discount_ratio, ultra_discount, price_tier, discount_tier.
- Customer feedback: rating, rating_count, review_title, review_content, customer_sentiment, pos_word, neg_word
- Identifiers: review_id, user_name
---

## 🧰 Tools & Technologies

| Purpose              | Tools/Frameworks Used             |
|----------------------|-----------------------------------|
| Data Manipulation    | `pandas`, `numpy`                 |
| Data Visualization   | `matplotlib`, `seaborn`, `plotly`|
| Notebook Interface   | `Jupyter Notebook`                |
| Environment Management | `virtualenv` / `venv`             |
| Version Control      | `Git`, `GitHub`                   |

---

## 🔍 Analysis Highlights

- ✅ Top-selling & underperforming categories (by ratings, rating count & sentiment)
- ✅ Price tier analysis — which tiers capture the highest satisfaction and engagement
- ✅ Discount effectiveness — do deeper discounts correlate with higher ratings or better sentiment?
- ✅ Customer sentiment vs. rating alignment — does textual sentiment reflect the numeric score?
- ✅ “Ultra-discount” products deep dive — who uses this lever effectively?
- ✅ Sentiment drivers — positive/negative keyword patterns in reviews
---

## 📈 Key Visuals

- Bar plots of top categories by rating count
- Distribution plots of discounts across categories
- Sentiment breakdown (positive, negative, mixed)
- Heatmap of discount tiers vs customer sentiment
- Boxplot: actual vs discounted prices by category
- Word cloud (optional) for most common positive/negative review terms
---

## 🧠 Insights & Business Use-Cases

| Insight                                  | Value for Client                                    |
|------------------------------------------|-----------------------------------------------------|
| Which categories dominate customer attention (ratings + reviews)?    | Helps allocate marketing budget and optimize inventory.   |
| How do discount tiers impact customer satisfaction?     | Guides pricing & promotional strategies.        |
| Are high discounts always linked to better reviews?       | Identifies when discounting is wasteful vs effective.    |
| Which products underperform despite high discounts?    | Flags inefficiencies in pricing strategy.| 
| What words/phrases define positive vs negative experiences?	 | Helps in branding, ad copy, and product description tuning.|


---

## 🚀 How to Run

1. Clone the repository  
   ```bash
   git clone https://github.com/CKohwo/amazon-sales-analysis.git
   cd amazon-sales-analysis

2. Set up a virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt

3. Launch jupyter notebook
   jupyter notebook 

---

## 🧾 Deliverables
- Clean and annotated Jupyter Notebook (.ipynb)

- CSV-cleaned dataset (with engineered features, such as - price_tier, discount_tier, customer_sentiment)

- Static charts exported as .png

- Optional report PDF (for client-ready submission)

- Executive summary of insights in notebook or PDF

- GitHub repository with reproducible code
  
---

📄 Project Status
✅ Completed initial data wrangling
✅ Visualizations and dashboards finalized
🔄 Currently drafting an executive summary for business users

---

🚀 **Roadmap**

- V1.0 (Current): Exploratory analysis + business insights

- V1.1: Convert to interactive dashboard (Streamlit/Dash)

- V2.0: Automate data ingestion + reporting pipelines
---

🧑‍💼 About the Developer
Charles – Mechanical Engineer, Data Scientist & python developer focused on turning raw data into clear, actionable business intelligence.

📫 LinkedIn

💼 Portfolio (Coming Soon)

🧠 Changing the world through mastery in Python + Data Science + Algorithmic thinking

---

📜 License
This project is licensed under the MIT License. See the LICENSE file for more information.

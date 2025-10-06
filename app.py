import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
  
# ==============================
# Page Config
# ==============================
st.set_page_config(
    page_title="E-commerce Growth Dashboard",
    page_icon="📈",
    layout="wide"
)
st.title("E-commerce Growth Dashboard 📈")
st.subheader("A strategic growth blueprint for Ecommerce Business")
st.write("""
        In the hyper-competitive e-commerce landscape, growth is not achieved by chance. It is the result of strategic, data informed decisions.
        This project introduces a reusable **Analytical Blueprint** to solve critical e-commerce challenges by answering three fundamental questions:
         
        • Which brands are truly driving value versus just volume?
        • Where should we focus our inventory and marketing resources?
        • Is our pricing and discount strategy building loyalty or eroding trust?
         
        The real competitive edge lies in data-driven strategy, the ability to see patterns hidden beneath sales numbers.
        """)
         
# This saves the data in cache to avoid reloading it every time the app runs
@st.cache_data
def load_data():
    df = pd.read_csv("data/cleaned_data/cleaned_data_2.csv")
    return df
# Load the data
df = load_data()
with st.expander("click here more details"):
    st.dataframe(df)  

#Saving the load data function output of brands_satisfaction to a variable and loading it          
@st.cache_data
def load_brand_satisfaction():
    brand_satisfaction = pd.read_csv("data/processed_data/Top_satisfied_brands.csv") # For now, we'll keep using this CSV
    return brand_satisfaction
# load the data
brand_satisfaction = load_brand_satisfaction()

#Saving the load data function output of brand_sentiment to a variable and loading it
@st.cache_data
def load_brand_sentiment():
    brand_sentiment = pd.read_csv("data/processed_data/brands_sentiment.csv") 
    return brand_sentiment
# Load the data
brand_sentiment = load_brand_sentiment()

#Saving the load data function output of category_sentiment to a variable and loading it
@st.cache_data
def load_category_sentiment():
    category_sentiment = pd.read_csv("data/processed_data/category_sentiment.csv") 
    return category_sentiment       
# Load the data
category_sentiment = load_category_sentiment()

# Saving the load data function output of price_sentiment to a variable and loading it
@st.cache_data
def load_price_sentiment():
    return pd.read_csv("data/processed_data/price_sentiment.csv")
price_sentiment = load_price_sentiment()

# Saving the load data function output of discount_sentiment to a variable and loading it
@st.cache_data
def load_discount_sentiment():
    return pd.read_csv("data/processed_data/discount_sentiment.csv")
discount_sentiment = load_discount_sentiment()

# Saving the load data function output of ultra_disc to a variable and loading it
@st.cache_data
def load_ultra_discount():
    return pd.read_csv("data/processed_data/ultra_disc_summary.csv")
ultra_disc = load_ultra_discount()


# ==============================
st.markdown("---")
# ==============================
# KPI Cards (Top Row)
# ==============================
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Reviews", f"{df['rating_count'].sum():,}")
col2.metric("Average Rating", round(df['rating'].mean(), 2))
col3.metric("Avg Discount %", f"{df['discount_percentage_num'].mean():.1f}%")
col4.metric("Brands Covered", df['brands'].nunique())
col5.metric("Categories Covered", df['category'].nunique())

st.markdown("---")
  
# ==============================
# Sidebar - User Input Features
# ==============================
brand_tab, category_tab, price_tab, ultra_tab = st.tabs([
    "📊 Brand Performance",
    "📦 Category Insights",
    "💸 Price & Discount Analysis",
    "⚠️ Ultra Discount Analysis"
])                    

# This displays Brand Performance sections based on user selection
with brand_tab:
    st.subheader("BRANDS PERFORMANCE") 
    st.markdown("Use the controls below to analyze brand performance based on customer ratings and satisfaction.")

    # --- Interactive Controls in the slider --- 
    min_reviews = st.slider(
        "Minimum number of reviews for a brand:",
        min_value=20,
        max_value=50000,  
        value=1000,  # Default value
        step=100,
        help="Filters out brands with fewer than this many reviews to reduce noise."
    )

    # ------------------------
    #Brands average rating 
    # ------------------------ 
    col1, col2 = st.columns([2, 1])   
    brands = (df.groupby("brands")
            .agg(avg_rating=("rating", "mean"),total_reviews=("rating_count", "sum"))
            .query(f"total_reviews >= {min_reviews}").reset_index())           
    brands["rating_index"] = (brands["avg_rating"] * np.log1p(brands["total_reviews"]))
    brands = brands.sort_values("rating_index", ascending=False).reset_index(drop=True)
    
    # Brands average rating vs review count
    with col1:
        fig = px.scatter(
                brands,
                x='total_reviews',
                y='avg_rating',
                size='total_reviews',  # Size of bubble represents review volume
                color='avg_rating',    # Color represents rating
                hover_name='brands',   # What to show on hover
                log_x=True,            # Use a log scale for better visualization of volume
                size_max=60,
                title="Brand Performance: Rating vs. Review Volume (Log Scale)",
                labels={'total_reviews': 'Total Reviews (Log Scale)', 'avg_rating': 'Average Rating'}
            )
        fig.update_layout(height=600) # Make the plot taller
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Brand Data Summary") 
        st.info("Displaying the Top Brands with more than {} reviews".format(min_reviews))  
        st.dataframe(brands) 

    st.info("""
    **Insight:** While most brands cluster around moderate satisfaction levels, 
    brands with high review volume but low satisfaction ratios represent 
    a *strategic risk*. These are likely overexposed in the marketplace and 
    may drive negative sentiment if not quality-controlled. 
    Brands in the top-right quadrant of the scatter plot (high reviews + high ratings) 
    are your 'Sustained Growth Champions'.
    """)
        
    #---------------------------------------------------- 
    # Weighted satisfaction score comparison across brands
    #----------------------------------------------------
    # Multiselect for brands
    selected_brands = st.multiselect(
        "Select brands to compare satisfaction scores:",
        options=brand_satisfaction['brands'].unique(),
        default=['AmazonBasics', 'pTron', 'Duracell', 'boAt', 'Samsung'] # Sensible defaults
    )

    if selected_brands:
        brands_satisfaction = brand_satisfaction[brand_satisfaction['brands'].isin(selected_brands)]
        
        fig2 = px.bar(
            brands_satisfaction,
            x='brands',
            y='weighted_satisfaction_score',
            color='brands',
            title='Comparison of Weighted Satisfaction Scores',
            labels={'weighted_satisfaction_score': 'Weighted Satisfaction Score', 'brands': 'Brand'}
        )
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.warning("Please select at least one brand to display the chart.")
    st.info("""
    **Insight:** Brands like `AmazonBasics` and `pTron` are clear 'Customer Champions' with exceptionally high satisfaction scores. While `boAt` is a volume leader, its satisfaction score is comparatively average. This highlights the need to partner with and promote high-satisfaction brands to build a reputation for quality.
    """)
# --------------------------------------------------
# Customer satisfaction rate vs dissatisfaction rate
# --------------------------------------------------
    st.subheader("Customer Satisfaction Rate vs Dissatisfaction Rate")
    if st.checkbox("Show detailed customer satisfaction/dissatisfaction bar chart"):
        brands_sentiment = brand_sentiment.head(30)
    
    # Create a bar chart
        fig = px.bar(
            brands_sentiment,
            x= ["satisfied_%", "dissatisfied_%"],
            y='brands',
            title='Top 30 Brands by Satisfaction x Dissatisfaction Rate',
            labels={'value': 'Percentage (%)', 'brands': 'Brand'},
            barmode='group',
            orientation='h', # Horizontal bar chart is better for long labels
            height=800
        )
        st.plotly_chart(fig, use_container_width=True)

    st.info("""
    **Insight:** This chart reveals brand perception.
    * **High Satisfaction, Low Dissatisfaction** (e.g., `pTron`, `Duracell`): These are your safest bets and "Customer Champions." They consistently delight customers.
    * **Low Satisfaction** (e.g., `Samsung`, `OnePlus`): These brands show a concerning gap between brand recognition and customer experience on the platform. This warrants a review of the products being sold.
    """)
# ==============================
# Category Insights
# ==============================     
with category_tab:
    st.subheader("CATEGORY INSIGHTS") 
    st.markdown("Category, average ratings & total reviews in respect to their rating_index")
 
    # ------------------------
    #Category average rating 
    # ------------------------ 
    col3, col4 = st.columns([2,1])
    category_ratings = (df.groupby("category")
            .agg(avg_rating=("rating", "mean"),total_reviews=("rating_count", "sum"))
            .query("total_reviews >= 100").reset_index())           
    category_ratings["rating_index"] = (category_ratings["avg_rating"] * np.log1p(category_ratings["total_reviews"]))
    category_ratings = category_ratings.sort_values("rating_index", ascending=False).reset_index(drop=True)
    
    with col3:
        # Category average rating vs review count
        fig = px.scatter(
                category_ratings,
                x='total_reviews',
                y='avg_rating',
                size='total_reviews',  # Size of bubble represents review volume
                color='avg_rating',    # Color represents rating
                hover_name='category',   # What to show on hover
                log_x=True,            # Use a log scale for better visualization of volume
                size_max=60,
                title="Category Insights: Rating vs. Review Volume (Log Scale)",
                labels={'total_reviews': 'Total Reviews (Log Scale)', 'avg_rating': 'Average Rating'}
            )
        fig.update_layout(height=600) # Make the plot taller
        st.plotly_chart(fig, use_container_width=True)
       
    with col4:
        st.subheader("Category Data Summary") 
        st.dataframe(category_ratings)
        st.info("Display of the Top Categories with more than 100 reviews")  

    st.info("""
    **Insight:** Not all categories perform equally.
    * `Electronics` is the undisputed **Volume King**, driving the most reviews. However, its average rating is mediocre, making it a **High-Risk, High-Reward** category.
    * `Computers & Accessories` and `Home & Kitchen` are the **Stable Pillars** of the business, showing a healthy balance of high review volume and strong average ratings.
    * `Office Products` is a **Hidden Gem**, with the highest average rating, indicating a highly satisfied customer base that could be targeted for growth.
    """)    
        
    #----------------------------------------------------
    # INSIGHTFUL TREEMAP: CATEGORY VOLUME VS. SATISFACTION
    #----------------------------------------------------
    st.subheader("Category Sentiment Analysis by Treemap")

    # Create the treemap
    fig_treemap = px.treemap(
        category_sentiment,
        # The path defines the hierarchy. Here, we just have one level: category.
        path=[px.Constant("All Categories"), 'category'],
        
        # 'values' determines the SIZE of the boxes. We'll use total sentiment count.
        values='total_sentiment',
        
        # 'color' determines the SHADE of the boxes. We'll use the satisfaction percentage.
        # This is powerful: SIZE = Volume, COLOR = Quality.
        color='satisfied_%',
        
        # hover_data shows extra info when you mouse over a box.
        hover_data=['total_satisfied', 'total_dissatisfied', 'dissatisfied_%'],
        
        # Configure the color scale
        color_continuous_scale ='RdYlGn',

        title='Customer Sentiment Analysis per Each Category'
    )

    fig_treemap.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    st.plotly_chart(fig_treemap, use_container_width=True)

    st.info("""
    **How to read this treemap:**
    * **Size of the Box:** Represents the total number of reviews (volume) for that category.
    * **Color of the Box:** Represents the customer satisfaction percentage (quality). Greener is better.
    """)

# ==============================
# Price & Discount Analysis 
# ==============================
with price_tab:
    st.subheader("PRICE & DISCOUNT ANALYSIS")

    #-----------------
    # Price tier summary
    #------------------ 
    price_summary = pd.read_csv("data/processed_data/price_rating.csv")
    st.subheader("Price Tier Summary")
    st.dataframe(price_summary)

    #---------------
    # Satisfactory rates across price tiers
    #---------------
    # Load the data
    price_sentiment = price_sentiment.sort_values('satisfactory_score', ascending=False) # Good practice to sort

    fig_bar = px.bar(
    price_sentiment,
    x='price_tier',
    y='satisfactory_score',
    color='price_tier',
    title='Satisfaction Score Across Price Tier',
    labels={'satisfactory_score': 'Weighted Satisfaction Score', 'price_tier': 'Price Tier'},
    text='satisfactory_score' # Adds the value label on top of the bar
    )

    # Improve the look of the value labels
    fig_bar.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig_bar.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig_bar, use_container_width=True)
    st.info("""
    **Insight:** The data challenges the assumption that "expensive means better." The **Low Price Tier** significantly outperforms others in customer satisfaction. This suggests customers on the platform are highly value-conscious and are most satisfied when they find quality products at an affordable price point.
    """)

    #----------------------
    # Disocunt tier summary
    #----------------------
    discount = pd.read_csv("data/processed_data/discount_rating.csv")
    st.subheader("Discount Tier Summary")
    st.dataframe(discount)

    #---------------
    # Satisfactory rates across discount tiers
    #---------------
    # Load the data
    discount_sentiment = discount_sentiment.sort_values('satisfactory_score', ascending=False) # Good practice to sort

    fig_bar = px.bar(
    discount_sentiment,
    x='discount_tier',
    y='satisfactory_score',
    color='discount_tier',
    title='Satisfaction Score Across Discount Tier',
    labels={'satisfactory_score': 'Weighted Satisfaction Score', 'Discount_Tier': 'Discount Tier'},
    text='satisfactory_score' # Adds the value label on top of the bar
    )

    # Improve the look of the value labels
    fig_bar.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig_bar.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig_bar, use_container_width=True)
    st.info("""
    **Insight:** This chart confirms the **Discount Ineffectiveness** theory. The 'High' discount tier (>70% off) provides no significant satisfaction benefit over the 'Mid' tier. This suggests that deep, blanket discounts may be an inefficient use of marketing budget, eroding margins without building customer loyalty.
    """)
# ==============================
# Ultra Discount Analysis   
# ==============================
with ultra_tab:
    st.subheader("ULTRA_DISCOUNT ANALYSIS")
    st.dataframe(ultra_disc)

    st.info("""
            The dataframe contains brands that implemented discounts of >90%. 
            As you might observe from the data, only two brands implemented such absurd discounts. 
            This forces me to believe that the ultra_discount model is a rare one and only used to clear warehouses and not a promotional/marketing strategy
    """)  


st.markdown("---")
st.caption("Built by Charles Onokohwomo — Data Strategist & Engineer | [GitHub](https://github.com/CKohwo) | [LinkedIn](www.linkedin.com/in/charles-onokohwomo)") 
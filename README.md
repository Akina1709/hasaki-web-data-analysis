# hasaki-web-data-analysis
This repository contains the code and analysis for scraping and analyzing data from the HASAKI e-commerce website.

## Steps Taken:

- **Data Scraping**: Data was scraped from the [HASAKI website](https://hasaki.vn/danh-muc/suc-khoe-lam-dep-c3.html) using Python with the BeautifulSoup library. The scraped data is stored in a CSV file [here](https://github.com/Akina1709/hasaki-web-data-analysis/blob/main/Data_hasaki_web/dataset_hasaki.csv), including features such as Brands (suppliers/manufacturers), Description (product name), New Price, Discount Percentage, and Old Price.

- **Data Cleaning in Power BI**:
  + Removed "đ" character from **New Price** and **Old Price** columns.
  + Removed "." from **New Price** and **Old Price** columns and converted them to decimal number data type.
  + Converted rows with "not available" to 0% for **Discount Percentage** and **Old Price** columns.
  + Removed duplicates in the **Description** column, resulting in 7304 rows.

- **Data Visualization**:
  + Counted the number of suppliers/manufacturers, products, discounted products, and non-discounted products.
  + Filtered the Top 10 products with the highest discounts.
  + Filtered the top 5 products with the highest prices.
  + Counted the number of products by supplier.

![Fig-1]([https://drive.google.com/uc?export=view&id=18TowsiXNOOymPl-U9p__qnMfhJc916lZ](https://github.com/Akina1709/hasaki-web-data-analysis/blob/main/visualize_hasaki_web.png)https://github.com/Akina1709/hasaki-web-data-analysis/blob/main/visualize_hasaki_web.png)
*<center>Dataset Hasaki Visualization</center>*

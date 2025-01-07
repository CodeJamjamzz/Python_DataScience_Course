# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values('date')

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1['cum_weekly_sales'] = sales_1_1['weekly_sales'].cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1['cum_max_sales'] = sales_1_1['weekly_sales'].cummax()

# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])

# Here’s a list of summary statistics methods in pandas:
# .count()
# .mean()
# .median()
# .mode()
# .std()
# .var()
# .min()
# .max()
# .sum()
# .cumsum()
# .cumprod()
# .quantile()
# .skew()
# .kurt()
# .describe()
# .corr()
# .cov()
# .agg() (for custom aggregation functions)
# .apply() (for custom functions on columns/rows)

# sales.drop_duplicates(subset=['store', 'type'])
# store_depts['department'].value_counts(sort=True, normalize=True)
# sales_by_type = sales.groupby("type")["weekly_sales"].sum()
# unemp_fuel_stats = sales.groupby('type')[['unemployment', 'fuel_price_usd_per_l']].agg([min, max, np.mean, np.median])
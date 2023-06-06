import pandas as pd

def group_and_aggregate(df):
    aggregations = {
        'Recency': 'first',
        'Invoice': 'nunique',  # = Order count -> frequency
        'Total': 'sum',  # -> Monetary
        'Quantity': 'sum',  # = Total Quantity
        'Price': 'mean',
        'StockCode': 'nunique',
        'Percent_cancelled': 'first',
        'Average_Quantity': 'first',
        'Order_Quantity': 'mean',  # Average_order_quantity
        'Average_Price': 'first',
        'Average_Basket': 'first',
        'Country': 'first',
        'Flag': 'first',
    }
    df_grouped = df.groupby('Customer ID').agg(aggregations)
    df_grouped_renamed = df_grouped.rename(columns={
        'Invoice': 'Frequency',
        'Total': 'Monetary',
        'Average_Basket': 'Ø_basket',
        'Average_Quantity': 'Ø_Qty',
        'Order_Quantity': 'Ø_InvoiceQty',
        'StockCode': '∃_items',  # ∃ = uniqueness
        'Price': 'Ø_Price',
        'Cancelled_order_count': 'n_Cancelled',
        'Percent_cancelled': '%_Cancelled',
    })
    return df_grouped_renamed

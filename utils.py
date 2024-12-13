import sqlite3 as sql
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def table_schema(connection, table_name) -> None:
    """Prints the schema of a sqlite table.

    Args:
        connection (sqlite3.Connection): The connection to the sqlite database.
        table_name (str): The name of the table to print the schema for.
    """
    query = f"PRAGMA table_info({table_name})"
    table_schema = connection.execute(query).fetchall()
    print(f"Schema for table {table_name}:")
    for col_info in table_schema:
        print(col_info)


def table_head(connection, table_name, n=5) -> None:
    """Prints the first n rows of a table.

    Args:
        connection (sqlite3.Connection): The connection to the sqlite database.
        table_name (str): The name of the table to print the head for.
        n (int, optional): The number of rows to print. Defaults to 5.
    """
    query = f"SELECT * FROM {table_name} LIMIT {n}"
    df = pd.read_sql_query(query, connection)
    print(f"Head of table {table_name}:")
    print(df.head(n))


def detailed_labels(pct, allvals):
    """Return a string with the absolute value and percentage of the total.
    """
    absolute = int(round(pct/100.*sum(allvals)))
    return f"{absolute}\n({pct:.1f}%)"


def two_pie_subplots(df1: pd.DataFrame, df2: pd.DataFrame,
                     title_1: str, title_2: str, color_palette: sns.color_palette) -> None:
    """Create two pie chart subplots with the specified parameters.
    Parameters
    ----------
    df1 : pd.DataFrame
        The first dataframe.
    df2 : pd.DataFrame
        The second dataframe.
    title_1 : str
        The title for the first subplot.
    title_2 : str
        The title for the second subplot.
    color_palette : sns.color_palette :
        The color palette to use for the pie charts.
    Returns
    -------
    None
    """
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    # Chart 1
    axes[0].pie(df1, labels=df1.index,
                    autopct=lambda pct: detailed_labels(pct, df1),
                    startangle=100, colors=color_palette)
    axes[0].set_title(title_1)
    # Chart 2
    axes[1].pie(df2, labels=df2.index,
                    autopct=lambda pct: detailed_labels(pct, df2),
                    startangle=100, colors=color_palette)
    axes[1].set_title(title_2)
    

def pie_chart(df: pd.DataFrame, title: str, color_palette: sns.color_palette) -> None:
    """Create a pie chart with the specified parameters.
    Parameters
    ----------
    df : pd.DataFrame
        The dataframe.
    title : str
        The title for the pie chart.
    color_palette : sns.color_palette
        The color palette to use for the pie chart.
    Returns
    -------
    None
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.pie(df, labels=df.index, autopct=lambda pct: detailed_labels(pct, df),
                    startangle=100, colors=color_palette)
    ax.set_title(title)
    

state_iso_mapping = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
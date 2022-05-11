import pandas as pd

pd.set_option('display.max_columns', None)
global df
df = pd.read_csv("national-budget.csv")


def education_budget(year: int) -> int:
    global df
    return df[(df["שם רמה 2"] == 'חינוך') & (df['שנה'] == year)]["הוצאה נטו"].sum()


def security_budget_ratio(year: int) -> float:
    global df
    return df[(df["שם רמה 2"] == 'בטחון') & (df['שנה'] == year)]["הוצאה נטו"].sum() / df[(df['שנה'] == year)][
        "הוצאה נטו"].sum()


def largest_budget_year(office: str) -> int:
    global df
    max_sum = 0.
    max_year = 0.
    for year in df['שנה'].unique():
        sum = df[(df['שנה'] == year) & (df["שם רמה 2"] == office)]["הוצאה נטו"].sum()
        if sum > max_sum:
            max_sum = sum
            max_year = year
    return max_year


# how much did a given department spend abroad over years
def spending_abroad(office: str) -> int:
    global df
    return df[(df["שם רמה 2"] == office) & (df["שם מיון רמה 2"] == 'קניות בחו"ל')]['הוצאה נטו'].sum()


if __name__ == '__main__':
    print(f'education budget in 2000: {education_budget(2000)}\n --------------------------------------')
    print(f'security budget ratio in 2000: {security_budget_ratio(2000)}\n --------------------------------------')
    print(f'security largest budget year: {largest_budget_year("בטחון")}\n --------------------------------------')
    print(f'security spending abroad: {spending_abroad("בטחון")}\n --------------------------------------')

import pandas as pd

df = pd.DataFrame({
    "Roll No": [1, 1, 2, 2, 1, 2],
    "Subject": ["DS", "Java", "DS", "Java", "DS", "Java"],
    "Marks": [25, 40, 30, 26, 40, 50],
    "Date": ["01-01-23", "02-01-23", "01-01-23",
             "02-01-23", "15-01-23", "15-01-23"]
})

print(df)


df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%y")

df = df.sort_values(
    ["Roll No", "Subject", "Date"],
    ascending=[True, True, False]
)

result = []

for (roll, subject), group in df.groupby(["Roll No", "Subject"]):

    marks = group["Marks"].tolist()
    dates = group["Date"].tolist()

    m1 = marks[0] if len(marks) > 0 else 0
    m2 = marks[1] if len(marks) > 1 else 0
    m3 = marks[2] if len(marks) > 2 else 0

    latest_date = dates[0]

    result.append([
        roll,
        subject,
        m1,
        m2,
        m3,
        latest_date
    ])

result = pd.DataFrame(
    result,
    columns=["Roll No", "Subject", "M1", "M2", "M3", "Date"]
)

result["Date"] = result["Date"].dt.strftime("%d-%m-%y")

print(result)
import pandas as pd
import matplotlib.pyplot as plt
import io
from google.colab import files


uploaded = files.upload()


filename = list(uploaded.keys())[0]
df = pd.read_csv(io.BytesIO(uploaded[filename]))


df = df.dropna(subset=['Sex', 'COVID-19 Deaths'])


deaths_by_sex = df.groupby('Sex')['COVID-19 Deaths'].sum()


print("\nعدد الوفيات حسب الجنس:")
print(deaths_by_sex)


if 'Male' in deaths_by_sex.index and 'Female' in deaths_by_sex.index:
    male_deaths = deaths_by_sex['Male']
    female_deaths = deaths_by_sex['Female']
    percentage_difference = ((male_deaths - female_deaths) / female_deaths) * 100
    
    print(f"\n📊 الفرق بالنسبة المئوية:")
    if percentage_difference > 0:
        print(f"عدد وفيات الذكور أعلى من الإناث بنسبة {percentage_difference:.2f}%")
    else:
        print(f"عدد وفيات الإناث أعلى من الذكور بنسبة {abs(percentage_difference):.2f}%")
else:
    print("\n⚠️ البيانات غير مكتملة (لا توجد معلومات كافية عن كلا الجنسين).")


plt.figure(figsize=(6,4))
colors = ['pink', 'lightblue', 'gray']
deaths_by_sex.plot(kind='bar', color=colors)
plt.title('عدد وفيات COVID-19 حسب الجنس')
plt.ylabel('عدد الوفيات')
plt.xlabel('الجنس')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
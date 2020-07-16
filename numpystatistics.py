import codecademylib
import numpy as np

calorie_stats = np.genfromtxt('cereal.csv',delimiter=",")

avarage_calories = np.mean(calorie_stats)
calorie_stats_sorted = np.sort(calorie_stats)
print(avarage_calories)
print(calorie_stats_sorted)

median_calories = np.median(calorie_stats)
print(median_calories)

print(np.percentile(calorie_stats,25))
print(np.percentile(calorie_stats,10))
print(np.percentile(calorie_stats,5))
print(np.percentile(calorie_stats,2))

nth_percentile = np.percentile(calorie_stats,5)
calorie_std = np.std(calorie_stats)
print(calorie_std)

# Most of the Producs are clustered around 100 Calories. We can also understand it from standard dviation that datas are spread around median(106.88) 19.35 below or above. Yummy's Corp can market its product as most healthies option. %95 of the products has more 60 calrie per serving which put YummyCopr's product in %5 niche area.

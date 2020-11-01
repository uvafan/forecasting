START_RATIO = .01
NORMAL_RATIO = .055
START_NUMBER = 500
NORMAL_NUMBER = 3000
MONTHS_TO_RETURN_TO_NORMAL = 6

overall_visas = 0
overall_chinese_visas = 0

for month in range(12):
    if month > MONTHS_TO_RETURN_TO_NORMAL:
        ratio = NORMAL_RATIO
        visas = NORMAL_NUMBER
    else:
        ratio = NORMAL_RATIO * (month / MONTHS_TO_RETURN_TO_NORMAL) + START_RATIO * ((MONTHS_TO_RETURN_TO_NORMAL - month) / MONTHS_TO_RETURN_TO_NORMAL)
        visas = NORMAL_NUMBER * (month / MONTHS_TO_RETURN_TO_NORMAL) + START_NUMBER * ((MONTHS_TO_RETURN_TO_NORMAL - month) / MONTHS_TO_RETURN_TO_NORMAL)

    overall_visas += visas
    overall_chinese_visas += visas * ratio

print(f'{overall_chinese_visas}/{overall_visas}={overall_chinese_visas/overall_visas}')

import numpy as np
import pandas as pd
from scipy import stats

def stat_test_2series(series_1, series_2, independent=True, p_value=0.05):
    s_total = pd.concat([series_1, series_2])
    
    if not independent:
        if series_1.shape[0] != series_2.shape[0]:
            independent = True
            
    shapiro = stats.shapiro(s_total)
    print('Результат теста Шапиро:')
    print(shapiro)
    if shapiro.pvalue > p_value:
        print('Распределение принято нормальным')
        if independent:
            leven = stats.levene(series_1, series_2)
            print('\t Результат теста Левена:')
            print('\t', leven)
            if leven.pvalue > p_value:
                print('\t Дисперсии выборок приняты равными')
                ttest = stats.ttest_ind(series_1, series_2)
                print('\t \t Т критерий Стюдента:')
                print('\t \t', ttest)      
                if ttest.pvalue > p_value:
                    print('\t \t Результат: распределения приняты равными')
                else:
                    print('\t \t Результат: распределения приняты НЕ равными')
            else:
                print('\t Дисперсии выборок НЕ приняты равными')
                uelch = stats.ttest_ind(series_1, series_2, equal_var=False)
                print('\t \t Критерий Уэлча:')
                print('\t \t', uelch)      
                if uelch.pvalue > p_value:
                    print('\t \t Результат: распределения приняты равными')
                else:
                    print('\t \t Результат: распределения приняты НЕ равными')
        else:
            tt_rel = stats.ttest_rel(series_1, series_2)
            print('\t Результат парного Т-теста:')
            print('\t', tt_rel)
            if tt_rel.pvalue > p_value:
                print('\t Результат: распределения приняты равными')
            else:
                print('\t Результат: распределения приняты НЕ равными')
    else:
        print('Распределение не принято нормальным')
        if independent:
            mann_wh = stats.mannwhitneyu(series_1, series_2)
            print('\t Результат теста Манна-Уитни:')
            print('\t', mann_wh)
            if mann_wh.pvalue > p_value:
                print('\t Результат: распределения приняты равными')
            else:
                print('\t Результат: распределения приняты НЕ равными')
        else:
            wilcxn = stats.wilcoxon(series_1, series_2)
            print('\t Результат теста Вилкоксона:')
            print('\t', wilcxn)
            if wilcxn.pvalue > p_value:
                print('\t Результат: распределения приняты равными')
            else:
                print('\t Результат: распределения приняты НЕ равными')
        
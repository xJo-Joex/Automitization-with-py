import calendar
from pathlib import Path

meses_ano = list(calendar.month_name[1:])
dias_semana = ['Dia 1', 'Dia 2', 'Dia 3']

for i, mes in enumerate(meses_ano):
    for dia in dias_semana:
        Path(f'2022/{i + 1}.{mes}/{dia}').mkdir(parents=True, exist_ok=True)

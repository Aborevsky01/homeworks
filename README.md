# Bioinfo Joins Pipeline

Контейнер выполняет 4 типа объединения (joins) по трём CSV-таблицам:
- sample_metadata.csv
- mass_spec_results.csv
- quality_data.csv

## Инструкции
1. Установить Docker
2. Для генерации входных данных:
   ```bash
   python3 generate_data.py
   ```
3. Собрать образ:
   ```bash
   docker build -t bioinfo-joins .
   ```
4. Выполнить join-процедуры и получить результат:
   ```bash
   ./run.sh
   ```

## Описание входных файлов
- `sample_metadata.csv`: образцы, пациенты, дата, тип, возраст, пол, диагноз
- `mass_spec_results.csv`: образец, белок, интенсивность, mz, время, пептиды, score
- `quality_data.csv`: образец, pH, температура, контаминация, дни, итог, целостность

## Результат
Четыре файла с объединениями в папке output:
- inner_join.csv
- left_join.csv
- right_join.csv
- outer_join.csv

Каждый шаг логируется в консоль.

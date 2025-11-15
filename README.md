Це проста Python утиліта для читання CSV-файлів, упакована в Docker.

## 🚀 Запуск

### 1. Підготовка файлу
Створіть CSV-файл:
echo "name,age" > data.csv
echo "Tom,22" >> data.csv
echo "Alice,19" >> data.csv

### 2. Запуск контейнера
docker run -e CSV_FILE=data.csv -v "$($pwd.Path):/app" mycsvtool:1.0



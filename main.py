
from time import sleep, time
import threading

def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)  # Пауза 0.1 секунды
    print(f"Завершилась запись в файл {file_name}")

# Измеряем время выполнения записи в файлы
start_time = time()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
end_time = time()
print(f"Работа функций {end_time - start_time:.6f} секунд")

# Функция для потока
def threaded_write_words(word_count, file_name):
    write_words(word_count, file_name)

# Создание и запуск потоков
threads = []
start_time_threads = time()

thread_args = [
    (10, "example5.txt"),
    (30, "example6.txt"),
    (200, "example7.txt"),
    (100, "example8.txt"),
]

for args in thread_args:
    thread = threading.Thread(target=threaded_write_words, args=args)
    threads.append(thread)
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

end_time_threads = time()
print(f"Работа потоков {end_time_threads - start_time_threads:.6f} секунд")



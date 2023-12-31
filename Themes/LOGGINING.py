# LOGGING - РАБОТАЕТ КАК ПРИНТ, ПОКАЗЫВАЕТ НАШИ НЕДОЧЁТЫ ПО ТИПУ - ОШИБОК
# ЕСТЬ 3 СТАДИИ СЕРЕЗНОСТИ ОШИБКИ
# DEBUG - ОШИБКА В КОДЕ - МОЖНО НЕ ОБРАЩАТЬ ВНИМАНИЕ
# INFO - ДАЕТ ИНФОРМАЦИЮ - ПРИМЕР: КЛИЕНТ ПОСЕТИЛ СТРАНИЦУ - ПРИМЕР КЛИЕНТ ВОШЕЛ В СИСТЕМУ КОТОРЫЙ НЕ ДОЛЖЕН БЫЛ ТАМ НАХОДИТЬСЯ
# WARNING - ОШИБКА В КОДЕ - ПРЕДУПРЕЖДЕНИЕ 
# ERROR - САЙТ РАБОТАЕТ БЕЗ НЕГО НО НУЖНО УСТРОНИТЬ НЕПОЛАДКИ
# CRITICAL - НЕ СМОЖЕТ ПРОДОЛЖИТЬ СВОЮ РАБОТУ ЕСЛИ НЕ ИСПРАВИТЬ ОШИБКУ

# 1. DEBUG (отладка): Сообщения уровня DEBUG используются для вывода детальной информации о ходе выполнения программы.
# Они обычно используются во время разработки и отладки приложения для обнаружения ошибок.

# 2. INFO (информация): Сообщения уровня INFO обычно предоставляют информацию о ходе выполнения программы.
# Они могут использоваться для отображения значимых событий, таких как запуск или завершение программы, успешное выполнение операций и прочее.

# 3. WARNING (предупреждение): Сообщения уровня WARNING предупреждают об возможных проблемах или ситуациях, которые могут потенциально привести к ошибке в будущем. Обычно они используются для выявления непредвиденных условий, но которые не критичны.

# 4. ERROR (ошибка): Сообщения уровня ERROR указывают на фактические ошибки или проблемы в работе приложения, которые требуют вмешательства разработчиков. Программа может продолжить свою работу, но эти ошибки требуют внимания.

# 5. CRITICAL (критическая ошибка): Сообщения уровня CRITICAL указывают на критические ошибки, которые могут привести к непредвиденному завершению программы или серьезным сбоям в работе системы. Требуется срочное вмешательство разработчиков или администраторов.


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# import translator

# q_text = 'какая погода сегодня?'
# print(translators.translate_text(q_text))

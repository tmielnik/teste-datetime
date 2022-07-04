from datetime import datetime

# Obtem a data atual do PC
def get_current_date():
    return datetime.now().strftime('%d/%m/%Y %H:%M:%S')

# Converte a data atual para timestamp
def convert_to_timestamp(date):
    return int(datetime.timestamp(date))

def convert_timestamp_to_date(timestamp):
    return datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y %H:%M:%S")
    
# Exibe a data atual
current_date = get_current_date()
print(f'Data atual: {current_date}')

# Exibe a data atual convertida em timestamp
date_timestamp = convert_to_timestamp(datetime.now())
print(f'Data em timestamp: {date_timestamp}')

# Exibe a data atual convertida de timestamp
print(f'Data convertida de timestamp: {convert_timestamp_to_date(date_timestamp)}')

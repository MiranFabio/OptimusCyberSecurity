# -*- coding: utf-8 -*-
import csv
from collections import defaultdict
from datetime import datetime, time

# --- Para o Curso: O que é Refatoração (Refactoring)? ---
# É o processo de reestruturar o código para melhorar seu design, sem alterar
# seu comportamento externo. Aqui, estamos separando a LÓGICA (encontrar alertas)
# da APRESENTAÇÃO (imprimir na tela). Isso torna nosso código mais limpo,
# reutilizável e, o mais importante, TESTÁVEL.

def analyze_brute_force(reader, failure_threshold=5):
    """Analisa logs para ataques de força bruta e retorna uma lista de alertas."""
    failed_login_counts = defaultdict(int)
    alerts = []
    for row in reader:
        if row['event_type'] == 'login_failed':
            failed_login_counts[row['username']] += 1
    
    for user, count in failed_login_counts.items():
        if count >= failure_threshold:
            alerts.append(f"[ALERTA DE FORÇA BRUTA] Usuário: '{user}', Tentativas: {count}")
    return alerts

def analyze_off_hours_access(reader, start_time=time(22, 0), end_time=time(6, 0)):
    """Analisa logs para acessos fora do horário comercial e retorna uma lista de alertas."""
    alerts = []
    for row in reader:
        login_time_dt = datetime.fromisoformat(row['timestamp'].replace('Z', ''))
        login_time = login_time_dt.time()
        
        is_off_hours = not (start_time <= end_time and start_time <= login_time <= end_time) or \
                       (start_time > end_time and (login_time >= start_time or login_time <= end_time))

        if row['event_type'] == 'login_success' and is_off_hours:
             alerts.append(f"[ALERTA DE HORÁRIO] Usuário: '{row['username']}' logou fora do horário às {login_time}")
    return alerts

def main(log_file_path):
    """Função principal que orquestra a análise e imprime os resultados."""
    print(f"[*] Iniciando análise do arquivo de log: {log_file_path}")
    
    try:
        with open(log_file_path, mode='r', encoding='utf-8') as csvfile:
            # Ler todo o conteúdo para poder passar o leitor para múltiplas funções
            logs = list(csv.DictReader(csvfile))
        
        # Executa as análises
        brute_force_alerts = analyze_brute_force(logs)
        off_hours_alerts = analyze_off_hours_access(logs)

        all_alerts = brute_force_alerts + off_hours_alerts

        print("---" * 10)
        if not all_alerts:
            print("[OK] Nenhuma anomalia detectada.")
        else:
            for alert in all_alerts:
                print(alert)
        print("---" * 10)

    except FileNotFoundError:
        print(f"[ERRO] O arquivo '{log_file_path}' não foi encontrado.")
    except Exception as e:
        print(f"[ERRO] Ocorreu um erro inesperado: {e}")
    
    print("[*] Análise finalizada.")

if __name__ == "__main__":
    main("auth_logs.csv")

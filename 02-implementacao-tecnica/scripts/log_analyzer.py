# -*- coding: utf-8 -*-
# Importa o módulo 'csv' para facilitar a leitura de arquivos CSV e
# o módulo 'collections' para usar o 'defaultdict', um dicionário especial.
import csv
from collections import defaultdict

# --- Momento de Estudo: O que é defaultdict? ---
# É um dicionário que não levanta um erro (KeyError) se você tentar acessar
# uma chave que não existe. Em vez disso, ele cria a chave com um valor padrão.
# No nosso caso, `defaultdict(int)` significa que se um usuário não estiver no
# nosso dicionário de contagem, ele será criado com o valor padrão de um inteiro, que é 0.
# Isso simplifica o código, pois não precisamos verificar se a chave já existe.

def analyze_logs(log_file_path, failure_threshold=5):
    """
    Analisa um arquivo de log de autenticação para detectar possíveis
    ataques de força bruta.

    Args:
        log_file_path (str): O caminho para o arquivo de log CSV.
        failure_threshold (int): O número de falhas de login que aciona um alerta.
                                 O padrão é 5.
    """
    print(f"[*] Iniciando análise do arquivo de log: {log_file_path}")

    # Cria um defaultdict para contar as falhas de login por usuário.
    # Ex: {'злоумышленник': 5, 'pedro.santos': 1}
    failed_login_counts = defaultdict(int)

    try:
        # Abre o arquivo de log para leitura. 'with' garante que o arquivo será fechado
        # automaticamente no final, mesmo que ocorram erros.
        with open(log_file_path, mode='r', encoding='utf-8') as csvfile:
            # 'csv.DictReader' lê o arquivo e trata cada linha como um dicionário,
            # usando o cabeçalho (primeira linha) como as chaves.
            # Ex: {'timestamp': '...', 'username': '...', 'event_type': '...'}
            reader = csv.DictReader(csvfile)

            # Itera sobre cada linha (log) no arquivo.
            for row in reader:
                # Verifica se o evento é uma falha de login.
                if row['event_type'] == 'login_failed':
                    # Se for, incrementa o contador para aquele usuário.
                    username = row['username']
                    failed_login_counts[username] += 1

    except FileNotFoundError:
        print(f"[ERRO] O arquivo '{log_file_path}' não foi encontrado.")
        return # Encerra a função se o arquivo não existir.
    except Exception as e:
        print(f"[ERRO] Ocorreu um erro inesperado ao ler o arquivo: {e}")
        return

    print("[*] Análise de contagem de falhas concluída.")
    print("---" * 10)

    # --- Geração de Alertas ---
    print("[!] Verificando se algum limite de falhas foi atingido...")
    alert_triggered = False
    # Itera sobre os usuários e suas contagens de falhas.
    for user, count in failed_login_counts.items():
        # Se a contagem de falhas para um usuário atingir ou exceder o limite...
        if count >= failure_threshold:
            print(f"  [ALERTA] Possível ataque de força bruta detectado!")
            print(f"  -> Usuário: '{user}'")
            print(f"  -> Tentativas de login falhas: {count} (Limite é {failure_threshold})")
            alert_triggered = True

    if not alert_triggered:
        print("[OK] Nenhum usuário atingiu o limite de falhas de login.")

    print("---" * 10)
    print("[*] Análise finalizada.")


# --- Ponto de Execução do Script ---
# A construção `if __name__ == "__main__":` é uma boa prática em Python.
# Ela garante que o código dentro deste bloco só será executado quando você
# rodar o script diretamente (ex: `python log_analyzer.py`), e não quando
# ele for importado por outro script.
if __name__ == "__main__":
    # Define o nome do arquivo de log que queremos analisar.
    log_filename = "auth_logs.csv"
    
    # Chama a nossa função principal para iniciar a análise.
    analyze_logs(log_filename)

import pytest
from log_analyzer import analyze_brute_force

# --- Para o Curso: O que é Pytest? ---
# Pytest é um framework de testes para Python. Ele torna a escrita de testes
# simples e poderosa. Um teste é apenas uma função que começa com 'test_'
# que 'afirma' (assert) que um resultado esperado é verdadeiro. Se a afirmação
# for falsa, o teste falha, nos avisando que nosso código tem um bug.

def test_brute_force_detection():
    """
    Testa se a função de detecção de força bruta identifica corretamente um ataque.
    """
    # 1. Preparação (Arrange): Criamos um log falso em memória.
    fake_logs = [
        {'timestamp': '2026-01-27T10:02:30Z', 'username': 'atacante', 'source_ip': '1.1.1.1', 'event_type': 'login_failed'},
        {'timestamp': '2026-01-27T10:02:35Z', 'username': 'atacante', 'source_ip': '1.1.1.1', 'event_type': 'login_failed'},
        {'timestamp': '2026-01-27T10:02:41Z', 'username': 'atacante', 'source_ip': '1.1.1.1', 'event_type': 'login_failed'},
        {'timestamp': '2026-01-27T10:02:49Z', 'username': 'atacante', 'source_ip': '1.1.1.1', 'event_type': 'login_failed'},
        {'timestamp': '2026-01-27T10:02:55Z', 'username': 'atacante', 'source_ip': '1.1.1.1', 'event_type': 'login_failed'},
        {'timestamp': '2026-01-27T10:03:01Z', 'username': 'usuario.normal', 'source_ip': '2.2.2.2', 'event_type': 'login_success'},
    ]

    # 2. Ação (Act): Executamos a função que queremos testar.
    alerts = analyze_brute_force(fake_logs, failure_threshold=5)

    # 3. Afirmação (Assert): Verificamos se o resultado é o esperado.
    assert len(alerts) == 1  # Esperamos que exatamente um alerta seja gerado.
    assert "atacante" in alerts[0] # Esperamos que o nome do atacante esteja no alerta.

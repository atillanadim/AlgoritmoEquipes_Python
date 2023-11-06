# Inicializar estatísticas
menor_pontuacao = 99999999999999
equipe_menor_pontuacao = ""
melhor_pontuacao = -999999999999
equipe_melhor_pontuacao = ""
total_vitorias = 0
total_derrotas = 0
total_empates = 0

# Ler a primeira equipe
equipe = input("Qual é a primeira equipe? ")
while equipe != "":
    # Estatísticas da equipe
    pontos = 0
    vitorias_da_equipe = 0
    empates_da_equipe = 0
    derrotas_da_equipe = 0
    gols_marcados_pela_equipe = 0
    gols_sofridos_pela_equipe = 0

    jogos = int(input("Quantos jogos a equipe jogou? "))
    for _ in range(jogos):
        gols_marcados = int(input("Quantos gols foram marcados? "))
        gols_recebidos = int(input("Quantos gols foram recebidos? "))

        # Processando a equipe
        gols_marcados_pela_equipe += gols_marcados
        gols_sofridos_pela_equipe += gols_recebidos

        # Verificar o resultado
        if gols_marcados > gols_recebidos:
            pontos += 3
            vitorias_da_equipe += 1
        elif gols_marcados == gols_recebidos:
            pontos += 1
            empates_da_equipe += 1
        else:
            derrotas_da_equipe += 1

    # Cálculo da diferença
    diferenca = gols_marcados_pela_equipe - gols_sofridos_pela_equipe

    # Exibir as estatísticas da equipe
    print("**** Resumo", equipe, "****")
    print("Vitórias:", vitorias_da_equipe, "Empates:", empates_da_equipe, "Derrotas:", derrotas_da_equipe)
    print("Pontos:", pontos)
    print("Diferença de gols marcados e sofridos:", diferenca)
    print("Gols marcados:", gols_marcados_pela_equipe, "Gols sofridos:", gols_sofridos_pela_equipe)
    print("**** Fim Resumo", equipe, "****")

    # Acumular estatísticas gerais
    total_vitorias += vitorias_da_equipe
    total_empates += empates_da_equipe
    total_derrotas += derrotas_da_equipe

    # Verificar a menor pontuação
    if pontos < menor_pontuacao:
        menor_pontuacao = pontos
        equipe_menor_pontuacao = equipe

    # Verificar a melhor pontuação
    if diferenca > melhor_pontuacao:
        melhor_pontuacao = diferenca
        equipe_melhor_pontuacao = equipe

    # Ler próxima equipe
    equipe = input("Qual é a próxima equipe? (Nada para terminar)")
    if equipe !="Nada":
      break

# Processar as estatísticas gerais
resultado_total = total_vitorias + total_empates + total_derrotas
percentual_vitorias = (total_vitorias * 100) / resultado_total
percentual_empates = (total_empates * 100) / resultado_total
percentual_derrotas = (total_derrotas * 100) / resultado_total

# Exibir as estatísticas gerais
print("***** Estatísticas *****")
print("A equipe com menos pontos foi", equipe_menor_pontuacao, "com", menor_pontuacao, "pontos")
print("A equipe com melhor diferença de gols foi", equipe_melhor_pontuacao, "com uma diferença de", melhor_pontuacao, "gols")
print(percentual_vitorias, "% vitórias", percentual_empates, "% empates", percentual_derrotas, "% derrotas")
print("***** Fim Estatísticas *****")
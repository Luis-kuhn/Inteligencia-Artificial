<p align="center">
  <img src="https://seeklogo.com/images/F/FURB-logo-051554756A-seeklogo.com.png">
</p>

## Descrição do Trabalho

**CONSTRUÇÃO DO AGENTE REATIVO SIMPLES**

Escreva uma função de Agente Reativo Simples para o mundo 4 x 4 do aspirador de pó automático que garante limpar toda a sala, independentemente da posição inicial. 
A função deve ser chamada agenteReativoSimples(percepcao) e deve retornar uma das 5 possíveis ações ('acima', 'abaixo', 'esquerda', 'direita', 'aspirar'). A variável "percepcao" dentro dos parênteses é a entrada da função, isto é a posição em que o agente se encontra e o status da percepção (limpo ou sujo).
Para movimentar o agente dentro do ambiente você pode considerar criar uma função de mapeamento (funcaoMapear) como um ponto de partida. Isto é, você pode fazer um caminho (ou mapa) onde o agente percorre todo o ambiente.
Tenha em mente que as ações contra a parede (por exemplo, mover para a esquerda quando já está posicionado no ponto (1, 1)) não têm nenhum efeito (isto não significa que são proibidas).

**CONSTRUÇÃO DO AGENTE  BASEADO EM OBJETIVO**

A partir da estrutura do Agente Reativo Simples, aumente o código para transformá-lo em Agentes Baseados em Objetivos, na qual:
o agente tem que limpar toda a sala (função objetivo)
o agente começa a partir quadrado (1, 1)
Escreva uma função de verificação (checkObj(sala)) fora do programa agente que verifica se há sujeira na sala (retorna 1 se tem sujeira, caso contrário retorna 0).
Acrescente a ação de Não Operar "NoOp" na lista de ações do agente e ajuste a ação para "NoOp" uma vez que a sala estiver limpa.
A função de agente deve ser chamada agenteObjetivo(percepcao, objObtido) e deve retornar uma das 6 ações possíveis (5 inicialmente definidas + "NoOp"). O parâmetro objObtido é a saída da função checkObj(sala).
Utilize também uma variável de contador (chamada pontos) que contém o número de passos que o agente leva até atingir o objetivo (inclusive a Ação Aspirar conta 1 ponto).
### Requisitos :heavy_check_mark:

  
### Tecnologias Utilizadas :computer:

<p align="center">
  <img height="100px" widht="100px" src="https://python.org.br/theme/img/site-logo.svg">
  <img height="100px" widht="100px" src="https://camo.githubusercontent.com/1971c0a4f776fb5351c765c37e59630c83cabd52/68747470733a2f2f7777772e707967616d652e6f72672f696d616765732f6c6f676f2e706e67">
</p>

### Utilização :mega:

1. É necessário utilizar a biblioteca Pygame 
```
python -m pip install -U pygame
```
2. Após a finalização, execute o comando 
```python3 map.py``` na pasta do projeto
---

<p align="center">
  <a href="https://github.com/thrnkk" ><img src="https://img.shields.io/badge/github-thrnkk-24292e"></a>
  <a href="https://github.com/Luis-kuhn" ><img src="https://img.shields.io/badge/github-Luis--kuhn-24292e"></a>
</p>

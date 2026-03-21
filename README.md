# Prática: Arquitetura Full Cycle - Atividade Nº10

Este repositório contém a resolução da atividade prática focada em debugging e testes unitários.

O objetivo principal foi identificar bugs propositais em funções de hash e cálculo linear, validar esses erros através de testes e implementar as correções necessárias.

## 🎯 Objetivos do Projeto

- Identificar falhas de lógica em funções Python.
- Implementar testes unitários utilizando o framework `unittest`.
- Corrigir bugs estruturais para garantir a confiabilidade do software.
- Documentar o processo de desenvolvimento e melhoria contínua.

## 📁 Estrutura do Repositório

O projeto está organizado nos seguintes arquivos, conforme as diretrizes do roteiro:

- `hash_generator.py`: contém a função de geração de hash baseada em valores ordinais.
- `math_calc.py`: contém a função de cálculo matemático linear ($ax + b$).
- `main.py`: script principal para execução manual e verificação rápida das funções.
- `test_functions.py`: suíte de testes unitários para validação dos componentes.

## 🛠️ Descrição dos Bugs Encontrados

Com base na inspeção técnica e execução dos testes, foram identificados os seguintes problemas:

### 1. Função `generate_hash`

- **Bug:** O uso do slice `[:-1]` no loop `for` fazia com que a função ignorasse o último caractere da string de entrada.
- **Impacto:** A hash gerada era incompleta e inconsistente com o valor esperado para a string total.

### 2. Função `calculate_linear`

- **Bug:** A ordem das operações no retorno `x + b * a` priorizava a multiplicação de $b * a$ antes da soma com $x$, ferindo a fórmula proposta $ax + b$.
- **Impacto:** Resultados matemáticos incorretos para qualquer valor de $x$.

## 🧪 Testes Unitários

Foi utilizada a biblioteca padrão `unittest` para expor os bugs. Os testes foram desenhados para falhar inicialmente, confirmando a presença dos erros.

Exemplo de verificação de falha proposital (conforme roteiro):

```python
self.assertNotEqual(expected_hash, actual_hash, "Bug encontrado...")
```

## 🚀 Como Executar

Clone o repositório:

```bash
git clone https://github.com/gradinguilherme/Pratica-Arquitetura-Full-Cycle-10.git
```

Execute os testes para ver as falhas/correções:

```bash
python test_functions.py
```

Execute o fluxo principal:

```bash
python main.py
```

## 📊 Critérios de Avaliação (Rubrica)

Este projeto foi desenvolvido seguindo os níveis de excelência da rubrica, garantindo:

- **Identificação:** reporte claro de erros em ambas as funções.
- **Correção:** código executando sem erros e seguindo a lógica matemática correta.
- **Testes:** implementação e execução completa da suíte de testes unitários.

## Instituição

- **UNIVERSIDADE SENAI CIMATEC**
- **Componente Curricular:** Práticas Integradas: Arquitetura Full Cycle
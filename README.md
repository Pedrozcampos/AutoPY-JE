# Journal Entries — Análise de Lançamentos Contábeis

**O problema:** revisar grandes volumes de lançamentos manualmente exige repetir filtros, conferir totais e organizar evidências em várias planilhas.

**Como resolve:** lê os lançamentos de um Excel ou CSV, organiza os campos e aplica filtros como materialidade, valores redondos, histórico vazio e movimentações em fins de semana.

**O resultado:** um Excel separado por procedimento e um gráfico com a quantidade de ocorrências, facilitando a escolha dos lançamentos que precisam de revisão.

## Procedimentos implementados

| Procedimento | Regra do código |
|---|---|
| Geral | Preserva a listagem dos lançamentos |
| Excede ET | Débito + crédito acima da materialidade informada |
| Valor redondo | Valor bruto positivo e múltiplo de 100 |
| Sem histórico | Campo ausente ou descrição com menos de dois caracteres |
| Final de semana | Data em sábado ou domingo |
| Palavras-chave | Termos como ajuste, estorno, erro, manual, urgente e socio |
| Débito x crédito | Diferença entre os totais de débito e crédito do arquivo |

## Executar

Requisitos: Python 3.11 ou superior e ambiente gráfico com Tkinter. O botão de abertura do Excel usa `os.startfile`, específico do Windows.

```bash
python -m pip install -r requirements.txt
python VAuto.py
```

Na interface, informe a materialidade, selecione a entrada `.xlsx` ou `.csv` e escolha o nome do relatório. Após o processamento, é possível visualizar o gráfico e abrir a saída.

## Entrada esperada

O arquivo deve conter os cabeçalhos `Data`, `Histórico` (ou `Historico`), `Débito` (ou `Debito`) e `Crédito` (ou `Credito`). Mantenha essa grafia para que as colunas sejam reconhecidas.

A conta pode estar em uma coluna `Conta` ou nas três colunas `Código da Conta`, `Classificação Contábil` e `Descrição da Conta`, que são combinadas. CSVs usam o separador padrão do pandas, vírgula. Prefira datas ISO e valores numéricos já normalizados.

## Testar com dados de exemplo

```bash
python gerar_exemplo.py
python VAuto.py
```

Selecione `data/lancamentos_demo.csv`. A base fictícia inclui materialidade excedida, valor redondo, histórico vazio e lançamentos em fim de semana. O gerador recusa sobrescrever um arquivo existente. Os dados e relatórios gerados não entram no Git.

## Tecnologias e organização

`VAuto.py` contém o motor `AuditProcessor`, a interface CustomTkinter e o painel Matplotlib. pandas organiza os dados, python-calamine lê Excel e openpyxl escreve e formata os relatórios.

`VAuto.spec` contém a configuração para gerar um executável com PyInstaller. Para usar essa opção, instale o PyInstaller separadamente.

## Limitações

- O valor bruto é a soma de débito e crédito, não o saldo líquido.
- O equilíbrio é conferido no total do arquivo, sem provar a correção de cada partida.
- Datas inválidas viram ausentes e valores não numéricos podem virar zero.
- Os filtros apontam ocorrências para revisão. Eles não comprovam fraude ou erro, nem cobrem todos os procedimentos de uma auditoria.
- O processamento roda em uma thread separada. O comportamento da interface com arquivos grandes ainda precisa de mais testes.

O repositório inclui apenas código e um gerador de dados fictícios. Planilhas de entrada e relatórios gerados ficam fora do Git.

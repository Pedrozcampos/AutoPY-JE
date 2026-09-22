"""Gera lançamentos inteiramente fictícios para demonstração local."""
import csv
from pathlib import Path


def main():
    output = Path(__file__).resolve().parent / "data" / "lancamentos_demo.csv"
    output.parent.mkdir(exist_ok=True)
    rows = [
        ["2026-01-05", "1.1 - Caixa", "Aporte fictício", 20000, 0],
        ["2026-01-05", "2.3 - Capital", "Aporte fictício", 0, 20000],
        ["2026-01-10", "3.2 - Despesas", "ajuste manual de exemplo", 100, 0],
        ["2026-01-10", "1.1 - Caixa", "", 0, 100],
        ["2026-01-11", "3.2 - Despesas", "estorno fictício", 45.75, 0],
        ["2026-01-11", "1.1 - Caixa", "Contrapartida fictícia", 0, 45.75],
    ]
    with output.open("x", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["Data", "Conta", "Histórico", "Débito", "Crédito"])
        writer.writerows(rows)
    print(f"Base fictícia criada: {output}")


if __name__ == "__main__":
    main()

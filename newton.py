import argparse
import sympy as sp

parser = argparse.ArgumentParser(description="Metoda Newtona do znajdowania miejsc zerowych funkcji.")
parser.add_argument("funkcja", type=str, help="Funkcja w postaci wyrażenia, np. x**2+x+1")
parser.add_argument("start", type=float, help="Punkt startowy dla metody Newtona")
parser.add_argument("-s", "--step", type=float, default=1e-5, help="Wielkość kroku w pochodnej")
parser.add_argument("-n", "--steps", type=int, default=100, help="Maksymalna liczba kroków")
parser.add_argument("-t", "--tolerance", type=float, default=1e-7, help="Tolerancja dla wyniku")

args = parser.parse_args()

x = sp.symbols('x')
f = sp.sympify(args.funkcja)
df = sp.diff(f, x) 

current_x = args.start
for step in range(args.steps):
    f_val = f.evalf(subs={x: current_x})
    df_val = df.evalf(subs={x: current_x})

    if abs(f_val) < args.tolerance:
        print(f"Znaleziono miejsce zerowe: x = {current_x:.10f}, w {step + 1} krokach.")
        break

    if df_val == 0:
        print("Pochodna jest zerowa. Metoda Newtona nie działa.")
        break

    current_x = current_x - f_val / df_val
else:
    print("Nie znaleziono miejsca zerowego w podanej liczbie kroków.")


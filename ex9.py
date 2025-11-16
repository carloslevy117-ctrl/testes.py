maior = None
for i in range(1,11):
    num = int(input(f"digite o {i+1}'numero :"))

    if maior is None or num > maior:
        maior = num

print(f"o maior numero foi: {maior}")


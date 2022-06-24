from tqdm import tqdm
import csv
import time

start_time = time.time()
fil = "data/dataset2_Python+P7.csv"

def read_csv(fil):
    with open(fil, 'r') as csvfile:
        elements = csv.reader(csvfile, delimiter=',')
        headings = next(elements)
        shares_list = []
        Output = []
        for row in elements:
            Output.append(row[:])

    for line in Output:
        share = (
            line[0],
            int(float(line[1])),
            float(float(line[1]) * float(line[2])/100)
            )
        shares_list.append(share)
    return shares_list

def clean_data(share_list):
    data_clean = []
    for i in share_list:
        if i[1] <= 0:
            pass
        else:
            data_clean.append(i)
    return data_clean

def algo_Dynamique(invest, shares_list):
    n = len(shares_list) # total number of shares
    cost = []
    profit = []

    for share in shares_list:
        cost.append(share[1])
        profit.append(share[2])
# find optimal profit
    matrice = [[0 for x in range(invest + 1)] for x in range(n + 1)]
    for i in tqdm(range(1, n + 1)):
        for w in range(1, invest + 1):
            if cost[i-1] <= w:
                matrice[i][w] = max(profit[i-1] + matrice[i-1][w-cost[i-1]], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]

    shares_best = []
    while invest >= 0 and n >= 0:
        e = shares_list[n-1]
        if matrice[n][invest] == matrice[n-1][invest-cost[n-1]] + profit[n-1]:
            shares_best.append(e)
            invest -= cost[n-1]
        n -= 1
    return shares_best

def main():
    shares_list = read_csv(fil)
    shares_clean = clean_data(shares_list)
    invest = 500
    cost = []
    profits = []
    rep = algo_Dynamique(invest, shares_clean)
    print(f"\nProcessing {len(shares_list)} shares for {invest}€ of investment :")
    print(f"\nThe most profitable {len(rep)} shares are :\n")
    print('Actions     | Coût par action| Bénéfice (après 2 ans)')
    for item in rep:
        print(f'{item[0]}  | {round((item[1]), 2)} €           | +{round(item[2], 2)} €         ')
        cost.append(item[1])
        profits.append(item[2])
    print(f"\nTotal cost : ", round((sum(cost)), 2), "€.")
    print(f"Profit after 2 years : +", round((sum(profits)), 2), "€.")
    print("\nTime elapsed : ", time.time() - start_time, "seconds")


if __name__ == "__main__":
    main()
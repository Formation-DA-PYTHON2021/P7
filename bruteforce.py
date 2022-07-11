import csv
import time

start_time = time.time()

def algo_ForceBrute(invest, shares, shares_selection=[]):
    if shares:
        val1, lstVal1 = algo_ForceBrute(invest, shares[1:], shares_selection) # notion de recussion
        val = shares[0]
        if val[1] <= invest:
            val2, lstVal2 = algo_ForceBrute(invest - val[1], shares[1:], shares_selection + [val])
            if val1 < val2:
                return val2, lstVal2
        return val1, lstVal1
    else:
        return sum([i[2] for i in shares_selection]), shares_selection

def calc_profits(share_selection):
    profits = []
    shares = share_selection[1]
    for i in shares:
        profits.append(i[1] * i[2] / 100)
    return sum(profits)


def read_csv():
    with open("data/data_forcebrute_P7.csv", 'r') as csvfile:
        elements = csv.reader(csvfile, delimiter=',')
        headings = next(elements)
        shares_list = []
        for line in elements:
            shares_list.append(
                (line[0], float(line[1]), float(line[2]))
            )

    return shares_list

def main():
    shares_list = read_csv()
    max_invest = 500
    print(f"\nProcessing {len(shares_list)} shares for {max_invest}€ of investment :")
    print(f"\nThe most profitable {len(algo_ForceBrute(max_invest, shares_list)[1])} shares are :\n")
    for item in algo_ForceBrute(max_invest, shares_list)[1]:
        print(f'{item[0]} | {item[1]} € | +{item[2]} %')
    print(f'\nProfit after 2 years : + {calc_profits(algo_ForceBrute(max_invest,shares_list))}€.')
    print("\nTime elapsed : ", time.time() - start_time, "seconds")

if __name__ == "__main__":
    main()
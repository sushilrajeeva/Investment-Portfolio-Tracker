from Packages.Data_Fetch_Module import data_fetcher as df


def input_portfolio():
    portfolio = []
    num_assets = int(input("Enter the number of assets in your portfolio: "))
    for _ in range(num_assets):
        asset_type = input("Enter asset type (eqty/gld/slvr/crypt/bond): ").lower()
        asset_name = input("Enter the name of the asset: ")
        quantity = float(input("Enter quantity of the asset: "))
        portfolio.append((asset_type, asset_name, quantity))
    return portfolio

def calculate_portfolio_value(portfolio):
    total_value = 0
    values = []
    for asset_type, asset_name, quantity in portfolio:
        current_price = df.fetch_price(asset_type, asset_name)
        value = quantity * current_price
        values.append((asset_type, asset_name, value))
        total_value += value
    return values, total_value

def main():
    portfolio = input_portfolio()
    values, total_value = calculate_portfolio_value(portfolio)
    for asset_type, asset_name, value in values:
        print(f"{asset_type.upper()} - {asset_name}: ${value}")
    print(f"Total Portfolio Value: ${total_value}")

if __name__ == "__main__":
    main()

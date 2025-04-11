import math

projects = {
    "proj_A": {"hours": 50, "multiplier": 2, "owner": "user_Tim"},
    "proj_B": {"hours": 100, "multiplier": 1.5, "owner": "user_Praveen"}
}

stock_infos = {
    "proj_A": {"current_price": None},
    "proj_B": {"current_price": None}
}

portfolios = {
    "investor_1": {"proj_A": 0, "proj_B": 0},
    "investor_2": {"proj_A": 0, "proj_B": 0}
}

user_credits = {
    "investor_1": 10000,
    "investor_2": 8000,
    "user_Tim": 500,
    "user_Praveen": 500
}


def initialize_stock(project_id):
    if project_id in projects and project_id in stock_infos:
        project = projects[project_id]
        start_price = project["hours"] * project["multiplier"]
        stock_infos[project_id]["current_price"] = start_price
        print(f"[INIT] Start price for {project_id} set to: {start_price:.2f} Credits")
        return True
    else:
        print(f"[ERROR] Project {project_id} not found for initialization.")
        return False

def get_stock_price(project_id):
    if project_id in stock_infos and stock_infos[project_id]["current_price"] is not None:
        return stock_infos[project_id]["current_price"]
    else:
        print(f"[ERROR] Price for {project_id} not available.")
        return None

def buy_stock(buyer_id, project_id, num_shares):
    if buyer_id not in user_credits:
        print(f"[ERROR] Buyer {buyer_id} not found.")
        return False
    if num_shares <= 0:
        print(f"[ERROR] Number of shares must be positive.")
        return False

    current_price = get_stock_price(project_id)
    if current_price is None:
        return False

    total_cost = num_shares * current_price

    if user_credits[buyer_id] < total_cost:
        print(f"[ERROR] {buyer_id} does not have enough credits (needs {total_cost:.2f}, has {user_credits[buyer_id]:.2f}).")
        return False

    user_credits[buyer_id] -= total_cost
    if buyer_id not in portfolios:
        portfolios[buyer_id] = {}
    portfolios[buyer_id][project_id] = portfolios[buyer_id].get(project_id, 0) + num_shares

    try:
        factor = math.pow(1.01, num_shares)
        new_price = current_price * factor
    except OverflowError:
         print(f"[WARNING] Very high number of shares ({num_shares}), price adjustment might be inaccurate.")
         new_price = current_price * (1 + 0.01 * num_shares)

    stock_infos[project_id]["current_price"] = new_price

    print(f"[BUY] {buyer_id} buys {num_shares} share(s) of {project_id} for {total_cost:.2f} Credits.")
    print(f"[PRICE] New price for {project_id}: {new_price:.2f} Credits.")
    return True


def sell_stock(seller_id, project_id, num_shares):
    if seller_id not in user_credits or seller_id not in portfolios or project_id not in portfolios[seller_id]:
        print(f"[ERROR] Seller {seller_id} or their portfolio for {project_id} not found.")
        return False
    if num_shares <= 0:
        print(f"[ERROR] Number of shares must be positive.")
        return False

    shares_owned = portfolios[seller_id].get(project_id, 0)
    if shares_owned < num_shares:
        print(f"[ERROR] {seller_id} does not have enough shares (owns {shares_owned}, wants to sell {num_shares}).")
        return False

    current_price = get_stock_price(project_id)
    if current_price is None:
        return False

    total_proceeds = num_shares * current_price

    user_credits[seller_id] += total_proceeds
    portfolios[seller_id][project_id] -= num_shares

    try:
        factor = math.pow(0.99, num_shares)
        new_price = current_price * factor
    except OverflowError:
        print(f"[WARNING] Very high number of shares ({num_shares}), price adjustment might be inaccurate.")
        new_price = current_price * max(0, (1 - 0.01 * num_shares))

    stock_infos[project_id]["current_price"] = max(0.01, new_price)

    print(f"[SELL] {seller_id} sells {num_shares} share(s) of {project_id} for {total_proceeds:.2f} Credits.")
    print(f"[PRICE] New price for {project_id}: {stock_infos[project_id]['current_price']:.2f} Credits.")
    return True


initialize_stock("proj_A")
initialize_stock("proj_B")
print("\n--- State after Initialization ---")
print("StockInfos:", stock_infos)
print("Portfolios:", portfolios)
print("Credits:", user_credits)

print("\n--- Investor 1 buys proj_A ---")
buy_stock("investor_1", "proj_A", 10)

print("\n--- Investor 2 buys proj_A ---")
buy_stock("investor_2", "proj_A", 5)

print("\n--- Investor 1 sells proj_A ---")
sell_stock("investor_1", "proj_A", 3)

print("\n--- Final State ---")
print("StockInfos:", stock_infos)
print("Portfolios:", portfolios)
print("Credits:", user_credits)

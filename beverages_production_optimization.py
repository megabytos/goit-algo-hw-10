import pulp as plp

def optimize_beverages_production():
    problem = plp.LpProblem("Beverages_items_production", plp.LpMaximize)

    x1 = plp.LpVariable("Lemonade_item", lowBound=0, upBound=None, cat=plp.LpContinuous)
    x2 = plp.LpVariable("Juice_item", lowBound=0, upBound=None, cat=plp.LpContinuous)

    problem += x1 + x2, "Total_items"

    problem += 2 * x1 + x2 <= 100, "Water_Constraint"
    problem += x1 <= 50, "Sugar_Constraint"
    problem += x1 <= 30, "Juice_Constraint"
    problem += 2 * x2 <= 40, "Puree_Constraint"

    problem.solve()

    print("Status:", plp.LpStatus[problem.status])    
    print(f"Lemonade items: {plp.value(x1):.0f}")
    print(f"Juice items: {plp.value(x2):.0f}")

    return plp.value(problem.objective)


if __name__ == "__main__":
    total_items = optimize_beverages_production()
    print(f"Total items: {total_items:.0f}")

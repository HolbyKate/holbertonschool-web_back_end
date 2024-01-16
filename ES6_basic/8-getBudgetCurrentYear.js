function getCurrentYear() {
    const date = new Date();
    return date.getFullYear();
  }
  
  export default function getBudgetForCurrentYear(income, gdp, capita) {
    const budget = {};
    budget.income = income;
    budget.gdp = gdp;
    budget.capita = capita;

    return budget;
  }

/* eslint-disable */
import ClassCurrency from './3-currency.js';

export default class Pricing {
    constructor(amount, currency) {
        this._amount = amount;
        this._currency = currency;
    }

    get amount() {
        this._amount = amount;
    }

    set amount(amount) {
        this._amount = amount;
    }

    get currency() {
      this._currency = currency;
    }

    set currency(currency) {
        this._currency = currency;
    }

    displayFullPrice() {
        return `${this._amount} ${this._currency.name} (${this._currency.code})`;
    }
    
    static convertPrice(amount, conversionRate) {
        return amount * conversionRate;
    }
}

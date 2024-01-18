/* eslint-disable */
import ClassCurrency from './3-currency.js';

export default class Pricing {
    constructor(amount, currency) {
        this._amount = amount;
        this._currency = currency;
    }

    get amount() {
        return this._amount;
    }

    set amount(amount) {
        if (typeof amount !== 'number') {
            throw TypeError('Amount must be a number');
        }
        this._amount = amount;
    }

    get currency() {
        return this._currency;
    }

    set currency(currency) {
        if (!(currency instanceof ClassCurrency)) {
            throw TypeError('Currency must be a class Currency');
        }
        this._currency = currency;
    }
}

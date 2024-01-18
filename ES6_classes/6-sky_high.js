/* eslint-disable */

import Building from '5-building.js';

export default class SkyHighBuilding extends Building {
    constructor(sqft, floors) {
        this._sqft = sqft;
        this._floors = floors;
    }
    get floors() {
        return this._floors;
    }
    evacuationWarningMessage() {
        return `Evacuate slowly the NUMBER_OF_FLOORS floors`;
    }
}
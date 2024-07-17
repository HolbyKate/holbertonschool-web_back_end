// Create test case

const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber', () => {
    describe('SUM', () => {
        it('should return 4 when inputs are 1 and 3', function () {
            expect.strictEqual(calculateNumber('SUM', 1, 3), 4);
        });

        it('should return 5 when inputs are 1 and 3.7', function () {
            expect.strictEqual(calculateNumber('SUM', 1, 3.7), 5);
        });

        it('should return 5 when inputs are 1.2 and 3.7', function () {
            expect.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
        });

        it('should return 6 when inputs are 1.5 and 3.7', function () {
            expect.strictEqual(calculateNumber('SUM', 1.5, 3.7), 6);
        });

        it('should return 0 when inputs are -0.4 and 0.4', function () {
            expect.strictEqual(calculateNumber('SUM', -0.4, 0.4), 0);
        });

        it('should return -1 when inputs are -0.6 and -0.4', function () {
            expect.strictEqual(calculateNumber('SUM', -0.6, -0.4), -1);
        });

        it('should return -2 when inputs are -1.4 and -0.6', function () {
            expect.strictEqual(calculateNumber('SUM', -1.4, -0.6), -2);
        });

        it('should return -2 when inputs are -1.5 and -1.4', function () {
            expect.strictEqual(calculateNumber('SUM', -1.5, -1.4), -2);
        });

        it('should return 1 when inputs are -1.5 and 2.4', function () {
            expect.strictEqual(calculateNumber('SUM', -1.5, 2.4), 1);
        });
    });

    describe('SUBTRACT', () => {
        it('should return -2 when inputs are 1 and 3', function () {
            expect.strictEqual(calculateNumber('SUBTRACT', 1, 3), -2);
        });

        it('should return -3 when inputs are 1 and 3.7', function () {
            expect.strictEqual(calculateNumber('SUBTRACT', 1, 3.7), -3);
        });

        it('should return -3 when inputs are 1.2 and 3.7', function () {
            expect.strictEqual(calculateNumber('SUBTRACT', 1.2, 3.7), -3);
        });

        it('should return -2 when inputs are 1.5 and 3.7', function () {
            expect.strictEqual(calculateNumber('SUBTRACT', 1.5, 3.7), -2);
        });

        it('should return -1 when inputs are -0.6 and -0.4', function () {
            expect.strictEqual(calculateNumber('SUBTRACT', -0.6, -0.4), -1);
        });

        it('should return 0 when inputs are -1.5 and -1.4', function () {
            expect.strictEqual(calculateNumber('SUBTRACT', -1.5, -1.4), 0);
        });
    });

    describe('DIVIDE', () => {
        it('should return 0.33 when inputs are 1 and 3', function () {
            expect.strictEqual(parseFloat(calculateNumber('DIVIDE', 1, 3).toFixed(2)), 0.33);
        });

        it('should return 0.25 when inputs are 1 and 3.7', function () {
            expect.strictEqual(parseFloat(calculateNumber('DIVIDE', 1, 3.7).toFixed(2)), 0.25);
        });

        it('should return 0.25 when inputs are 1.2 and 3.7', function () {
            expect.strictEqual(parseFloat(calculateNumber('DIVIDE', 1.2, 3.7).toFixed(2)), 0.25);
        });

        it('should return 0.5 when inputs are 1.5 and 3.7', function () {
            expect.strictEqual(parseFloat(calculateNumber('DIVIDE', 1.5, 3.7).toFixed(1)), 0.5);
        });

        it('should return Error when inputs are -0.4 and 0.4', function () {
            expect.strictEqual(calculateNumber('DIVIDE', -0.4, 0.4), 'Error');
        });

        it('should return 1 when inputs are -1.5 and -1.4', function () {
            expect.strictEqual(calculateNumber('DIVIDE', -1.5, -1.4), 1);
        });

        it('should return Error when inputs are 1.4 and 0.4', function () {
            expect.strictEqual(calculateNumber('DIVIDE', 1.4, 0.4), 'Error');
        });
    });
});

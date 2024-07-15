/* eslint-disable */
// Create test case

const assert = require("assert");
const calculateNumber = require("./0-calcul.js");

describe('calculateNumber', () => {
  it('should return 4 for (1, 3)', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('should return 5 for (1, 3.7)', () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('should return 5 for (1.2, 3.7)', () => {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('should return 6 for (1.5, 3.7)', () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  // Additional edge cases
  it('should return 0 for (0, 0)', () => {
    assert.strictEqual(calculateNumber(0, 0), 0);
  });

  it('should return -2 for (-1.4, -1.4)', () => {
    assert.strictEqual(calculateNumber(-1.4, -1.4), -2);
  });

  it('should return -1 for (-1.6, 0.6)', () => {
    assert.strictEqual(calculateNumber(-1.6, 0.6), -1);
  });
});
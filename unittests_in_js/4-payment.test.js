// Test for sendPaymentRequestToApi

const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', function() {
    let calculateNumberStub;
    let consoleLogSpy;

    beforeEach(function() {
        calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(10);
        consoleLogSpy = sinon.spy(console, 'log');
    });

    afterEach(function() {
        calculateNumberStub.restore();
        consoleLogSpy.restore();
    });

    it('should call Utils.calculateNumber with SUM, 100, 20 and log the correct total', function() {
        sendPaymentRequestToApi(100, 20);

        expect(calculateNumberStub.calledOnce).to.be.true;
        expect(calculateNumberStub.calledWith('SUM', 100, 20)).to.be.true;
        
        expect(consoleLogSpy.calledOnce).to.be.true;
        expect(consoleLogSpy.firstCall.args[0]).to.equal('The total is: 10');
    });
});
// Create unittest

const request = require('request');
const chai = require('chai');

describe('integration test', () => {
  it('should return status code 200', (done) => {
    chai.request('http://localhost:7865')
      .get('/')
      .end((err, res) => {
        res.should.have.status(200);
        done();
      });
  });

  it('should return Welcome to the payment system', (done) => {
    chai.request('http://localhost:7865')
      .get('/')
      .end((err, res) => {
        res.text.should.equal('Welcome to the payment system');
        done();
      });
  });
});
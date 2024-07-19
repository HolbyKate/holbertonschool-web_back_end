// Create unittest

const request = require('request');
const chai = require('chai');

describe('basic integration testing', () => {
  describe('GET /', () => {
    it('endpoint GET /', (done) => {
      request('http://localhost:7865', (error, response, body) => {
        if (error) {
          done(error);
          return;
        }
        chai.expect(response.statusCode).to.equal(200);
        chai.expect(body).to.equal('Welcome to the payment system');
        done();
      });
    });
  });
});
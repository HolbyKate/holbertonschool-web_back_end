//Create an instance of express called app

const express = require('express');
const app = express();
const port = 7865;

app.get('/', (req, res) => res.end('Welcome to the payment system'));
app.get('/cart/:id')


app.listen(port, () => console.log(`API available on localhost port ${port}`));
const express = require('express');
const { get, patch } = require('axios');

const app = express();
const port = 3003;
const apiKey = '0689378ff42d654cba8983aaaafeed19';
const baseUrl = 'http://api.openweathermap.org/data/2.5/weather';

const longparam = '.'.repeat(10000000);

app.get('/200', async (req, res) => {
    try {
        const response = await get(`${baseUrl}?q=London&appid=${apiKey}`, {
        });
        res.status(response.status).send(response.data);
    } catch (error) {
        res.status(error.response.status).send(error.response.data);
    }
});

app.get('/304', async (req, res) => {
    try {
        const response = await get(`${baseUrl}?q=London&appid=${apiKey}`, {
            headers: {'If-None-Match': '*'}
        });
        res.status(response.status).send(response.data);
    } catch (error) {
        res.status(error.response.status).send(error.response.data);
    }
});

app.get('/400', async (req, res) => {
    try {
        const response = await get(`${baseUrl}?appid=${apiKey}`, {
        });
        res.status(response.status).send(response.data);
    } catch (error) {
        res.status(error.response.status).send(error.response.data);
    }
});

app.get('/401', async (req, res) => {
    try {
        const response = await get(`${baseUrl}?q=London&appid=InvalidApiKey`, {
        });
        res.status(response.status).send(response.data);
    } catch (error) {
        res.status(error.response.status).send(error.response.data);
    }
});

app.get('/404', async (req, res) => {
    try {
        const response = await get(`${baseUrl}?q=InvalidCity&appid=${apiKey}`, {
        });
        res.status(response.status).send(response.data);
    } catch (error) {
        res.status(error.response.status).send(error.response.data);
    }
});

app.get('/405', async (req, res) => {
    try {
        const response = await patch(`${baseUrl}?q=London&appid=${apiKey}`, {
        });
        res.status(response.status).send(response.data);
    } catch (error) {
        res.status(error.response.status).send(error.response.data);
    }
});

app.get('/412', async (req, res) => {
    try {
        const response = await get(`${baseUrl}?q=London&appid=${apiKey}`, {
            headers: {'If-Match': 'audio/basic'}
        });
        res.status(response.status).send(response.data);
    } catch (error) {
        res.status(error.response.status).send(error.response.data);
    }
});

app.get('/413', async (req, res) => {
    try {
        const response = await get(`${baseUrl}?q=London&appid=${apiKey}`, {
            headers: {'Content-Length': '1000000000'}
        });
        res.status(response.status).send(response.data);
    } catch (error) {
        res.status(error.response.status).send(error.response.data);
    }
});

app.get('/414', async (req, res) => {
    try {
        const response = await get(`${baseUrl}?q=London&appid=${apiKey}&long_param=${longparam}`, {
        });
        res.status(response.status).send(response.data);
    } catch (error) {
        res.status(error.response.status).send(error.response.data);
    }
});

app.get('/431', async (req, res) => {
    // В response data описание совпадающее с описанием для 431 статус кода, но response.status равен 400
    try {
        const response = await get(`${baseUrl}?q=London&appid=${apiKey}`, {
            headers: {longparam: longparam}
        });
        res.status(response.status).send(response.data);
    } catch (error) {
        res.status(error.response.status).send(error.response.data);
    }
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});

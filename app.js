const express = require('express');
const request = require('request');

const app = express();
const PORT = process.env.PORT || 8000;

const VALID_KEYS = new Set(['RamiyaYT', 'HEX', '444S@URN', 'slffnews']);

app.get('/api/ban_check/:uid', (req, res) => {
    const api_key = req.query.key;

    if (!api_key || !VALID_KEYS.has(api_key)) {
        return res.status(403).json({ error: 'Invalid or missing key. Contact @astute_ff on TikTok to get a key' });
    }

    const uid = req.params.uid;
    const url = `https://ff.garena.com/api/antihack/check_banned?lang=en&uid=${uid}`;

    const headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'Accept': 'application/json, text/plain, /',
        'authority': 'ff.garena.com',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'referer': 'https://ff.garena.com/en/support/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'x-requested-with': 'B6FksShzIgjfrYImLpTsadjS86sddhFH',
    };

    request({ url, headers }, (error, response, body) => {
        if (error) {
            return res.status(500).json({ error: 'Internal Server Error' });
        }
        res.json(JSON.parse(body));
    });
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

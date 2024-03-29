from flask import Flask, jsonify, request, render_template_string
import requests

app = Flask(__name__)

VALID_KEYS = {'RamiyaYT', 'HEX','444S@URN','slffnews'}

@app.route('/api/ban_check/<uid>', methods=['GET'])
def check_banned(uid):   
    api_key = request.args.get('key')

    if not api_key or api_key not in VALID_KEYS:

        return render_template_string("""
            <html>
            <head>
                <title>Redirecting...</title>
                <style>
                    body {
                        background-color: black;
                        color: white;
                    }
                </style>
                <script>
                    function redirectWithCountdown() {
                        var countdown = 7;
                        var countdownElement = document.getElementById('countdown');
                        var intervalId = setInterval(function() {
                            countdown--;
                            countdownElement.textContent = countdown;
                            if (countdown === 0) {
                                clearInterval(intervalId);
                                window.location.href = "{{ tiktok_url }}";
                            }
                        }, 1000);
                    }
                    window.onload = redirectWithCountdown;
                </script>
            </head>
            <body>
                <p>Error : Invalid or Missing Access key.</p>
                <p>Contact @astute_ff on TikTok to get a key.</p>
                <p>Redirecting to <a href="{{ tiktok_url }}">@astute_ff</a> in <span id="countdown">7</span> seconds...</p>

            </body>
            </html>
        """, tiktok_url="https://www.tiktok.com/@astute_ff")

    url = f"https://ff.garena.com/api/antihack/check_banned?lang=en&uid={uid}"

    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
        'Accept': "application/json, text/plain, /",
        'authority': "ff.garena.com",
        'accept-language': "en-GB,en-US;q=0.9,en;q=0.8",
        'referer': "https://ff.garena.com/en/support/",
        'sec-ch-ua': "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\"",
        'sec-ch-ua-mobile': "?1",
        'sec-ch-ua-platform': "\"Android\"",
        'sec-fetch-dest': "empty",
        'sec-fetch-mode': "cors",
        'sec-fetch-site': "same-origin",
        'x-requested-with': "B6FksShzIgjfrYImLpTsadjS86sddhFH",
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  

        return jsonify(response.json())

    except requests.exceptions.RequestException as e:
        # If an error occurs, redirect to TikTok page after 7 seconds
        return jsonify({'error': 'Invalid or missing key. Contact @astute_ff in TikTok to Get a Key'}), 403


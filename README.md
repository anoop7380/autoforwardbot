# Telegram Deal Auto-Forward Bot

This bot automatically forwards all messages from given Telegram channels to your EarnKaro bot in real time.

## Setup

1. Get `api_id` and `api_hash` from [my.telegram.org](https://my.telegram.org).
2. Edit `forward_bot.py`:
   - Put your `api_id` and `api_hash`.
   - Add source channel usernames in `source_usernames`.
   - Set `earnkaro_bot` to your bot username.
3. Deploy to Railway:
   - Fork this repo to your GitHub.
   - Connect it to Railway.
   - Set **Start Command** to `python forward_bot.py`.
4. First run will ask for OTP in Railway logs — enter it.
5. Bot will run 24/7.

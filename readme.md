# Arpav Downloader

Set up a cronjob that fetches new radar images every 10 minutes:
```bash
sudo crontab -e
# Insert
*/10 * * * * cd /root/arpav && python3 run.py >> log.txt
```

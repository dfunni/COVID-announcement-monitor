#!/bin/bash
MAIL_PASSWORD=$(cat /home/pi/mailpass.env)
/usr/local/bin/docker-compose -f /home/pi/COVID-announcement-monitor/docker-compose.yml up
/usr/local/bin/docker-compose -f /home/pi/COVID-announcement-monitor/docker-compose.yml down



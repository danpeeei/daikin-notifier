# daikin-dotifier

Water supply notifier by using [DAIKIN-API](https://github.com/nasshu2916/DAIKIN-API)

## Description

When your air cleaner is needed to supply water, This tool notifies that by [LINE Notify](https://notify-bot.line.me/doc/ja/)

## Requirements

## Install

```
pip install git+https://github.com/danpeeei/daikin-notifier.git
```

## Run

```bash
export DAIKIN_CLEANER_ENDPOINT=<your cleaner IP endpoint> # like http://192.168.1.10
export LINE_API_TOKEN=<your LINE Notify TOKEN>
daikin-notifier
```

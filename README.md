# notbad-app

This repo deploys very very simple webapp to https://app.notbad.liiv.eu:8089/

## Setup

1. Set `DOCKERHUB_USERNAME`, `DOCKERHUB_PASSWORD`, `AWS_ACCESS_KEY_ID` and `AWS_ACCESS_KEY_ID` to Github actions secrets.
1. Let pipeline deploy the app.

## Usage

```
curl -X POST -H "NotBad: true" https://app.notbad.liiv.eu:8089/
```

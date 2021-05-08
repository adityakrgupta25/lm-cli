# LM CLI tool

## Introdction
This Cli tool allows you to publish the messages to users and additionally provides several other related management utils for the same.

## Requirements
This project can be run without any external python deps. 
(Note: For using debug command you need to have have python's `pdb` package installed) 

## Usage
Clone the repo and run `python main.py`

### Available commands
* `addUser <userName> <role>` 
* `addTopic <topicName> <userName>` (Note: access only allowed too `admin` users)
* `subscribeTopic <topicName> <userName>` 
* `publishMessage <topicName> <text>`
* `processMessages` 
* `quit` 

Dev commands:
* `debug` (Note: To exit out of debug mode, use `c`)

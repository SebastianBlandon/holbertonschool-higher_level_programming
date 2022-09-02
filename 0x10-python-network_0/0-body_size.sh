#!/bin/bash
# CURL body size: The size must be displayed in bytes
curl -sI {$1} | grep Content-Length | cut -d' ' -f2

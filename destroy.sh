#!/bin/sh

cd infra
tofu destroy -auto-approve
cd - 

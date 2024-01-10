# target: all - Default target. Does nothing.
all:
	echo "Hello, this is make for jewelry-recomender"
	echo "Try 'make help' and search available options"

# target: help - List of options
help:
	egrep "^# target:" [Mm]akefile

# target: dev - run docker-compose
serve-kaf:
	sh ./scripts/kaf.sh

# target: down - stop and down docker stack
down-kaf:
	docker compose -f docker-stack-kaf.yml down

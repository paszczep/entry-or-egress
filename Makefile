dev:
	docker compose --profile dev up --build
prod:
	docker compose --profile prod up -d --build
kill:
	@docker kill $$(docker ps -q --filter "name=odbijacz")
remove:
	docker rmi -f $$(docker images -q --filter=reference='odbijacz*')

.PHONY: build check-env

build: check-env
	docker buildx build --platform linux/arm64,linux/amd64,linux/386 . --tag registry.gmatiukhin.site/telegram-notifier:$V --push

check-env:
ifndef V
	$(error V is undefined. Please use it to set the version)
endif

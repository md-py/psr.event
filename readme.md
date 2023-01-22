# psr.event

[PSR-14][psr-url] (php standard recommendation) port for python 3.5+

---

This repository holds all interfaces related to [PSR-14 (Event Dispatcher)][psr-url].

Note that this is not an Event Dispatcher implementation of its own. 
It is merely interfaces that describe the components of an Event Dispatcher.
See the specification for more details.

## Architecture overview

[![Architecture overview][architecture-overview]][architecture-overview]

## Installation

```sh
pip install psr.event --index-url=https://source.md.land/python/
```

## [Documentation](docs/index.md)

Read documentation with examples: https://development.md.land/python/psr.event/

---

Take a look for [md.event](../md.event/) — the first implementation.

[psr-url]: https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-14-event-dispatcher.md
[architecture-overview]: docs/_static/architecture.class-diagram.svg

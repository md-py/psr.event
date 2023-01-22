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

## Usage

If you need an event dispatcher, you can use the interface like this:

```python3
import md.event
import psr.event


class BeforeOperation(md.event.StoppableEvent):
    def __init__(self, context: dict) -> None:
        super().__init__()
        self.context = context


class AfterOperation:
    def __init__(self, context: dict) -> None:
        self.context = context


class Operation:  # just dummy example
    def __init__(self, event_dispatcher: psr.event.EventDispatcherInterface) -> None:
        self._event_dispatcher = event_dispatcher

    def operate(self, context: dict) -> None:
        before_operation_event = BeforeOperation(context=context)
        self._event_dispatcher.dispatch(before_operation_event)
        
        if before_operation_event.is_propagation_stopped():
            return 

        # do something useful

        self._event_dispatcher.dispatch(AfterOperation(context=context))
```

You can then pick one of the implementations of the interface to get an event dispatcher.

If you want to implement the interface, you can require this package and
implement `psr.log.EventDispatcherInterface` in your code. Please read the
[specification text][psr-url]
for details.

---

Take a look for [md.event](../md.event/) — the first implementation.

[psr-url]: https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-14-event-dispatcher.md
[architecture-overview]: _static/architecture.class-diagram.svg

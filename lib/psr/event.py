""" PSR-14 Event dispatcher interface port (see https://www.php-fig.org/psr/psr-14/). """

import typing


# Metadata
__version__ = '1.0.0'
__all__ = (
    # Metadata
    '__version__',
    # Contracts
    'EventDispatcherInterface',
    'ListenerProviderInterface',
    'StoppableEventInterface',
)


# Contracts
class EventDispatcherInterface:
    """ Defines a dispatcher for events. """
    def dispatch(self, event: object) -> object:
        """
        Provide all relevant listeners with an event to process.

        :param object event: The object to process.
        :return: The Event that was passed, now modified by listeners.
        """
        raise NotImplementedError


class ListenerProviderInterface:
    """ Mapper from an event to the listeners that are applicable to that event. """
    def get_listeners_for_event(self, event: object) -> typing.Iterable[typing.Callable[[object], typing.Any]]:
        """
        :param object event: An event for which to return the relevant listeners.

        :return: An iterable (array, iterator, or generator) of callables.
                 Each callable MUST be type-compatible with `event`.
        """
        raise NotImplementedError


class StoppableEventInterface:
    """
    An Event whose processing may be interrupted when the event has been handled.

    A Dispatcher implementation MUST check to determine if an Event
    is marked as stopped after each listener is called.  If it is then it should
    return immediately without calling any further Listeners.
    """
    def is_propagation_stopped(self) -> bool:
        """
        Is propagation stopped?

        This will typically only be used by the Dispatcher to determine if the
        previous listener halted propagation.

        :return: True if the Event is complete and no further listeners should be called.
                 False to continue calling listeners.
        """
        raise NotImplementedError

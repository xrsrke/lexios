"""State."""

from typing import Dict, Optional, TypeVar

T = TypeVar("T")


class State:
    """Add states to object."""

    def __init__(self):
        """Initialize the state."""
        self._states: Dict[str, T] = dict()

    def set_states(self, states: Dict[str, T]):
        """Set a list of states."""
        assert isinstance(states, dict), f"Expected states be a dict, but got {type(states)}"

        for k, v in states.items():
            self.set_state(k, v)

    def set_state(self, name: str, value: T):
        """Add state.

        Args:
            name (str): name of state
            value (T): value of state
        """
        self._states[name] = value

    def get_state(self, name: str) -> Optional[Dict[str, T]]:
        """Get state.

        Args:
            name (str): name of state

        Returns:
            Dict[str, T]: value of state
        """
        return self._states.get(name)

    @property
    def states(self) -> Dict[str, str | T]:
        """Return all states.

        Returns:
            Dict[str, Union[str, T]]: _description_
        """
        return self._states

from abc import ABC, abstractmethod
from typing import Any, Dict, Sequence, Tuple

from snorkel.end_model.data import MultitaskDataLoader


class Scheduler(ABC):
    """Return batches from all dataloaders in a specified order
    """

    def __init__(self):
        pass

    @abstractmethod
    def get_batches(
        self, dataloaders: Sequence[MultitaskDataLoader]
    ) -> Tuple[Tuple[Dict[str, Any], Dict[str, Any]], MultitaskDataLoader]:
        """Return batches in shuffled order from dataloaders

        Parameters
        ----------
        dataloaders
            A sequence of dataloaders to get batches from

        Yields
        -------
        (batch, dataloader)
            batch is a tuple of (X_dict, Y_dict) and dataloader is the dataloader
            that that batch came from. That dataloader will not be accessed by the
            model; it is passed primarily so that the model can pull the necessary
            metadata to know what to do with the batch it has been given.
        """
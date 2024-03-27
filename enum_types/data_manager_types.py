### IMPORTING
# Import external libraries
from enum import Enum, auto


class DataManagerFlowType(Enum):
    """
    An Enum the defines a DataManager's type regarding data inflow or outflow.
    It answers the question: can I import from this DataManager? Can I export to it?
    For example, Notes/ Obsidian can do both (offer data to summarize and store summaries) so it is likely UNIVERSAL

    Returns:
        None
    """
    IMPORT = auto()
    EXPORT = auto()
    UNIVERSAL = auto()

    def can_import(self):
        """
        Returns if the current DataManagerFlowType supports import

        Returns:
            bool: If import is allowed by this DataManagerFlowType
        """
        return (self == DataManagerFlowType.IMPORT) or (self == DataManagerFlowType.UNIVERSAL)
    
    def can_export(self):
        """
        Returns if the current DataManagerFlowType supports export

        Returns:
            bool: If export is allowed by this DataManagerFlowType
        """
        return (self == DataManagerFlowType.EXPORT) or (self == DataManagerFlowType.UNIVERSAL)
    
